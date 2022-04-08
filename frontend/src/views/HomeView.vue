<template>
  <div class="home d-flex flex-column">
    <div class="about-info">

    </div>

    <div class="choose-btns">
      <router-link to="/anon_send">Создать обращение</router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
  components: {

  }
}
</script>

<style scoped>
  .about-info{
    background-color: white;
    opacity: 0.65;
  }
</style>
