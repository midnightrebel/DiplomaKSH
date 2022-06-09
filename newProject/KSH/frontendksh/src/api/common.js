import axios from "axios";
export const HTTP = axios.create({
  baseURL: "http://localhost:8000/api/view/",
});
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
