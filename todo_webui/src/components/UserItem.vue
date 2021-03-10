<template lang="html">

  <div class="card m-2 p-1 has-text-white has-background-success-dark">
    <div class="card-content">
      <div class="content">{{ name }}</div>
    </div>
    <footer class="card-footer">
      <div class="card-footer-item">
        <b-button type="is-danger is-rounded" @click="delete_user" size="is-small">
          Delete
        </b-button> 
      </div>
      <div class="card-footer-item">
        <b-switch v-model="is_shown"
                  :rounded="false"
                  @input="toggle_show"
                  type="is-info is-small">Show?</b-switch>
      </div>
    </footer>
  </div>

</template>

<script lang="js">
  import Axios from 'axios';

  export default  {
    name: 'user-item',
    props: ["name"],
    inject: ["fetch_items", "update_user_show_status"],
    mounted () {

    },
    data () {
      return {
        is_shown: true
      }
    },
    methods: {
      delete_user_exec () {
        Axios.delete("/users/" + this.name).then(() => {
          this.fetch_items();
        })
      },
      delete_user () {
        this.$buefy.dialog.confirm({
            message: 'Really delete user ' + this.name + ' and all corresponding items?',
            onConfirm: () => this.delete_user_exec()
        })
      },
      toggle_show () {
        this.update_user_show_status(this.name, this.is_shown);
      }
    },
    computed: {

    }
}


</script>

<style>
</style>
