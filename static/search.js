// Functions contain Jquery

// Send data to the server and receive a response with Ajax
$(function() {
    $("#search").on("keyup", function() {
        $.getJSON("/search", {
            q: $("#search").val(),
        },  function(data) {
            let html = '';
            // Loop through the receiver JSON data
            for (let i in data) {
                let serv = data[i].service;
                // Make the data formatted as a list item
                html += '<li class="item">' + serv + "</li>";
            }
            $("ul").html(html);
        });
    });
});


// Fetch additional data
$(function() {
    $(".list").click(function() {
        var serv = $(this).find(".item").html();
        $.getJSON("/info", {
            service: serv,
        }, function(data) {
            // If more than one account prompt for more info
            if (data.length > 1) {
                $("#additional").css("visibility", "visible");
                $("#additional").keyup(function() {
                    for (let i in data) {
                        if (data[i].username == $(this).val()) {
                            $("#service").html(data[i].service);
                            $("#username").html(data[i].username);
                            $("#srcpassword").html(data[i].password);
                            $("#additional").css("visibility", "hidden").val(null);
                            return;
                        }
                    }
                }
            )}
            // If only one then use the data received
            else {
                $("#service").html(data[0].service);
                $("#username").html(data[0].username);
                $("#srcpassword").html(data[0].password);
            }
        });
    });
});