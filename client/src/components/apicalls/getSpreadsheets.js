async function getSpreadsheets () {
  const response = await fetch('/api/spreadsheet/files', {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json'
    }
  })

  const data = await response.json()

  return {
    status: response.statusCode,
    ok: response.ok,
    data
  }
}

module.exports = { getSpreadsheets }
