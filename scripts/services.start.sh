#!/usr/bin/env bash

base_path=$(cd `dirname $0`; pwd)
/home/kylin/Program/pyenvs/github/bin/supervisord -c ${base_path}/conf/supervisor_run.conf
