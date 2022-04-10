<template>
<div class="container">
  <div class="d-flex mt-2 justify-content-md-center position-relative">
    <div class="profile-list mt-2 ps-4 ps-md-0 text-md-center flex-md-shrink-1">
      <div class="profile-status-wrapper ps-1 d-md-flex justify-content-center">
        <div v-if="isAdmin" class="profile-status py-1  px-4 text-center mb-3 ">
          <span>Сотрудник</span>
        </div>
        <div class="d-flex flex-column mt-2 text-end pe-4 position-absolute edit-btn">
          <router-link v-on:click="signOut" to="/">
            <img src="../svg/signOutIcon.svg" alt="">
          </router-link>
          <router-link class="mt-2" to="/change_profile">
            <img src="../svg/_icons.svg" alt="">
          </router-link>
        </div>
      </div>
      <div class="prophile-img-container mb-2">
        <img src="../img/Union.png" alt="">
      </div>
      <div class="personal-data ps-2">
        <h1 class="last-name ">{{firstName}}</h1>
        <h1 class="second-name">{{lastName}}</h1>
        <h1 class="first-name">{{patronymic}}</h1>
      </div>

    </div>

  </div>


  <div class="bg-white accordion-wrapper">
    <h1 style="font-family: 'Inter';font-weight: 900" class="mt-4 text-center applies-header position-relative">Обращения
      <button v-if="false" class="btn upl-button position-absolute me-3 me-lg-0">
        <router-link style="text-decoration: none" to="/apply_add" class="text-white">Add+</router-link>
      </button>
    </h1>
    <div class="accordion accordion-flush" id="our_accordion">
      <div class="accordion-item mb-2" >
        <h2 class="accordion-header" id="flush-heading1" style="font-family: 'Inter';font-weight: 400">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse1" aria-expanded="false" aria-controls="flush-collapse1">
            <span class="m-0 pe-4 apply-num">#1:</span>
            <span style="font-family: 'Inter';font-weight: 400" class=" m-0 text-truncate apply-header">Довожу до Вашего сведения, что (дата) на горячую линию обратилась клиент (ФИО, тел.) с жалобой на ПЗ.  Клиент недовольна качеством обслуживания. Клиенту удобно обращаться в указанный ПЗ. Клиент недовольна тем, что сотрудник общается неприветливо, не отвечает на вопросы   клиента по   подготовке и правилах сбора и хранения биоматериала. Клиент просит разобраться и принять меры. Ждет звонка администрации.</span>
            <span style="font-family: 'Inter';font-weight: 400" class="flex-grow-1 text-end px-3">
              <img src="../svg/clock.svg" alt="" class="status-img">
            </span>
          </button>
        </h2>
        <div id="flush-collapse1" class="accordion-collapse collapse" aria-labelledby="flush-heading1" data-bs-parent="#our_accordion">
          <div style="font-family: 'Inter';font-weight: 400" class="accordion-body">
            <span class="pb-1 text-wrap text-wrapper">
              <strong>Дата создания обращения:</strong>
              <span class="date-text">
                25.08.2019
              </span>
              <br>
              <br>
               <span class="user-apply pt-3">
                <strong>Ваше обращение: </strong>
                <span class="user-apply-text">
                       Довожу до Вашего сведения, что 25.08.2019 на горячую линию обратилась клиент Иванова Л.М. с жалобой на ПЗ. Клиент недовольна качеством обслуживания. Клиенту удобно обращаться в указанный ПЗ. Клиент недовольна тем, что сотрудник общается неприветливо, не отвечает на вопросы клиента по подготовке и правилах сбора и хранения биоматериала. Клиент просит разобраться и принять меры. Ждет звонка администрации.
                </span>
              </span>
            </span>
            <br>
            <span class="pb-1 text-wrap text-wrapper d-none">
              <br>
               <span class="date-answer">
                  <strong>Дата ответа: </strong>
                  <span class="date-text">
                  11.04.2020
                </span>
               </span>
              <br>
              <br>
              <span class="admin-answer-wrapper">
                <strong>Ответ администратора: </strong>
                <span class="admin-answer">
                  Ответ на Вашу служебную записку от Иванова Л.М с жалобой на ПЗ. Во время диалога с пациентом выяснилось, что клиент в принципе считает недопустимым прием материала на исследование «Коронавирус» в детской лаборатории «Baby Lab». Пациенту даны пояснения, что лаборатория CL обладает всеми необходимыми разрешениями Роспотребнадзора, а также лицензиями на право проведения исследований 3-4 группы патогенности. Соблюдаются все меры защиты и предосторожности при обслуживании пациентов. К сожалению, наличие таковых документов не убедило клиента в законности проведения анализа на «Коронавирус» в указанном филиале.
                </span>
              </span>
              <br>
            </span>
          </div>
        </div>
      </div>
      <div class="accordion-item mb-2">
        <h2 class="accordion-header" id="flush-heading2">
          <button class="accordion-button collapsed justify-content-between" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse2" aria-expanded="false" aria-controls="flush-collapse2">
            <span style="font-family: 'Inter';font-weight: 400" class="m-0 pe-4 apply-num ">#2:</span>
            <span class=" m-0 text-truncate apply-header">Довожу до Вашего сведения, что на горячую линию обратилась клиент Пелипенко Е.Ю. с жалобой на ПЗ Ейск. Клиент обратилась в указанный ПЗ для сдачи биоматериала на исследование «Коронавирус». Клиент недовольна тем, что сотрудник ПЗ сфотографировала паспорт клиента на личный телефон. Клиент считает это нарушением. Клиент просит разобраться и принять меры. Ждет звонка администрации.</span>
            <span class="flex-grow-1 text-end pe-3 ps-2">
              <img src="../svg/msg-check.svg" alt="" class="status-img">
            </span>
          </button>
        </h2>
        <div id="flush-collapse2" class="accordion-collapse collapse" aria-labelledby="flush-heading2" data-bs-parent="#our_accordion">
          <div class="accordion-body" style="font-family: 'Inter';font-weight: 400">
             <span class="pb-1 text-wrap text-wrapper"><strong>Дата создания обращения:</strong>
              <span class="date-text">
                25.08.2019
              </span>
              <br>
              <br>
               <span class="user-apply pt-3">
                <strong>Ваше обращение: </strong>
                <span class="user-apply-text">
                  Довожу до Вашего сведения, что на горячую линию обратилась клиент Пелипенко Е.Ю. с жалобой на ПЗ Ейск. Клиент обратилась в указанный ПЗ для сдачи биоматериала на исследование «Коронавирус». Клиент недовольна тем, что сотрудник ПЗ сфотографировала паспорт клиента на личный телефон. Клиент считает это нарушением. Клиент просит разобраться и принять меры. Ждет звонка администрации.
                </span>
              </span>
            </span>
            <br>
            <span class="pb-1 text-wrap text-wrapper">
              <br>
               <span class="date-answer">
                  <strong>Дата ответа: </strong>
                  <span class="date-text">
                  11.04.2020
                </span>
               </span>
              <br>
              <br>
              <span class="admin-answer-wrapper">
                <strong>Ответ администратора: </strong>
                <span class="admin-answer">
                  Ответ на Вашу служебную записку Пелипенко Е.Ю. с жалобой на ПЗ Ейск. По обращению пациента проверена информация. Установлено, что медсестра фотографировала паспорт пациента для отправки в ОЭБ согласно предоставленной ранее инструкции по оформлению пациентов на CoVid 19. После отправки данных, информация удаляется. Необходимость в паспортных данных пациента – одно из требований Роспотребнадзора, т.к. в случае положительного результата вся информация передается в Роспотребнадзор, в случае отрицательного результата копии документа пациента удаляются.
                </span>
                </span>
              <br>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import store from "@/store";
