Vue.component('players-list', {
  template: `
    <span>
      <li class="player" v-for="player in players">
        <span v-if="player.name == name">
          <strong>{{player.name}}</strong>
          <span class="choice">&nbsp;| {{player.choice}}</span>
        </span>
        <span v-else>
          {{player.name}}
          <span class="choice">&nbsp;|
            <span v-if="hideChoices">
              <span v-if="player.choice" class="hidden">0</span>
            </span>
            <span v-else>{{player.choice}}</span>
          </span>
        </span>
      </li>
    </span>`,
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
    }
  },
  props: ['players', 'name', 'finished']
})
