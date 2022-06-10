<template>
  <div>
    <head>
      <meta charset="utf-8" />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no"
      />
      <meta name="description" content="" />
      <meta name="author" content="" />
      <title>Домашняя страница</title>
    </head>
    <!-- Page header with logo and tagline-->
    <header class="py-5 bg-light border-bottom mb-4">
      <div class="container">
        <div class="text-center my-5">
          <h1 class="fw-bolder">Добро пожаловать!</h1>
          <span :src="user_data">{{ user_data }}</span>
        </div>
      </div>
    </header>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "AutorizedHomePage",
  beforeCreate() {
    this.$store.commit("initializeStore");
    const access = this.$store.state.access;
    if (access) {
      axios.defaults.headers.common["Authorization"] = "JWT " + access;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  data() {
    return {
      user_data: "",
    };
  },
  mounted() {
    this.getuser();
  },
  methods: {
    getuser() {
      axios
        .get(`/api/v1/users/me/`)
        .then((response) => {
          console.log(response);
          this.user_data = response.data.username;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
