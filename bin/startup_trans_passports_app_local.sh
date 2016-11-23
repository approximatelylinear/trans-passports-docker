#!/usr/bin/env bash
# Startup application et al. via supervisor
echo "Starting supervisor for local work..."
/opt/venv/bin/supervisord -c /etc/supervisord_local.conf -n
