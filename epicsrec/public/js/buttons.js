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

function init_accordian(){
    $("dl.accordian dd").hide();
    $("dl.accordian a").click(function(){
            $("dd:visible").slideUp("slow");
            $(this).next().slideDown("slow",tutor_major);
            return false;
            });
}

var school_selected = false
var major_selected = false
var team_selected = false

function tutor_major(){
    school_selected = true;
    if (!major_selected){
        var tut_top = $("dd:visible").offset().top + 30 + "px";
        $("#tutorial").css({"top":tut_top,"left":"310px"});
        $("#tutorial").text("Choose your major...");
    }
}

function tutor_teams(){
    if(!major_selected){
        $("#tutorial").css({"top":"400px","left":"350px"});
        $("#tutorial").html("We think you might like one of the teams highlighted below. <p> Click on any teams you are interested in to learn more.");
    }
    major_selected = true
}

function tutor_learn(){
    if(!team_selected){
        $("#tutorial").text("Your selections will be used to help others find teams they like.");
        $("#tutorial").css({"top":"570px","left":"300px"});
    }
    team_selected = true
}

$(document).ready(function(){
    init_accordian();
    $(".button").mousedown(function(){
        $(this).addClass("depressed");
    });

    $(".button").mouseout(function(){
        $(this).removeClass("depressed active");
    });
    $(".button").mouseover(function(){
        $(this).addClass("active");
    });
    $(".button").mouseup(
        function(){
            $(this).removeClass("depressed");
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
		var is_team = $(this).filter('.team').size();
		if ( is_team ){
            if(!team_selected){
                tutor_learn();
                $("#tutorial").fadeTo(9000,1)
                $("#tutorial").fadeOut("slow")
            }
            $('#information').load( url );
		}
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
                        tutor_teams();
                    });
                 }
            );
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

