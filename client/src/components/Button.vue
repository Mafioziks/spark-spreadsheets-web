<template>
<button
  class="btn"
  v-bind:class="{
    'btn-primary': buttonType === 'primary',
    'btn-secondary': buttonType === 'secondary',
    'btn-success': buttonType === 'success',
    'btn-danger': buttonType === 'danger',
    'btn-warning': buttonType === 'warning',
    'btn-info': buttonType === 'info',
    'btn-light': buttonType === 'light',
    'btn-dark': buttonType === 'dark'
  }" >
  <slot></slot>
</button>
</template>

<script>
export default {
  name: 'Button',
  props: {
    buttonType: {
      type: String,
      default: 'primary',
      validator: (value) => {
        return ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'].indexOf(value) !== -1
      }
    }
  }
}
</script>

<style scoped>

</style>
