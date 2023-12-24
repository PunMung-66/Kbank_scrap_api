// Your JSON response
var jsonResponse = '{"result": "{\'balance\': 43.16, \'status\': \\"Update \'Pun\' status completed\\"}", "time": 37.81937313079834}';

// Parse the outer JSON string
var parsedResponse = JSON.parse(jsonResponse);

// Parse the inner JSON string
var result = JSON.parse(parsedResponse.result);

// Accessing values from the inner JSON
var balance = result.balance;
var status = result.status;

// Displaying values in the console
console.log('Balance:', balance);
console.log('Status:', status);