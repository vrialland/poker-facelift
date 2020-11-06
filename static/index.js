var socket = io('http://127.0.0.1:5000/');

Vue.component('room', {
  template: `
    <div>
      <h3>Room</h3>
      <ul>
        <li v-for="participant in participants">
          {{participant}}
        </li>
      </ul>
    </div>`,
  props: ['participants']
});

Vue.component('input-name', {
  template: `
    <div>
      <label for="name">Your name:</label>
      <input type="text" id="name" v-model="username">
      <button v-on:click="enter">Enter</button>
    </div>`,
  data: function () {
    return {
      username: null
    }
  },
  methods: {
    enter: function() {
      socket.emit('join', this.username);
      this.$emit('enter');
    }
  }
});

var app = new Vue({ 
  el: '#app',
  data: {
    message: 'Poker FaceLift',
      connected: false,
      participants: []
  },
  methods: {
    enter: function() {
      this.connected = true;
    },
    onParticipantsUpdate: function(participants) {
      this.participants = participants;
    }
  },
  created: function() {
    socket.on('participants_update', this.onParticipantsUpdate);
  }
});
