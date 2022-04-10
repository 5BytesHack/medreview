<template>
<div class="container w-100 h-100 py-4">
  <div class="white-platform ps-4 pe-4 ">
    <form action="" class="d-flex flex-column h-100 pb-3 ">
      <div v-if="isLogin" class="form-group mt-4 mb-2 ">
        <label style="font-family: 'Inter';font-weight: 700" for="fioinput" class="form-label">ФИО:</label>
        <input v-model="fio" style="font-family: 'Inter';font-weight: 400" type="email" class="form-control" id="fioinput" aria-describedby="emailHelp" placeholder="Введите ФИО">
      </div>
      <div v-if="isLogin" class="form-group mb-2">
        <label style="font-family: 'Inter';font-weight: 700" for="emailinput" class="form-label">E-mail:</label>
        <input v-model="email" style="font-family: 'Inter';font-weight: 400" type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Введите Email">
      </div>
      <div class="form-group mb-2">
        <label style="font-family: 'Inter';font-weight: 700" for="applyinput" class="form-label">Обращение:</label>
        <textarea v-model="text" style="font-family: 'Inter';font-weight: 400" class="form-control h-100 ps-4 pe-4 apply-input" id="applyinput" rows="3"></textarea>
      </div>
      <div class="form-check mb-2">
        <div class="d-flex flex-row align-items-center ">
          <div class="me-3">
            <input v-model="checked" type="checkbox" class="form-check-input" id="exampleCheck1">
          </div>
          <div class="">
            <label class="form-check-label form-label pt-2" for="exampleCheck1" style="font-family: 'Inter';font-weight: 700">
              Согласен с <a href="" class="our-link">политикой</a> обработки данных</label>
          </div>
        </div>
      </div>
      <div class="flex-grow-1 d-flex justify-content-center align-items-end">
        <div class="text-center w-100">
          <button v-on:click="sendApply" style="font-family: 'Inter';font-weight: 400" type="button" class=" btn align-self-center py-2"><strong>Отправить</strong></button>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
import store from "@/store";

export default {
  name: "ApplySend",
  data() {
    return {
      fio: '',
      email: '',
      text: '',
      checked: false,
    }
  },
  methods: {
    sendApply() {
      const req_body = {
        review: {
          author: {
            email:'',
            first_name:'',
            last_name:'',
            patronymic:'',
            is_staff:'',
            token:''
          }
        },
        fio: this.fio,
        email: this.email,
        text: this.text
      }
      if (store.getters.isLogin) {
        const fio = store.getters.fio.split(' ')
        req_body.review.author.email = store.getters.email
        req_body.review.author.first_name = fio[0]
        req_body.review.author.last_name = fio[1]
        if (fio[2]) {
          req_body.review.author.patronymic = fio[2]
          req_body.review.author.is_staff = store.getters.isAdmin
          req_body.review.author.token = store.getters.userToken

          req_body.review.fio = store.getters.fio
          req_body.review.email = store.getters.email
          req_body.review.text = this.text
        }
        else{
          req_body.review.author = null
        }
        console.log('req_body ', req_body)
      }
      store.dispatch('sendApply', req_body)
    },
    computed: {
      isLogin() {
        return store.getters.isLogin;
      }
    }
  }
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
.our-link{
  color: #42b983;
}
.our-link:hover{
  color: #1F7A74;
}
.white-platform{
  background-color: rgb(255,255,255,.65);
  border-radius: 40px;
  max-width: 600px;
  margin: 0 auto;
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
.apply-input{
  height: 305px !important;
  font-size:20px;
  color: #24958C !important;
}
.form-label{
  font-size: 1.4rem;
  font-weight: 650;
}
</style>