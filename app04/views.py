#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from app04.models import UserInfo,UserList,SvnRev,svn_project
from django.db import models
import os
import json
# Create your views here.

def Ajax(request):  
    if request.method == 'POST':
        print  request.POST
        #result = svn_project.objects.filter(id='1')
        result = svn_project.objects.all().values('project')
        print result
        print "~~~~~~"
        #for i in range(2):
        #   print result[i] #{'project': u'cms'}
        
        list_svn_num = request.POST.getlist('dat',None)
        print list_svn_num
        print type(list_svn_num)
        int_svn_num = int(list_svn_num[0])
        #data_num = {'version_num':int_svn_num,'msg':'请求成功','result':result}
        #print type(int_svn_num)
        return render_to_response('./app04/ajax.html', {'List':json.dumps(result),'status':'sucess'
        })
        
        
        #return HttpResponse(json.dumps(data_num))
        #return render_to_response('./app04/ajax.html',{'status':int_svn_num})
    else:
        print HttpResponse('not ok')
        return render_to_response('./app04/ajax.html')

def Add(request):
        UserInfo.objects.create(username='zzz',age=10 )
        return HttpResponse('create OK')
def Update(request):
    return HttpResponse('update OK')

def Userlist(request):
    if request.method == 'POST':
        list_selectText = request.POST.getlist('selectText')
        print list_selectText
        print type(list_selectText)
        
        #将获取到的数据按数据库惊查询
        list_mysql_svndir=[]
        mysql_svndir = svn_project.objects.all().values('svndir').filter(project=list_selectText[0])
        print mysql_svndir
        print type(mysql_svndir)
        for m in mysql_svndir:
            list_mysql_svndir.append(m.get('svndir'))
        print list_mysql_svndir
        print type(list_mysql_svndir)
        
        #return render_to_response('./app04/userlist.html',{'list_selectText':list_selectText,})
        data_num = {'list_selectText':list_selectText,'msg':'获取信息成功','list_mysql_svndir':list_mysql_svndir}
        return HttpResponse(json.dumps(data_num))
    
    
    else:
        list=[]
        list_dir=[]
        result = svn_project.objects.all().values('project')
        #result = svn_project.objects.all()
        #列表中嵌套字典，列表先循环出来，在传至前台
        for i in result:
            list.append(i.get('project'))
        print type(list)
        result1 = svn_project.objects.all().values('svndir')
        print result1
        for k in result1:
            list_dir.append(k.get('svndir'))
        return render_to_response('./app04/userlist.html',{'result':result,'List':list,'listdir':list_dir,})
def Register(request):
    if request.method == "POST":
        username = request.POST.get("username",None)        
        password = request.POST.get("password",None)
        print username,password
        result = UserList.objects.filter(username=username,password=password).count()
        print result
        if result <= 1:
            UserList.objects.create(username=username,password=password)
            return render_to_response('./app04/registerok.html',{'status':'注册成功'})
        else:
            return render_to_response('./app04/register.html',{'status':'用户惨被注册'})
    else:
        return render_to_response('./app04/register.html')

def Index(request):
 
    if request.method == 'POST':
        print  request.POST
        #list_svn_num = request.POST.getlist('dat',None)
        #list_svn_dir = request.POST.getlist('svndir',)

        #for item in list_svn_num:
        #    print item[2]
       # print list_svn_num
        #str_svn_dir = str(list_svn_dir)
        #print type(str_svn_dir)
       # print type(list_svn_num)
       # print 0
        #int_svn_num = int(list_svn_num[0])
        #获取svn版本号
        list_svn_num = request.POST.getlist('svnversion')
        print list_svn_num
        print type(list_svn_num)
        #获取二级联动相关属性    
        print "------------1--------------------"
        list_selectText = request.POST.getlist('selectText')
        print list_selectText
        print type(list_selectText)
        if list_selectText:        
            list_mysql_svndir=[]
            mysql_svndir = svn_project.objects.all().values('svndir').filter(project=list_selectText[0])
            for m in mysql_svndir:
                list_mysql_svndir.append(m.get('svndir'))
                print list_mysql_svndir
                print "---------------2--------------"
            data_num = {'msg':'请求成功','list_mysql_svndir':list_mysql_svndir}
            return HttpResponse(json.dumps(data_num))
        else:
            
            #data_num = {'version_num':int_svn_num,'msg':'获取版本号:','list_mysql_svndir':list_mysql_svndir,}
            data_num = {'list_svn_num':list_svn_num,}
            print "--------------3----------------"
            #print type(int_svn_num)
            return HttpResponse(json.dumps(data_num))
            #return render_to_response('./app04/ajax.html',{'status':int_svn_num})
    else:
        print HttpResponse('not ok')
        #获取mysql中的值类似于elect project from svn_project;
        list=[]
        result = svn_project.objects.all().values('project')
        for i in result:
            list.append(i.get('project'))
        #list_dir=[]
        #result1 = svn_project.objects.all().values('svndir')
        #print result1
        #for k in result1:
        #    list_dir.append(k.get('svndir'))
        #list_select = request.POST.getlist('selectText')
        #print list_select
        #return render_to_response('./app04/index.html',{'List':list,'listdir':list_dir,})
        return render_to_response('./app04/index.html',{'List':list,})

