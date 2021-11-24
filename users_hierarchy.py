# Example inputs
roles = [
{
"Id": 1,
"Name": "System Administrator",
"Parent": 0},
{
"Id": 2,
"Name": "Location Manager",
"Parent": 1
},
{
"Id": 3,
"Name": "Supervisor",
"Parent": 2
},
{
"Id": 4,
"Name": "Employee",
"Parent": 3
},
{
"Id": 5,
"Name": "Trainer",
"Parent": 3
}
]

users = [
{
"Id": 1,
"Name": "Adam Admin",
"Role": 1
},
{
"Id": 2,
"Name": "Emily Employee",
"Role": 4
},
{
"Id": 3,
"Name": "Sam Supervisor",
"Role": 3
},
{
"Id": 4,
"Name": "Mary Manager",
"Role": 2
},
{"Id": 5,
"Name": "Steve Trainer",
"Role": 5
}
]

class UsersHierarchy(object):
    def __init__(self,head = None):
        super().__init__()

    def getSubOrdinates(self, user_id):
        result = []
        # Get user of given User Id
        user = next((user for user in users if user["Id"] == user_id), False)
        # Get role of given User
        role = user['Role']
    
        for u in users:
            if u['Role'] > role:
                result.append(u)
        print(result)
        return result
