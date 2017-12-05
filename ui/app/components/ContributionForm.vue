<template>
  <b-container>
    <b-form @submit="onSubmit">
      <h4>Transaction Detail</h4>
      <b-form-group
        label="Contributor Type"
        label-for="contributor_type">
        <b-form-select
          id="contributor_type"
          v-model="form.contributor_type"
          :options="contributorTypes"></b-form-select>
      </b-form-group>
      <b-form-group
        label="Full Name of Contributor"
        label-for="full_name">
        <b-form-input
          id="full_name"
          v-model="form.full_name"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Description"
        label-for="description">
        <b-form-input
          id="description"
          v-model="form.description"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Date"
        label-for="date">
        <b-form-input
          id="date"
          type="date"
          v-model="form.date"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Amount"
        label-for="amount">
        <b-form-input
          id="amount"
          type="number"
          v-model="form.amount"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Contributor Address Line 1"
        label-for="contributor_address_line_1">
        <b-form-input
          id="contributor_address_line_1"
          v-model="form.contributor_address_line_1"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Contributor Address Line 2"
        label-for="contributor_address_line_2">
        <b-form-input
          id="contributor_address_line_2"
          v-model="form.contributor_address_line_2"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Contributor City"
        label-for="contributor_city">
        <b-form-input
          id="contributor_city"
          v-model="form.contributor_city"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Contributor State"
        label-for="contributor_state">
        <b-form-input
          id="contributor_state"
          v-model="form.contributor_state"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Contributor ZIP"
        label-for="contributor_zip">
        <b-form-input
          id="contributor_zip"
          v-model="form.contributor_zip"></b-form-input>
      </b-form-group>

      <h4>Employee Detail</h4>
      <b-form-group
        label="Employer"
        label-for="employer">
        <b-form-input
          id="employer"
          v-model="form.employer"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Occupation"
        label-for="occupation">
        <b-form-input
          id="occupation"
          v-model="form.occupation"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Employer Address Line 1"
        label-for="contributor_address_line_1">
        <b-form-input
          id="employer_address_line_1"
          v-model="form.employer_address_line_1"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Employer Address Line 2"
        label-for="employer_address_line_2">
        <b-form-input
          id="employer_address_line_2"
          v-model="form.employer_address_line_2"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Employer City"
        label-for="employer_city">
        <b-form-input
          id="employer_city"
          v-model="form.employer_city"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Employer State"
        label-for="employer_state">
        <b-form-input
          id="employer_state"
          v-model="form.employer_state"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Employer ZIP"
        label-for="employer_zip">
        <b-form-input
          id="employer_zip"
          v-model="form.employer_zip"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Save</b-button>
    </b-form>
  </b-container>
</template>

<script>
  export default {
    props: {
      contributionType: {
        type: String,
        required: true
      },
      onSave: {
        type: Function,
        required: true
      }
    },
    data () {
      let emptyForm = {
        contribution_type: this.contributionType,
        contributor_type: null,
        full_name: null,
        description: null,
        date: null,
        amount: null,
        contributor_address_line_1: null,
        contributor_address_line_2: null,
        contributor_city: null,
        contributor_state: null,
        contributor_zip_code: null,
        employer: null,
        occupation: null,
        employer_address_line_1: null,
        employer_address_line_2: null,
        employer_city: null,
        employer_state: null,
        employer_zip_code: null
      }

      return {
        contributorTypes: [
          {
            text: 'Individual',
            value: 'individual'
          },
          {
            text: 'Campaign',
            value: 'campaign'
          }
        ],
        form: emptyForm,
        emptyForm
      }
    },
    methods: {
      onSubmit (e) {
        e.preventDefault()
        this.onSave(this.form)
        this.form = this.emptyForm
      }
    }
  }
</script>

<style lang="css">

</style>
