import { listSheets, getSheetData, addSheetData } from '@/components/apicalls/workbook'

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
        data,
        fetched: false
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
    appendSheetData (state, { sheetName, data }) {
      if (state.sheets[sheetName] === undefined) {
        console.log(sheetName + ' does not exist')
        // TODO: Sheet does not exists
        return
      }

      if (data !== undefined && Object.keys(data).length > 0) {
        state.sheets[sheetName].data.push(...data)
      }
    },
    setSheetColumns (state, { sheetName, columns }) {
      if (state.sheets[sheetName] === undefined) {
        console.log(sheetName + ' does not exist')
        // TODO: Sheet does not exists
        return
      }

      state.sheets[sheetName].columns = columns
    },
    setFetched (state, sheetName) {
      if (state.sheets[sheetName] === undefined) {
        console.log(sheetName + ' does not exists')
        return
      }

      state.sheets[sheetName].fetched = true
    },
    clear (state) {
      state.file = ''
      state.sheets = {}
    }
  },
  actions: {
    async fetchSheets ({ commit, state }) {
      if (state.file === '') {
        console.log('No selected file to fetch sheet')
        // TODO: No file selected
        return
      }

      const sheets = await listSheets(state.file)

      if (sheets.ok) {
        sheets.data.forEach(sheetName => commit('addSheet', { sheetName, columns: [], data: [] }))
      }
    },
    async fetchData ({ commit, getters }, { sheetName, force = false }) {
      if (!getters.fileDefined) {
        console.log('No file selected to fetch data')
        // TODO: No file selected
        return
      }

      if (!getters.sheetDefined(sheetName)) {
        console.log('Sheet not in fetched sheet list')
        return
      }

      if (getters.getColumnAmount(sheetName) !== 0 && !force) {
        console.log('Columns already fetched')
        return
      }

      const result = await getSheetData(getters.currentFile, sheetName)

      if (result.ok) {
        commit('setSheetColumns', { sheetName, columns: result.data.schema.fields })
        commit('setSheetData', { sheetName, data: result.data.data })
        commit('setFetched', sheetName)
      }
    },
    async fetchFile ({ commit, dispatch }, fileName) {
      await commit('setFile', fileName)
      dispatch('fetchSheets')
    },
    async addDataRow ({ getters, commit }, { sheetName, values }) {
      // Stringified because otherwise data is cleared out till adding to vuex as reactive property of data has kep
      const jsonString = JSON.stringify(values)
      const response = await addSheetData(getters.currentFile, sheetName, values)

      if (response.ok) {
        commit('appendSheetData', { sheetName, data: JSON.parse(jsonString) })
      }
    },
    async clear ({ commit }) {
      await commit('clear')
    }
  },
  getters: {
    currentFile: state => state.file,
    getSheetNames: state => Object.keys(state.sheets),
    getColumnNames: (state) => (sheetName) => state.sheets[sheetName]?.columns || [],
    getData: (state) => (sheetName) => state.sheets[sheetName]?.data || [],
    sheetDefined: (state) => (sheetName) => state.sheets[sheetName] !== undefined,
    fileDefined: (state) => state.file !== undefined,
    getColumnAmount: (state) => (sheetName) => state.sheets[sheetName]?.columns === undefined
      ? 0
      : state.sheets[sheetName].columns.length,
    isFetched: (state) => (sheetName) => state.sheets[sheetName]?.fetched || false
  }
}
