const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = process.argv[2];
    fs.readFile(databasePath, 'utf8', (err, data) => {
      if (err) {
        res.end('This is the list of our students\nCannot load the database');
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

      res.end(output.trim());
    });
  }
});

app.listen(1245);

module.exports = app;
