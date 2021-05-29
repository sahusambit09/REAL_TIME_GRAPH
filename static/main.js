var socket=new WebSocket('ws://127.0.0.1:9000/ws/polData/')
socket.onmessage = function(e){
    var djangoData=JSON.parse(e.data)
    console.log(djangoData)
}