var express = require('express');
var fs = require('fs');

var app = express();
var PORT = 3000;

function readJsonFileSync(filepath, encoding){

  if (typeof (encoding) == 'undefined'){
    encoding = 'utf8';
  }
  var file = fs.readFileSync(filepath, encoding);
  return JSON.parse(file);

}

function getJsonFiles(path){

  data = [];
  files = fs.readdirSync(path);

  for (var i in files) {
    // TODO: Filepaths are not OS safe
    data.push(readJsonFileSync(path + '/' + files[i]));
  };

  return data;
}

app.get('/api/twytta/', function (req, res) {

  data = getJsonFiles('texts/tweets');
  res.send(data);

});

app.get('/api/instapic/', function (req, res) {

  data = getJsonFiles('texts/instagram');
  res.send(data);

});

app.get('/api/friendface/', function (req, res) {

  data = getJsonFiles('texts/facebook');
  res.send(data);

});

app.get('/api/mail/', function (req, res) {

  data = getJsonFiles('texts/facebook');
  res.send(data);

});

app.get('/api/sms/', function (req, res) {

  data = getJsonFiles('texts/facebook');
  res.send(data);

});

app.get('/api/notes/', function (req, res) {

  data = getJsonFiles('texts/facebook');
  res.send(data);

});

app.listen(PORT);
