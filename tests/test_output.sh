#!/bin/bash
set -e +x

# check file exists
[[ -f repository_statistics.json ]]

# check file is not empty
[[ -s repository_statistics.json ]]
