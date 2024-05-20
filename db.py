import json

class DataBase:

    def insert(self, username, email, password):
        with open('users.json', 'r') as rf:
            users = json.load(rf)
            if email in users:
                return 0
            else:
                users[email] = [username, password]
        
        with open('users.json', 'w') as wf:
            json.dump(users, wf)
            return 1