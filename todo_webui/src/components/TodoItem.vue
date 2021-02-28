<template lang="html">

  <div class="card m-2 p-1 has-text-info-light has-background-info-dark">
    <header class="card-header">
      <p class="header-title">{{ display_datetime(status_change_date) }}</p>
    </header>
    <div class="card-content">
      <div class="content">{{ content }}</div>
    </div>
    <footer class="card-footer">
      <div class="card-footer-item" v-if="status_prev">
        <button class="button is-rounded">&#60;</button>
      </div>
      <div class="card-footer-item"
           v-for="user in users"
           v-bind:key="user">
        {{ user }}
      </div>
      <div class="card-footer-item" v-if="status_next">
        <button class="button is-rounded">&#62;</button>
      </div>
    </footer>
  </div>

</template>

<script lang="js">

  export default  {
    name: 'todo-item',
    props: ["content", "priority", "users", "status", "status_prev", "status_next", "status_change_date"],
    mounted () {

    },
    data () {
      return {

      }
    },
    methods: {
      display_datetime(dt) {
        var datetime = new Date(dt);

        var day = datetime.getDate();
        var month = datetime.getMonth() + 1;
        var year = datetime.getFullYear();

        var date = year + "-" + month + "-" + day;

        return date;
      }

    },
    computed: {

    }
}


</script>

<style>
</style>
