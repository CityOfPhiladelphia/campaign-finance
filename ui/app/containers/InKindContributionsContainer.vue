<template>
  <b-container>
    <item-table
      :items="contributions"
      :fields="fields"></item-table>

    <b-button variant="primary" @click="showAddModal"><octicon name="plus"></octicon> Add In-Kind Contribution</b-button>

    <b-modal ref="addModal" hide-footer title="Add In-Kind Contribution">
      <contribution-form contribution-type="in_kind" :on-save="submitContribution"></contribution-form>
    </b-modal>
  </b-container>
</template>

<script>
  import { mapState, mapActions } from 'vuex'

  import ItemTable from '../components/ItemTable.vue'
  import ContributionForm from '../components/ContributionForm.vue'

  export default {
    components: {
      ItemTable,
      ContributionForm
    },
    data () {
      return {
        fields: [
          {
            key: 'contributor_type',
            label: 'Contributor Type'
          },
          {
            key: 'full_name',
            label: 'Full Name'
          },
          {
            key: 'date',
            label: 'Date'
          },
          {
            key: 'amount',
            label: 'Amount'
          }
        ]
      }
    },
    computed: mapState({
      contributions (state) {
        let report = state.reports.filter(report => report.id = this.$route.params.id)[0]
        return report.contributions.filter(contribution => contribution.contribution_type == 'in_kind')
      }
    }),
    methods: {
      ...mapActions([
        'addContribution'
      ]),
      submitContribution (contribution) {
        this.hideAddModal()
        this.addContribution({ reportId: this.$route.params.id, contribution })
      },
      showAddModal () {
        this.$refs.addModal.show()
      },
      hideAddModal () {
        this.$refs.addModal.hide()
      }
    }
  }
</script>

<style lang="css">
  .contributions-list {
    margin: .5em;
  }
</style>
