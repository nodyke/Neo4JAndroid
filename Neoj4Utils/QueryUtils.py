user = 'app150253094-11630428245111380'
password = 'b.TUEkTw35WtVH.NY3HIFhT6Kj2cHwr'

from neo4j import GraphDatabase,basic_auth


uri = "bolt://hobby-deeblmpbgjnagbkegbbohnel.dbs.graphenedb.com:24787"
driver = GraphDatabase.driver(uri, auth=basic_auth(user, password), secure = True)



import Neo4jData
delete_query = 'MATCH (n) DETACH DELETE n'

with driver.session() as session:
    print(session.run(delete_query))

def create_question_query(q):
    return f"CREATE (:Question {{question: '{q}' }});"

for question in Neo4jData.Questions.splitlines():
    if question != '':
        with driver.session() as session:
            print(session.run(create_question_query(question)).summary().statement)

def create_solution_query(s):
    return f"CREATE (:Solution {{solution: '{s}' }});"


for solution in Neo4jData.Solutions.splitlines():
    if solution != '':
        with driver.session() as session:
            print(session.run(create_solution_query(solution)).summary().statement)




def create_question_2_solution_relationship(q, relation, s):
    return f"" \
        f"MATCH (a:Question),(b:Solution) " \
        f"WHERE a.question = '{q}' AND b.solution = '{s}' " \
        f"CREATE (a)-[r:{relation['name']} {{ name: '{relation['relationship']}' }}]->(b) RETURN type(r), r.name;"


def create_question_2_question_relationship(question_l, relation, question_r):
    return f"MATCH (a:Question), (b:Question) " \
        f"WHERE a.question = '{question_l}' AND b.question = '{question_r}' " \
        f"CREATE (a)-[r:{relation['name']} {{ name: '{relation['relationship']}' }}]->(b) RETURN type(r), r.name;"


for triplet in Neo4jData.q2q_triplets:
    try:
        with driver.session() as session:
            print(session.run(create_question_2_question_relationship(triplet[0], Neo4jData.getRelation(triplet[1]), triplet[2])).summary().statement)
    except Exception as e:
        print(e)
        print(triplet)

for location in Neo4jData.Locations.splitlines():
    try:
        if location != '':
            with driver.session() as session:
                print(session.run(create_question_query(location)).summary().statement)
                print(session.run(create_question_2_question_relationship('Место локализации', Neo4jData.getRelation('Локализация'),
                                                                          location)).summary().statement)
    except Exception as e:
        print(e)
        print(location)

for triplet in Neo4jData.q2s_triplets:
    try:
        with driver.session() as session:
            print(session.run(create_question_2_solution_relationship(triplet[0], Neo4jData.getRelation(triplet[1]), triplet[2])).summary().statement)
    except Exception as e:
        print(e)
        print(triplet)





driver.close()


