// TODO: change function arguments to be an separate values than constant block of values
async function postLogin (formData) {
  const response = await fetch('/api/user/login', {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(formData),
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

module.exports = { postLogin }
