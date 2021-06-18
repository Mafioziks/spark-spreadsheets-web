import { listSheets, getSheetData } from '@/components/apicalls/workbook'

export default {
  namespaced: true,
  state: {
    file: '',
    sheets: {}
  },
  mutations: {
    setFile: (state, fileName) => {
      state.file = fileName
      state.sheets = {}
    },
    addSheet (state, { sheetName, columns, data }) {
      if (state.sheets[sheetName] !== undefined) {
        // TODO: Sheet already exists
        return
      }

      state.sheets[sheetName] = {
        columns,
        data
      }
    },
    setSheetData (state, { sheetName, data }) {
      if (state.sheets[sheetName] === undefined) {
        console.log(sheetName + ' does not exist')
        // TODO: Sheet does not exists
        return
      }

      state.sheets[sheetName].data = data
    },
    setSheetColumns (state, { sheetName, columns }) {
      if (state.sheets[sheetName] === undefined) {
        console.log(sheetName + ' does not exist')
        // TODO: Sheet does not exists
        return
      }

      state.sheets[sheetName].columns = columns
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
        sheets.data.forEach(sheetName => commit('addSheet', { sheetName, columns: [], data: [] }))
      }
    },
    async fetchData ({ commit, getters }, sheetName, force = false) {
      if (!getters.fileDefined) {
        // TODO: No file selected
        return
      }

      if (!getters.sheetDefined(sheetName)) {
        return
      }

      if (getters.getColumnAmount(sheetName) !== 0 && !force) {
        return
      }

      const result = await getSheetData(getters.currentFile, sheetName)

      if (result.ok) {
        commit('setSheetColumns', { sheetName, columns: result.data.schema.fields })
        commit('setSheetData', { sheetName, data: result.data.data })
      }
    },
    async fetchFile ({ commit, dispatch }, fileName) {
      await commit('setFile', fileName)
      dispatch('fetchSheets')
    }
  },
  getters: {
    currentFile: state => state.file,
    getSheetNames: state => Object.keys(state.sheets),
    getColumnNames: (state) => (sheetName) => state.sheets[sheetName]?.columns,
    getData: (state) => (sheetName) => state.sheets[sheetName]?.data,
    sheetDefined: (state) => (sheetName) => state.sheets[sheetName] !== undefined,
    fileDefined: (state) => state.file !== undefined,
    getColumnAmount: (state) => (sheetName) => state.sheets[sheetName]?.columns === undefined
      ? 0
      : state.sheets[sheetName].columns.length
  }
}
