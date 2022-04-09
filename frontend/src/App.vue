<template>
  <div class="my-body d-flex flex-column h-100">
    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container">
        <router-link to="/" class="navbar-brand">
          <img src="./img/logo_white.png" alt="">
          MedReview
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <ul class="navbar-nav">
          <li class="nav-item"><router-link to="/user_cabinet" class="nav-link">Личный кабинет</router-link></li>
        </ul>
      </div>
      </div>
    </nav>
    <div class="flex-grow-1 flex-shrink-1 main-content">
      <router-view></router-view>
    </div>

  </div>
</template>

<script>
export default {
  data(){
    return{

    }
  }
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
.navbar{
  background-color: #2DB5AB;
}
.my-body{
  background-color: #2DB5AB;
}
.main-content{
  background-image: url("./svg/background.svg");
  background-repeat: no-repeat;
  background-size: 100%;
}
</style>
