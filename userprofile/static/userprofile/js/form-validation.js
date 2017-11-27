function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

$('.custom-file-input').on('change',function(){
  $(this).next('.form-control-file').addClass("selected").html($(this).val());
})
