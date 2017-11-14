$(function() {
  $("#tagInput").autocomplete({
    source: "/get_tags/",
    minLength: 2,
  });
});
