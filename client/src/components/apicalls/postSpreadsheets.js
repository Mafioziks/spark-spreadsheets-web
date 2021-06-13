async function postSpreadsheets (name) {
  const response = await fetch('/api/spreadsheet/files', {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify({ name }),
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

module.exports = { postSpreadsheets }
