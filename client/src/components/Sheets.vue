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
    {{ name }}
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

export default {
  name: 'Sheets',
  components: { Icon, SheetContent, SheetTab },
  props: {
    sheets: {
      type: Object
    }
  },
  data () {
    return {
      newSheet: 'add-new'
    }
  },
  setup (props) {
    const file = reactive({
      selectedSheet: 'add-new'
    })

    const store = useStore()

    const sheetList = computed(() => store.getters['workbook/getSheetNames'])

    if (file.selectedSheet === '' && store.getters['workbook/getSheetNames']().length !== 0) {
      file.selectedSheet = store.getters['workbook/getSheetNames'][0]
    }

    function handleTabClick (sheetName) {
      file.selectedSheet = sheetName
    }

    function isSelected (value) {
      return file.selectedSheet === value
    }

    return {
      file,
      handleTabClick,
      isSelected,
      sheetList
    }
  }
}
</script>

<style scoped>

</style>
