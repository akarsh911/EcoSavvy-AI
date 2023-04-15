var express = require('express');
var app = express();
var router = express.Router();

router.get('/', function (req, res) {
    res.send('GET route on things.');
});
router.post('/', function (req, res) {
    res.send('POST route on things.');
});
var things = require('./routers/auth.route.js');

//both index.js and things.js should be in same directory
app.use('/things', things);

//export this router to use in our index.js
module.exports = router;

app.listen(3000);
