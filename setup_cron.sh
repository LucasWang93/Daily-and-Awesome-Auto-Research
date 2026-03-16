#!/usr/bin/env bash
# setup_cron.sh - Install daily cron job for the auto-research updater
# Usage: bash setup_cron.sh [HOUR] [MINUTE]
#   Default: 08:00 UTC

set -euo pipefail

HOUR="${1:-8}"
MINUTE="${2:-0}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/logs"
RUNNER="${SCRIPT_DIR}/run_daily_update.sh"

mkdir -p "${LOG_DIR}"

CRON_CMD="${MINUTE} ${HOUR} * * * ${RUNNER} >> ${LOG_DIR}/cron.log 2>&1"

(crontab -l 2>/dev/null | grep -v "daily_papers.*run.py" | grep -v "run_daily_update.sh" || true; echo "${CRON_CMD}") | crontab -

echo "Cron job installed:"
echo "  Schedule: ${MINUTE} ${HOUR} * * * (daily)"
echo "  Script:   ${RUNNER}"
echo "  Log:      ${LOG_DIR}/cron.log"
echo ""
echo "Current crontab:"
crontab -l
