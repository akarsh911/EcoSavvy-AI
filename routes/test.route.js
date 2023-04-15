var express = require('express');
var router = express.Router();

router.get('/', function (req, res) {
    res.send('GET route on things.');
});
router.post('/', function (req, res) {
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

//export this router to use in our index.js
module.exports = router;