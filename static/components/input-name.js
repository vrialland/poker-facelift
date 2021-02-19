Vue.component('input-name', {
  template: `
    <div>
      <label for="name">Your name:</label>
      <input type="text" id="name" v-model="username">
      <button @click="player">Play</button>
      <button @click="observe">Observe</button>
    </div>`,
  data: function () {
    return {
      username: null
    }
  },
  methods: {
    player: function() {
      socket.emit('join_player', this.username)
      this.$emit('enter', this.username)
    },
    observe: function() {
      socket.emit('join_observer', this.username)
      this.$emit('enter', this.username)
    }
  }
})
