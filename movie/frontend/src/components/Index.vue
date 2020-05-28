<template>
    <div class="container">

        <div class="jumbotron text-center">
            <h1><span class="fa fa-lock"></span> {{ msg }}</h1>

            <p>Login or Register with:</p>

            <button class="btn btn-default" @click="onLogin"><span class="fa fa-user"></span> Local Login</button>
            <button class="btn btn-default" @click="onRegister"><span class="fa fa-user"></span> Local Signup</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Index",
        data(){
            return {
                msg: "Vue Loginx Demo"
            }
        },
        methods: {
            onLogin: function () {
                this.$router.push({name: 'login'})
            },
            onRegister: function () {
                this.$router.push({name: 'register'})
            },

        }

    }
</script>

<style scoped>

</style>
