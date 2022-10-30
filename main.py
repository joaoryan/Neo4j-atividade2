from db.classroom import ClassroomDB
from db.school import SchoolDB
from db.teacher import TeacherCRUD
from helper.write_a_json import write_a_json


# Questão 01
schoolDao = SchoolDB()
# A
aux = schoolDao.read_teacher_renzo()
# wj(aux, '1A')
write_a_json(aux, '1A')

# B

# wj(aux, '1B')
write_a_json(aux, '1B')

# C
aux = schoolDao.read_city_name()
# wj(aux, '1C')
write_a_json(aux, '1C')

# D
aux = schoolDao.read_school()
# wj(aux, '1D')
write_a_json(aux, '1D')

# Questão 02
classroomDao = ClassroomDB()
# A
aux = classroomDao.read_teacher_age_new_old()
# wj(aux, '2A')
write_a_json(aux, '2A')

# B
aux = classroomDao.read_city_population()
# wj(aux, '2B')
write_a_json(aux, '2B')

# C
aux = classroomDao.read_city_cep()
# wj(aux, '2C')
write_a_json(aux, '2C')

# D
aux = classroomDao.read_teacher_name()
# wj(aux, '2D')
write_a_json(aux, '2D')

# Questão 03
# A
# CRUD feito no arquivo db/teacher
teacherDao = TeacherCRUD()
# B
aux = teacherDao.create("Chris Lima", 1956, "189.052.396-66")
write_a_json(aux, '3B')

# C
aux = teacherDao.read("Chris Lima")
write_a_json(aux, '3C')

# D
aux = teacherDao.update("Chris Lima", "162.052.777-77")
write_a_json(aux, '3D')

schoolDao.db.close()
classroomDao.db.close()
teacherDao.db.close()
