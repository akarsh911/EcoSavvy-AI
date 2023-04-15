const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();


app.use(bodyParser.json());


const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'mydb'
});

db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL');
});

app.post('/register', (req, res) => {
  const { username, password } = req.body;
    const sql = 'INSERT INTO users (username, password) VALUES (?, ?)';
    const values = [username, hash];
    db.query(sql, values, (err, result) => {
      if (err) {
        if (err.code === 'ER_DUP_ENTRY') {
          res.status(409).json({ error: 'Username already exists' });
        } else {
          res.status(500).json({ error: 'Internal server error' });
        }
      } else {
        res.status(201).json({ message: 'User registered successfully' });
        res.redirect('/login');
      }
    });
});