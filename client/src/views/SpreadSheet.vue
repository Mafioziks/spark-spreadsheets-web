<template>
  <div class="container-fluid">
    <header class="page-header">
      <div class="row mb-3">
        <div class="col-6">
          <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
            <Dialog id="file-modal" button-type="secondary">
              <template v-slot:title>
                Choose file
              </template>

              <template v-slot:default>

                <Alert type="danger" v-if="errors.fileSelectModal">{{errors.fileSelectModal}}</Alert>
                <form @submit.prevent="handleFileCreate">
                  <CustomInput v-model="database.new" label="New File" name="new-name"/>
                  <Button><Icon icon="bi-plus"/> Create</Button>
                </form>
                <hr/>
                <div class="file-modal-content">
                  <div
                    class="btn btn-light btn-block file-select text-left text-uppercase pt-2"
                    v-bind:class="{'btn-dark': name === database.selected}"
                    v-for="(name, index) in database.list"
                    v-bind:key="index"
                    @click="handleClickToChildInput"
                  >
                    <label for="file-select" class="pt-2"><Icon icon="bi-file-earmark-ruled"/> {{ name }}</label>
                    <input type="radio" :value="name" name="file" id="file-select" class="hide" @click="handleFileSelected">
                  </div>
                </div>
              </template>

              <template v-slot:footer>
                <Button buttonType="primary" @click="handleFileOpen">Open</Button>
              </template>
            </Dialog>
            <Button button-type="secondary"><Icon icon="bi-save" /> Save</Button>

            <div class="btn-group" role="group">
              <Button
                id="btnGroupDrop1"
                button-type="secondary"
                class="dropdown-toggle"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false">
                <Icon icon="bi-cloud-download" />
                Export
              </Button>
              <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                <a class="dropdown-item" href="#"><Icon icon="bi-file-earmark-excel" /> Excel (.xlsx)</a>
                <a class="dropdown-item" href="#"><Icon icon="bi-file-earmark-text" /> CSV (.csv)</a>
              </div>
            </div>
          </div>
        </div>
        <div class="col-6 text-right">
          <ProfileButton />
        </div>
      </div>
    </header>
    <div>
      <div class="row">
        <div class="col-12">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon1">f=</span>
            </div>
            <input type="text" class="form-control" placeholder="Formula" aria-label="Formula" aria-describedby="basic-addon1">
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="row">
        <div class="col-12">
          <Sheets />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileButton from '@/components/ProfileButton'
import { onMounted, reactive } from 'vue'
import { useStore } from 'vuex'
import { listWorkbooks, createWorkbook } from '@/components/apicalls/files'
import { createSheet } from '@/components/apicalls/workbook'
import { getChildElementsByClassName, simulateClick } from '@/utils/dom'
import Dialog from '@/components/Dialog'
import Button from '@/components/Button'
import Icon from '@/components/Icon'
import CustomInput from '@/components/CustomInput'
import Alert from '@/components/Alert'
import Sheets from '@/components/Sheets'

export default {
  name: 'SpreadSheet',
  components: { Sheets, Alert, CustomInput, Icon, Dialog, Button, ProfileButton },
  setup () {
    const database = reactive({
      list: [],
      selected: '',
      new: '',
      current: {
        name: ''
      }
    })

    const errors = reactive({
      fileSelectModal: ''
    })

    const store = useStore()

    onMounted(async () => {
      const databasesData = await listWorkbooks()
      database.list = databasesData.data
    })

    function handleFileSelected (event) {
      database.selected = document.querySelector('input[name=' + event.target.name + ']:checked').value
      // TODO: toggle button by giving toggling value to button as property
    }

    async function handleFileOpen () {
      if (!database.selected) {
        errors.fileSelectModal = 'No file selected!'
        return
      }

      store.commit('workbook/setFile', database.selected)

      const modal = document.getElementById('file-modal')
      if (modal) {
        const closeElements = getChildElementsByClassName(modal, 'close')
        if (closeElements.length === 1) {
          simulateClick(closeElements[0])
        }
      }

      await store.dispatch('workbook/fetchSheets')
      errors.fileSelectModal = ''

      if (store.getters['workbook/getSheetNames'].length === 0) {
        const sheets = await createSheet(store.getters['workbook/currentFile'], 'Sample')

        if (!sheets.ok) {
          return
        }

        await store.dispatch('workbook/fetchSheets')
      }
    }

    async function handleFileCreate () {
      if (database.new.trim() === '') {
        // TODO: Inform user that database already exists
        return
      }

      const name = database.new.trim()
      database.new = ''
      database.selected = name

      const databaseCreate = await createWorkbook(name)

      if (!databaseCreate.ok) {
        // TODO: Inform user about database creation problem
        return
      }

      database.list.push(database.selected)
    }

    function handleClickToChildInput (event) {
      let input

      event.target.childNodes.forEach(node => {
        if (node.nodeName === 'INPUT') {
          input = node
        }
      })

      if (input) {
        simulateClick(input)
      }
    }

    return {
      database,
      errors,
      handleFileSelected,
      handleFileCreate,
      handleFileOpen,
      handleClickToChildInput
    }
  }
}
</script>

<style scoped lang="scss">
.file-modal-content {
  max-height: 50vh;
  overflow-y: auto;
}

.hide {
  display: none;
}
</style>
