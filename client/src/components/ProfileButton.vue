<template>
  <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <Icon icon="bi-person" /> {{ button.text }}
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" v-if="button.status === 'logged'">
      <button class="dropdown-item" type="button" @click="handleLogout">Log out</button>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import router from '@/router'
import { getProfile, logout } from '@/components/apicalls/user'
import Icon from '@/components/Icon'

export default {
  name: 'ProfileButton',
  components: { Icon },
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
        await router.push('Login')
        return
      }

      button.text = profile.data.firstName + ' ' + profile.data.lastName
      button.status = 'logged'
    })

    async function handleLogout () {
      const data = await logout()

      if (data.ok) {
        await router.push('Login')
      }
      // TODO: Add global alert
    }
    return { button, handleLogout }
  }
}
</script>

<style scoped>

</style>
