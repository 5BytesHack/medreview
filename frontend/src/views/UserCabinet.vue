<template>
<div class="container">
  <div class="row mt-2">
    <div class="col profile-list mt-2 ps-4">
      <div class="profile-status-wrapper ps-1">
        <div class="profile-status py-1 w-75 px-2 text-center mb-3">
          <span>Сотрудник</span>
        </div>
      </div>
      <div class="prophile-img-container mb-2">
        <img src="../img/Union.png" alt="">
      </div>
      <div class="personal-data ps-2">
        <h1 class="last-name ">Ухина</h1>
        <h1 class="second-name">Диана</h1>
        <h1 class="first-name">Андреевна</h1>
      </div>
    </div>
    <div class="col mt-2 text-end pe-4">
      <a href="">
        <img src="../svg/_icons.svg" alt="">
      </a>
    </div>
  </div>
  <div class="bg-white accordion-wrapper">
    <div class="accordion accordion-flush" id="our_accordion">
      <div class="accordion-item">
        <h2 class="accordion-header" id="flush-heading1">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse1" aria-expanded="false" aria-controls="flush-collapse1">
            Обращение 1
          </button>
        </h2>
        <div id="flush-collapse1" class="accordion-collapse collapse" aria-labelledby="flush-heading1" data-bs-parent="#our_accordion">
          <div class="accordion-body">Здесь должен быть какой то текст</div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "UserCabinet"
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
.profile-status{
  background-color: #FDA82E;
  border-radius: 40px;
  color: #1F7A74;
  font-size: 1.2rem;
  font-weight: 500;
}
.personal-data:nth-child(n) {
  color: #24958C;
}
.accordion-item{
  border: 2px solid #36B3B5 !important;
  border-radius: 39px !important;

}
.accordion-button{
  border-radius: 39px !important;
}
.accordion{
  border-radius: 39px !important;
}
.accordion-header{
  border-radius: 39px !important;
}
.accordion-wrapper{
  border-radius: 39px;
}
.accordion-button:not(.collapsed) {
  color: white;
  background-color: #36B3B5;
  box-shadow: inset 0 -1px 0 rgb(0 0 0 / 13%);
}
</style>