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
router.get('/inventory-capacity', function (req, res) {
    res.sendFile('static/html/inventoryCapacity.html', { root: process.cwd() })
});
router.get('/current-inventory', function (req, res) {
    res.sendFile('static/html/currentInventory.html', { root: process.cwd() })
});
router.get('/components-availaible', function (req, res) {
    res.sendFile('static/html/componentsAvailaible.html', { root: process.cwd() })
});
router.get('/shred-composition', function (req, res) {
    res.sendFile('static/html/shredComposition.html', { root: process.cwd() })
});
//export this router to use in our index.js
module.exports = router;