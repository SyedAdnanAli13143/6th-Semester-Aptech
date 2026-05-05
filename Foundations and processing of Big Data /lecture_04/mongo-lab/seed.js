// Loads the demo data for Lab 4.
// Run with: docker exec -i mongo-lab mongosh < seed.js

db = db.getSiblingDB('school');

db.students.drop();
db.profiles.drop();

db.students.insertMany([
  {student_id:'S001', name:'Ali',    course:'Math',    score:82, passed:1},
  {student_id:'S002', name:'Sara',   course:'Math',    score:45, passed:0},
  {student_id:'S003', name:'Omar',   course:'Math',    score:71, passed:1},
  {student_id:'S004', name:'Fatima', course:'Math',    score:90, passed:1},
  {student_id:'S005', name:'Hassan', course:'Math',    score:38, passed:0},
  {student_id:'S001', name:'Ali',    course:'Science', score:76, passed:1},
  {student_id:'S002', name:'Sara',   course:'Science', score:55, passed:1},
  {student_id:'S003', name:'Omar',   course:'Science', score:48, passed:0},
  {student_id:'S004', name:'Fatima', course:'Science', score:88, passed:1},
  {student_id:'S005', name:'Hassan', course:'Science', score:61, passed:1},
  {student_id:'S001', name:'Ali',    course:'English', score:68, passed:1},
  {student_id:'S002', name:'Sara',   course:'English', score:73, passed:1},
  {student_id:'S003', name:'Omar',   course:'English', score:52, passed:1},
  {student_id:'S004', name:'Fatima', course:'English', score:84, passed:1},
  {student_id:'S005', name:'Hassan', course:'English', score:29, passed:0}
]);

db.profiles.insertOne({
  student_id: 'S001',
  name: 'Ali',
  contact: { email: 'ali@school.edu', phone: '0300-1234567' },
  hobbies: ['cricket', 'reading', 'coding'],
  parents: [
    { relation: 'father', name: 'Ahmed', phone: '0300-9999999' },
    { relation: 'mother', name: 'Sara',  phone: '0300-8888888' }
  ]
});

print('students inserted: ' + db.students.countDocuments());
print('profiles inserted: ' + db.profiles.countDocuments());
