const axios = require('axios');
const apiUrl = 'https://punnawat01-cpe101-fast-api.hf.space';

// Testing the login endpoint
const loginData = {
    name: 'Kamil',
    bank_u: 'Genshin',
    bank_p: 'Primogem',
};
const login = async () => {
    try {
    const response = await axios.post(`${apiUrl}/login`, loginData);
    console.log('Login Result:', response.data.result);
  } catch (error) {
    console.error('Login Error:', error);
  }
}
//Testing add_pocket endpoint
const pocketData = {
        Pocket: 'Test1',
        Amount: 100,
};

const addPocket = async () => {
    try {
    const name = 'Pun_o_o'; // Replace with the desired username
    const response = await axios.post(`${apiUrl}/add_pocket/${name}`, pocketData);
    console.log('Add Pocket Result:', response.data.result);
  } catch (error) {
    console.error('Add Pocket Error:', error);
  }
};

const readPocket = async () => {
    try {
    const name = 'Pun_o_o'; // Replace with the desired username
    const response = await axios.get(`${apiUrl}/read_pocket/${name}`);
    console.log('Read Pocket Result:', response.data.result);
  } catch (error) {
    console.error('Read Pocket Error:', error);
  }
};