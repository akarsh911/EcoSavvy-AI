// Import required modules
const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

// Create express app
const app = express();

// Configure bodyParser to parse JSON data
app.use(bodyParser.json());

// Create MySQL connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'mydb'
});

// Connect to MySQL
db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL');
});

// Router for user registration
app.post('/register', (req, res) => {
  const { username, password } = req.body;
    // Insert user data into database
    const sql = 'INSERT INTO users (username, password) VALUES (?, ?)';
    const values = [username, hash];
    db.query(sql, values, (err, result) => {
      if (err) {
        // Check for duplicate username error
        if (err.code === 'ER_DUP_ENTRY') {
          res.status(409).json({ error: 'Username already exists' });
        } else {
          res.status(500).json({ error: 'Internal server error' });
        }
      } else {
        res.status(201).json({ message: 'User registered successfully' });
      }
    });
});