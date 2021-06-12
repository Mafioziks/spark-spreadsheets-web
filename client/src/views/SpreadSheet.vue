<template>
  <div class="container-fluid">
    <header class="page-header">
      <div class="row mb-3">
        <div class="col-6">
          <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
            <Button type="button" button-type="secondary" data-toggle="modal" data-target="#file-modal">Open File</Button>
            <Button button-type="secondary">Save</Button>

            <div class="btn-group" role="group">
              <Button
                id="btnGroupDrop1"
                button-type="secondary"
                class="dropdown-toggle"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false">
                Export
              </Button>
              <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                <a class="dropdown-item" href="#">Excel (.xlsx)</a>
                <a class="dropdown-item" href="#">CSV (.csv)</a>
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
      <ul>
        <li v-for="(name, index) in database.list" v-bind:key="index">{{ name }}</li>
      </ul>
    </template>
  </Dialog>
</template>

<script>
import ProfileButton from '@/components/ProfileButton'
import { onMounted, reactive } from 'vue'
import { getSpreadsheets } from '@/components/apicalls/getSpreadsheets'
import Dialog from '@/components/Dialog'
import Button from '@/components/Button'

export default {
  name: 'SpreadSheet',
  components: { Dialog, Button, ProfileButton },
  setup () {
    const database = reactive({ list: [] })

    onMounted(async () => {
      const databasesData = await getSpreadsheets()

      console.log(databasesData)

      database.list = databasesData.data
    })

    return {
      database
    }
  }
}
</script>

<style scoped lang="scss">
//.page-header {
//  background-color: #42b983;
//}
</style>