def ChouTi(request):
    return render_to_response('./app04/chouti.html')
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        result = UserList.objects.filter(username=username,password=password).count()
        if result == 1:
            return render_to_response('./app04/index.html')
        else:
            return render_to_response('./app04/login.html',{'status':'用户或者密码错误'})
    else:
        return render_to_response('./app04/login.html')
def UpLoad(request):
    #这个数据只是数据库获取的一个对象，需要遍历才能出来具体的数
    obj = SvnRev.objects.all()
    for item in obj:
        rev_num_old = item.svnreversion
        ##
    if request.method == "POST":
        rev_num_new = request.POST.get("rev_num_new",None)
        up_url1 = request.POST.get("up_url",None)

        result = SvnRev.objects.filter(id='1').update(svnreversion=rev_num_new) 
        print rev_num_new,rev_num_old,result
        res = [rev_num_new,up_url1]
        reu=all(res)
        print reu
        if reu:
            #output = os.popen('sh ./script/svnexport.sh ' + rev_num1)
            #setoutput = output.read()
            output = os.system('sh ./script/svnexport.sh ' + rev_num_new )
            if output == 0:
                #num_int=[rev_num_new,rev_num_old]
                #传递多参数到脚本
                diff_num=os.popen('sh ./script/diff.sh %d %d ' %(int(rev_num_new),int(rev_num_old)) )
                new_diff_num=diff_num.read()
                return render_to_response('./app04/upload.html',{'status':'获取包成功','diff':new_diff_num})
            else: 
                return render_to_response('./app04/upload.html',{'status':'获取包失败，查看源码错误提示'})
        else:
            return HttpResponse('你有其中一个的参数是错误的或者并未填写')
    else:
        return render_to_response('./app04/upload.html')
def SvnupLoad(request):
    output = os.popen('sh ./script/svnexport.sh')
    setoutput = output.read()
    print setoutput
    return HttpResponse(setoutput)
def Tar(request):
    if request.method == "POST":
        obj = SvnRev.objects.all()
        for item in obj:
            rev_num_new = item.svnreversion
            print type(rev_num_new)
        output = os.system('sh ./script/tar.sh %d' %(rev_num_new))
        #tar_output=output.read()
        if output == 0:
            return render_to_response('./app04/upload.html',{'status2':'打包执行成功'})
        else:
            return render_to_response('./app04/upload.html',{'status2':'获取包失败'})
    else:
       return render_to_response('./app04/upload.html',{'status2':'tar包失败，查看源码错误提示'})
def LoadDir(request):
    if request.method == "POST":
        load_dir1 = request.POST.get("load_dir",None)
        obj = SvnRev.objects.all()
        for item in obj:
            rev_num_new = item.svnreversion
        print load_dir1,rev_num_new
        if load_dir1 == None:
            return render_to_response('./app04/upload.html',{'status3':'请加入需要上传路径参数参数'})
        else:
            output = os.system('sh ./script/load.sh %s %d ' %(load_dir1,int(rev_num_new)) )
            if output == 0:
                return render_to_response('./app04/upload.html',{'status3':'上传成功并完成软连接'})
            else:
                return render_to_response('./app04/upload.html',{'status3':'上传脚本未成功执行'})
    else:
        return render_to_response('./app04/upload.html',{'status3':'上传包失败，检查源码报错'})
            