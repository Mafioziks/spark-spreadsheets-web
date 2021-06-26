<template>
  <tr>
      <td v-for="value in schema" :key="value.name">
        <input class="form-control" type="text" :name="value.name" v-model="formData[value.name]" />
      </td>
  </tr>
  <tr>
    <td :colspan="spanAmount"></td>
    <td>
      <Button class="btn-block" @click="addRow"><Icon icon="bi-plus-lg"/> Store and add row</Button>
    </td>
  </tr>
</template>

<script>
import { computed, reactive } from 'vue'
import { useStore } from 'vuex'
import Button from '@/components/Button'
import Icon from '@/components/Icon'
import { isEmpty } from '@/utils/dom'

export default {
  name: 'DataRow',
  components: { Icon, Button },
  props: {
    sheet: {
      type: String,
      required: true
    }
  },
  setup (props) {
    const store = useStore()

    const schema = computed(() =>
      store.getters['workbook/getColumnNames'](props.sheet)
    )
    const spanAmount = computed(() =>
      Math.max(store.getters['workbook/getColumnNames'](props.sheet).length - 1, 0)
    )

    const formData = reactive({})

    console.log(schema)

    async function addRow (event) {
      // TODO: Submit data
      if (isEmpty(formData)) {
        return
      }

      await store.dispatch('workbook/addDataRow', { sheetName: props.sheet, values: [formData] })

      console.log('resetting formData')

      Object.keys(formData).forEach(key => { formData[key] = '' })

      console.log('resetted formData')
    }

    return { addRow, schema, formData, spanAmount }
  }
}
</script>

<style scoped>

</style>
