

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