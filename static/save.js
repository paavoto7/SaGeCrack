
$(function() {
    $("input[name='password']").keypress(function(e) {
        if (e.which == 13) {
            $("#savebut").click();
        }
    });
});

$(function() {
    $("#savebut").on("click", function() {
        $.post("/save", {
            service: $("input[name='service']").val(),
            name: $("input[name='name']").val(),
            password: $("input[name='password']").val()
        }, function(data) {
            $("#sucs").text(data.result);
            $("input").val("");
        }, "json");
    });
});