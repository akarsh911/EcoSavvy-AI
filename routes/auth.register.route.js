const express = require('express');
const mysql = require('mysql');
const router = express.Router();
const bodyParser = require('body-parser');
const app = express();
router.use(bodyParser.urlencoded({ extended: true }));

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ecosavvyai'
});

db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL');
});
router.get('/', function (req, res) {
  res.send('GET route on register.');
});
router.post('/', function (req, res) {
  const { username, password } = req.body;
  const sql = 'INSERT INTO users (f_name,l_name,username, password) VALUES (?, ?)';
  const values = [f_name,l_name,username, password];
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

//export this router to use in our index.js
module.exports = router;