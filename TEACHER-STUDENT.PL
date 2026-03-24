teaches(sharma, math101).
teaches(rao, cs102).

studies(ram, math101).
studies(sita, cs102).

student_teacher(Student, Teacher) :-
    studies(Student, Sub),
    teaches(Teacher, Sub).