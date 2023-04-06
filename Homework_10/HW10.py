# Refer to HW10.pdf

class Room: # entire class provided
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Room(name: {})".format(self.name)

class Task:
    def __init__(self, name,isCompleted = False):
        self.name = name
        self.isCompleted = isCompleted
        
    def __eq__(self,other):
        return (self.name, self.isCompleted) == (other.name, other.isCompleted)

    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)
    
class Crewmate:
    def __init__(self,color,accessories = (),isAlive = True,tasksDone = 0):
        self.color = color
        self.accesssories = accessories
        self.isAlive = isAlive
        self.tasksDone = tasksDone
    
    def doTask(self, Task):
        if Task.isCompleted is True:
            return "Nothing to do here"
        else:
            Task.isCompleted = True
            self.tasksDone += 1

    def vote(self, AmongUs):
        for member in AmongUs.crewmates:
            if member[0] == self[0] and member != self:
                if member.isAlive:
                    return member
        for member in AmongUs.impostors:
            if member[0] == self[0] and member != self:
                if member.isAlive:
                    return member
    
    def callMeeting(self,AmongUs):
        votes = {}
        for member in AmongUs.crewmates + AmongUs.impostors:
            votee = member.vote(AmongUs).name
            if votee  not in votes:
                votes[votee] = 1
            else:
                votes[votee] += 1
        
        maxVotes = max(votes.values())
        
        for key, value in votes:
            if value == maxVotes:
                if key in AmongUs.crewmates:
                    key.isAlive == False
                    return f'{key} was not an Impostor.'
                if key in AmongUs.impostors:
                    key.isAlive == False
                    return f'{key} was an Impostor.'

    def __repr__(self): # provided
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)
    

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, name, color, accessories = (), isAlive = True, eliminateCount = 0):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = isAlive
        self.eliminateCount = eliminateCount

    def eliminate(self,player):
        if type(self) == type(player):
            return "They're on your team -_-"
        if type(self) != type(player):
            player.isAlive = False
            self.eliminateCount += 1
    
    def vote(self, AmongUs):
        for member in AmongUs.crewmates:
            if member[0] == self[0] and member != self:
                if member.isAlive:
                    return member
        for member in AmongUs.impostors:
            if member[0] == self[0] and member != self:
                if member.isAlive:
                    return member
            

    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)
    
    def __str__(self):
        return f"My name is {self.name} and I'm an impostor."

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxPlayers, rooms = {}, crewmates = [], impostors = []):
        self.maxPlayers = maxPlayers
        self.rooms = rooms
        self.crewmates = crewmates
        self.impostors = impostors

    def registerPlayer(self, player):
        if len(self.crewmates) + len(self.impostors) >= self.maxPlayers:
            return "Lobby is full."
        for member in self.crewmates + self.impostors:
            if member.name == player.name:
                return f"Player with name: {player.name} exists."
            
        if type(player) == Crewmate:
            self.crewmates.append(player)
        else:
            self.impostors.append(player)
    
    def registerTask(self, newTask, newRoom):
        if newTask in self.rooms.values():
            return "This task has already been registered."
        
        if newRoom.name not in self.rooms:
            self.rooms[newRoom.name] = [newTask,]
        else:
            self.rooms[newRoom.name].append(newTask)

    def gameOver(self):
        aCrew = 0
        aImp = 0
        for player in self.crewmates:
            if player.isAlive is True:
                aCrew += 1
        for player in self.impostors:
            if player.isAlive is True:
                aImp += 1
        if aCrew == 0:
            return "Defeat! All crewmates have been eliminated."
        elif aImp == 0:
            return "Victory! All impostors have been eliminated."
        else:
            return "Game is not over yet!"

    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)