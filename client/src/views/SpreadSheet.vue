<template>
  <div class="container-fluid">
    <header class="page-header">
      <div class="row">
        <div class="col-12 mb-3">
          <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
            <button type="button" class="btn btn-secondary">Open</button>
            <button type="button" class="btn btn-secondary">Save</button>

            <div class="btn-group" role="group">
              <button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Export
              </button>
              <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                <a class="dropdown-item" href="#">Excel (.xlsx)</a>
                <a class="dropdown-item" href="#">CSV (.csv)</a>
              </div>
            </div>
          </div>
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
</template>

<script>
export default {
  name: 'SpreadSheet'
}
</script>

<style scoped lang="scss">
//.page-header {
//  background-color: #42b983;
//}
</style>
