#!/usr/bin/env bash
# Run the daily ingest pipeline, send email, and push tracked updates to GitHub.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/logs"
VENV_DIR="${DAILY_PAPERS_VENV:-${VIRTUAL_ENV:-}}"
ENV_FILE="${DAILY_PAPERS_ENV_FILE:-}"

if [[ -z "${VENV_DIR}" ]]; then
  if [[ -x "${SCRIPT_DIR}/.venv/bin/python" ]]; then
    VENV_DIR="${SCRIPT_DIR}/.venv"
  else
    VENV_DIR="${SCRIPT_DIR}/venv"
  fi
fi

if [[ -z "${ENV_FILE}" && -f "${SCRIPT_DIR}/.env.sh" ]]; then
  ENV_FILE="${SCRIPT_DIR}/.env.sh"
fi

PYTHON_BIN="${VENV_DIR}/bin/python"

mkdir -p "${LOG_DIR}"

if [[ -n "${ENV_FILE}" && -f "${ENV_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
fi

if [[ ! -x "${PYTHON_BIN}" ]]; then
  echo "Python not found: ${PYTHON_BIN}" >&2
  exit 1
fi

cd "${SCRIPT_DIR}"

"${PYTHON_BIN}" run.py ingest

if ! git diff --quiet -- README.md data run.py src tests .gitignore LICENSE config.yaml.example; then
  git add README.md data run.py src tests .gitignore LICENSE config.yaml.example
  if ! git diff --cached --quiet; then
    git commit -m "Daily auto-research update ($(date -u +%Y-%m-%d))"
    GIT_SSH_COMMAND='ssh -o StrictHostKeyChecking=accept-new' git push origin main
  fi
fi
