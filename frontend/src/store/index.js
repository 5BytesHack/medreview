import { createStore } from 'vuex'

export default createStore({
  state: {
    is_admin:false,
    isLogin:false,
    fio:'',
    email:'',
    user_token:'',
    reqURL:'http://127.0.0.1:8000/api/registration/'
  },
  getters: {
    isAdmin(state){
      return state.is_admin
    },
    isLogin(state){
      return state.isLogin
    },
    fio(state){
      return state.fio
    },
    email(state){
      return state.email
    },
    userToken(state){
      return state.user_token
    },
    reqURL(state){
      return state.reqURL
    }
  },
  mutations: {
    setUser(state, user){
      state.fio = user.fistname + user.lastname + user.patronymic
      state.email = user.email
      state.user_token = user.token
    },
    setIsAdmin(state, is_admin){
      state.is_admin = is_admin
    },
    setIsLogin(state, isLogin){
      state.isLogin = isLogin
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
