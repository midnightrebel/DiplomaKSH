import { HTTP } from "./common";
export const Note = {
  create(config) {
    return HTTP.post("/view/", config).then((response) => {
      return response.data;
    });
  },
  delete(student) {
    return HTTP.delete(`/view/${student.id}/`);
  },
  list() {
    return HTTP.get("/view/").then((response) => {
      return response.data;
    });
  },
  retrieve(student) {
    return HTTP.get(`/user/${student.id}/`).then((response) => {
      return response.data;
    });
  },
};
