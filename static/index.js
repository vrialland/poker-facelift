let originUrl = 'http://127.0.0.1:5000/'

if (window.location.origin === 'https://poker-facelift.herokuapp.com') {
  originUrl = 'https://poker-facelift.herokuapp.com/'
}

let socket = io(originUrl)

let app = new Vue({
  el: '#app',
  data: {
    message: 'Poker FaceLift',
      connected: false,
      name: '',
      players: [],
      observers: [],
      finished: false
  },
  methods: {
    enter: function(name) {
      this.name = name;
      this.connected = true;
    },
    onRoomUpdate: function(room) {
      this.players = room.players
      this.observers = room.observers
      this.finished = room.finished
    }
  },
  created: function() {
    socket.on('room_update', this.onRoomUpdate)
    // when closing the tab / page, we send an event
    window.addEventListener('beforeunload', (event) => {
      socket.emit('left', this.name)
    })
  }
})
