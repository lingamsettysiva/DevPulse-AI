import axios from "axios"; //

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const analyzeRepository = async (repoUrl) => {

  const response = await API.post("/analyze", {
    repo_url: repoUrl,
  });

  return response.data;
};