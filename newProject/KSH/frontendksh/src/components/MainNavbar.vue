<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand">Генерация групп КШ</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#"
              >Домашняя страница</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#/groups"
              >Список групп</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Генерация группы
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li>
                <a class="dropdown-item" href="#/generate/contester/"
                  >Contester</a
                >
              </li>
            </ul>
          </li>
        </ul>
        <!-- <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            /> -->
        <a
          class="btn btn-outline-success me-2"
          href="#/signin"
          role="button"
          position="relative"
        >
          Войти
        </a>
        <a class="btn btn-outline-success" type="submit" href="#/register">
          Зарегистрироваться
        </a>
        <!-- </form> -->
      </div>
    </div>
  </nav>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "MainNavbar",
  computed: mapState(["accessToken"]),
};
</script>

<style scoped>
a {
  color: #000;
}
</style>
