<template>
<div
  class="alert alert-dismissible fade show"
  v-bind:class="{
    'alert-primary': type === 'primary',
    'alert-secondary': type === 'secondary',
    'alert-success': type === 'success',
    'alert-danger': type === 'danger',
    'alert-warning': type === 'warning',
    'alert-info': type === 'info',
    'alert-light': type === 'light',
    'alert-dark': type === 'dark'
  }"
  role="alert">
  {{message}}
<!--  <button type="button" class="close" data-dismiss="alert" aria-label="Close">-->
<!--    <span aria-hidden="true">&times;</span>-->
<!--  </button>-->
</div>
</template>

<script>
export default {
  name: 'Alert',
  props: {
    message: {
      default: ''
    },
    type: {
      validator (value) {
        return ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'].indexOf(value) !== -1
      }
    }
  },
  setup () {
    // TODO: Add hiding and reset
  }
}
</script>

<style scoped>

</style>
