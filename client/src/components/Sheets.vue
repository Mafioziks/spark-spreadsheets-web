<template>
<nav>
  <div class="nav nav-tabs" id="nav-tab" role="tablist">
    <SheetTab v-for="(sheet, name) in sheets"
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
  <SheetContent v-for="(sheet, name) in sheets"
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
import { reactive } from 'vue'

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

    if (file.selectedSheet === '' && Object.keys(props.sheets).length !== 0) {
      file.selectedSheet = Object.keys(props.sheets)[0]
    }

    function handleTabClick (sheetName) {
      file.selectedSheet = sheetName
    }

    function isSelected (value) {
      return file.selectedSheet === value;
    }

    return { file, handleTabClick, isSelected }
  }
}
</script>

<style scoped>

</style>
