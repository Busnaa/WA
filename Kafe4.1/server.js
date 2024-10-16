// Import necessary modules
const express = require('express');      // Express framework
const bodyParser = require('body-parser'); // To parse JSON request bodies
const mysql = require('mysql');          // MySQL driver

// Create an Express application
const app = express();

// Use body-parser to handle JSON requests
app.use(bodyParser.json());

// MySQL database connection settings
const db = mysql.createConnection({
  host: 'localhost',          // Your database host
  user: 'user',      // Replace with your MySQL username
  password: 'password',  // Replace with your MySQL password
  database: 'coffe_lmsoft_cz' // Your MySQL database name
});

// Connect to MySQL database
db.connect((err) => {
  if (err) {
    console.error('Database connection error: ' + err.stack);
    return;
  }
  console.log('Connected to MySQL as id ' + db.threadId);
});

// Endpoint to get the list of types (like your `procedure.php?cmd=getTypesList`)
app.get('/getTypesList', (req, res) => {
  const query = 'SELECT * FROM types'; // Replace with your actual query that returns types
  db.query(query, (err, results) => {
    if (err) {
      res.status(500).json({ error: err });
      return;
    }
    res.json(results); // Send the result back to the client
  });
});

// Endpoint to get the list of people (like your `procedure.php?cmd=getPeopleList`)
app.get('/getPeopleList', (req, res) => {
  const query = 'SELECT * FROM people'; // Replace with your actual query that returns people
  db.query(query, (err, results) => {
    if (err) {
      res.status(500).json({ error: err });
      return;
    }
    res.json(results); // Send the result back to the client
  });
});

// Catch-all route for undefined routes
app.use((req, res) => {
  res.status(404).send('Not Found');
});

// Start the server on port 3000
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
