var selected_image = '/img/button-yellow-depressed.png';
var recomended_image = '/img/button-recomended.png';
var button_image = '/img/button-unlit.png';

function cfade(obj, trans_time){
    if (typeof trans_time == "undefined"){
        trans_time = 500;
    }
    var o_left = $(obj).offset().left;
    var o_top  = $(obj).offset().top;
    var clone = $(obj).clone();
    $(clone).css({position:"absolute",left:o_left,top:o_top})
        .addClass("hover")
        .insertAfter(obj)
        .fadeOut(trans_time,function(){
                $(clone).remove();});
    return obj;
}

$(document).ready(function(){
    $("span.button").mousedown(function(){
        $(this).addClass("depressed");
    });

    $("span.button").mouseup(function(){
        $(this).removeClass("depressed");
    });

    $("span.button").mouseout(function(){
        $(this).removeClass("depressed active");
    });
    $("span.button").mouseover(function(){
        $(this).addClass("active");
    });
    $("span.button").click(
        function(){
            $(".button").stop(1,1);
            var des_name = '';
            var s_name = '';
            if( $(this).hasClass("selected") ){
                $(this).removeClass("selected");
                des_name = $(this).attr("name");
            }else{
                $(this).addClass("selected");
                s_name = $(this).attr("name");
                var url = '/choose/info/' + s_name;
                $('#information').load( url );
            }
            $.post('/choose/ajax',
                {
                selected: s_name,
                deselected: des_name,
                sid_hash: $('#sid_hash').attr('value')
                },
                function(xml){
                    $(xml).find('rec').each(function(){
                        var team = $(this).text();
                        var rec_button = $('[name='+team+']');
                        cfade(rec_button,700);
                        $(rec_button).addClass("recomended");
                    });
                    $('.recomended').each(function(){
                        var rec_selector = "[name='"+$(this).attr('name')+"']";
                        var matches = $(xml).find(rec_selector);
                        if( matches.size()==0){
                            cfade(this,700);
                            $(this).removeClass("recomended");
                        }
                    });
                 }
            );
        });
    var lit_school = '';
    var fgcolor = '#cecaff';
    var bgcolor = '#202061';
    $(".button.major").each(function(i){
        var school = $(this).children("[name='school']").text();
        var school_print = school.replace(/\_/,' ');
        var first_button = $('.'+school+':first');
        var first_x = first_button.offset().left;
        var first_y = first_button.offset().top;
        $(this).mouseover(function(){
            $('.'+school).css({borderColor:fgcolor});
            $('#school').html(school_print).css({opacity:0.7,top:first_y,left:first_x}).stop(1,1).show();
        }).mouseout(function(){
            $('.'+school).css({borderColor:bgcolor});
            $('#school').stop(1,1).hide('fast');
        });
    });
    $(".button.team").each(function(i){
        var tooltip = $("#description");
        var description_suspect =  $(this).children("[name='title']").text() + "<br/>"
                          +$(this).children("[name='description']").text();
        if (description_suspect != "<br/>"){
            var description = description_suspect;
        }else{
            var description = "";
        }
        $(this).mouseover(function(){
            if (description){
               tooltip.stop(1).css({opacity:0.8}).fadeIn("fast")
               .html( description );
            }
        }).mousemove(function(kmouse){
            var tt_left = kmouse.pageX + 15;
            var tt_right = tt_left  + tooltip.width() + 20;
            if ( tt_right > $("body").width() ){
                tt_left -= tooltip.width();
            }
            var tt_top = kmouse.pageY - tooltip.height() - 20;
            tooltip.css({left:tt_left, top:tt_top});
        }).mouseout(function(){
            tooltip.stop(1).fadeOut("fast");
        });
    });
});

