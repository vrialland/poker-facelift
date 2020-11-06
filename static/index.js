var socket = io('http://127.0.0.1:5000/');
//socket.emit('join', 'jean-michel');

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
    }
  }
});

var app = new Vue({ 
    el: '#app',
    data: {
        message: 'Poker FaceLift',
        username: ''
    }
});
