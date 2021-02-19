Vue.component('observers-list', {
  template: `
    <span id="observers">
      <li v-for="observer in observers">
        <span v-if="observer.name == name">
          <strong>{{observer.name}}</strong>
        </span>
        <span v-else>
          {{observer.name}}
        </span>
      </li>
    </span>`,
  props: ['observers', 'name']
})
