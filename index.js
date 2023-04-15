const express = require('express');
const app = express();
const PORT = 81;
const authRoute = require('./routes/auth.route');
app.use("/auth", authRoute);

app.listen(PORT, () => {
    console.log("Server is running");
});
