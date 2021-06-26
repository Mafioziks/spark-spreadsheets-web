import { getProfile, logout, login } from '@/components/apicalls/user'

export default {
  namespaced: true,
  state: {
    user: {},
    authorized: false
  },
  mutations: {
    setUser (state, { id, firstName, lastName, email }) {
      state.user = {
        id,
        firstName,
        lastName,
        email
      }
      state.authorized = true
    },
    removeUser (state) {
      state.user = {}
      state.authorized = false
    }
  },
  actions: {
    async getProfile ({ commit }) {
      const response = await getProfile()

      if (response.ok) {
        commit('setUser', response.data)
      }
    },
    async login ({ dispatch }, { email, password }) {
      const response = await login(email, password)

      if (response.ok) {
        await dispatch('getProfile')
      }
    },
    async logoutUser ({ commit }) {
      const result = await logout()

      if (result.ok) {
        commit('removeUser')
      }
    }
  },
  getters: {
    authorized: state => state.authorized,
    getUser: state => state.user,
    getFullName: (state, getters) => getters.authorized ? state.user.firstName + ' ' + state.user.lastName : ''
  }
}
