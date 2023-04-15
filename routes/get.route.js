const express = require('express');
const app = express();
const router = express.Router();
const mysql = require('mysql');
router.get("/", (req, res) => {
    res.send("Get route is displaying data")
})
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'ecosavvyai'
});

// Connect to MySQL database
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL database: ' + err.stack);
        return;
    }
    console.log('Connected to MySQL database as id ' + connection.threadId);
});

// Define route to read the "logistics" table and send as a JSON response
router.get('/logistics', (req, res) => {
    const query = 'SELECT * FROM logistics';
    connection.query(query, (error, results, fields) => {
        if (error) throw error;
        res.json(results);
    });
});
router.get('/inventory', (req, res) => {
    const query = 'SELECT * FROM inventory';
    connection.query(query, (error, results, fields) => {
        if (error) throw error;
        res.json(results);
    });
});

module.exports = router;
