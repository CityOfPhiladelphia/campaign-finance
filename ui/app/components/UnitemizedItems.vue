<template>
  <b-container class="unitemized-form">
    <b-row align-v="center">
      <b-col><label for="cash_contributions">Unitemized Cash Contributions</label></b-col>
      <b-col>
        <b-input-group left="$">
          <b-form-input id="cash_contributions"></b-form-input>
        </b-input-group>
      </b-col>
      <b-col>
        <p>Total of contributions below $50.01 not entered as details</p>
      </b-col>
    </b-row>
    <b-row align-v="center">
      <b-col><label for="inkind_contributions">Unitemized In-Kind Contributions</label></b-col>
      <b-col>
        <b-input-group left="$">
          <b-form-input id="inkind_contributions"></b-form-input>
        </b-input-group>
      </b-col>
      <b-col>
        <p>Total of in-kind contributions below $50.01 not entered as details</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    data () {
      return {
      }
    }
  }
</script>

<style lang="css">
  .unitemized-form label {
    margin: 0;
  }

  .unitemized-form p {
    margin: 0;
    padding: .5em;
  }
</style>
