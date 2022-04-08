<template>
  <div class="my-body">
    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container">
        <a href="" class="navbar-brand">
          <img src="./img/logo_white.png" alt="">
          MedReview
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <ul class="navbar-nav">
          <li class="nav-item"><a href="" class="nav-link">Личный кабинет</a></li>
        </ul>
      </div>
      </div>
    </nav>
    <div class="container main-content">

    </div>
    <router-view/>
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
  height: 100vh;
  background-color: #2DB5AB;
}
.main-content{
  height: 100%;
  background-image: url("./svg/background.svg") ;
  background-position: left;
}
</style>
