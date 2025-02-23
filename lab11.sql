DROP TABLE IF EXISTS 'student';
DROP TABLE IF EXISTS 'student_marks';
DROP TABLE IF EXISTS 'group';
CREATE TABLE student (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  group_id INTEGER NOT NULL REFERENCES "group" (id));
INSERT INTO 'student' VALUES(1,'Богдан',2402);
INSERT INTO 'student' VALUES(2,'Олег',2402);
INSERT INTO 'student' VALUES(3,'Акакий',2401);
CREATE TABLE student_marks (
  student_id INTEGER PRIMARY KEY REFERENCES student (id),
  math_mark_average FLOAT,
  physics_mark_average FLOAT,
  python_mark_average FLOAT);
INSERT INTO 'student_marks' VALUES(1,5,4.8,5);
INSERT INTO 'student_marks' VALUES(2,3.5,3.67,4.33);
INSERT INTO 'student_marks' VALUES(3,4.67,4,4.5);
CREATE TABLE "group" (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255));
INSERT INTO 'group' VALUES(2401,'БВТ2401','Группа с баллами ЕГЭ 270+');
INSERT INTO 'group' VALUES(2402,'БВТ2402','Группа с баллами ЕГЭ 250+');
