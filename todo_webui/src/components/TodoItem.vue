<template lang="html">

  <div class="card m-2 p-1 has-text-info-light has-background-info-dark">
    <header class="card-header columns">
      <div class="header-title column">
        {{ users.join(", ") }}
      </div>
      <div class="header-title column has-text-right is-one-quarter">
        {{ display_datetime(status_change_date) }}
      </div>
    </header>
    <div class="card-content">
      <div class="content">{{ content }}</div>
    </div>
    <footer class="card-footer">
      <div class="card-footer-item" v-if="status_prev">
        <b-button type="is-rounded" size="is-small">&#60;</b-button>
      </div>
      <div class="card-footer-item">
        <b-button type="is-rounded" size="is-small">Edit</b-button>
      </div>
      <div class="card-footer-item">
        <b-button type="is-danger is-rounded" size="is-small">Delete</b-button> 
      </div>
      <div class="card-footer-item" v-if="status_next">
        <b-button type="is-rounded" size="is-small">&#62;</b-button>
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
