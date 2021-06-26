async function call (method, url, content) {
  const response = await fetch(url, {
    method,
    credentials: 'include',
    body: JSON.stringify(content),
    headers: {
      'Content-Type': 'application/json'
    }
  })

  const data = await response.json()

  return {
    status: response.status,
    ok: response.ok,
    data
  }
}

module.exports = { call }
