#!/usr/bin/env bash
# Unified daily automation entrypoint.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/logs"
RUNNER="${SCRIPT_DIR}/run_daily_update.sh"
PYTHON_BIN=""

usage() {
  cat <<'EOF'
Usage:
  ./run_daily_update.sh run
  ./run_daily_update.sh install-cron [HOUR] [MINUTE]

Environment:
  DAILY_PAPERS_VENV       Python virtualenv directory to use
  DAILY_PAPERS_ENV_FILE   Shell env file to source before running
EOF
}

resolve_venv_dir() {
  local venv_dir="${DAILY_PAPERS_VENV:-${VIRTUAL_ENV:-}}"

  if [[ -z "${venv_dir}" ]]; then
    if [[ -x "${SCRIPT_DIR}/.venv/bin/python" ]]; then
      venv_dir="${SCRIPT_DIR}/.venv"
    else
      venv_dir="${SCRIPT_DIR}/venv"
    fi
  fi

  printf '%s\n' "${venv_dir}"
}

resolve_env_file() {
  local env_file="${DAILY_PAPERS_ENV_FILE:-}"

  if [[ -z "${env_file}" && -f "${SCRIPT_DIR}/.env.sh" ]]; then
    env_file="${SCRIPT_DIR}/.env.sh"
  fi

  printf '%s\n' "${env_file}"
}

load_runtime() {
  local env_file
  local venv_dir

  mkdir -p "${LOG_DIR}"

  env_file="$(resolve_env_file)"
  venv_dir="$(resolve_venv_dir)"
  PYTHON_BIN="${venv_dir}/bin/python"

  if [[ -n "${env_file}" && -f "${env_file}" ]]; then
    # shellcheck disable=SC1090
    source "${env_file}"
  fi

  if [[ ! -x "${PYTHON_BIN}" ]]; then
    echo "Python not found: ${PYTHON_BIN}" >&2
    exit 1
  fi

  cd "${SCRIPT_DIR}"
}

stage_repo_updates() {
  local candidate_paths=(
    README.md
    data
    reports
    run.py
    run_daily_update.sh
    setup_cron.sh
    src
    tests
    .gitignore
    LICENSE
    config.yaml.example
    requirements.txt
  )
  local existing_paths=()
  local path

  for path in "${candidate_paths[@]}"; do
    if [[ -e "${path}" ]]; then
      existing_paths+=("${path}")
    fi
  done

  if (( ${#existing_paths[@]} > 0 )); then
    git add -A -- "${existing_paths[@]}"
  fi
}

run_daily_update() {
  load_runtime
  "${PYTHON_BIN}" run.py ingest
  stage_repo_updates

  if ! git diff --cached --quiet; then
    git commit -m "Daily auto-research update ($(date -u +%Y-%m-%d))"
    GIT_SSH_COMMAND='ssh -o StrictHostKeyChecking=accept-new' git push origin main
  fi
}

install_cron() {
  local hour="${1:-8}"
  local minute="${2:-0}"
  local env_file
  local venv_dir
  local cron_prefix=""
  local cron_cmd

  mkdir -p "${LOG_DIR}"

  env_file="$(resolve_env_file)"
  venv_dir="$(resolve_venv_dir)"

  if [[ -n "${venv_dir}" ]]; then
    printf -v cron_prefix '%sDAILY_PAPERS_VENV=%q ' "${cron_prefix}" "${venv_dir}"
  fi

  if [[ -n "${env_file}" ]]; then
    printf -v cron_prefix '%sDAILY_PAPERS_ENV_FILE=%q ' "${cron_prefix}" "${env_file}"
  fi

  printf -v cron_cmd '%s %s * * * cd %q && %s%q run >> %q 2>&1' \
    "${minute}" \
    "${hour}" \
    "${SCRIPT_DIR}" \
    "${cron_prefix}" \
    "${RUNNER}" \
    "${LOG_DIR}/cron.log"

  (crontab -l 2>/dev/null | grep -v "daily_papers.*run.py" | grep -v "run_daily_update.sh" || true; echo "${cron_cmd}") | crontab -

  echo "Cron job installed:"
  echo "  Schedule: ${minute} ${hour} * * * (daily)"
  echo "  Script:   ${RUNNER} run"
  if [[ -n "${venv_dir}" ]]; then
    echo "  Venv:     ${venv_dir}"
  fi
  if [[ -n "${env_file}" ]]; then
    echo "  Env file: ${env_file}"
  fi
  echo "  Log:      ${LOG_DIR}/cron.log"
  echo ""
  echo "Current crontab:"
  crontab -l
}

main() {
  local command="${1:-run}"

  case "${command}" in
    run)
      shift || true
      run_daily_update "$@"
      ;;
    install-cron)
      shift || true
      install_cron "${1:-8}" "${2:-0}"
      ;;
    help|-h|--help)
      usage
      ;;
    *)
      usage >&2
      exit 1
      ;;
  esac
}

main "$@"
