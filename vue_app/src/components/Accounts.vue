<template>
  <div class="Accounts">
    <ul id="account-list">
      <li v-for="item in accounts">
        {{ item.account_id }} | {{ item.balance }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Accounts',
  data () {
    return {
      accounts: [
        {
          account_id:"1",
          balance:"1000"
        },
        {
          account_id:"2",
          balance:"1000"
        },
        {
          account_id:"3",
          balance:"1000"
        }
      ]
    }
  },
  methods: {
    test() {
      alert("hi: "+this.username+"\nyour password is: "+this.password);
      this.password='';
      this.rejected=true;
    }
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
