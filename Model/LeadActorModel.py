class LeadActorModel:
    def __init__(self):
        self.leadActor_id = None
        self.actorName = None
        self.actorAge = None

    def get_leadActor_id(self):
        return self.leadActor_id

    def get_actorName(self):
        return self.actorName

    def get_actorAge(self):
        return self.actorAge

    
    def set_leadActor_id(self, leadActor_id):
        self.leadActor_id = leadActor_id

    def set_actorName(self, actorName):
        self.actorName = actorName

    def set_actorAge(self, actorAge):
        self.actorAge = actorAge

    
    def _str_(self):
        return f"Lead Actor Details: {self.leadActor_id}, {self.actorName}, {self.actorAge}"