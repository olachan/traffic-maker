#!/bin/bash

base_path=$(cd `dirname $0`; pwd)
/home/kylin/Program/pyenvs/github/bin/supervisorctl -c ${base_path}/conf/supervisor_run.conf
