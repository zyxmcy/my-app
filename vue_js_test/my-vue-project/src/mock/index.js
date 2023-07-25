import Mock from "mockjs";
import permission from "./permission";

Mock.mock(/api/, "get", permission.getMenu);
