const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  fs.readFile(databasePath, 'utf8', (err, data) => {
    if (err) {
      res.send('This is the list of our students\nCannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    let output = 'This is the list of our students\n';
    output += `Number of students: ${students.length}\n`;

    const fields = {};
    for (const student of students) {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    for (const [field, firstnames] of Object.entries(fields)) {
      output += `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}\n`;
    }

    res.send(output.trim());
  });
});

app.listen(1245);

module.exports = app;
