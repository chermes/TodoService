<template>
  <div>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <div class="navbar-item">
          ToDo List
        </div>
      </div>
    </nav>
    <div class="columns">
      <div class="column is-one-fifth">
        <div class="title p-0 m-0 columns">
          <div class="column">
            Users
          </div>
          <div class="column has-text-right">
            <b-button class="is-rounded is-success" size="is-small">Create</b-button>
          </div>
        </div>
        <user-item v-for="user in user_list"
                   v-bind:key="user.name"
                   v-bind:name="user.name"></user-item>
      </div>
      <div class="column">
        <div class="title p-0 m-0 columns">
          <div class="column">
            Backlog
          </div>
          <div class="column has-text-right">
            <b-button class="is-rounded is-info" size="is-small">Create</b-button>
          </div>
        </div>
        <todo-item v-for="item in item_backlog_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
                   v-bind:status="item.status"
                   v-bind:status_prev="item.status_prev"
                   v-bind:status_next="item.status_next"
                   v-bind:status_change_date="item.status_change_date">
        </todo-item>
      </div>
      <div class="column">
        <div class="title p-0 m-0 columns">
          <div class="column">
            In Progress
          </div>
        </div>
        <todo-item v-for="item in item_inprogress_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
                   v-bind:status="item.status"
                   v-bind:status_prev="item.status_prev"
                   v-bind:status_next="item.status_next"
                   v-bind:status_change_date="item.status_change_date">
        </todo-item>
      </div>
      <div class="column">
        <div class="title p-0 m-0 columns">
          <div class="column">
            Done
          </div>
        </div>
        <todo-item v-for="item in item_done_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
                   v-bind:status="item.status"
                   v-bind:status_prev="item.status_prev"
                   v-bind:status_next="item.status_next"
                   v-bind:status_change_date="item.status_change_date">
        </todo-item>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';
import TodoItem from './components/TodoItem.vue'
import UserItem from './components/UserItem.vue'

export default {
  name: 'App',
  components: {
    TodoItem,
    UserItem
  },
  data () {
    return {
      user_list: [],
      item_backlog_list: [],
      item_inprogress_list: [],
      item_done_list: []
    }
  },
  created () {
    // update the page title by the environment title var
    document.title = process.env.VUE_APP_TITLE;

    this.fetch_items();
  },
  methods: {
    fetch_items () {
      Axios.get("/users").then((response) => {
        this.user_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })

      Axios.get("/items?status=backlog").then((response) => {
        this.item_backlog_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })

      Axios.get("/items?status=in_progress").then((response) => {
        this.item_inprogress_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })

      Axios.get("/items?status=done").then((response) => {
        this.item_done_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })
    }
  },
  provide: function() {
    return {
      fetch_items: this.fetch_items
    }
  }
}
</script>

<style>
</style>
