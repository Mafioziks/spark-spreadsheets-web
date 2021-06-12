<template>
  <div class="mb-3">
    <label class="form-label" :for="name">{{ label }}</label>
    <input class="form-control" :type="type" :id="name" :name="name" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" />
  </div>
</template>

<script>
export default {
  name: 'Input',
  emits: ['update:modelValue'],
  props: {
    name: {
      type: String,
      default: 'sample'
    },
    type: {
      type: String,
      default: 'text'
    },
    label: {
      type: String,
      default: 'sample'
    },
    modelValue: {
      default: ''
    }
  },
  setup () {
  }
}
</script>

<style scoped>

</style>
