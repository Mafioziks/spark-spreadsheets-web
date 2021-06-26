import { createStore } from 'vuex'
import VuexPersist from 'vuex-persist'
import workbook from './modules/workbook'
import auth from './modules/auth'

const vuexPersist = new VuexPersist({
  key: 'spark-sheets',
  storage: window.sessionStorage
})

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    workbook,
    auth
  },
  plugins: [vuexPersist.plugin]
})
