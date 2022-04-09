<template>
  <div class="container d-flex flex-column w-100 h-100 py-3">
    <div class="white-platform ps-4 pe-4 flex-grow-1">
      <form action="" class="d-flex flex-column h-100 pb-3 ">
        <div class="form-group mt-4 mb-2">
          <label for="fioinput" class="form-label">ФИО:</label>
          <input type="text" class="form-control" id="fioinput" aria-describedby="fio" v-bind:value="fio" placeholder="ФИО">
        </div>
        <div class="form-group mb-2">
          <label for="oldpasswordinput" class="form-label">Старый пароль:</label>
          <input type="password" class="form-control" id="oldpasswordinput" aria-describedby="password" placeholder="старый пароль">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput" class="form-label">Новый пароль:</label>
          <input type="password" class="form-control" id="newpasswordinput" aria-describedby="password" placeholder="новый пароль">
        </div>
        <div class="form-group mb-2">
          <label for="newpasswordinput_2" class="form-label">Повторите новый пароль:</label>
          <input type="password" class="form-control" id="newpasswordinput_2" aria-describedby="password" placeholder="повторите новый пароль">
        </div>
        <div class="flex-grow-1 d-flex flex-column justify-content-end">
          <div class="text-center w-100 mt-2">
            <button type="button" class="w-75 btn  align-self-center py-2"><strong>Сохранить</strong></button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import store from "@/store";

export default {
  name: "ChangeUserProfile",
  data(){
    return {
      checked: false,
    }
  },
  computed:{
    fio(){
      return store.getters.fio;
    },
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
.form-control{
  border-width: 2px;
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