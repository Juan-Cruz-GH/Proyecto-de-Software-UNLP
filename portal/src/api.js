import axios from "axios";

const apiService = axios.create({
  baseURL: "https://admin-grupo23.proyecto2022.linti.unlp.edu.ar",
  withCredentials: true,
  xsrfCookieName: "csrf_access_token",
});

export { apiService };
