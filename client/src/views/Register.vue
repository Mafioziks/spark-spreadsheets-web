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
            <CustomInput label="First Name" name="first_name" v-model="form.firstName" />
            <CustomInput label="Last Name" name="last_name" v-model="form.lastName" />
            <CustomInput label="Email" name="email" type="email" v-model="form.email" />
            <CustomInput label="Password" name="password" type="password" v-model="form.password" />
            <CustomInput label="Password Repeated" name="passwordVerify" type="password" v-model="form.passwordVerify"/>
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
import CustomInput from '@/components/CustomInput'
import { reactive } from 'vue'
import router from '@/router'
import { register } from '@/components/apicalls/user'

export default {
  name: 'Register',
  components: { CustomInput },
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

    async function handleRegistration () {
      // TODO: add email verification
      const result = await register(form)

      if (result.ok) {
        await router.push('/spreadsheet')
      }
      // result.data.forEach((element, key) => { formValidation[key] = element })
    }

    return { handleRegistration, form }
  }
}
</script>

<style scoped>

</style>
