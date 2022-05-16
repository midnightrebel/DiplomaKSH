// Путь к приложению в котором храниться статика django
const static_dir = "../mainapp/static";
// Путь, относительно static_dir
// В него webpack положит шаблон Vue приложения
const template_path = ".../templates/index.html";

const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:8000",
      },
    },
  },
});