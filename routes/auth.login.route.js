const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

const db = mysql.createConnection({
    host : 'localhost',
    user: 'root',
    password: '',
    database: 'mydb'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL');
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
  
    // Retrieve user data from database
    const sql = 'SELECT * FROM users WHERE username = ?';
    db.query(sql, [username], (err, result) => {
      if (err) throw err;
  
      // Check if user exists
      if (result.length === 0) {
        res.status(401).json({ error: 'Invalid username or password' });
      } else {  
          // Check if password is correct
          if (flag) {
            res.status(200).json({ message: 'Login successful' });
            res.redirect('/dashboard');
          } else {
            res.status(401).json({ error: 'Invalid username or password' });
          }
        
      }
    });
  });
  