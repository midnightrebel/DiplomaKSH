<template lang="pug">
MainNavbar
<router-view></router-view>
</template>

<script>
import MainNavbar from "./components/MainNavbar.vue";
export default {
  name: "app",
  components: {
    MainNavbar: MainNavbar,
  },
};
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Eczar);
@import url(https://fonts.googleapis.com/css?family=Work+Sans);

body {
  font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Eczar", sans-serif;
}
</style>
