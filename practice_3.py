from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    tutor_klass = ((x, y) for x, y in zip_longest(tutors, klasses, fillvalue='None'))
    for i in tutor_klass:
        print(i)
else:
    tutor_klass = ((x, y) for x, y in zip(tutors, klasses))
    for i in tutor_klass:
        print(i)

print(type(tutor_klass))