import json
class Database:
    def add_data(self,name,email,password):
        with open("db.json","r") as rf:  # w write mode replace old data  # read mode
            database =json.load(rf)

        if email in database:
            return 0
        else:
            database[email]=[name,password]
            with open("db.json","w") as wf:
                json.dump(database,wf)
            return  1