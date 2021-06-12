<template>
  <div class="row mt-5">
    <div class="col"></div>
    <div class="col-xs-12 col-sm-10 col-md-6 col-lg-4">
      <div class="card">
        <header class="card-header text-center">
          <h3>Login</h3>
        </header>
        <form class="card-body" @submit.prevent="handleLogin">
          <Alert type="danger" v-if="errors.form" :message="errors.form"/>
          <Input label="Email" type="email" name="email" v-model="form.email" />
          <Input label="Password" type="password" name="password" v-model="form.password"/>
          <button class="btn btn-primary btn-block">Login</button>
        </form>
        <footer class="card-footer text-center">
          Don't have an account? <RouterLink to="/register">Register</RouterLink>
        </footer>
      </div>
    </div>
    <div class="col"></div>
  </div>
</template>

<script>
import Input from '@/components/Input'
import { reactive } from 'vue'
import router from '@/router'
import Alert from '@/components/Alert'
import { postLogin } from '@/components/apicalls/postLogin'

export default {
  name: 'Login',
  components: { Alert, Input },
  setup () {
    const form = reactive({
      email: '',
      password: ''
    })

    const errors = reactive({
      form: ''
    })

    async function handleLogin () {
      errors.form = ''

      const loginData = await postLogin(form)

      if (loginData.ok) {
        await router.push('SpreadSheet')
        return
      }

      errors.form = loginData.data.message || ''
    }

    return { form, errors, handleLogin }
  }
}
</script>

<style scoped>

</style>
