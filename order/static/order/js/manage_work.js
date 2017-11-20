$(".manage-status__WAITINGFORWORK").hover(
  function() {
    $(this).addClass('workdone-hover');
    var order_no = $(this).attr('order')
    order_no = Number(order_no) * 9876 - 5555
    $(this).html('<a class="rate-work" href="/rate_employer/' + btoa(order_no) + '">CONFIRM WORK DONE</a>');
  }, function() {
    $(this).text("WAITING FOR WORK DONE");
  }
);

$(".manage-status__WAITSELLERMARKDONE").hover(
  function() {
    $(this).addClass('workdone-hover');
    var order_no = $(this).attr('order')
    order_no = Number(order_no) * 9876 - 5555
    $(this).html('<a class="rate-work" href="/rate_employer/' + btoa(order_no) + '">CONFIRM WORK DONE</a>');
  }, function() {
    $(this).text("WAIT SELLER MARK DONE");
  }
);

$(".manage-status__TOBEACCEPTED").hover(
  function() {
    $(this).addClass('accept-hover');
      $(this).text("ACCEPT");
  }, function() {
    $(this).text("TO BE ACCEPTED");
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
        $(element).removeClass("manage-status__TOBEACCEPTED");
        $(element).addClass("manage-status__ACCEPTED");
        $(element).unbind();
        $(element).text("ACCEPTED!")
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
            location.reload();
          }
        }
      });
    }
  })
});
