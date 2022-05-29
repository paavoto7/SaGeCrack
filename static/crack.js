

$(function() {
    $("#subm").on("click", function() {
        $.getJSON("/cracked", {
            passw: $("input[name='crackp']").val(),
            type: $("select[name='type']").val()
        }, function(data) {
            $("#result").text(data.result);
            $("#time").text(data.time)
        });
    });
});