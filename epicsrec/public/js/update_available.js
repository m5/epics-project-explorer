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
var send_availability = function(caller){
  var data ='';
  $('.selected').each(function(){
      data += this.id + ';';
    });
  alert(data);
  $.post('/admin/update_available',{
      selected: data
        },
    function(xml){
      caller.after("<span>Update Successful</span>").fadeOut(1000)
    }
    );
};
  

$(document).ready(function(){
    $(".update").click(function(){
        alert("poke!");
        send_availability(this);
      });
    $(".button").mousedown(function(){
        $(this).addClass("depressed");
      });
    $(".button").mouseout(function(){
        $(this).removeClass("depressed active");
      });
    $(".button").mouseover(function(){
        $(this).addClass("active");
      });
    $(".button").mouseup(function(){
        $(this).removeClass("depressed");
        $(".button").stop(1,1);
        if( $(this).hasClass("selected") ){
          $(this).removeClass("selected");
        }else{
          $(this).addClass("selected");
        }
      });
  });

