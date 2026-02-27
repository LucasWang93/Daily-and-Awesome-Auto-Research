#!/usr/bin/env bash
# setup_cron.sh - Install daily cron job for the papers assistant
# Usage: bash setup_cron.sh [HOUR] [MINUTE]
#   Default: 08:00 UTC

set -euo pipefail

HOUR="${1:-8}"
MINUTE="${2:-0}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="/home/sw2572/project_pi_yz875/sw2572/venvs/fars"
ENV_FILE="/home/sw2572/Keys/env.sh"
LOG_DIR="${SCRIPT_DIR}/logs"

mkdir -p "${LOG_DIR}"

CRON_CMD="${MINUTE} ${HOUR} * * * source ${ENV_FILE} && source ${VENV_DIR}/bin/activate && cd ${SCRIPT_DIR} && python run.py >> ${LOG_DIR}/cron.log 2>&1"

(crontab -l 2>/dev/null | grep -v "daily_papers.*run.py" || true; echo "${CRON_CMD}") | crontab -

echo "Cron job installed:"
echo "  Schedule: ${MINUTE} ${HOUR} * * * (daily)"
echo "  Script:   ${SCRIPT_DIR}/run.py"
echo "  Log:      ${LOG_DIR}/cron.log"
echo ""
echo "Current crontab:"
crontab -l
