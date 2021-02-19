Vue.component('room', {
  template: `
    <div>
      <h3>Welcome {{name}}</h3>
      <div class="players">
        <ul id="players">
          <players-list :players="players" :name="name" :finished="finished"/>
          <observers-list :observers="observers" :name="name"/>
        </ul>
      </div>
      <br>
      <vote :name="name"/>
      <br><br>
      <button @click="reveal()">Reveal</button>
      <button @click="clear()">Clear</button>
      <br><br>
    </div>`,
  methods: {
    reveal: function() {
      socket.emit('reveal')
    },
    clear: function() {
      socket.emit('clear')
    }
  },
  props: ['players', 'observers', 'name', 'finished']
})
