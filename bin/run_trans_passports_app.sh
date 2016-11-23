#!/usr/bin/env bash
/opt/venv/bin/newrelic-admin \
	run-program \
	/opt/venv/bin/gunicorn \
	trans_passports:flask_app \
	-w 4 \
	-b 0.0.0.0:5000 \
	--log-level=debug \
	--chdir=/opt/trans_passports/code
	--timeout=$((60 * 5)) \
	--worker-class=gthread
