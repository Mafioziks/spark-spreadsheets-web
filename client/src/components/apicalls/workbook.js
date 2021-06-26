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

async function getSheetData (workbookName, sheetName) {
  return await api.call('GET', '/api/spreadsheet/sheet?file=' + workbookName + '&sheet=' + sheetName)
}

async function addSheetData (workbookName, sheetName, data) {
  return await api.call('POST', '/api/spreadsheet/sheet/data', { file: workbookName, sheet: sheetName, data })
}

module.exports = { listSheets, createSheet, getSheetData, addSheetData }
