import requests
import json

# --- 1. 初期設定 ---
GRAPHQL_URL = "http://localhost/api/gql/console"
API_TOKEN = "xxxxxxxx"


# --- 2. セッションの準備（Cookie維持のため） ---
session = requests.Session()
headers = {
        'Content-Type' : 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {API_TOKEN}'
        }


# --- 3. 認証 ---
auth_query = """
query authLogin($credentials: Object) {
        authLogin(
            provider: "token",
            credentials: $credentials
        ) {
            authStatus
        }
}
"""

auth_vars = {
    "credentials": {
        "token": API_TOKEN
    }
}

auth_response = session.post(
    GRAPHQL_URL,
    headers=headers,
    json={
        'query': auth_query,
        'variables': auth_vars
        },
    verify=False)
print("🔑 authLogin response:", auth_response.json())

# --- 4. 接続作成 ---
create_query = '''
mutation CreateConnection($config: ConnectionConfig!) {
  createConnection(config: $config) {
    id
    name
    driverId
  }
}
'''

create_vars = {
    "config": {
        "name": "token-conn",
        "driverId": "mysql:mysql8",
        "host": "db.example.com",
        "port": "3306",
        "databaseName": "testdb",
        "userName": "admin"
    }
}

create_response = session.post(GRAPHQL_URL, headers=headers, json={
    'query': create_query,
    'variables': create_vars
}, verify=False)

create_data = create_response.json()
print("🛠️ connectionCreate response:", json.dumps(create_data, indent=2))
