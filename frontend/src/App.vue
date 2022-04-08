<template>
  <div class="">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="/">Navbar</a>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav mr-auto mt-2 mt-md-0">
          <li class="nav-item active">
            <a class="nav-link" href="#">Личный кабинет<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/about">О нас</a>
          </li>
        </ul>
      </div>
    </nav>
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

.nav-header{
  background-color: #2DB5AB;
}
.nav-header a{
  color: white;
  /*font-family: Inter;*/
  font-style: italic;
  font-size: 2.1618rem;
  font-weight: 800;
  text-decoration: none;
}

.navbar{
  background-color: #2DB5AB;
}
</style>
