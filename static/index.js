var socket = io('http://127.0.0.1:5000/');
socket.emit('join');

var app = new Vue({ 
    el: '#app',
    data: {
        message: 'Hello Vue!'
    }
});
