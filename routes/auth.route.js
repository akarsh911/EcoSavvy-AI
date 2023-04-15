const express = require('express')
const router = express.Router()
router.get("/", (req, res) => {
    res.send("Contact route is displaying data")
})
module.exports = router; 
const loginRoute = require('./auth.login.route');
app.use("/login", loginRoute);
const registerRoute = require('./auth.register.route');
app.use("/register", registerRoute);

