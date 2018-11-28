                // 动态减少二级导航栏 动态添加触发的不能直接用click
                parent.$(function(){
                    parent.$("#secondNavs").delegate('#minusSecondNav','click',function(){
                        console.log(parent.$(this).index());
                        parent.$(this).parent().parent().remove();
                    });
                });

                // 动态添加和减少二级菜单
                parent.$(function(){
			console.log(2232);
                        // 如果有一级url那就让添加二级菜单
                        parent.$("#fNavUrl").blur(function(){
                            if((parent.$("#fNavUrl").val()) == ''){
                                parent.$("#addSecondNav").show();
                                parent.$("#secondNavs").show();
                            }else if((parent.$("#fNavUrl").val()) != ''){
                                parent.$("#addSecondNav").hide();
                                parent.$("#secondNavs").hide();
                            }
                        });
                        // 动态添加二级导航栏
                        parent.$("#addSecondNav").click(function(){
                            var subNavForm = parent.$("#preAddSecondNavIndex").html();
                            // 动态添加二级导航栏dom 到 #secondNavs 下
                            parent.$("#secondNavs").append(subNavForm);
                        });
                });

		// ajax 提交addmodal 的 form 表单
		parent.$(function(){
			parent.$("#addFirstNav").click(function(){
				var form_data = {};
				var t = parent.$("form[id='addFirstNavForm']").serializeArray();
				var navPris = new Array();
				var sNavs = new Array();
				var sNav = {}; 
				$.each(t,function(){
					if(this.name == 'navPri'){
						navPris.push(this.value);
					}else if(this.name == 'sNavName' && Object.keys(sNav).length == 0){
						sNav['sNavName'] = this.value;
					}else if(this.name == 'sNavUrl' && sNav['sNavName'] != ''){
						sNav['sNavUrl'] = this.value;
						sNavs.push(sNav);
						sNav = {};
					}else{
						form_data[this.name] = this.value;
					}
				});
				form_data['navPris'] = navPris;
				form_data['sNavs'] = sNavs;
				data = JSON.stringify(form_data);
				console.log(data);
				// 提交到服务器
				parent.$.post("/houtai/addFNav",{"data":data},function(data,status){
					console.log(data);
					// 提交结果
					if(data['code'] == 200){
						parent.layer.msg('<span>添加成功!</span>');
						// 关闭模态框
						$(window.top.document.body).find("#myModal").modal('hide');
						window.location.reload();
					}else{
						parent.layer.msg('<span style="color:red;">添加失败,请检查参数</span>');
					}
				});
			});
		});
