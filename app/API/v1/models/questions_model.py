# from app.API.v1.views.user_views import user_model

class QuestionsModel:
    """ add a question to the database """

    def __init__(self):
        self.db = []

    def write_question(self, item):
        if item:
            self.db.append(item)
            return self.db
            
    def edit_question(self, id, updates=None):
        for i in range(len(self.db)):
            if self.db[i]["id"] == updates["id"]:
                self.db[i] = updates
                return self.db
            else:
                return self.db
    def del_question(self, id):
        que = [que for que in self.db if que['id'] == id]
        self.db.remove(que[0])
        return self.db
