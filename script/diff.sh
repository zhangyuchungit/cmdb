#!/bin/sh
#对旧包和新包进行对比
#qq:1013888351@qq.com
#版本之间的对比
set -x
reversion_old=$2
reversion_new=$1
svnexport_dir="/data/up"
diff -ruNaq ${svnexport_dir}/cmdb_${reversion_new} ${svnexport_dir}/cmdb_${reversion_old} | awk '{print $4}';
diff -ruNaq ${svnexport_dir}/cmdb_${reversion_new} ${svnexport_dir}/cmdb_${reversion_old} | awk '{print $4}' | wc -l;
