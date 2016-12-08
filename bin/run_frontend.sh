#!/usr/bin/env bash

# Copy over the node_modules to the volumed directory (they are created on build, but not stored in the git repo)
cp -r /opt/src/* /opt/trans_passports

npm start
