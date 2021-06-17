<template>
<div class="tab-pane fade"
     v-bind:class="{
        'show active': selected
     }"
     :id="contentId"
     role="tabpanel"
     :aria-labelledby="arialLabel">
  <slot></slot>
</div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'SheetContent',
  props: {
    name: {
      type: String,
      required: true
    },
    selected: {
      type: Boolean,
      default: false
    }
  },
  setup (props) {
    const contentId = computed(() => 'nav-' + props.name)
    const arialLabel = computed(() => 'nav-' + props.name + '-tab')

    return { contentId, arialLabel }
  }
}
</script>

<style scoped>

</style>
