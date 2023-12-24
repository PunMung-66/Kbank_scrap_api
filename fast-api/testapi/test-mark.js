const axios = require('axios');

const apiUrl = 'https://punnawat01-cpe101-fast-api.hf.space';
const name = '344327222951280643';

const discordId = '344327222951280643'; // Replace with the actual Discord ID

const pocket_ob = 'yed tood'; // Replace with the actual pocket name
const amount_ob = 100; // Replace with the actual amount

const addPocket = {
  Pocket: pocket_ob,
  Amount: amount_ob
};

const pocket_name = 'bana'; // Replace with the actual pocket name

const updatePocket = async (apiUrl, name, addPocket, pocket_name) => {
  try {
    const response = await axios.put(`${apiUrl}/update_pocket/${name}/${pocket_name}`, addPocket);
    console.log('Update Pocket Result:', response.data.result);
  } catch (error) {
    console.error('Update Pocket Error:', error);
  }
};

// Call the function
updatePocket(apiUrl, name, addPocket, pocket_name);