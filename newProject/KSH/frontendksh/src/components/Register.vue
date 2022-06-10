<template>
  <div class="wrapper">
    <div class="text-center mt-4 name">Регистрация</div>
    <form @submit.prevent="submitForm" class="p-3 mt-3">
      <div class="form-field d-flex align-items-center">
        <span class="far fa-user"></span>
        <input
          type="email"
          name="email"
          placeholder="name@example.com"
          v-model="username"
        />
      </div>
      <div class="form-field d-flex align-items-center">
        <span class="fas fa-key">Пароль</span>
        <input
          type="password"
          name="password"
          v-model="password"
          placeholder="Password"
        />
      </div>
      <div>
        <text class="danger" name="errors"
          >Пароль должен быть не менее 8 символов</text
        >
      </div>
      <button class="btn mt-3" type="submit">Вход</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Register",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      errors: "",
    };
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("access");
      const formData = {
        email: this.username,
        username: this.username,
        password: this.password,
      };
      axios
        .post("/api/v1/users/", formData)
        .then((response) => {
          console.log(response);
          this.$router.push("/");
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
