import { createStore } from 'vuex'

export default createStore({
  state: {
    is_admin:false,
    is_login:false,
    fio:'',
    email:'',
    user_token:'',
    reqURL:'http://127.0.0.1:8000/api/'
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
    },
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
      state.is_login = isLogin
    },
    setFio(state, fio){
      state.fio = fio
    },
    setEmail(state, email){
      state.email = email
    },
    setUserToken(state, user_token){
      state.user_token = user_token
    },
    setIsDeclined(state, value){
      state.isDeclined = value
    }
  },
  actions: {
    async registerReq(context, user){
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
        response = await fetch(context.getters.reqURL+'registration/', req_opts)
        userData = await response.json()
        //console.log('UserData ',userData)
      }catch (e){
        console.log(e)
        return
      }
      context.commit('setIsLogin', true)
      context.commit('setIsAdmin', false)
      context.commit('setFio', userData.user.first_name)
      context.commit('setUser', userData.user)
    },

    async getUserInfo(context) {
      const req_opts = {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': 'Token '+ context.getters.userToken
        },
      }
      let response
      let userData
      try{
        response = await fetch(context.getters.reqURL+'user/', req_opts)
        userData = await response.json()
      }catch (e){
        console.log(e)
        return
      }
      context.commit('setIsAdmin', userData.user.is_staff)
      context.commit('setFio', userData.user.first_name + userData.user.last_name + userData.user.patronymic)
      context.commit('setUser', userData.user)

    },

    saveToLocal(context){
      const user = {
        fio : context.state.fio,
        email : context.state.email,
        user_token : context.state.user_token,
        isAdmin : context.state.is_admin,
        isLogin : context.state.is_login
      }
      console.log('userInLS ',user)
      localStorage.clear()
      localStorage.setItem('user', JSON.stringify(user))
    },

    loadUserIfExist(context){
      const user = JSON.parse(localStorage.getItem('user'))
      if(user){
        console.log('parsedUser ', user)
        context.state.fio = user.fio
        context.state.email = user.email
        context.state.user_token = user.user_token
        context.state.is_login = user.isLogin
        context.state.is_admin = user.isAdmin
        //context.commit('setIsLogin', user.isLogin)
        //context.commit('setIsAdmin', user.isAdmin)
      }
    },

    async logInReq(context, user){
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
        response = await fetch(context.getters.reqURL+'login/', req_opts)
        userData = await response.json()
        console.log('UserData ',userData)
      }catch (e){
        console.log(e)
        return
      }
      context.commit('setIsLogin', true)
      context.commit('setIsAdmin', false)
      context.commit('setEmail', userData.user.email)
      context.commit('setUserToken', userData.user.token)
      //context.commit('setUser', userData.user)
    },

    async sendApply(context, req_body){
      const req_opts = {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(req_body)
      }
      let response
      try {
        response = await fetch(context.getters.reqURL+'create_review/', req_opts)
        if(response.ok){
          this.$router.push('/')
        }
        else{
          alert("Что-то пошло не так")
        }
      }catch (e){
        console.log(e)
        return
      }
    }
  },
  modules: {
  }
})
