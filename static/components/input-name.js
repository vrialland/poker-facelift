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
      socket.emit('join', this.username)
      this.$emit('enter', this.username)
    }
  }
})
