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
        <p class="title m-2 p-1">Users</p>
        <user-item v-for="user in user_list"
                   v-bind:key="user.name"
                   v-bind:name="user.name"></user-item>
      </div>
      <div class="column">
        <p class="title m-2 p-1">Backlog</p>
        <todo-item v-for="item in item_backlog_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
                   v-bind:status_change_date="item.status_change_date">
        </todo-item>
      </div>
      <div class="column">
        <p class="title m-2 p-1">In Progress</p>
        <todo-item v-for="item in item_inprogress_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
                   v-bind:status_change_date="item.status_change_date">
        </todo-item>
      </div>
      <div class="column">
        <p class="title m-2 p-1">Done</p>
        <todo-item v-for="item in item_done_list"
                   v-bind:key="item.item_id"
                   v-bind:content="item.content"
                   v-bind:priority="item.priority"
                   v-bind:users="item.users"
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

    this.fetch_users();
    this.fetch_items();
  },
  methods: {
    fetch_users () {
      Axios.get("/users").then((response) => {
        this.user_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })
    },
    fetch_items () {
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
      fetch_users: this.fetch_users,
      fetch_items: this.fetch_items
    }
  }
}
</script>

<style>
</style>
