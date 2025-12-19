import api from "./base.api";

const createCrud = (endpoint) => ({
    list: async () => {
        const resp = await api.get(endpoint);
        return resp.data;
    },

    get: async (id) => {
        const resp = await api.get(`${endpoint}${id}/`);
        return resp.data;
    },
    
    create: async (data) => {
        const resp = await api.post(endpoint, data);
        return resp.data;
    },
    
    update: async (id, data) => {
        const resp = await api.put(`${endpoint}${id}/`, data);
        return resp.data;
    },
    
    delete: async (id) => {
        const resp = await api.delete(`${endpoint}${id}/`);
        return resp.data;
    }
});

export default createCrud;