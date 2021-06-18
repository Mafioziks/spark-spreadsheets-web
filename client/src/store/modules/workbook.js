import { listSheets } from '@/components/apicalls/workbook'

export default {
  namespaced: true,
  state: {
    file: '',
    sheets: {}
  },
  mutations: {
    setFile: (state, fileName) => { state.file = fileName },
    addSheet (state, sheetName, columnList, data) {
      if (state.sheets[sheetName] !== undefined) {
        // TODO: Sheet already exists
        return
      }

      state.sheets[sheetName] = {
        columns: columnList,
        data: data
      }
    }
  },
  actions: {
    async fetchSheets ({ commit, state }) {
      if (state.file === '') {
        // TODO: No file selected
        return
      }

      const sheets = await listSheets(state.file)

      if (sheets.ok) {
        sheets.data.forEach(sheetName => commit('addSheet', sheetName, [], []))
      }
    }
  },
  getters: {
    currentFile: state => state.file,
    getSheetNames: state => Object.keys(state.sheets),
    getColumnNames: (state, sheetName) => state.sheets[sheetName]?.columns,
    getData: (state, sheetName) => state.sheets[sheetName]?.data
  }
}
