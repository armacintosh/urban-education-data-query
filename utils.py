parse_user_query = """
You are an expert in querying knowledge graphs. 
Convert the following user query into a Cypher query for a Neo4j database. 

The graph contains the following entities:
- Variables: Represent data fields, with properties "label" and "format".
- Endpoints: Represent API access points.
- Sources: Represent data providers.
Make sure the Cypher query returns only valid entities and properties.

Here is an example of a user query and its expected Cypher query:
'''
User Query: "What data is available about enrollment?"
Expected Cypher Query:
MATCH (v:Variable)
WHERE v.label CONTAINS "enrollment"
RETURN v.name AS variable, v.label AS label
'''

User Query: "{user_query}"
Expected Cypher Query:
"""

