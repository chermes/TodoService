<template lang="html">
  <form action="">
    <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Create Item</p>
            <button
                type="button"
                class="delete"
                @click="$emit('close')"/>
        </header>
        <section class="modal-card-body">

          <b-field label="Description">
              <b-input
                  v-model="content"
                  placeholder="ToDo item description."
                  maxlength="120"
                  type="textarea"
                  required>
              </b-input>
          </b-field>

          <b-field label="Priority">
            <div class="block">
                <b-radio v-model="priority"
                    name="priority"
                    native-value="low">
                    low
                </b-radio>
                <b-radio v-model="priority"
                    name="priority"
                    native-value="medium">
                    medium
                </b-radio>
                <b-radio v-model="priority"
                    name="priority"
                    native-value="high">
                    high
                </b-radio>
            </div>
          </b-field>

          <b-field label="Assign Users">
            <div class="block">
                <b-checkbox v-model="selected_users"
                    v-for="user in avail_users"
                    v-bind:key="user"
                    v-bind:native-value="user">
                    {{user}}
                </b-checkbox>
            </div>
          </b-field>


        </section>
        <footer class="modal-card-foot">
            <b-button
                label="Close"
                @click="$emit('close')" />
            <b-button
                label="Create"
                @click="add_item"
                type="is-primary" />
        </footer>
    </div>
  </form>
</template>

<script lang="js">
  import Axios from 'axios';

  export default  {
    name: 'create-item-dialog',
    props: [],
    inject: ["fetch_items"],
    mounted () {
      Axios.get("/users").then((response) => {
        this.avail_users = [];
        this.selected_users = [];
        response.data.forEach(element => {
          this.avail_users.push(element.name)
          this.selected_users.push(element.name)
        });
      })

    },
    data () {
      return {
        content: "",
        priority: "low",
        avail_users: [],
        selected_users: []
      }
    },
    methods: {
      add_item () {
        Axios.post("/item", {
          content: this.content,
          priority: this.priority,
          status: "backlog",
          users: this.selected_users
        }).then(() => {
          this.$buefy.toast.open({
              duration: 3000,
              message: 'Created item.',
              position: 'is-bottom',
              type: 'is-info'
          });
          this.fetch_items();
          this.$emit('close');
        }).catch((e) => {
          this.$buefy.toast.open({
              duration: 5000,
              message: 'Sorry. Unable to create item.</br>' + e.response.data.detail,
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
