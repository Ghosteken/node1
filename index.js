
const express = require('express');

const app = express();

app.use(express.json());

const port = process.env.PORT || 3000;

let products = [
  { id: 1, name: 'Product 1', price: 19.99 },
  { id: 2, name: 'Product 2', price: 15.99 },
  { id: 3, name: 'Product 3', price: 24.99 }]
  // 

  // Endpoint to get all products
app.get('/products', (req, res) => {
    res.send(products);
})

  // Endpoint to get a product by id
  app.get('/products/:id', (req, res) => {
    const productId = parseInt(req.params.id);
    const product = products.find(p => p.id === productId)}).first();

    app.listen(3000)