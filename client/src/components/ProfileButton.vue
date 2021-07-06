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
import Icon from '@/components/Icon'
import { useStore } from 'vuex'

export default {
  name: 'ProfileButton',
  components: { Icon },
  setup () {
    const button = reactive({
      text: 'User Name',
      status: 'logged',
      link: ''
    })

    const store = useStore()

    onMounted(async () => {
      await store.dispatch('auth/getProfile')

      if (!store.getters['auth/authorized']) {
        await router.push('Login')
        return
      }

      button.text = store.getters['auth/getFullName']
      button.status = 'logged'
    })

    async function handleLogout () {
      await store.dispatch('auth/logoutUser')

      if (!store.getters['auth/authorized']) {
        await store.dispatch('workbook/clear')
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
