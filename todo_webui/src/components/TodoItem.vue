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
        <b-button type="is-rounded" @click="update_status_prev" size="is-small">&#60;</b-button>
      </div>
      <div class="card-footer-item">
        <b-button type="is-rounded" size="is-small">Edit</b-button>
      </div>
      <div class="card-footer-item">
        <b-button type="is-danger is-rounded" @click="delete_item" size="is-small">Delete</b-button> 
      </div>
      <div class="card-footer-item" v-if="status_next">
        <b-button type="is-rounded" @click="update_status_next" size="is-small">&#62;</b-button>
      </div>
    </footer>
  </div>

</template>

<script lang="js">
  import Axios from 'axios';

  export default  {
    name: 'todo-item',
    props: ["item_id", "content", "priority", "users", "status", "status_prev", "status_next", "status_change_date"],
    inject: ["fetch_items"],
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
      },
      delete_item_exec () {
        Axios.delete("/items/" + this.item_id).then(() => {
          this.fetch_items();
        })
      },
      delete_item () {
        this.$buefy.dialog.confirm({
            message: 'Really delete this item?',
            onConfirm: () => this.delete_item_exec()
        })
      },
      update_status_prev () {
        Axios.post("/items/" + this.item_id + "/status/" + this.status_prev).then(() => {
          this.fetch_items();
        })
      },
      update_status_next () {
        Axios.post("/items/" + this.item_id + "/status/" + this.status_next).then(() => {
          this.fetch_items();
        })
      }
    },
    computed: {

    }
}


</script>

<style>
</style>
