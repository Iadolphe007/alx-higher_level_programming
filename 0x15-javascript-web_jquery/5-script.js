$(document).ready(function() {
    $('DIV#add_item').click(function() {
        const newTag = $("<li>Item</li>");
        $("UL.my_list").append(newTag)
    });
});