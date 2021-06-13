<template>
  <div class="container-fluid">
    <header class="page-header">
      <div class="row mb-3">
        <div class="col-6">
          <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
            <Button type="button" button-type="secondary" data-toggle="modal" data-target="#file-modal"><Icon icon="bi-folder" /> Open File</Button>
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
      <table class="table table-bordered table-sm table-hover">
        <thead class="thead-dark">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">First Name</th>
            <th scope="col">Last Name</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Name</td>
            <td>Surname</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <Dialog id="file-modal">
    <template v-slot:title>
      Choose file
    </template>

    <template v-slot:default>
      <Input v-model="database.new" label="New File" name="new-name"/>
      <hr/>
      <div class="row">
        <Button class="p-3 m-1 btn-block" button-type="light" v-for="(name, index) in database.list" v-bind:key="index" @click="handleFileSelected">
          <Icon icon="bi-file-earmark-ruled"/> {{ name }}
        </Button>
      </div>
    </template>

    <template v-slot:footer>
      <Button buttonType="primary" @click="handleFileAction">Save</Button>
    </template>
  </Dialog>
</template>

<script>
import ProfileButton from '@/components/ProfileButton'
import { onMounted, reactive } from 'vue'
import { getSpreadsheets } from '@/components/apicalls/getSpreadsheets'
import { postSpreadsheets } from '@/components/apicalls/postSpreadsheets'
import Dialog from '@/components/Dialog'
import Button from '@/components/Button'
import Icon from '@/components/Icon'
import Input from '@/components/Input'

export default {
  name: 'SpreadSheet',
  components: { Input, Icon, Dialog, Button, ProfileButton },
  setup () {
    const database = reactive({
      list: [],
      selected: '',
      new: ''
    })

    onMounted(async () => {
      const databasesData = await getSpreadsheets()

      console.log(databasesData)

      database.list = databasesData.data
    })

    function handleFileSelected (event) {
      database.selected = database.list[event.target.value]
      // TODO: toggle button by giving toggling value to button as property
    }

    async function handleFileOpen () {
    }

    async function handleFileAction () {
      if (
        (database.selected === '' || database.selected === null) &&
        database.new
      ) {
        database.selected = database.new
        await handleFileCreate()
      }

      await handleFileOpen()
    }

    async function handleFileCreate () {
      if (database.new.trim() === '') {
        // TODO: Inform user that database already exists
        return
      }

      const name = database.new.trim()
      database.new = ''

      const databaseCreate = await postSpreadsheets(name)

      if (!databaseCreate.ok) {
        return
      }

      database.list.push(database.selected)
    }

    return {
      database,
      handleFileSelected,
      handleFileCreate,
      handleFileOpen,
      handleFileAction
    }
  }
}
</script>

<style scoped lang="scss">
//.page-header {
//  background-color: #42b983;
//}
</style>
