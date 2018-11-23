                // 动态减少二级导航栏 动态添加触发的不能直接用click
                $(function(){
                    $("#secondNavs").delegate('#minusSecondNav','click',function(){
                        
                        console.log($(this).index());
                        $(this).parent().parent().remove();
                    });
                });

                // 动态添加和减少二级菜单
                $(function(){
                        // 如果有一级url那就让添加二级菜单
                        $("#fNavUrl").blur(function(){
                            if(($("#fNavUrl").val()) == ''){
                                $("#addSecondNav").show();
                                $("#secondNavs").show();
                            }else if(($("#fNavUrl").val()) != ''){
                                $("#addSecondNav").hide();
                                $("#secondNavs").hide();
                            }
                        });
                        // 动态添加二级导航栏
                        $("#addSecondNav").click(function(){
                            var subNavForm = $("#preAddSecondNavIndex").html();
                            // 动态添加二级导航栏dom 到 #secondNavs 下
                            $("#secondNavs").append(subNavForm);
                        });
                });
