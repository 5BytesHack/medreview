<template>
  <div class="container w-100 h-100 py-4">
    <div class="white-platform ps-4 pe-4 pt-2">
      <div class="d-flex flex-row align-items-center">
        <h5 class="pt-2 flex-grow-1" style="font-family: 'Inter';"><strong>Выбрать фото: </strong></h5>
        <div class="flex-grow-1 text-end">
          <button class="btn add-app-btn  text-white" type="button" style="font-family: 'Inter';font-weight: 400">
            Add+
            <input type="file" name="file" multiple/>
          </button>
        </div>

      </div>
      <form action="" class="d-flex flex-column h-100 pb-3 ">
        <div class="form-group  mt-3 mb-2">
          <label for="fioinput" class="form-label" style="font-family: 'Inter';font-weight: 700">ФИО:</label>
          <input type="email" class="form-control" id="fioinput" aria-describedby="emailHelp" placeholder="ФИО">
        </div>
        <div class="form-group mb-2">
          <label for="emailinput" class="form-label" style="font-family: 'Inter';font-weight: 700">E-mail:</label>
          <input type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Email" style="font-family: 'Inter';font-weight: 400">
        </div>
        <div class="form-group mb-2">
          <label for="applyinput" class="form-label" style="font-family: 'Inter';font-weight: 700">Обращение:</label>
          <textarea class="form-control h-100 ps-4 pe-4 apply-input" id="applyinput" rows="3" style="font-family: 'Inter';font-weight: 400"></textarea>
        </div>

        <div class="flex-grow-1 d-flex justify-content-center align-items-end">
          <div class="text-center w-100">
            <button type="button" class=" btn send-btn align-self-center py-2" style="font-family: 'Inter';font-weight: 700">Добавить</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ApplyAdd"
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';

.add-app-btn{
  position: relative;
  overflow: hidden;
  background-color: #42b983;
  border-color: #42b983;
}
.add-app-btn > input{
  position: absolute;
  opacity: 0;
  right: 0;
  top: 0;
}
.add-app-btn:hover{
  background-color: #2DB5AB;
  border-color: #2DB5AB;
}
.white-platform{
  background-color: rgb(255,255,255,.65);
  border-radius: 40px;
  max-width: 600px;
  margin: 0 auto;
}
.btn{
  border-radius: 13px;
  font-size: 1.25rem;
}
.send-btn{
  letter-spacing: 0.1rem;
  color: white;
  background-color: #FFBD5E;
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
.apply-input{
  height: 305px !important;
  font-size:20px;
  color: #24958C !important;
}
.form-label{
  font-size: 1.4rem;
}
</style>