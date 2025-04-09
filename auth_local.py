import requests
import json

GRAPHQL_URL = 'http://localhost:8978/api/gql'
USERNAME = 'test'
PASSWORD = 'password'

session = requests.session()

# headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }

# # --- 3. 認証 ---
# auth_query = """
# query Login($credentials: Object) {
#   authLogin(provider: "local", credentials: $credentials) {
#     authStatus
#   }
# }
# """

# auth_vars = {
#     "credentials": {
#         "user": "test",
#         "password": "password"
#     }
# }

# auth_response = session.post(GRAPHQL_URL, headers=headers, json={
#     'query': auth_query,
#     'variables': auth_vars
# }, verify=False)

# print("🔑 authLogin response:", auth_response.json())



# query = """mutation {
#     openSession{
#     createTime,
#     lastAccessTime,
#     valid,
#     remainingTime,
#     }
# }"""
# open_session_response = session.post(
#     GRAPHQL_URL,
#     json={"query": query},
#     verify=False
# )

# open_session_data = open_session_response.json()
# print("🛠️ open_session_data response:", json.dumps(open_session_data, indent=2))


# create_query = '''
# mutation CreateConnection($config: ConnectionConfig!) {
#   createConnection(config: $config) {
#     id
#     name
#     driverId
#   }
# }
# '''

# create_vars = {
#     "config": {
#         "name": "token-conn",
#         "driverId": "mysql:mysql8",
#         "host": "db.example.com",
#         "port": "3306",
#         "databaseName": "testdb",
#         "userName": "admin"
#     }
# }

# create_response = session.post(GRAPHQL_URL, json={
#     'query': create_query,
#     'variables': create_vars
# }, verify=False)

# create_data = create_response.json()
# print("🛠️ connectionCreate response:", json.dumps(create_data, indent=2))


# ### session_state
# session_state_query = '''{
#   sessionState {
#     createTime,
#     valid,
#     remainingTime
#   }
# }'''

# session_state_response = session.post(GRAPHQL_URL, json={
#     'query': session_state_query
# }, verify=False)

# session_state_data = session_state_response.json()
# print("🛠️ session_state_data response:", json.dumps(session_state_data, indent=2))


# ### listProjects
# listProjects_query = '''{
#   listProjects {
#     id,	
#     global,
#     shared,
#     name
#   }
# }'''

# listProjects_response = session.post(GRAPHQL_URL, json={
#     'query': listProjects_query
# }, verify=False)

# listProjects_data = listProjects_response.json()
# print("🛠️ listProjects response:", json.dumps(listProjects_data, indent=2))


# ### activeUser
# activeUser_query = '''{
#   activeUser {
#     userId,
#     displayName
#   }
# }'''

# activeUser_response = session.post(GRAPHQL_URL, json={
#     'query': activeUser_query
# }, verify=False)

# activeUser_data = activeUser_response.json()
# print("🛠️ activeUser_data response:", json.dumps(activeUser_data, indent=2))


### listTeams
listTeams_query = '''{
  listTeams {
    teamId,
    teamName,
    description
  }
}'''

listTeams_response = session.post(GRAPHQL_URL, json={
    'query': listTeams_query
}, verify=False)

listTeams_data = listTeams_response.json()
print("🛠️ listTeams_data response:", json.dumps(listTeams_data, indent=2))
