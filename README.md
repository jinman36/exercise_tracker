# exercise_tracker

## Recreate students.db

CREATE TABLE classes (course_id INTEGER, class_name TEXT, Description MEDIUMTEXT);

CREATE TABLE students (
	student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
	user_name TEXT NOT NULL, 
	student_firstname TEXT NOT NULL, 
	student_lastname TEXT NOT NULL, 
	hash TEXT NOT NULL, 
	punch_card INT NOT NULL DEFAULT 0);

CREATE TABLE attendance (
	course_id INTEGER, 
	student_id INTEGER, 
	day INT, month INT, 
	year INT, 
	punch_card INT NOT NULL DEFAULT 0);

1|admin|admin|admin|pbkdf2:sha256:600000$QEhoVkT0NhC4z0lM$bb431fe32243b77639e191a2c92d79b819837404e77c35fcecd2cd7dae38d507|2
2|timmy|timmy|phillips|pbkdf2:sha256:600000$gjd76r2lIDlvsX8y$dfdaf9d99e2a78a98b4771bec8ede64223b0bb38852101927b44d458ce0225da|5
3|santa|santa|claus|pbkdf2:sha256:600000$OgH4rscvwHHyOO29$095f7171d7f36a7884b02025e73a9b70ca20a511cddd055fb157ebdef4cc93d8|12
4|pirate|Jolly|Rodger|pbkdf2:sha256:600000$ma8mabWloXgQ3y5I$edcc6ced43785d9be4c1ee0e3a1867bcf9f4180ef32952fdd2ebfa298c1ecb34|0


INSERT INTO classes (course_id, class_name, Description) Values(1, "CAVE BASICS", "Ideal for those just starting out or new to our gym, Cave Basics is an instructional class which builds a foundation for the skills, drills and techniques used in training sessions offered at our gym. Exercise modifications and progressions ensure a safe, challenging workout for your personal fitness goals.");

INSERT INTO classes (course_id, class_name, Description) Values(2, "CAVE TRAINING", "A combination of strength, endurance, power, agility and speed, this class is like no other. Physically and mentally challenging, the format is never the same. Designed to take you to the next level with measurable results.");

INSERT INTO classes (course_id, class_name, Description) Values(3, "GROUP THERAPY", "Invigorate mind and body in this 60 minute session. Martial arts striking meets bootcamp during the first portion of the class, moving to the yoga/stretch segment and rounding out the hour with a relaxing meditation. (MMA training gloves recommended for this class)");

INSERT INTO classes (course_id, class_name, Description) Values(4, "KETTLEBELL TRAINING", "Burning 20 percent more calories in less time than traditional weights makes for the benefit and the bonus of this most effective training tool. The abdominal and stabilizing muscles spring into action as we complete functional movements useful for everyday activities. Kettlebell training requires the body to work as one unit, improving balance, coordination, strength and endurance.");

INSERT INTO classes (course_id, class_name, Description) Values(5, "MAC (Martial Arts Conditioning)", "Offered as a group fitness class and a supplement to our martial arts programs, we welcome all ages 7 & up. This 35-minute class incorporates bag work, obstacle courses, relays and team drills to develop kinesthetic awareness, coordination and gross motor skills. (MMA gloves recommended for this class)");

INSERT INTO classes (course_id, class_name, Description) Values(6, "MEDITATION", "No experience necessary-just come and chill with us!");

INSERT INTO classes (course_id, class_name, Description) Values(7, "YOGA/MOBILITY", "Improve your flexibility, stability and movement patterns at any stage, any age! This class combines yoga postures & movements, joint mobility and classic stretching techniques.");

INSERT INTO classes (course_id, class_name, Description) Values(8, "LUNCH CRUNCH", "This workout session is available anytime during our Open Gym hours. There is no “set” time this class begins-you’ll be guided through your workout, at your pace, and be out the door in 30 minutes!");

INSERT INTO classes (course_id, class_name, Description) Values(9, "3/2/1", "A unique interval training session designed to deliver a full-body workout. You’ll be challenged through timed segments of cardio, strength and core development — all in under an hour!");