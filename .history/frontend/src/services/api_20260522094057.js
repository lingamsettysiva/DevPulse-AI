import axios from "axios"; //frontend calls backend api

const API = axios.create({ //  retaing the backend connection
  baseURL: "http://127.0.0.1:8000",
});

export const analyzeRepository = async (repoUrl) => {

  const response = await API.post("/analyze", {
    repo_url: repoUrl,
  });

  return response.data;
};