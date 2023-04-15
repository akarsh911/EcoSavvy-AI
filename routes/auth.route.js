var express = require('express');
var app = express();

var login = require('auth.login.route.js');
var register = require('auth.register.route.js');
app.use('/login', login);
app.use('/register', register);
const router = express.Router();
module.exports = router;