export default {
  name: "UserCabinet",
  data(){
    return{

    }
  },
  computed:{
    firstName(){
      const first_name = store.getters.fio?.split(' ')[0];
      return first_name === null?'':first_name
    },
    lastName(){
      const last_name = store.getters.fio?.split(' ')[1];
      return last_name === null?'':last_name
    },
    patronymic(){
      const patronymic = store.getters.fio?.split(' ')[2];
      return patronymic === null?'':patronymic
    },
    isAdmin(){
      return store.getters.isAdmin;
    }
  },
  methods:{
    signOut(){
      localStorage.clear();
      store.commit('setIsLogin', false)
      store.commit('setIsAdmin', false)

      store.commit('setFio', '')
      store.commit('setEmail', '')
      store.commit('setUserToken', '')
    }
  }
}
</script>

<style scoped>
@import'bootstrap/dist/css/bootstrap.min.css';
@font-face {
  font-family: 'Inter';
  font-weight: 400;
  font-style: normal;
  src:local('Inter'),
  url('../fonts/Inter-Regular.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 700;
  font-style: normal;
  src:local('Inter'),
  url('../fonts/Inter-Bold.ttf') format('truetype');
}
@font-face {
  font-family: 'Inter';
  font-weight: 900;
  font-style: normal;
  src:local('Inter'),
  url("../fonts/Inter-Black.ttf") format('truetype');
}
.upl-button{
  background-color: #FFBD5E;
  border-color: #FFBD5E;
  top:0;
  right: 0;
  bottom: 0;
}
.upl-button:hover{
  background-color: #FDA82E;
  color: #FDA82E;
}
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
  border-radius: 13px !important;
}
.accordion-button{
  border-radius: 13px !important;
  border: 2px solid #36B3B5 !important;
  color: #1F7A74;
}
.accordion{
  border-radius: 13px !important;


}
.accordion-header{
  border-radius: 13px !important;
}
.accordion-wrapper{
  border-radius: 13px;
  background-color: transparent !important;
  max-width: 900px !important;
  margin: 0 auto;
}
.accordion-button:not(.collapsed) {
  color: white;
  background-color: #36B3B5;
  box-shadow: inset 0 -1px 0 rgb(0 0 0 / 13%);
}
.status-img{
width: 28px;
  height: auto;
}
.apply-num{
  font-size: 1.2rem;
  font-weight: 500;
}
.apply-header{
font-size: 1rem;
}
.applies-header{
  color: #24958C;
}
.edit-btn{
  top:0;
  bottom: 0;
  right: 0;
}
</style>