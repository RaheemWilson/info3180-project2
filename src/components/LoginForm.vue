<template>
    <div class="login-form">
        <div v-if="error" class="error">Invalid login information</div>
        <div class="alert alert-success" role="alert" v-if="message">{{ message }}</div>
        <form @submit.prevent="loginUser" method="post">
            <div class="form-field">
                <label for="username">Username</label>
                <input 
                    type="text" 
                    name="username" 
                    id="username" 
                    v-model="username"
                    required
                />
            </div>
            <div class="form-field">
                <label for="password">Password</label>
                <input 
                    type="password" 
                    name="password" 
                    id="password" 
                    v-model="password"
                    required
                />
            </div>
            <button type="submit" class="submit-btn">Login</button>
        </form>
    </div>
</template>

<script>
import AuthService from '@/services/auth.service.js'
import TokenService from '@/services/token.service.js'
import store from '@/store/store.js'
export default {
    data(){
        return {
            username: '',
            password: '',
            error: false,
            message: ''
        }
    },
    async created(){
        let res = await TokenService.getCrsfToken()
        this.csrf = res.csrf_token
    },
    methods: {
        async loginUser(){
            let userInfo = { username: this.username, password: this.password }
            let res = await AuthService.login(userInfo, this.csrf)

            if(res?.errors){
                this.error = true
            } else {
                store.commit('setAuth', { auth: res.token })
                store.commit('setUser', { user: res.id })

                localStorage.setItem('authToken', res.token)
                localStorage.setItem('id', res.id)
                this.$router.push("/explore")
            }
        }
    }
}
</script>

<style scoped>
.login-form{
    padding: 0 2rem;
    width: 100%;
}

.login-form, input{
    border: 1px solid rgba(19, 19, 19, 0.1);
    border-radius: 5px;
}

.form-field, .submit-btn{
    margin: 1rem 0;
}

.form-field input{
    display: block;
}

.submit-btn, input{
    width: 100%;
    height: 44px;
}

.submit-btn{
    border: none;
    border-radius: 5px;
    background: #0eb881;
    color: #ffffff;
}
</style>