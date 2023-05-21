require('dotenv').config();
const functions = require('@google-cloud/functions-framework');
CLIENT_ID = process.env.CLIENT_ID
CLIENT_SECRET = process.env.CLIENT_SECRET
var request = require("request");

var options = {
   method: 'POST',
   url: 'https://oauth.fatsecret.com/connect/token',
   method : 'POST',
   auth : {
      user : CLIENT_ID,
      password : CLIENT_SECRET
   },
   headers: { 'content-type': 'application/x-www-form-urlencoded'},
   form: {
      'grant_type': 'client_credentials',
      'scope' : 'basic'
   },
   json: true
};
functions.http('refresh_token', (req, res) => {
    request(options, function (error, response, body) {
        if (error) throw new Error(error);

        res.send(body);
    })
});