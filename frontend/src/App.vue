<template>
  <div class="my-body d-flex flex-column h-100">
    <nav class="navbar navbar-expand-lg navbar-dark pb-1 pt-2 justify-content-center">
      <div class="container m-1">
        <router-link to="/" class="navbar-brand d-flex flex-row">
          <img src="./img/logo_white.png" alt="">
          <h1 class="m-0 pt-2">MedReview</h1>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <ul class="navbar-nav">
          <li class="nav-item d-inline-flex"><span id="user-cabinet-link" v-on:click="goToUserCabinetIfLogin" class="nav-link text-nowrap pb-0 pt-md-4 h5 m-0">Личный кабинет <span v-if="isLogin">{{'('+ shortFio +')'}}</span></span></li>
        </ul>
      </div>
      </div>
    </nav>
      <div class="flex-grow-1 flex-shrink-1 main-content overflow-auto">
        <router-view></router-view>
      </div>


  </div>
</template>

<script>
import store from "@/store";
export default {
  data(){
    return{

    }
  },
  created(){
    store.dispatch('loadUserIfExist')
  },
  computed:{
    shortFio() {
      if (store.getters.isLogin) {
        const fio = store.getters.fio.split(' ');
        let patronymic = ' ';
        if (fio[2]) {
          patronymic = fio[2]
        }
        let shortFio = ''
        if(fio) {
          shortFio = fio[0] + " " + fio[1].charAt(0) + '.' + patronymic.charAt(0) + '.';
        }
        return shortFio;
      }
      return ''
    },
    isLogin(){
      return store.getters.isLogin
    }
  },
  methods:{
    goToUserCabinetIfLogin(){
      if(this.$store.getters.isLogin){
        this.$router.push('/user_cabinet')
      }
      else{
        this.$router.push('/user_signin')
      }
    }
  }
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
#user-cabinet-link:hover{
  cursor: pointer;
}
.navbar{
  background-color: #2DB5AB;
}
.my-body{
  background-color: #2DB5AB;
}
.main-content{
  background: url("./svg/background.svg") 0 0/cover no-repeat;
  background-size: 100%;
}

@media (min-width: 768px) {
  .main-content{
    background: url("./svg/background_1024.svg") 0 0/cover no-repeat;
    background-size: 100%;
  }
}
</style>
