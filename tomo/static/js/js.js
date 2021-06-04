const homeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/home/'
);

homeSocket.onopen = function(e) {
    homeSocket.send(JSON.stringify({
        'status': 'connected',
    }));
}

homeSocket.onclose = function(e) {
    console.error('Home socket closed unexpectedly');
};

homeSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);

    //if (document.getElementById("online-status-0".replace("0", data.user_id)) === null) {
        name_span = document.createElement('span');
        name_span.textContent = data.username;
        status_span = document.createElement('span');
        img = document.createElement('img');
        img.src = "https://img.icons8.com/emoji/48/000000/green-circle-emoji.png";
        img.width = 15;
        img.height = 15;
        status_span.appendChild(img);
        div = document.createElement('div');
        div.className = "col-md-12 a-friend";
        div.id = "online-status-0".replace("0", data.user_id.toString());
        div.setAttribute('onclick', "window.location='/user/0'".replace("0", data.user_id));
        div.setAttribute('role', 'button');
        div.appendChild(name_span);
        div.appendChild(status_span);
        document.getElementById("friends-status").appendChild(div);
    //}
};
