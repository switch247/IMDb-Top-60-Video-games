const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());

app.all('/api/*', (req, res) => {
  const djangoAPIUrl = 'http://imdbezra.com';
  const targetUrl = `${djangoAPIUrl}${req.url}`;

  req.pipe(request(targetUrl)).pipe(res);
});

exports.api = functions.https.onRequest(app);

