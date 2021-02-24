<template>
  <!-- <div id="app"></div> -->
  <div>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <div class="navbar-item">
          ToDo List
        </div>
      </div>
    </nav>
    <div class="columns">
      <div class="column">
        <p class="title m-2 p-1">Users</p>
        <user-item></user-item>
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
import TodoItem from './components/TodoItem.vue'
import UserItem from './components/UserItem.vue'

export default {
  name: 'App',
  components: {
    TodoItem,
    UserItem
  }
}
</script>

<style>
</style>
