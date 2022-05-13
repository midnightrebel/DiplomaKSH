// Путь к приложению в котором храниться статика django 
const static_dir = '../mainapp/static'
// Путь, относительно static_dir
// В него webpack положит шаблон Vue приложения
const template_path = '../../templates/index.html'

module.exports = {
  devServer: {
      proxy: {
          "/": {
              target: "http://localhost:8000"
          }
      },
  }
}