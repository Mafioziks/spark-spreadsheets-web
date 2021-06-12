<template>
  <div class="row">
    <div class="col"></div>
    <div class="col-md-6 col-sm-12">
      <div class="card">
        <header class="card-header text-center">
          <h3>Register</h3>
        </header>
        <div class="card-body">
          <form @submit.prevent="handleRegistration">
            <Input label="First Name" name="first_name" v-model="form.firstName" />
            <Input label="Last Name" name="last_name" v-model="form.lastName" />
            <Input label="Email" name="email" type="email" v-model="form.email" />
            <Input label="Password" name="password" type="password" v-model="form.password" />
            <Input label="Password Repeated" name="passwordVerify" type="password" v-model="form.passwordVerify"/>
            <button class="btn btn-primary btn-block">Register</button>
          </form>
        </div>

        <div class="card-footer text-center">
          Have account? <RouterLink to="/login">Login</RouterLink>
        </div>
      </div>
    </div>
    <div class="col"></div>
  </div>
</template>

<script>
import Input from '@/components/Input'
import { reactive } from 'vue'
import router from '@/router'

export default {
  name: 'Register',
  components: { Input },
  setup () {
    const form = reactive({
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      passwordVerify: ''
    })

    // const formValidation = reactive({
    //   firstName: '',
    //   lastName: '',
    //   email: '',
    //   password: '',
    //   passwordVerify: ''
    // })

    // const http = inject('axios')

    function handleRegistration () {
      // TODO: add email verification
      fetch('/api/user/register', {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(form),
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(
        response => router.push('/spreadsheet'),
        error => {
          console.log(error)
          // const data = error.response.json()
          // data.each((element, key) => { formValidation[key] = element })
        }
      )
    }

    return { handleRegistration, form }
  }
}
</script>

<style scoped>

</style>
