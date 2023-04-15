const express = require('express');
const app = express();
const router = express.Router();
router.get("/", (req, res) => {
    res.send("Auth route is displaying data")
})
const loginRoute = require('./test.route');
router.use("/login", loginRoute);

module.exports = router;


