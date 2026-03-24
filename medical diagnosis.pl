symptom(fever).
symptom(cough).

disease(flu).

has_disease(flu) :-
    symptom(fever),
    symptom(cough).