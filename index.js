const express = require('express');
const app = express();
const PORT = 3000;
const authRoute = require('./routes/auth.route');
app.get('/login', function (req, res) {
    res.sendFile('/static/html/login.html', { root: __dirname })
});
app.use("/auth", authRoute);
const path = require('path')
app.use('/css', express.static(path.join(__dirname, 'static/css')))
app.use('/html', express.static(path.join(__dirname, 'static/html')))
app.use('/js', express.static(path.join(__dirname, 'static/js')))
app.use('/media', express.static(path.join(__dirname, 'static/media')))
app.listen(PORT, () => {
    console.log("Server is running");
});
