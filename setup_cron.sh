#!/usr/bin/env bash
# Backward-compatible wrapper around run_daily_update.sh install-cron.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec "${SCRIPT_DIR}/run_daily_update.sh" install-cron "$@"
