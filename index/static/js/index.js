function js_good() {
    $.get('js_good',function (data) {
        $(data).each(function (i, obj) {
            let time = 0;
            let typeGood = "<div style='overflow: hidden;margin-top: 15px'><p class='type-good' style='margin-bottom: 10px;border-top: solid'>" +
                "<img style='height: 100px;width: 100px' src="+obj["type"]["picture"]+">" +
                "<a style='float: right' href=\"\">更多</a>" +
                "</p></div>";
            $(obj['good']).each(function (j, gd) {
                time +=1;
                let content = "";
                if (time%5){
                    content += "<div class='item' style='overflow: hidden'>"
                }else {
                    content += "<div class='item no-margin' style='overflow: hidden'>"
                }
                content += "<div id="+(10*i+j).toString()+" class='proImg'>";
                content += "<img src="+gd["picture"]+" style='width:190px;height:190px'>";
                content += "</div>";
                content += "<p>"+gd['name'];
                content += "<a href='javascript:add_cart("+gd['id'].toString()+")'>";
                content += "<img src='/static/images/cart.png' style='width: 30px;height: 30px'>";
                content += "</a>";
                content += '<img src='+obj["type"]["picture"]+' style="height:30px;width:30px;">';
                content += "</p>";
                content += '<span class="">&yen; '+gd["price"]+'</span>';
                content += "</div>";
                typeGood = $(typeGood).append(content);
            });
            $("#main").append(typeGood);
        })
    }, 'json')
}


function add_cart(gid){
    $.get('add_cart',{'gid':gid}, function (data) {
        if (data['message'] ===0){
            alert('请先登录')
        }
    },'json')
}


$(function () {
    js_good();
});