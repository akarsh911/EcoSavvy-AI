const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const router = express.Router();
const app = express();
app.use(bodyParser.json());


router.get('/', function (req, res) {
    res.sendFile('static/html/statistics.html', { root: process.cwd() })
});
router.get('/logistics', function (req, res) {
    res.sendFile('static/html/logistics.html', { root: process.cwd() })
});
router.get('/waste-status', function (req, res) {
    res.sendFile('static/html/wasteStatus.html', { root: process.cwd() })
});
//export this router to use in our index.js
module.exports = router;