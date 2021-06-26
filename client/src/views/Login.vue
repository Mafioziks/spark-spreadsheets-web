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
          <CustomInput label="Email" type="email" name="email" v-model="form.email" />
          <CustomInput label="Password" type="password" name="password" v-model="form.password"/>
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
import { reactive } from 'vue'
import { useStore } from 'vuex'
import router from '@/router'
import CustomInput from '@/components/CustomInput'
import Alert from '@/components/Alert'

export default {
  name: 'Login',
  components: { Alert, CustomInput },
  setup () {
    const form = reactive({
      email: '',
      password: ''
    })

    const store = useStore()

    const errors = reactive({
      form: ''
    })

    async function handleLogin () {
      errors.form = ''

      await store.dispatch('auth/login', form)

      if (store.getters['auth/authorized']) {
        await router.push('SpreadSheet')
      }
      // errors.form = loginData.data.message || ''
    }

    return { form, errors, handleLogin }
  }
}
</script>

<style scoped>

</style>
