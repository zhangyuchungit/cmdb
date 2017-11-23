#!/bin/sh
set -x
reversion_new=$1
SVN="/usr/bin/svn"
svnexport_dir="/data/up"
SVN_URL=svn://192.168.117.128/brunch/alp
#/usr/bin/svn export  --force svn://192.168.117.128/brunch/alp /data/up/
/usr/bin/svn export --force $SVN_URL ${svnexport_dir}/cmdb_${reversion_new}