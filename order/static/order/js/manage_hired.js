$(".manage-status__WAITINGFORWORK").hover(
  function() {
    $(this).addClass('workdone-hover');
    var order_no = $(this).attr('order')
    order_no = Number(order_no) * 9876 - 5555
    $(this).html('<a class="rate-work" href="/rate_employee/' + btoa(order_no) + '">CONFIRM WORK DONE</a>');
  }, function() {
    $(this).text("WAITING FOR WORK");
  }
);

$(".manage-status__WAITBUYERMARKDONE").hover(
  function() {
    $(this).addClass('workdone-hover');
    var order_no = $(this).attr('order')
    order_no = Number(order_no) * 9876 - 5555
    $(this).html('<a class="rate-work" href="/rate_employee/' + btoa(order_no) + '">CONFIRM WORK DONE</a>');
  }, function() {
    $(this).text("WAIT BUYER MARK DONE");
  }
);

$(".manage-status__TOBEACCEPTED").hover(
  function() {
    $(this).addClass('cancel-hover');
      $(this).text("CANCEL");
  }, function() {
    $(this).text("TO BE ACCEPTED");
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

$(".close-button").click(function() {
  var element = $(this)
  bootbox.confirm("Are you sure? your rating will be decrease by 10%", function(result) {
    if(result) {
      $.ajax({
        url: '/ajax/cancel_work_penalty',
        data: {
          'order_no': element.attr('order'),
          'username': element.attr('username'),
          'usertype': element.attr('usertype')
        },
        dataType: 'json',
        success: function(data) {
          if(data.success) {
            console.log("success!!")
          }
        }
      });
    }
  })
});
