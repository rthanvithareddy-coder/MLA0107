bird(sparrow).
bird(eagle).
bird(ostrich).

cannot_fly(ostrich).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).