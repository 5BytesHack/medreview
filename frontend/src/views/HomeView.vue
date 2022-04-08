<template>
  <div class="home container d-flex flex-column">
    <div class="about-info flex-grow-1 mt-3">
      hello
    </div>

    <div class="choose-btns d-flex flex-column flex-grow-1 mt-2 p-3">
      <div class="flex-grow-1 d-flex align-items-center">
        <p class="choose-title text-center mt-3">Выберите одно из возможных действий</p>
      </div>
      <div class="d-flex flex-grow-1 flex-column justify-content-center align-items-center">
        <router-link to="/anon_send">Создать обращение</router-link>
        <router-link to="/rating">Рейтинг клиник</router-link>
      </div>
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
@import'bootstrap/dist/css/bootstrap.min.css';
@font-face {
  font-family: 'Inter';
  font-weight: 400;
  font-style: normal;
  src:local('Inter'),
  url('~@/fonts/Inter-Regular.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 700;
  font-style: normal;
  src:local('Inter'),
  url('~@/fonts/Inter-Bold.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 900;
  font-style: normal;
  src:local('Inter'),
  url("~@/fonts/Inter-Black.ttf") format('truetype');
}
.home{
  height: 100%;
}
.about-info{
    background-color: white;
    border-radius: 39px;
    opacity: 0.65;
  }
.choose-btns{
  background-color: white;
  border-radius: 39px;
  opacity: 0.65;
}
.choose-title{
  font-family: 'Inter';
  font-weight: 400;
  font-style: normal;
  font-size: 1.75rem;
  line-height: 2.118rem;
  color: #24958C;
}
</style>
