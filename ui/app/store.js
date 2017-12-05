import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const mutationTypes = {
  NEW_CONTRIBUTION: 'NEW_CONTRIBUTION'
}

export default new Vuex.Store({
  state: {
    reports: [
      {
        id: 1,
        contributions: [],
        receipts: [],
        expenditures: [],
        unpaid_debts: []
      }
    ]
  },
  actions: {
    addContribution ({ commit }, addContribution) {
      commit(mutationTypes.NEW_CONTRIBUTION, addContribution)
    }
  },
  mutations: {
    [mutationTypes.NEW_CONTRIBUTION] (state, { reportId, contribution }) {
      for (var i in state.reports) {
        if (state.reports[i].id == reportId) {
          state.reports[i].contributions.push(contribution)
          break
        }
      }
    }
  }
})
