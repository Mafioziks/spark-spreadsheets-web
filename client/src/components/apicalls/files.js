const api = require('./api')

async function createWorkbook (name) {
  return await api.call('POST', '/api/spreadsheet/files', { name })
}

async function listWorkbooks () {
  return await api.call('GET', '/api/spreadsheet/files')
}

module.exports = { createWorkbook, listWorkbooks }
