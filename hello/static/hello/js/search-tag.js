var tags = {};
var list = [];


// Create a new list item when clicking on the "Add" button
function newElement() {
  var inputValue = document.getElementById("tagInput").value;

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

    a.role = "button"
    a.href = "/tags/"+tag+"/";
    a.className = "btn btn-light btn-sm";
    a.appendChild(t);

    div.appendChild(a);

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");

    span.id = i;
    span.appendChild(txt);
    span.onclick = function() {delElement(this);};
    div.appendChild(span);
    document.getElementById("tags").appendChild(div);
  }
  document.getElementById('tag_list').value = list.toString();
}
