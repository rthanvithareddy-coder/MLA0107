disease(diabetes).
disease(obesity).

diet(diabetes, 'Avoid sugar').
diet(obesity, 'Eat low fat food').

suggest(Disease, Advice) :-
    diet(Disease, Advice).