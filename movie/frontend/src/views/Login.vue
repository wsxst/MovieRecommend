<template>
    <div class="container">


        <div class="col-sm-6 col-sm-offset-3">

            <h1><span class="fa fa-sign-in"></span> Welcome</h1>

            <!-- LOGIN FORM -->

                <div class="form-group">
                    <label>Username</label>
                    <el-input v-model="payload.username" placeholder="请输入用户名"></el-input>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <el-input v-model="payload.password" type="password" placeholder="请输入密码"></el-input>
                </div>

                <el-button type="primary" @click="login">Login</el-button>
                <el-button type="warning" @click="onSignup">Go Signup</el-button>

            <hr>

        </div>

    </div>
</template>

<script>
	/* eslint-disable */
    import authController from '../controller/authController'
    export default {
        name: "Login",
        data(){
            return {
                payload: {
                    username:"",
                    password:"",
                },
            }
        },
        methods: {
            login: async function () {
                //Try to Login
                console.log("Login Payload " + JSON.stringify(this.payload))
                if (this.payload.username == "" || this.payload.password == ""){
                    this.$message({
                        message: '用户名或密码不能为空',
                        type: 'error'
                    });
                    return
                }
                let response = false
                try {
                   response  = await authController.login(this.payload)
                } catch (e) {
                    console.error('Error in Login')
                    console.error(e)
                }
                if(response){
                    this.$root.$data.userDetail = response
                    this.$cookie.set('userid',response.userid , 1);
                    this.$cookie.set('username',response.username , 1);
                    this.$router.push({
                        name: "profile"
                    });
                } else{
                    this.$message({
                        message: '用户名或密码错误',
                        type: 'error'
                    });
                    /*alert("")*/
                }
            },
            onSignup: function () {
                // Jump to Signup
                this.$router.push({path: 'register'})
            }
        }
    }
</script>

<style scoped>

</style>
