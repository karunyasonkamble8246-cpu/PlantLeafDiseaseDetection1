#!/usr/bin/env bash
# Create and install into .venv
set -e
if [ -d ".venv" ]; then
  echo "Virtual environment .venv already exists."
else
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate
pip install --upgrade pip
pip install -r "$(dirname "$0")/requirements.txt"

echo
echo "Setup complete. To activate in a new shell:"
echo "  source .venv/bin/activate"
echo "Then run:"
echo "  streamlit run $(dirname "$0")/app.py"
