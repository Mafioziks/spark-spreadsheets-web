<template>
<i
  class="bi"
  v-bind:class="icon"
/>
</template>

<script>
export default {
  name: 'Icon',
  props: {
    icon: {
      type: String
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~bootstrap-icons/font/bootstrap-icons.css";
</style>
