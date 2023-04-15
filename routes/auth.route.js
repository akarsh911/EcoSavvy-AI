const express = require('express');
const app = express();
const router = express.Router();
router.get("/", (req, res) => {
    res.send("Auth route is displaying data")
})
const loginRoute = require('./auth.login.route');
router.use("/login", loginRoute);
const registerRoute = require('./auth.register.route');
router.use("/register", registerRoute);

module.exports = router;


