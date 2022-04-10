<template>
  <div class="container d-flex flex-column w-100 h-100 py-3">
    <div class="white-platform ps-4 pe-4 flex-grow-1">
      <form action="" class="d-flex flex-column h-100 pb-3 ">
        <div class="form-group mt-4 mb-2">
          <label for="fioinput" class="form-label">ФИО:</label>
          <input v-model="fio" type="text" class="form-control" id="fioinput" aria-describedby="fio" placeholder="ФИО">
        </div>
        <div class="form-group mb-2">
          <label for="emailinput" class="form-label">E-mail:</label>
          <input v-model="email" type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="email">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput" class="form-label">Пароль:</label>
          <input v-model="password" type="password" class="form-control" id="newpasswordinput" aria-describedby="password" placeholder="новый пароль">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput_2" class="form-label">Повторите пароль:</label>
          <input type="password" class="form-control" id="newpasswordinput_2" aria-describedby="password" placeholder="повторите новый пароль">
        </div>
        <div class="form-check mb-2">
          <div class="d-flex flex-row align-items-end">
            <div class="me-3">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
            </div>
            <div class="">
              <label class="form-check-label form-label" for="exampleCheck1" >
                Согласен с <a href="">политикой</a> обработки данных</label>
            </div>
          </div>
        </div>
        <div class="flex-grow-1 d-flex flex-column justify-content-end">
          <div class="text-center w-100 mt-2">
            <button v-on:click="register" type="button" class="w-75 btn align-self-center py-2"><strong>Зарегистрироваться</strong></button>
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
  methods:{
    register(){
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
      store.dispatch('loginReq', req_body)
      //console.log('URL', this.$store.getters(''))
      store.dispatch('saveToLocal')
    }
  }
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
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
  font-weight: 650;
}
</style>