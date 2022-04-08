<template>
  <div class="">
    <!--<nav class="nav-header d-flex justify-content-between">
      <router-link to="/"><img src="@/img/logo_white.png" alt="user_icon">MedReview</router-link>
      <router-link to="/about"></router-link>
    </nav>-->
    <nav class="navbar navbar-expand-lg">

        <div class="">
          <a class="navbar-brand" href="#!"><img src="@/img/logo_white.png" alt="user_icon">MedReview</a>
        </div>

        <div class="collapse navbar-collapse justify-content-end" id="navbarTogglerDemo02">
          <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon">ggg</span>
          </button>
          <ul class="navbar-nav mr-auto mt-2 mt-md-0 ">
            <li class="nav-item active">
              <a class="nav-link" href="#!">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#!">Link</a>
            </li>
          </ul>
        </div>
    </nav>

    <router-view/>
  </div>
</template>

<style>
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
