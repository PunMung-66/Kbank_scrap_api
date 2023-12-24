const axios = require('axios');

const apiUrl = 'https://punnawat01-cpe101-fast-api.hf.space'; // Replace with your API URL
const name = 'Pun_o_o'; // Replace with the desired username

const readPocket = async () => {
  try {
    const response = await axios.get(`${apiUrl}/read_pocket/${name}`);
    console.log('Read Pocket Result:', response.data.result);
  } catch (error) {
    console.error('Read Pocket Error:', error);
  }
};

// Call the asynchronous function
readPocket();
