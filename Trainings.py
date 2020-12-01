class Trainings(object):
    prts_for_trainings = dict()

    def __init__(self,rules):
        for trainer in rules.rules["Trainings"]:
            for training in rules.rules["Trainings"][trainer]:
                if training not in self.prts_for_trainings:
                    self.prts_for_trainings[training] = list()

    def loadTrainingsFromPeople(self,people):
        for participant in people.people:
            for training in people.people[participant]["Trainings"]:
                self.prts_for_trainings[training].append(participant)

    def printPrtsForTrainingsCount(self):
        total = 0
        for tr in self.prts_for_trainings:
            total += len(self.prts_for_trainings[tr])
            print(tr, ": ", len(self.prts_for_trainings[tr]))
        print("Total: ", total)

    def countTotalPrtsForTrainings(self):
        total = 0
        for tr in self.prts_for_trainings:
            total += len(self.prts_for_trainings[tr])
            #print(tr, ": ", len(self.prts_for_trainings[tr]))
        return total
