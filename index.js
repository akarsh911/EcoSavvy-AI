const express = require('express');
const app = express();
const PORT = 80;
const authRoute = require('./routes/auth.route');
app.use("/auth", authRoute);

app.get('/login',)

app.listen(PORT, () => {
    console.log("Server is running");
});
