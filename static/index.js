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
      name: 'Toto',
      players: []
  },
  methods: {
    enter: function(name) {
      this.name = name;
      this.connected = true;
    },
    onPlayersUpdate: function(players) {
      this.players = players;
    }
  },
  created: function() {
    socket.on('players_update', this.onPlayersUpdate)
    // when closing the tab / page, we send an event
    window.addEventListener('beforeunload', (event) => {
      console.log('left called')
      socket.emit('left', this.name)
    })
  }
})
