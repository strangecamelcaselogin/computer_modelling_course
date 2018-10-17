from app.model import Model


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

    def new_session(self, name):
        return self.model.new_session(name)

    # def load_session(self, name):
    #     return self.model.load_session(name)

    def delete_session(self, name):
        return self.model.delete_session(name)

    def save_session(self, session, save_as=None):
        return self.model.save_session(session, save_as)
