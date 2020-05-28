import api from './api'

export default {
    login(data){
        return api.callApi(`post`,`/login`, data)
    },
    logout(){
        return api.callApi(`get`,`/logout`)
    },
    register(data){
        return api.callApi(`post`, '/register', data)
    }
}
