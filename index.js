const express = require('express');
const app = express();
const PORT = 8080;
const authRoute = require('./routes/auth.route');
app.use("/auth", authRoute);

app.listen(PORT, () => {
    console.log("Server is running");
});
