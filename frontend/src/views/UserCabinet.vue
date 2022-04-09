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
</style>