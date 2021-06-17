<template>
  <div class="mb-3">
    <label class="form-label" :for="name" v-if="label">
      <slot>{{label}}</slot>
    </label>
    <input class="form-control" :type="type" :id="name" :name="name" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"/>
  </div>
</template>

<script>
import { reactive } from 'vue'

export default {
  name: 'CustomInput',
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
      default: ''
    },
    modelValue: {
      default: ''
    }
  },
  setup () {
    const data = reactive({
      checked: false
    })

    return { data }
  }
}
</script>

<style lang="scss" scoped>

</style>
