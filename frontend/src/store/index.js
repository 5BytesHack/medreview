import { createStore } from 'vuex'

export default createStore({
  state: {
    is_admin:false,
    is_login:false,
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
      return state.is_login
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
      state.fio = [user.first_name,user.last_name,user.patronymic].join(' ')
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
    async loginReq(context, user){
      const req_opts = {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(user)
      }
      let response
      let userData
      try {
        response = await fetch(context.getters.reqURL, req_opts)
        userData = await response.json()
      }catch (e){
        console.log(e)
        return
      }
      if(userData.user.token === '' || userData.user.token === null)
        return
      context.commit('setIsLogin', true)
      context.commit('setIsAdmin', false)
      context.commit('setUser', userData.user)
    },

    saveToLocal(context){
      const user = {
        fio : context.getters.fio,
        email : context.getters.email,
        user_token : context.getters.userToken,
        isAdmin : context.getters.isAdmin,
        isLogin : context.getters.isLogin
      }
      console.log(user)
      localStorage.setItem('user', JSON.stringify(user))
    },

    loadUserIfExist(context){
      const user = JSON.parse(localStorage.getItem('user'))
      if(user){
        context.commit('setUser', user)
        context.commit('setIsLogin', user.isLogin)
        context.commit('setIsAdmin', user.isAdmin)
      }
    }
  },
  modules: {
  }
})
