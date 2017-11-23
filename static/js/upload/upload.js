//获取第一个div的下拉框选项触发事件
    $(document).ready(function() {
        //绑定下拉框change事件，当下来框改变时调用 SelectChange()方法
        $("#update_select").change(function() { 
        	SelectChange();
        	}); 
        })
		function SelectChange() {
        //获取下拉框选中项的text属性值
        var selectText = $("#update_select").find("option:selected").text();; 
           $.ajax({
            	url:'/app04/index/',
            	type:'POST',
            	data:{selectText:selectText},
        		success:function(arg){
        			var obj = jQuery.parseJSON(arg);
        			console.log(arg);
        			console.log(obj.msg);
        			console.log(obj.list_mysql_svndir[0]);
        			console.log('sucess');
        			console.log(obj.list_mysql_svndir[0]);
        			$('#list_mysql_svndir').html(obj.list_mysql_svndir[0]);
        		},
        		error:function(){
        			console.log('error')
        		}
            })
        
        console.log(selectText);       
            //alert(selectText);
		}
    
//getsvn版本号    
	function Getsvnversion(){
    	var get_update_num = $('#get_update_num').val();
    	
        if(get_update_num.length==0){
        	$('#testisnotnull').show();
        	$('#testisnotnull').html('版本号不允许为空')
        	console.log('版本号不允许为空')
        	
        	//alert('版本号不允许为空');
        }else{
    	$('#get_update_num').val('');
    	$('#testisnotnull').hide();
    	$.ajax({
    		url:'/app04/index/',
    		type:'POST',
    		data:{"svnversion":get_update_num},
    		success:function(arg){
    			var obj = jQuery.parseJSON(arg);
    			console.log(arg);
    			console.log('sucess');
    			//console.log(obj.msg);
    			console.log(obj.list_svn_num);
    			//console.log(obj.version_num)
    			//$('#List').val(obj.version_num);
    			
    			//$('#update_web_code_update_log_num').html(obj.msg);
    			//$('#update_web_code_update_log').html(obj.version_num);
    			
    			//$('#update_svn_get1').val(obj.version_num);    			
    		},
    		error:function(){
    			console.log('getsvnversion error')
    		}
    	});
        }
    }
    
