<template>
  <div class="Accounts">
    <div v-if="loading">
      <p>
        Loading...
      </p>
    </div>
    <div v-if="error">
      <p>
        Error...
      </p>
    </div>
    <div v-if="loaded">
      <p>
        Hi {{ username }} your accounts are as follows:
      </p>
      <ul id="account-list">
        <li v-for="item in accounts">
          {{ item[0] }} | {{ item[1] }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import Vue from 'vue'
import VueLocalStorage from 'vue-localstorage'

Vue.use(VueLocalStorage)

export default {
  name: 'Accounts',
  data () {
    return {
      accounts: null,
      error: false,
      loading: true,
      loaded: true,
      username: this.$localStorage.get("username")
    }
  },
  localStorage: {
    user : {
      username : {
        type : String
      },
      password : {
        type : String
      }
    }
  },
  methods: {
    fetchData() {
      console.log("fetching accounts for: ");
      console.log(this.$localStorage.get("username"));
      axios.post("/api/get_user_accounts/",
        {"username":this.$localStorage.get('username'), "password":this.$localStorage.get('password')}
      )
      .then(response => {
        console.log(response);
        this.accounts = response.data.accounts;
        this.err = false;
        this.loading = false;
      })
      .catch(err => {
        this.loading = false;
        this.accounts = null
        this.err = true;
      });
    }
  },
  watch: {
    '$route':'fetchData'
  },
  created() {
    this.fetchData()
  }
}
</script>

<style>

.Accounts {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  max-width: 500px;
  margin: 0 auto;

  ul {
    list-style: none;
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
