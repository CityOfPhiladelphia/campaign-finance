<template>
  <b-container class="cf-item-table">
    <b-table small striped hover :items="items" :fields="fields"></b-table>
  </b-container>
</template>

<script>
  export default {
    props: {
      items: {
        type: Array
      },
      fields: {
        type: Array
      }
    },
    data () {
      return {
      }
    }
  }
</script>

<style lang="css">

</style>
