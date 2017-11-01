$(".manage-status__WAITINGFORWORK").hover(
  function() {
    $(this).addClass('workdone-hover');
      $(this).text("MARK AS DONE");
  }, function() {
    $(this).text("WAITING FOR WORK DONE");
  }
);

$(".manage-status__WAITINGFORWORK").click(confirm_workdone);
$(".manage-status__WAITBUYERMARKDONE").click(confirm_workdone);



$(".manage-status__TOBEACCEPTED").hover(
  function() {
    $(this).addClass('cancel-hover');
      $(this).text("CANCEL");
  }, function() {
    $(this).text("TO BE ACCEPTED");
  }
);

$(".manage-status__WAITBUYERMARKDONE").hover(
  function() {
    $(this).addClass('workdone-hover');
      $(this).text("MARK AS DONE");
  }, function() {
    $(this).text("WAIT BUYER MARK DONE");
  }
);

$(".manage-status__TOBEACCEPTED").click(function(){
  var element = this
  $.ajax({
    url: '/ajax/cancel_work',
    data: {
      'order_no': $(this).attr('order')
    },
    dataType: 'json',
    success: function(data) {
      if(data.success) {
        $(element).attr("class", "manage-status__CANCELLED");
        $(element).unbind();
        $(element).text("CANCELLED")
      }
    }
  });
});

function confirm_workdone(){
  element = this
  $.ajax({
    url: '/ajax/buyer_confirm_workdone',
    data: {
      'order_no': $(this).attr('order')
    },
    dataType: 'json',
    success: function(data) {
      if(data.success) {
        $(element).attr("class", "manage-status__WORKDONE");
        $(element).unbind();
        $(element).text("WORK DONE")
      }
    }
  });
}
