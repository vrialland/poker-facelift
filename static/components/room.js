Vue.component('room', {
  template: `
    <div>
      <h3>Welcome {{name}}</h3>
      <label for="players">List of players:</label>
      <ul id="players">
        <li class="player" v-for="player in players">
          <span v-if="player.name == name">
            <strong>{{player.name}}</strong>
            <span class="choice">&nbsp;| {{player.choice}}</span>
          </span>
          <span v-else>
            {{player.name}}
            <span class="choice">&nbsp;| <span v-bind:class="{hidden: hideChoices}">{{player.choice}}</span></span>
          </span>
        </li>
      </ul>
      <label for="observers">List of observers:</label>
      <ul id="observers">
        <li v-for="observer in observers">
          <span v-if="observer.name == name">
            <strong>{{observer.name}}</strong>
          </span>
          <span v-else>
            {{observer.name}}
          </span>
        </li>
      </ul>
      <vote v-bind:name="name"/>
      <br><br>
      <button v-on:click="reveal()">Reveal</button>
      <button v-on:click="clear()">Clear</button>
    </div>`,
  computed: {
    hideChoices: function() {
      if (this.finished) {
        return false
      }
      for (const player of this.players) {
        if (!player.choice) {
          return true
        }
      }
      return false
    },
  },
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
