async function getLogout () {
  const response = await fetch('/api/user/logout', {
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

module.exports = { getLogout }
