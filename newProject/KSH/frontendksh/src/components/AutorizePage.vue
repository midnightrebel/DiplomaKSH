<template>
  <div class="wrapper">
    <div class="text-center mt-4 name">Вход в учётную запись</div>
    <form @submit.prevent="submitForm" class="p-3 mt-3">
      <div class="form-field d-flex align-items-center">
        <span class="far fa-user"></span>
        <input
          type="email"
          name="email"
          placeholder="name@example.com"
          v-model="email"
        />
      </div>
      <div class="form-field d-flex align-items-center">
        <span class="fas fa-key"></span>
        <input
          type="password"
          name="password"
          v-model="password"
          placeholder="Password"
        />
      </div>
      <button class="btn mt-3" type="submit">Вход</button>
    </form>
    <div class="text-center fs-6">
      <a href="#">Забыли пароль?</a> <br />
      <a @onClick="Login" href="#">Войти</a>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AutorizePage",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("access");
      const formData = {
        email: this.email,
        password: this.password,
      };
      axios
        .post("/api/v1/jwt/create/", formData)
        .then((response) => {
          const access = response.data.access;
          const refresh = response.data.refresh;
          this.$store.commit("setAccess", access);
          this.$store.commit("setRefresh", refresh);
          axios.defaults.headers.common["Authorization"] = "JWT " + access;
          localStorage.setItem("access", access);
          localStorage.setItem("refresh", refresh);
          this.$router.push("/home");
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
/* Reseting */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #ecf0f3;
}

.wrapper {
  max-width: 350px;
  min-height: 500px;
  margin: 80px auto;
  padding: 40px 30px 30px 30px;
  background-color: #ecf0f3;
  border-radius: 15px;
  box-shadow: 13px 13px 20px #cbced1, -13px -13px 20px #fff;
}

.wrapper .name {
  font-weight: 600;
  font-size: 1.6rem;
  letter-spacing: 0.3px;
  padding-left: 10px;
  color: #555;
}

.wrapper .form-field input {
  width: 100%;
  display: block;
  border: none;
  outline: none;
  background: none;
  font-size: 1.2rem;
  color: #666;
  padding: 10px 15px 10px 10px;
  /* border: 1px solid red; */
}

.wrapper .form-field {
  padding-left: 10px;
  margin-bottom: 20px;
  border-radius: 20px;
  box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;
}

.wrapper .form-field .fas {
  color: #555;
}

.wrapper .btn {
  box-shadow: none;
  width: 100%;
  height: 40px;
  background-color: #03a9f4;
  color: #fff;
  border-radius: 25px;
  font-size: 1.3rem;
  box-shadow: 3px 3px 3px #b1b1b1, -3px -3px 3px #fff;
  letter-spacing: 1.3px;
}

.wrapper .btn:hover {
  background-color: #039be5;
}

.wrapper a {
  text-decoration: none;
  font-size: 1.8rem;
  color: #03a9f4;
}

.wrapper a:hover {
  color: #039be5;
}

@media (max-width: 380px) {
  .wrapper {
    margin: 30px 20px;
    padding: 40px 15px 15px 15px;
  }
}
</style>
