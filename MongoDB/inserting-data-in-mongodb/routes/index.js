var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
     title: 'inserting-data-in-mongodb',
     head:'Insert the following data in MongoDB using Mongoose!'
  });
});

module.exports = router;
