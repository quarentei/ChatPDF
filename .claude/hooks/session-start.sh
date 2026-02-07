#!/bin/bash
set -euo pipefail

# Only run in remote (Claude Code on the web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install Python dependencies, filtering out pywin32 which is Windows-only
grep -v "pywin32" "$CLAUDE_PROJECT_DIR/requirements.txt" \
  | pip install --break-system-packages --ignore-installed -r /dev/stdin 2>&1 | tail -5

# Install linter (flake8) for Python code quality checks
pip install --break-system-packages flake8 2>&1 | tail -3

# Install pytest for running tests
pip install --break-system-packages pytest 2>&1 | tail -3
