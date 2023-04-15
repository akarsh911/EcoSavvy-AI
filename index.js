const express = require('express');
const app = express();
const PORT = 80;
const authRoute = require('./routes/auth.route');
app.use("/auth", authRoute);

app.post('/login', (req, res) => {
    let username = req.body.username;
    let password = req.body.password;
    res.send(`Username: ${username} Password: ${password}`);
  });

app.listen(PORT, () => {
    console.log("Server is running");
});
