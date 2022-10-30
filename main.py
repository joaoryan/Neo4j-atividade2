from pprintpp import pprint as pp
from db.school import SchoolDB
from helper.write_a_json import write_a_json


def divider():
    print('\n' + '-' * 80 + '\n')


dao = SchoolDB()

# Questão 01
# A
aux = dao.read_teacher_renzo()
# wj(aux, '1A')
write_a_json(aux, '1A')

# B

#wj(aux, '1B')
write_a_json(aux, '1B')

# C
aux=dao.read_city_name()
#wj(aux, '1C')
write_a_json(aux, '1C')

# D
aux=dao.read_school()
#wj(aux, '1D')
write_a_json(aux, '1D')

# Questão 02
# A

#wj(aux, '2A')

# B

#wj(aux, '2B')

# C

#wj(aux, '2C')

# D

#wj(aux, '2D')

# Questão 03
# A

# B

# C

# D

dao.db.close()
