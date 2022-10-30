from db.database import Graph


class TeacherCRUD:
    def __init__(self):
        self.db = Graph(uri='bolt://34.206.54.226:7687',
                        user='neo4j', password='authorizations-soaps-restriction')

    def create(self, name, ano_nasc, cpf):
        return self.db.execute_query('CREATE (n:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return n',
                              {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})

    def read(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) RETURN n',
                                     {'name': name})

    def update(self, name, newCpf):
        return self.db.execute_query(
            'MATCH (n:Teacher {name:$name}) SET n.cpf = $cpf RETURN n',
            {'name': name, 'cpf': newCpf})

    def delete(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) DELETE n',
                                     {'name': name})