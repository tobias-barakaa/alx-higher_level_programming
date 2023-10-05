$(document).ready(function() {
    // Add item
    $("#add_item").click(function() {
        // Create a new <li> element with text "Item"
        var newItem = $("<li>").text("Item");
        // Append the new item to the <ul> with class "my_list"
        $(".my_list").append(newItem);
    });

    // Remove item
    $("#remove_item").click(function() {
        // Select the last <li> element in the list and remove it
        $(".my_list li:last-child").remove();
    });

    // Clear list
    $("#clear_list").click(function() {
        // Remove all <li> elements from the list
        $(".my_list").empty();
    });
});

