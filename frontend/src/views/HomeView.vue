<template>
  <div class="home container d-flex flex-column my-3">
    <div class="about-info">
      <p class="choose-title text-center py-3 px-2">Добро пожаловать на сайт MedReview! <br> Здесь вы можете создать обращение по работе медицинских учреждений. Мы ценим ваше мнение!</p>
    </div>

    <div class="choose-btns d-flex flex-column mt-2 justify-content-around">
      <div class="pt-2">
        <p class="choose-title text-center">Выберите одно из возможных действий</p>
      </div>
      <div class="d-flex flex-column align-items-center justify-content-center">
        <button type="button" class="w-75 btn py-2 my-3">
          <router-link id="makeApplyLink" to="/anon_send"><strong>Создать обращение</strong></router-link>
        </button>
        <button type="button" class="w-75 btn py-2 mb-3">
          <router-link id="clinicRatingLink" to="/"><strong>Рейтинг клиник</strong></router-link>
        </button><!-- rating -->
        <button v-on:click="test" class="btn">ТЕСТ</button>
      </div>
    </div>
  </div>
</template>

<script>
import store from "@/store";
export default {
  name: 'HomeView',
  components: {

  },
  methods:{
    test(){
      store.dispatch('getUsers')
    }
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
  font-size: 1.5rem;
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
