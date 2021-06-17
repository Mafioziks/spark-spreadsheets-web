<template>
<div class="mb-3 btn" v-bind:class="{'btn-dark': data.checked}" @click="handleClick">
    <label class="form-label pt-2" :for="name" v-if="label">
      <slot>{{label}}</slot>
    </label>
    <input
      class="form-control"
      type="checkbox"
      :id="name"
      :name="name"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :checked="data.checked"
    />
  </div>
</template>

<script>
import { reactive } from 'vue'

export default {
  name: 'ToggleButton',
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

    function handleClick () {
      data.checked = !data.checked
    }

    return { data, handleClick }
  }
}
</script>

<style lang="scss" scoped>
input {
  display: none;
}
</style>
