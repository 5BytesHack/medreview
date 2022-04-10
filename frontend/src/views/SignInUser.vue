<template>
  <div class="container d-flex flex-row w-100 h-100 py-3 justify-content-center align-items-lg-center">
    <div class="white-platform ps-4 pe-4 flex-grow-1">
      <form  action="" class="d-flex flex-column h-100 pb-3 mt-3">
        <div class="form-group mb-2">
          <label for="emailinput" class="form-label">E-mail:</label>
          <input v-model="email" type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="введите email">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput" class="form-label">Пароль:</label>
          <input v-model="password" type="password" class="form-control" id="newpasswordinput" aria-describedby="password" placeholder="введите пароль">
        </div>
        <div class="flex-grow-1 d-flex flex-column justify-content-end">
          <div class="d-flex flex-column text-center w-100 mt-5 mb-3">
            <button type="button" v-on:click="login" class="w-75 btn  align-self-center py-2"><strong>Войти</strong></button>
            <router-link to="/user_register">Регистрация</router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignInUser",
  data(){
    return{
      fio:'',
      email:'',
      password:''
    }
  },
  methods:{

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
  url('../fonts/Inter-Regular.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 700;
  font-style: normal;
  src:local('Inter'),
  url('../fonts/Inter-Bold.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 900;
  font-style: normal;
  src:local('Inter'),
  url("../fonts/Inter-Black.ttf") format('truetype');
}
.white-platform{
  background-color: rgb(255,255,255,.65);
  border-radius: 40px;
  max-width: 600px;

}
.btn{
  background-color: #FFBD5E;
  color: white;
  border-radius: 13px;
  font-size: 1.25rem;
  letter-spacing: 0.1rem;
}
.form-control{
  border-radius: 39px;
  height: 46px;
}
.form-control{
  border-width: 2px;
  border-color: #36B3B5;
}
.white-platform{
  color: #24958C;
}
.form-label{
  font-family: 'Inter';
  font-size: 1.4rem;
  font-weight: 400;
}
</style>