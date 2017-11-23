#!/bin/sh
set -x
reversion=$1
svnexport_dir=/data/up
tar_dir=/data/up/src
#检测这个目录是否存在
if [[ ! -d ${tar_dir} ]];then
    mkdir -p ${tar_dir};
fi
#开始打包
cd ${svnexport_dir}
/bin/tar zcvfP ${tar_dir}/cmdb_${reversion}.tar.gz cmdb_${reversion}/ 
 echo "tar包成功"
 #此处需要设置ssh密钥，设置完ssh密钥之后请连接一下
 