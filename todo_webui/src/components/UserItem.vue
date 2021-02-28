<template lang="html">

  <div class="card m-2 p-1 has-text-white has-background-success-dark">
    <div class="card-content">
      <div class="content">{{ name }}</div>
    </div>
    <footer class="card-footer">
      <div class="card-footer-item">
        <b-button type="is-danger is-rounded" size="is-small">Delete</b-button> 
      </div>
      <div class="card-footer-item">
        <b-switch :value="true" type="is-info is-small">Show</b-switch>
      </div>
    </footer>
  </div>

</template>

<script lang="js">

  export default  {
    name: 'user-item',
    props: ["name"],
    inject: ["fetch_users"],
    mounted () {

    },
    data () {
      return {

      }
    },
    methods: {

    },
    computed: {

    }
}


</script>

<style>
</style>
