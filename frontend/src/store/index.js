import { createStore } from 'vuex'

export default createStore({
  state: {
    is_admin:false,
    fio:'',
    email:'',
    user_token:''
  },
  getters: {
    isAdmin(state){
      return state.is_admin
    },
    fio(state){
      return state.fio
    },
    email(state){
      return state.email
    },
    userToken(state){
      return state.user_token
    }
  },
  mutations: {
    setIsAdmin(state, is_admin){
      state.is_admin = is_admin
    },
    setFio(state, fio){
      state.fio = fio
    },
    setEmail(state, email){
      state.email = email
    },
    setUserToken(state, user_token){
      state.user_token = user_token
    }
  },
  actions: {

  },
  modules: {
  }
})
