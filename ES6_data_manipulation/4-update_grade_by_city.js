export default function updateStudentGradeByCity(students, city, gradeList) {
    return students
        .filter(student => student.location === city)
        .map(student => {
            const gradeObject = gradeList.find(
                grade => grade.studentId === students.id
            );

            return {
                ...student,
                grade: gradeObject ? gradeObject.grade : 'N/A'
            };
        });
}