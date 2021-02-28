<template lang="html">

  <div class="card m-2 p-1 has-text-white has-background-success-dark">
    <header class="card-header">
      <p class="header-title">{{ name }}</p>
    </header>
    <footer class="card-footer">
      <div class="card-footer-item"><button class="button is-danger is-rounded">Delete</button></div>
      <label class="checkbox card-footer-item">
        <input type="checkbox">
        Show ToDo's?
      </label>
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
