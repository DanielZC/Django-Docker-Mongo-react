import axios from "axios";

const clientApiAuth = axios.create({
  baseURL: "http://localhost:8000/auth/register",
  headers: {
    "Content-Type": "application/json",
  },
});

export default clientApiAuth;
