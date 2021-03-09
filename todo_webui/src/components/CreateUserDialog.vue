<template lang="html">
  <form action="">
    <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Create User</p>
            <button
                type="button"
                class="delete"
                @click="$emit('close')"/>
        </header>
        <section class="modal-card-body">
            <b-field label="User Name">
                <b-input
                    v-model="user_name"
                    placeholder="John"
                    required>
                </b-input>
            </b-field>
        </section>
        <footer class="modal-card-foot">
            <b-button
                label="Close"
                @click="$emit('close')" />
            <b-button
                label="Create"
                @click="add_user_name"
                type="is-primary" />
        </footer>
    </div>
  </form>
</template>

<script lang="js">
  import Axios from 'axios';

  export default  {
    name: 'create-user-dialog',
    props: [],
    inject: ["fetch_items"],
    mounted () {

    },
    data () {
      return {
        user_name: ""
      }
    },
    methods: {
      add_user_name() {
        Axios.put("/user", {
          "name": this.user_name
        }).then(() => {
          this.$buefy.toast.open({
              duration: 3000,
              message: 'Created user ' + this.user_name,
              position: 'is-bottom',
              type: 'is-info'
          });
          this.fetch_items();
          this.$emit('close');
        }).catch((e) => {
          this.$buefy.toast.open({
              duration: 5000,
              message: 'Sorry. Unable to create user ' + this.user_name + '</br>' + e,
              position: 'is-bottom',
              type: 'is-danger'
          })
        })

      }

    },
    computed: {

    }
  }
</script>

<style>
</style>
