<template>
  <div class="container py-4 h-100 ">
    <div class="white-platform px-4 px-lg-5">
      <form action="" class="d-flex flex-column h-100 pb-3 flex-grow-1">
        <div class="form-group mb-3">
          <label for="applyinput" class="form-label mt-2">
            Обращение
            <span class="apply-num">#1:</span>
          </label>
          <div class="mb-3 user-text-wrapper">
           <span class="user-text text-wrap">
             <strong>Сообщение: </strong>
              <span class="text-black text-apply text-wrap">шав ргвашишловарп шуав
          Я конещвы ошо вигш ор шовапшо вашо
                  ошварпошв ароп шрвшо шваш швао ошва швар гшвар шв ровшарпшв ршва шва шов
                </span>
            </span>
          </div>
          <textarea class="form-control h-100 ps-4 pe-4 apply-input " id="applyinput" rows="3"></textarea>
        </div>
        <div class="d-flex justify-content-center">
          <div class="">
            <button type="button" class="btn hint-btn text-white mx-1 mb-1">Добрый</button>
            <button type="button" class="btn hint-btn text-white mx-1 mb-1">Плохой</button>
            <button type="button" class="btn hint-btn text-white mx-1 mb-1">Зайчик</button>
            <button type="button" class="btn hint-btn text-white mx-1 mb-1">Черт</button>
            <button type="button" class="btn hint-btn text-white mx-1 mb-1">Козел</button>
          </div>
        </div>
        <div class="flex-grow-1 d-flex justify-content-center align-items-end ">
          <div class="text-center mt-3">
            <button type="button" class="send-btn btn align-self-center py-2"><strong>Отправить</strong></button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ApplyDetails"
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
.white-platform{
  background-color: rgb(255,255,255,.65);
  border-radius: 40px;
}
.hint-btn{
  background-color: #36B3B5;
  border-color: #24958C;
}
.send-btn{
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
  max-width: 700px;
  margin: 0 auto;
}
.apply-input{
  height: 305px !important;
  font-size:20px;
  color: #24958C !important;
}
.form-label, .apply-num{
  font-size: 1.4rem;
  font-weight: 650;
}
.user-text{
  color: #24958C ;
}
.user-text-wrapper{

}
</style>