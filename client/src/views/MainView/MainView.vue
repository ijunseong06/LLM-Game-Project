<script>
import AddButton from './components/AddButton.vue';

export default {
  components: {
    AddButton,
  }
}
</script>

<template>
  <div style="position: relative">
    <h1 class="main-menu-header">LLM Game project</h1>
    <add-button class="add-button"></add-button>
  </div>
</template>

<style>
* {
  padding: 0;
  margin: 0;
}
body {
  background-color: rgb(24, 24, 24);
  margin: 0;
  padding: 0%;
}
.main-menu-header {
  text-align: center;
  color: white;
}
.add-button {
  position: fixed;
  top: 92%;
  left: 96%;
  width: 50px;
  height: 50px;
}
</style>
