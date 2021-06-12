import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
import axios from 'axios'
// import cors from 'cors'

const Http = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: true
})

const app = createApp(App)

app.provide('axios', Http)
// app.use(cors())
app.use(store).use(router).mount('#app')
