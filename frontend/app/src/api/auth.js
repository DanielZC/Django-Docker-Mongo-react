import clientApiAuth from "./apiClient";

export const getUsers = async () => {
  const response = await clientApiAuth.get(`/get/user/`);
  return response.data;
};

export const createUser = async (data) => {
  const response = await clientApiAuth.post(`/user/`, data);
  return response.data;
};
