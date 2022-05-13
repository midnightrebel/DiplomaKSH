import { HTTP } from "./common";
export const Note = {
  create(config) {
    return HTTP.post("/view/", config).then((response) => {
      return response.data;
    });
  },
  delete(view) {
    return HTTP.delete(`/view/${view.id}/`);
  },
  list() {
    return HTTP.get("/view/").then((response) => {
      return response.data;
    });
  },
};
