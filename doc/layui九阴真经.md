######Layui监听
    1:
    //监听表单单选框复选框选择
    form.on('radio', function (data) {
       console.log(data.value); //得到被选中的值
    });
     
    2:
    //监听表单下拉菜单选择
     form.on('select', function (data) {
       console.log(data.value); //得到被选中的值
    });
     
    3
    //监听表单复选框选择
     form.on('checkbox', function (data) {
       console.log(data.value); //得到被选中的值
    });
     
    4
    //监听表格复选框选择
    table.on('checkbox(demo)', function (obj) {
       console.log(obj);
    });
     
    5:
    //layui监听input内容变动简单粗暴
    $(function(){
       //输入框的值改变时触发
      $("#inputid").on("input",function(e){
        //获取input输入的值
        console.log(e.delegateTarget.value);
      });
    });
     
    6:
    //点击触发监听
    $(document).on('click','.class',function(othis){
         var data = othis.currentTarget;
         data.remove();
         layer.msg('清除成功');
    });

    7:
    form.on('event(过滤器值)', callback);
 
    8:
    //监听checkbox复选
    form.on('checkbox(filter)', function(data){
        console.log(data.elem); //得到checkbox原始DOM对象
        console.log(data.elem.checked); //是否被选中，true或者false
        console.log(data.value); //复选框value值，也可以通过data.elem.value得到
        console.log(data.othis); //得到美化后的DOM对象
    });
     
    9:
    //监听switch复选
    form.on('switch(filter)', function(data){
    　　console.log(data.elem); //得到checkbox原始DOM对象
    　　console.log(data.elem.checked); //开关是否开启，true或者false
    　　console.log(data.value); //开关value值，也可以通过data.elem.value得到
    　　console.log(data.othis); //得到美化后的DOM对象
    }); 
     
    10:
    //监听radio单选：
    form.on('radio(filter)', function(data){
        console.log(data.elem); //得到radio原始DOM对象
        console.log(data.value); //被点击的radio的value值
    });
     
    11:
    //监听submit提交：
    <button lay-submit lay-filter="*">提交</button>
    form.on('submit(*)', function(data){
        console.log(data.elem) //被执行事件的元素DOM对象，一般为button对象
        console.log(data.form) //被执行提交的form对象，一般在存在form标签时才会返回
        console.log(data.field) //当前容器的全部表单字段，名值对形式：{name: value}
        return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
    });


######jquery根据name和id取值
    根据name取值：
        $("input[name='mobile']").val()
    根据id取值:
        $("#mobile_reg_form").html()
    根据name取值了遍历：
        $("input[name='mobile']").each(
            function(){
            alert($(this).val());
            }
        ) 