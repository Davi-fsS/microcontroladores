import axios from 'axios';

const _apiBaseUrl = 'http://127.0.0.1:5000/';

export const getAllDrinks = async () => {
    const _endpoint = 'get_all_drinks';

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        if (response.status === 200) {
            return response.data
        }
        else {
            return [];
        }

    }
    catch (error) {
        return error.response.data;
    }
};

export const getDetailById = async (id) => {
    const _endpoint = `get_detail_by_id?id=${id}`;

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        if (response.status === 200) {
            return response.data
        }
        else {
            return [];
        }

    }
    catch (error) {
        return error.response.data;
    }
};

export const verifyDoses = async (doseA, doseB) => {
    const _endpoint = `verify-doses?dose_A=${doseA}&dose_B=${doseB}`;

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        return response.data;

    }
    catch (error) {
        return error.response.data;
    }
};

