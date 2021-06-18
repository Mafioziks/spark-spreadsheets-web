<template>
<button
  class="nav-link"
  :class="{
    'active': selected
  }"
  :id="tabId"
  data-bs-toggle="tab"
  :data-bs-target="targetId"
  type="button"
  role="tab"
  :aria-controls="ariaControls"
  :aria-selected="ariaSelected"
  @click="handleClickInternal">
  <slot></slot>
</button>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'SheetTab',
  props: {
    target: {
      type: String,
      require: true
    },
    selected: {
      type: Boolean,
      default: false
    },
    handleClick: {
      type: Function,
      required: true
    }
  },
  setup (props) {
    const targetId = computed(() => '#nav-' + props.target)
    const tabId = computed(() => 'nav-' + props.target + '-tab')
    const ariaControls = computed(() => 'nav-' + props.target)

    const ariaSelected = computed(() => props.selected ? 'true' : 'false')

    function handleClickInternal () {
      props.handleClick(props.target)
    }

    return { tabId, targetId, ariaControls, ariaSelected, handleClickInternal }
  }
}
</script>

<style scoped>

</style>
