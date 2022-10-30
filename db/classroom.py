from db.database import Graph


class ClassroomDB:
    def __init__(self):
        self.db = Graph(uri='bolt://34.206.54.226:7687',
                        user='neo4j', password='authorizations-soaps-restriction')

    def read_teacher_age_new_old(self):
        return self.db.execute_query('MATCH(n:Teacher) RETURN MAX(n.ano_nasc), MIN(n.ano_nasc);')

    def read_city_population(self):
        return self.db.execute_query('MATCH(n:City) RETURN AVG(n.population);')

    def read_city_cep(self):
        return self.db.execute_query('MATCH(n:City) WHERE n.cep = "37540-000" RETURN REPLACE(n.name, "a", "A");')

    def read_teacher_name(self):
        return self.db.execute_query('MATCH(n:Teacher) RETURN substring(n.name, 3, 1);')