const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const router = express.Router();
const app = express();
app.use(bodyParser.json());

const db = mysql.createConnection({
    host : 'localhost',
    user: 'root',
    password: '',
    database: 'ecosavvyai'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL');
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
  
    const sql = 'SELECT * FROM users WHERE username = ?';
    db.query(sql, [username, password], (err, result) => {
      if (err) throw err;
  
      if (result.length === 0) {
        res.status(401).json({ error: 'Invalid username or password' });
      } else {  
          if (flag) {
            res.status(200).json({ message: 'Login successful' });
            res.redirect('/dashboard');
          } else {
            res.status(401).json({ error: 'Invalid username or password' });
          }
        
      }
    });
  });
  