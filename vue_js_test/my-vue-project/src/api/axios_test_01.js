import "../mock/index";
import axios from "axios";

export default axios.get("/api").then((data) => {
  return new Promise((resolve, reject) => {
    resolve(data);
    reject("error");
  });
});
