from db.database import Graph


class SchoolDB:
    def __init__(self):
        self.db = Graph(uri='bolt://34.206.54.226:7687',
                        user='neo4j', password='authorizations-soaps-restriction')

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def read_teacher_renzo(self):
        return self.db.execute_query('MATCH (n:Teacher {name:"Renzo"}) RETURN n.ano_nasc, n.cpf')

    def read_city_name(self):
        return self.db.execute_query('MATCH (n:City) RETURN n.name')

    def read_school(self):
        return self.db.execute_query('MATCH (n:School) WHERE n.number >= 150 AND n.number <= 550 RETURN n.name, n.address, n.number')