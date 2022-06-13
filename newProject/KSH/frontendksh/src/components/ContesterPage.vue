<template>
  <div class="form-group">
    <h1 class="d-flex justify-content-center align-items-center">
      Вставьте ссылку на список учащихся ресурса VtCLOUD
    </h1>
    <input
      type="email"
      class="col-sm-2 col-form-label"
      placeholder="http://ulivt.ru:8080/ru/contestscoreboard-cid-139c?p=0"
    />
    <button class="btn btn-primary" type="submit">Получить данные</button>
  </div>
</template>

<style scoped>
button {
  margin: 0 auto;
  margin-top: 50px;
  display: block;
}
input {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  margin-top: auto;
}
h1 {
  padding-bottom: 20px;
  margin-top: 15em;
}
</style>
