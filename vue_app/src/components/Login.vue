<template>
  <div class="Login">
    <h1>{{ msg }}</h1>
    <form class="col" v-on:submit.prevent="test">
      <transition name="fade">
        <div v-if="rejected" class="col-xs-12 ">
          <div class="col-xs-12" id="login-error">
            Incorrect name or password.
          </div>
        </div>
      </transition>

      <div class="col-xs-12 large-text column-stack">
        <label>Username</label>
        <input type="text" v-model="username">
      </div>

      <div class="col-xs-12 large-text column-stack">
        <label>Password</label>
        <input type="password" v-model="password">
      </div>


      <div class="col-xs-12">
        <input type="checkbox" v-model="remember_me" id="remember-me">
        <label for="remember-me">Remember me</label>
      </div>


      <div class="col-xs-12">
        <button class="btn btn-success btn-block" :disabled="username.length == 0 || password.length == 0">
            SUBMIT
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import Auth from "../auth"

axios.get("/api/test")
.then(response => {
  console.log(response.data);
})
.catch(e => {
  console.log(e);
});

export default {

  name: 'Login',
  data () {
    return {
      msg: 'Welcome to Piggy Money2',
      username: '',
      password: '',
      remember_me: true,
      rejected: false,
    }
  },
  methods: {
    test() {
      Auth.authenticate(this.username, this.password, this.remember_me)
      .then(response => {
        console.log(response);
        if (response.data.valid) {
          this.$router.push("/accounts");
        } else {
          this.rejected = true;
        }
      })
      .catch(err => {
        console.log(err);
      });

    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

#login-error {
  overflow: hidden;
  padding: 10px;
  background-color: red;
  max-height: 3rem;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 2s;

}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}


.Login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  max-width: 500px;
  margin: 0 auto;

  input {
    padding: 5px;
  }

  .large-text {
      font-size: 2rem;
  }

  .column-stack {
      display: flex;
      flex-direction: column;
      margin-bottom: 15px;
  }

  button {
      margin-top: 1.5rem;
      font-size: 1.2rem;
  }

}
</style>
