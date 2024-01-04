const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const productRouter = require("./src/routers/productRouter");

const app = express();

app.use(bodyParser.json());
app.use(productRouter);

const user = "admin";
const password = "WDnKTB0wfMO4FzsQ";
const databasename = "products";

mongoose
  .connect(
    `mongodb+srv://${user}:${password}@cluster0.dfibsha.mongodb.net/${databasename}?retryWrites=true&w=majority`
  )
  .then(() => {
    console.log("Connected to database");
  })
  .catch((error) => {
    console.log(error);
  });

app.listen(5000, () => {
  console.log("Server 5000 port ile çalışıyor");
});
