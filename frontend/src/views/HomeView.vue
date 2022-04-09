<template>
  <div class="home container d-flex flex-column py-3">
    <div class="about-info flex-grow-1">
      hello
    </div>

    <div class="choose-btns flex-column flex-grow-1">
      <div class="align-items-center justify-content-center">
        <p class="choose-title text-center">Выберите одно из возможных действий</p>
      </div>
      <div class="flex-column justify-content-center align-items-center">
        <button type="button" class="w-75 btn align-self-center py-2">
          <router-link id="makeApplyLink" to="/anon_send"><strong>Создать обращение</strong></router-link>
        </button>
        <button type="button" class="w-75 btn align-self-center py-2">
          <router-link id="clinicRatingLink" to="/rating"><strong>Рейтинг клиник</strong></router-link>
        </button>
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
    background-color: rgba(255, 255, 255, 0.65);
    border-radius: 39px;
  }
.choose-btns{
  background-color: rgba(255, 255, 255, 0.65);
  border-radius: 39px;
}
.choose-title{
  font-family: 'Inter';
  font-weight: 400;
  font-style: normal;
  font-size: 1.75rem;
  line-height: 2.118rem;
  color: #24958C;
}

.btn{
  background-color: #FFBD5E;
  color: white;
  border-radius: 13px;
  font-size: 1.25rem;
  letter-spacing: 0.1rem;
}
#makeApplyLink{
  color: white;
  text-decoration: none;
}
#clinicRatingLink{
  color: white;
  text-decoration: none;
}
</style>
