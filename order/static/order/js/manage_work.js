$(".manage-status__WAITINGFORWORK").hover(
  function() {
    $(this).addClass('workdone-hover');
      $(this).text("MARK AS DONE");
  }, function() {
    $(this).text("WAITING FOR WORK");
  }
);

$(".manage-status__WORKDONENOTRATED").hover(
  function() {
    $(this).addClass('workdone-hover');
    var order_no = $(this).attr('order')
    $(this).html('<a class="rate-work" href="/rate_employer/' + order_no + '">RATE</a>');
  }, function() {
    $(this).text("WORK DONE NOT RATED");
  }
);

$(".manage-status__WAITINGFORWORK").click(confirm_workdone);
$(".manage-status__WAITSELLERMARKDONE").click(confirm_workdone);



$(".manage-status__TOBEACCEPTED").hover(
  function() {
    $(this).addClass('accept-hover');
      $(this).text("ACCEPT");
  }, function() {
    $(this).text("TO BE ACCEPTED");
  }
);

$(".manage-status__WAITSELLERMARKDONE").hover(
  function() {
    $(this).addClass('workdone-hover');
      $(this).text("MARK AS DONE");
  }, function() {
    $(this).text("WAIT SELLER MARK DONE");
  }
);

$(".manage-status__TOBEACCEPTED").click(function(){
  var element = this
  $.ajax({
    url: '/ajax/accept_work',
    data: {
      'order_no': $(this).attr('order')
    },
    dataType: 'json',
    success: function(data) {
      if(data.success) {
        $(element).attr("class", "manage-status__ACCEPTED");
        $(element).unbind();
        $(element).text("ACCEPTED!")
      }
    }
  });
});

function confirm_workdone(){
  element = this
  $.ajax({
    url: '/ajax/seller_confirm_workdone',
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
