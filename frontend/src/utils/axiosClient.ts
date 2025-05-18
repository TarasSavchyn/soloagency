import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { handleErrorFromServer } from '../helpers/handleErrorFromServer';

// export const hostName = 'https://soloagency.org/rest';
export const hostName = 'http://127.0.0.1:8000';

const instance = axios.create({ baseURL: `${hostName}/api` });

export const client = {
  get: async <T>(url: string, config?: AxiosRequestConfig): Promise<T> => {
    try {
      const response: AxiosResponse<T> = await instance.get<T>(url, config);

      return response.data;
    } catch (error) {
      return handleErrorFromServer(error);
    }
  },

  post: async <T, D>(url: string, data: D): Promise<T> => {
    try {
      const response: AxiosResponse<T> = await instance.post<T>(url, data);

      return response.data;
    } catch (error) {
      return handleErrorFromServer(error);
    }
  },

  patch: async <T, D>(url: string, data: D): Promise<T> => {
    try {
      const response: AxiosResponse<T> = await instance.patch<T>(url, data);

      return response.data;
    } catch (error) {
      return handleErrorFromServer(error);
    }
  },

  delete: async <T>(url: string): Promise<T> => {
    try {
      const response: AxiosResponse<T> = await instance.delete<T>(url);

      return response.data;
    } catch (error) {
      return handleErrorFromServer(error);
    }
  },
};

instance.interceptors.request.use(config => {
  let token: string | null = null;

  if (localStorage.getItem('persist:root') !== null) {
    token = JSON.parse(
      JSON.parse(localStorage.getItem('persist:root') || '').auth,
    ).token;
  }

  if (token) {
    config.headers.Authorization = `token ${token}`;
  }

  return config;
});
