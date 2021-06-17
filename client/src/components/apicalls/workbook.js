const api = require('./api')

async function listSheets (workbookName) {
  return await api.call('GET', '/api/spreadsheet/file/sheets?file=' + workbookName)
}

async function createSheet (workbookName, sheetName, columns) {
  return await api.call('PUT', '/api/spreadsheet/sheet', {
    file: workbookName,
    sheet: sheetName,
    columns: columns
  })
}

module.exports = { listSheets, createSheet }
