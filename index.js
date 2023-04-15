const express = require('express');
var bodyParser = require('body-parser')
const app = express();
const PORT = 3000;
const authRoute = require('./routes/auth.route');
const dashboardRoute = require('./routes/dashboard.route');
const getRoute = require('./routes/get.route');
app.get('/', function (req, res) {
    res.sendFile('/static/html/home.html', { root: __dirname })
});
app.get('/login', function (req, res) {
    res.sendFile('/static/html/login.html', { root: __dirname })
});
app.get('/register', function (req, res) {
    res.sendFile('/static/html/register.html', { root: __dirname })
});
app.get('/testing', function (req, res) {
    res.sendFile('/static/html/statistics.html', { root: __dirname })
});
app.use("/auth", authRoute);
app.use("/dashboard", dashboardRoute);
app.use("/get", getRoute);
const path = require('path')
app.use('/css', express.static(path.join(__dirname, 'static/css')))
app.use('/html', express.static(path.join(__dirname, 'static/html')))
app.use('/js', express.static(path.join(__dirname, 'static/js')))
app.use('/media', express.static(path.join(__dirname, 'static/media')))

app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

app.listen(PORT, () => {
    console.log("Server is running");
});
