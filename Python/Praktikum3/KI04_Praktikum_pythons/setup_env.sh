#!/usr/bin/env bash
# setup_env.sh - Startet setup_env.py unter macOS/Linux.
# Fuer einen venv an anderem Ort (analog zu Windows):
#   sh setup_env.sh --venv-dir /pfad/zum/venv

cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
    python3 setup_env.py "$@"
else
    python setup_env.py "$@"
fi
status=$?

if [ $status -ne 0 ]; then
    echo
    echo "FEHLER: Setup wurde nicht erfolgreich abgeschlossen."
fi
echo
read -rp "Enter zum Beenden ..."
exit $status
