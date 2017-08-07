import axios from 'axios';



export default {

  authenticate(username, password, remember_me=false) {
    return axios.post("/api/authenticate/",
    // TODO: hash function
      {"username":username, "password":password}
    )
    .then(response => {
      return Promise.resolve(response);
    })
    .catch(err => {
      return Promise.reject(err);
    });
  }

}
