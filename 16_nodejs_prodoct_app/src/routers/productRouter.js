// const express = require("express")
// const router = express.Router()

const router = require("express").Router();
const Product = require("../models/productModel");

router.get("/", (req, res) => {
  Product.find()
    .then((products) => {
      res.json(products);
    })
    .catch((error) => {
      res.json(error);
    });
});

router.get("/:id", (req, res) => {
  Product.findById(req.params.id)
    .then((product) => {
      res.json(product);
    })
    .catch((err) => {
      res.json(err);
    });
});

router.post("/", (req, res) => {
  const product = new Product({
    name: req.body.name,
    price: req.body.price,
    description: req.body.description,
  });
  product.save();
  res.json(product);
});

router.put("/:id", (req, res) => {
  Product.findByIdAndUpdate(req.params.id, req.body).then((product) => {
    res.json(req.body).catch((err) => {
      res.json(err);
    });
  });
});

router.delete("/:id", (req, res) => {
  Product.findByIdAndDelete(req.params.id)
    .then((product) => {
      res.send(`${req.params.id} ürünü silindi`);
    })
    .catch((error) => {
      res.json(error);
    });
});

module.exports = router;
