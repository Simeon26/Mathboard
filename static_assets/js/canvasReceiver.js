var canvas;
var updatecounter = 1;

$(document).ready(function () {
    canvas = new fabric.StaticCanvas('c', {backgroundColor: "white"});
    window.addEventListener('resize', resizeCanvas, false);

    resizeCanvas();
    loaddrawing();
    loadcomments();

    $("#messageBox").keyup(function (event) {
        if (event.keyCode == 13) {
            sendMessage();
        }
    });
});

function resizeCanvas() {
    canvas.setHeight(window.innerHeight - 52);
    canvas.setWidth(document.body.clientWidth);
    canvas.renderAll();
}

setInterval(prepareDownloadButton, 3000);
function prepareDownloadButton() {
	$("#save-canvas").attr("href", canvas.toDataURL('png'));
}

function openChat() {
    $("#chatbar").toggleClass("toggle");
}

function sendMessage() {
    if ($('#messageBox').val() !== '') {
        var room = getParameterByName("r");
        var comment = "<li class='comment'>" + getCookie("name") + ": " + $('#messageBox').val() + "</li>";
        var data = "room=".concat(room).concat("&comment=").concat(comment);

        $.ajax({
            url: "/comment",
            type: "POST",
            data: data,
            success: function (response) {
                loadcomments();
            },
        });

        $('#messageBox').val("");
    }
}


function loaddrawing() {
    var room = getParameterByName("r");
    $("#roomnumber").html(room);
    var data = "room=".concat(room).concat("&updatecounter=").concat(updatecounter);
    $.ajax({
        url: "/view",
        type: "POST",
        data: data,
        success: function (response) {
            if (response !== null && response !== "") {
                //response = decodeURIComponent(response).replace("http", "https");
                updatecounter = response.split("sometext like this sh3ould never a ctually apper so is a grt div%er")[0];
                newcanvas = response.split("sometext like this sh3ould never a ctually apper so is a grt div%er")[1];
                canvas.loadFromJSON(newcanvas);
            }
            //        canvas.loadFromJSON(c);
        },
    });
}

function loadcomments() {
    var room = getParameterByName("r");
    $.ajax({
        url: "/comment?r=" + room,
        type: "GET",
        success: function (response) {
            if (response !== null && response !== "") {
                $("#messageList").html(response);
                //Ensure the list is always at the bottom
                $('#messages').scrollTop($('#messages')[0].scrollHeight);
            }
        }
    });
}

loaddrawing();

window.setInterval(function () {
    loaddrawing();
}, 3000);
window.setInterval(function () {
    loadcomments();
}, 1000);

function getParameterByName(name) {
    var url = window.location.href;
    var name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

$("#messageBox").keyup(function(event){
    if(event.keyCode == 13){
        sendMessage();
    }
});