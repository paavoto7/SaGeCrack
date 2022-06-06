

function type(value) {
    var set;
    if (value == 0) {
        set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefqhijklmnopqrstuvwxyz1234567890!#¤%&/()=?'*,.-_'$@€";
    }
    else if (value == 1) {
        set = "1234567890"
    }
    else if (value == 2) {
        set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefqhijklmnopqrstuvwxyz";
    }
    else {
        return 0;
    }
    return set;
}

function NewPassw() {
    var result = '';
    var length = document.getElementById("length").value;
    var x = document.getElementById("type");
    var set = type(x.value);

    for (var i = 0; i < length; i++) {
        result += set.charAt(Math.floor(Math.random() * set.length));
    }
    document.getElementById("NewPass").value = result;
    $("#copy").val(result);
}