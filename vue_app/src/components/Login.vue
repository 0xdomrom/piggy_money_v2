<template>
  <div class="Login">
    <h1>{{ msg }}</h1>
    <form class="col">
      <div class="col-xs-12 large-text column-stack">
        <label>Unikey</label>
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
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Welcome to Piggy Money',
      username: '',
      password: '',
      remember_me: true,
      rejected: false,
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

#Login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  #remember-me {
      margin-right: 10px;;
  }

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
