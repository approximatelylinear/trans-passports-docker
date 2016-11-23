#!/usr/bin/env bash
# Startup application et al. via supervisor
echo "Starting supervisor for app..."
/opt/venv/bin/supervisord -c /etc/supervisord.conf -n
