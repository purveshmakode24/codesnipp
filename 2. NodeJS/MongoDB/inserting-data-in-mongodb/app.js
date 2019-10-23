var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mongoose = require('mongoose');
var indexRouter = require('./routes/index');


var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

//MongoDB connection
mongoose.connect('mongodb://localhost:27017/inserting-data-in-mongodb');
var Schema = new mongoose.Schema({
    _id: String,
    name: String,
    age: Number
});
var user = mongoose.model('users', Schema);
app.post('/insert', function (req,res) {
    new user({
        _id: req.body.email,
        name:req.body.name,
        age:req.body.age
    }).save(function (err,doc) {
        if(err) res.send(err);
        else res.send("Successfully inserted!")
    })
});
//mongodb connection end//

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
