const header = $("header");
const toggleHeader = $("#toggle_header");
toggleHeader.on("click", function() {
  const currentClass = header.attr("class");
  if (currentClass === "red") {
    header.removeClass("red").addClass("green");
  } else {
    header.removeClass("green").addClass("red");
  }
});
