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
        <user-item v-for="user in user_list" v-bind:name="user.name" v-bind:key="user.name"></user-item>
      </div>
      <div class="column">
        <p class="title">Backlog</p>
        <todo-item></todo-item>
        <todo-item></todo-item>
      </div>
      <div class="column">
        <p class="title">In Progress</p>
        <todo-item></todo-item>
        <todo-item></todo-item>
      </div>
      <div class="column">
        <p class="title">Done</p>
        <todo-item></todo-item>
        <todo-item></todo-item>
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
      user_list: []
    }
  },
  created () {
    // update the page title by the environment title var
    document.title = process.env.VUE_APP_TITLE;

    this.fetch_users();
  },
  methods: {
    fetch_users () {
      Axios.get("/users").then((response) => {
        console.log(response.data);
        this.user_list = response.data;
      }).catch((error) => {
        console.log(error.response.data);
      })
    }
  },
  provide: function() {
    return {
      fetch_users: this.fetch_users
    }
  }
}
</script>

<style>
</style>
