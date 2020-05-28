<template>
    <div class="container">

        <h2><p v-show="alert">{{alertMessage}}</p></h2>
        <div class="col-sm-6 col-sm-offset-3">

            <h1><span class="fa fa-sign-in"></span> Signup</h1>

            <!-- Register FORM -->
            <div class="form-group">
                <label>UserName</label>
                <el-input v-model="payload.username" placeholder="请输入用户名"></el-input>
            </div>
                <div class="form-group">
                    <label>Password</label>
                    <el-input v-model="payload.password" type="password" placeholder="请输入密码"></el-input>
                </div>

                <el-button type="primary" @click="register">register</el-button>

            <hr>

            <p>Already have an account? <a @click="onLogin">Go Login</a></p>

        </div>

    </div>
</template>

<script>
	/* eslint-disable */
    import authController from '../controller/authController'
    export default {
        name: "Register",
        data(){
            return {
                payload: {},
                alert: false,
                alertMessage: "nothing"
            }
        },
        methods:{
          register: async function () {
              //Register User
              console.log("Register Payload" + JSON.stringify(this.payload))
              let response = false
              try {
                  response = await authController.register(this.payload)
              }catch (e) {
                  console.error('Error in registring');
                  console.error(e)
              }
              if(response){
                  console.log("Registered Success!");
                  this.$router.push({path: 'login'})
              } else {
                  this.alert = true
                  this.alertMessage = "Registration Fail"
              }

          },
          onLogin: function () {
              //Jump to Login
              this.$router.push({path: 'login'})
          }
        }
    }
</script>

<style scoped>

</style>
