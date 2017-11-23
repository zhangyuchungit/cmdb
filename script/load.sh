#!/bin/sh
set -x
load_dir=$1
reversion_new=$2
tar_dir=/data/up/src
untat_dir=/data/cmdb/src
python_path=/usr/local/python/bin/python
project
/bin/cp -r ${tar_dir}/cmdb_${reversion_new}.tar.gz ${load_dir}
#进入目录进行解压
cd ${untat_dir}
/bin/tar zxvf ${load_dir}/cmdb_${reversion_new}.tar.gz;
#制作软连接
/bin/ln -snf ${untat_dir}/cmdb_${reversion_new}/cmdb /data/cmdb/cmdb
#重启php或者java