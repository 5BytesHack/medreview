<template>
  <div class="container d-flex flex-column w-100 h-100 py-3">
    <div class="white-platform ps-4 pe-4 flex-grow-1">
      <p v-if="isDeclined" style="color:red">Ошибка регистрации</p>
      <form action="" class="d-flex flex-column h-100 pb-3 ">
        <div class="form-group mt-4 mb-2">
          <label for="fioinput" class="form-label" style="font-family: 'Inter';font-weight: 700">ФИО:</label>
          <input v-model="fio" type="text" class="form-control" id="fioinput" aria-describedby="fio" placeholder="ФИО" style="font-family: 'Inter';font-weight: 400">
        </div>
        <div class="form-group mb-2">
          <label for="emailinput" class="form-label" style="font-family: 'Inter';font-weight: 700">E-mail:</label>
          <input v-model="email" type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="email" style="font-family: 'Inter';font-weight: 400">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput" class="form-label" style="font-family: 'Inter';font-weight: 700">Пароль:</label>
          <input v-model="password" type="password" class="form-control" id="newpasswordinput" aria-describedby="password" placeholder="новый пароль" style="font-family: 'Inter';font-weight: 400">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput_2" class="form-label" style="font-family: 'Inter';font-weight: 700">Повторите пароль:</label>
          <input type="password" class="form-control" id="newpasswordinput_2" aria-describedby="password" placeholder="повторите новый пароль" style="font-family: 'Inter';font-weight: 400">
        </div>
        <div class="form-check mb-2">
          <div class="d-flex flex-row align-items-end">
            <div class="me-3">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
            </div>
            <div class="">
              <label class="form-check-label form-label" for="exampleCheck1" style="font-family: 'Inter';font-weight: 700">
                Согласен с <a href="" class="our-link">политикой</a> обработки данных</label>
            </div>
          </div>
        </div>
        <div class="flex-grow-1 d-flex flex-column justify-content-end">
          <div class="text-center w-100 mt-2">
            <button v-on:click="register" type="button" class="w-75 btn align-self-center py-2" style="font-family: 'Inter';font-weight: 700">Зарегистрироваться</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import store from "@/store";
export default {
  name: "RegisterUser",
  data(){
    return{
      checked:false,
      fio:'',
      email:'',
      password:''
    }
  },
  computed:{
    isDeclined(){
      return store.getters.isDeclined
    }
  },
  methods:{
    async register(){
      const fio_split = this.fio.split(' ')
      let first_name = ''
      let last_name = ''
      let patronymic = null
      if(fio_split[0]) {
        first_name = fio_split[0]
      }
      if(fio_split[1]) {
        last_name = fio_split[1]
      }
      if(fio_split[2]) {
        patronymic = fio_split[2]
      }
      console.log(first_name, last_name, patronymic)
      const req_body = {
        user:{
          email:this.email,
          first_name:first_name,
          last_name:last_name,
          patronymic:patronymic,
          password:this.password
        }
      }
      await store.dispatch('registerReq', req_body)
      //console.log('URL', this.$store.getters(''))
      if(store.getters.isLogin) {
        await store.dispatch('saveToLocal')
        this.$router.push('/user_cabinet')
      }
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
.our-link{
  color: #42b983;
}
.our-link:hover{
  color: #1F7A74;
}
.white-platform{
  background-color: rgb(255,255,255,.65);
  border-radius: 40px;
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

.form-control, .form-check-input{
  border-width: 2px;
  border-color: #36B3B5;
}
.form-check-input{
  border-radius: 0 !important;
  height: 30px;
  width: 30px;
}
.form-check-input:checked {
  background-color: #36B3B5;
  border-color: #36B3B5;
}
.white-platform{
  color: #24958C;
}
.form-label{
  font-size: 1.4rem;
}
</style>