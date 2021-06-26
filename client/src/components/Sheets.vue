<template>
<nav>
  <div class="nav nav-tabs" id="nav-tab" role="tablist">
    <SheetTab v-for="name in sheetList"
              :key="name"
              :target="name"
              :handle-click="handleTabClick"
              :selected="isSelected(name)"
              >
      {{ name }}
    </SheetTab>
    <SheetTab :target="newSheet"
              :handle-click="handleTabClick"
              :selected="isSelected(newSheet)">
      <Icon icon="plus" /> Add new sheet
    </SheetTab>
  </div>
</nav>
<div class="tab-content" id="nav-tabContent">
  <SheetContent v-for="name in sheetList"
                v-bind:key="name"
                :name="name"
                :selected="isSelected(name)"
                >
    <table class="table table-bordered table-sm table-hover">
        <thead class="thead-dark">
          <tr>
            <th scope="col" v-for="column in columnList" :key="column.name">{{ column.name }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in sheetData" :key="index">
            <td v-for="(field, index) in row" :key="index">{{ field }}</td>
          </tr>
          <DataRow :sheet="file.selectedSheet" />
        </tbody>
      </table>
  </SheetContent>
  <SheetContent :name="newSheet" :selected="isSelected(newSheet)">Empty sheet</SheetContent>
</div>
</template>

<script>
import SheetTab from '@/components/SheetTab'
import SheetContent from '@/components/SheetContent'
import Icon from '@/components/Icon'
import { computed, reactive } from 'vue'
import { useStore } from 'vuex'
import DataRow from '@/components/DataRow'

export default {
  name: 'Sheets',
  components: { DataRow, Icon, SheetContent, SheetTab },
  props: {
    newSheet: {
      type: String,
      default: 'add-new'
    }
  },
  setup (props) {
    const file = reactive({
      selectedSheet: 'add-new'
    })

    const store = useStore()

    const sheetList = computed(() => store.getters['workbook/getSheetNames'])
    const columnList = computed(() => store.getters['workbook/getColumnNames'](file.selectedSheet))
    const sheetData = computed(() => store.getters['workbook/getData'](file.selectedSheet))

    if (file.selectedSheet === '' && store.getters['workbook/getSheetNames'].length !== 0) {
      file.selectedSheet = store.getters['workbook/getSheetNames'][0]
    }

    async function handleTabClick (sheetName) {
      file.selectedSheet = sheetName

      if (sheetName !== props.newSheet) {
        await store.dispatch('workbook/fetchData', { sheetName, force: true })
      }
    }

    function isSelected (value) {
      return file.selectedSheet === value
    }

    return {
      file,
      handleTabClick,
      isSelected,
      sheetList,
      columnList,
      sheetData
    }
  }
}
</script>

<style scoped>

</style>
