import { createStore } from 'vuex'

export default createStore({
  state: {
    is_admin:false,
    fio:'',
    email:'',
    user_token:''
  },
  getters: {
    isAdmin(){
      return this.state.is_admin
    },
    fio(){
      return this.state.fio
    },
    email(){
      return this.state.email
    },
    userToken(){
      return this.state.user_token
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
