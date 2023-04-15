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
  res.send('GET route on login.');
});
router.post('/', function (req, res) {

  username = req.body.username;
  password = req.body.password;
  const sql = 'SELECT * FROM users WHERE username = ?';
  db.query(sql, [username, password], (err, result) => {
    if (err) throw err;

    if (result.length === 0) {
      res.status(401).json({ error: 'Invalid username or password' });
    } else {

      if (result[0].password == password) {
        res.redirect('/dashboard');
      } else {
        res.status(401).json({ error: 'Invalid username or password' });
      }

    }
  });

});

//export this router to use in our index.js
module.exports = router;