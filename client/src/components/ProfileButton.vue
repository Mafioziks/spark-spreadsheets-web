<template>
  <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      {{ button.text }}
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" v-if="button.status === 'logged'">
      <button class="dropdown-item" type="button" @click="handleLogout">Log out</button>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import router from '@/router'
import { getProfile } from '@/components/apicalls/getProfile'
import { getLogout } from '@/components/apicalls/getLogout'

export default {
  name: 'ProfileButton',
  setup () {
    const button = reactive({
      text: 'User Name',
      status: 'logged',
      link: ''
    })

    onMounted(async () => {
      // TODO: Add user authorization in more global place for page
      const profile = await getProfile()

      if (!profile.ok) {
        console.log(profile.data)
        await router.push('Login')
        return
      }

      button.text = profile.data.firstName + ' ' + profile.data.lastName
      button.status = 'logged'
    })

    async function handleLogout () {
      const data = await getLogout()

      if (data.ok) {
        await router.push('Login')
        return
      }

      // TODO: Add global alert
      console.log(data)
    }
    return { button, handleLogout }
  }
}
</script>

<style scoped>

</style>
