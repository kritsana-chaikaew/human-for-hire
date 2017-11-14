var tags = {};
var list = [];

// Create a new list item when clicking on the "Add" button
function newElement() {
  var inputValue = document.getElementById("tagInput").value;
  inputValue = inputValue.toLowerCase();

  if (inputValue === '') {
    alert("You must write something!");
  } else if (!list.includes(inputValue)) {
    list.push(inputValue);
  } else {
    alert("tag is added!");
  }

  document.getElementById("tagInput").value = "";
  render();
}

function delElement(obj) {
  var id = obj.id;

  list.splice(id, 1);
  render();
}

function render() {
  document.getElementById("tags").innerHTML = "";

  for (var i=0; i<list.length; i++) {
    var tag = list[i];
    var div = document.createElement("div");
    var a = document.createElement("a");
    var t = document.createTextNode(tag);
    var span = document.createElement("span");
    var icon = document.createElement("i");

    a.role = "button"
    a.href = "/tags/"+tag+"/";
    a.className = "btn btn-light btn-sm btn-secondary";
    icon.className = "fa fa-times";
    span.className = "btn btn-light btn-sm btn-secondary";
    span.onclick = function() {delElement(this);};
    span.id = i;
    div.className = "btn-group mr-2";

    a.appendChild(t);
    span.appendChild(icon);
    div.appendChild(a);
    div.appendChild(span);

    document.getElementById("tags").appendChild(div);
  }
  document.getElementById('tag_list').value = list.toString();
}
