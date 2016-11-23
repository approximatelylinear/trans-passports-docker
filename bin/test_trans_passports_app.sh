#!/usr/bin/env bash
# Install coveralls for python
/opt/venv/bin/pip install git+git://github.com/z4r/python-coveralls.git@master

# Run test
/opt/venv/bin/coverage run --source /opt/trans_passports /opt/trans_passports/code/tests.py

# Conditional on test exit code
if [ $? == 0 ]; then
   #Tests Successfully Passed, continuing build
   COVERALLS_REPO_TOKEN= /opt/venv/bin/coveralls \
   --base_dir /opt/trans_passports \
   --data_file /.coverage \
   --config_file /opt/.coveragerc
else
   #Tests Failed, exiting build
   exit 1
fi
