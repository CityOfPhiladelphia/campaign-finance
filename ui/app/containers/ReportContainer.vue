<template>
  <b-container>
    <h3>Report</h3>

    <b-tabs class="report-tabs" @input="tabInput">
      <b-tab v-for="tab in tabs" :title="tab.label" :active="matchesTabRoute(tab.route)"></b-tab>
    </b-tabs>

    <router-view></router-view>
  </b-container>
</template>

<script>
  export default {
    data () {
      return {
        tabs: [
          {
            label: 'Unitemized Items',
            route: 'unitemized-items'
          },
          {
            label: 'Monetary Contributions',
            route: 'monetary-contributions'
          },
          {
            label: 'In-Kind Contributions',
            route: 'in-kind-contributions'
          },
          {
            label: 'Receipts',
            route: 'receipts'
          },
          {
            label: 'Expenditures',
            route: 'expenditures'
          },
          {
            label: 'Unpaid Debts',
            route: 'unpaid-debts'
          }
        ]
      }
    },
    methods: {
      tabInput (tab_index) {
        this.$router.push('/reports/' + this.$route.params.id + '/' + this.tabs[tab_index].route)
      },
      matchesTabRoute (tabRoute) {
        return this.$router.history.current.path.indexOf(tabRoute) > -1
      }
    }
  }
</script>

<style lang="css">
  .report-tabs {
    margin: 1em;
  }
</style>
