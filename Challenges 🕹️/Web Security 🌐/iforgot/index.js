const express = require('express');
const app = express();
const port = 3000;

// Possiamo esporre tutta la directory corrente, tanto ho già eliminato
// la flag dal repository e nessuno sarà in grado di recuperarla 😈
app.use(express.static('.'));

app.get('/', function (req, res) {
  res.end('nothing here UwU');
});

app.listen(port, () => {
  console.log(`Listening at port ${port}`);
});
