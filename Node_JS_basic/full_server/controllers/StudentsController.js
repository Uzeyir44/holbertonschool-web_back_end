import { readDatabase } from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((fields) => {
        let output = 'This is the list of our students\n';
        const sortedFields = Object.keys(fields).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
        for (const field of sortedFields) {
          output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
        response.status(200).send(output.trim());
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((fields) => {
        const firstnames = fields[major] || [];
        response.status(200).send(`List: ${firstnames.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
