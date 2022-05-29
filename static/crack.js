

function disable() {
    document.getElementById("subm").disabled = true;
}

$(function() {
    $("#subm").on("click", function() {
        $.getJSON("/cracked", {
            passw: $("input[name='crackp']").val(),
            type: $("select[name='type']").val()
        }, function(data) {
            $("#result").val(data.result);
            $("#time").text(data.time)
            $("#subm").prop("disabled", false);
        });
    });
});