const path = require("path");
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  // Paths
  // Рабочая директория сборки
  // Я обычно указываю директорию приложения django, которое отвеает за фронт
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../static"),
  indexPath: path.resolve(__dirname, "../templates/", "mainapp", "index.html"),
  transpileDependencies: true,
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:8000",
      },
    },
  },
});
