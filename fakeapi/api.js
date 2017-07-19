var express = require('express');
var fs = require('fs');

var app = express();
var PORT = 3000;

function readJsonFileSync(filepath, encoding) {

  if (typeof (encoding) == 'undefined'){
    encoding = 'utf8';
  }

  try {
    var file = fs.readFileSync(filepath, encoding);
    return JSON.parse(file);
  } catch (err) {
    console.log(err);
    return {};
  }

}

function getJsonFiles(path) {

  data = [];

  try {
    files = fs.readdirSync(path);
  } catch (err) {
    return data;
  }

  for (var i in files) {
    // TODO: Filepaths are not OS safe
    data.push(readJsonFileSync(path + '/' + files[i]));
  };

  return data;
}

app.get('/api/twytta/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/tweets/' + username);
  res.send(data);

});

app.get('/api/instapic/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/instagram/' + username);
  res.send(data);

});

app.get('/api/friendface/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/facebook/' + username);
  res.send(data);

});

app.get('/api/mail/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/mail/' + username);
  res.send(data);

});

app.get('/api/sms/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/sms/' + username);
  res.send(data);

});

app.get('/api/notes/:username', function (req, res) {

  username = req.params.username;
  data = getJsonFiles('texts/notes/' + username);
  res.send(data);

});

app.listen(PORT);
