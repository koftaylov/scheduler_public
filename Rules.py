# -*- coding: utf-8 -*-
class Rules(object):
    def __init__(self):
        self.rules = dict()

    def loadFromCSV(self,filename):
        input = open(filename, 'r')
        while True:
            line = input.readline()

            # Trainings
            if line.split(';')[0] == "Trainings":
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[1] or line.split(";")[2]:
                    if '\n' in line: line = line.replace('\n', '')
                    if line.split(";")[1]:
                        sub_head = line.split(';')[1]
                        self.rules[head][sub_head] = dict()
                        keys = line.split(';')[3:]
                    else:
                        val = line.split(';')[2]
                        values = line.split(';')[3:]

                        self.rules[head][sub_head][val] = dict(zip(keys, values))
                        pr = self.rules[head][sub_head][val]["previous"]
                        if pr != "":
                            self.rules[head][sub_head][val]["previous"] = list(pr.split("|"))
                        else:
                            self.rules[head][sub_head][val]["previous"] = list()
                    line = input.readline()
            # Trainings end

            line = input.readline()
            # roles
            if line.split(';')[0] == 'roles':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = line.split(';')[1:]
                    self.rules[head][val] = [value for value in values if value != '']
                    line = input.readline()

            # roles end

            line = input.readline()
            # Region_Manager_roles
            if line.split(';')[0] == 'Region_Manager_roles':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = line.split(';')[1:]
                    self.rules[head][val] = [value for value in values if value != '']
                    line = input.readline()

            # Region_Manager_roles end

            line = input.readline()

            # roles_hierarchy
            if line.split(';')[0] == 'roles_hierarchy':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = int(line.split(';')[1])
                    self.rules[head][val] = values
                    line = input.readline()
            # roles_hierarchy end

            line = input.readline()
            # gap start
            if line.split(';')[0] == 'gap':
                head = line.split(';')[0]

                gap = input.readline().split(";")[0]
                self.rules[head] = int(gap)
            # gap end
            line = input.readline()
            line = input.readline()

            # region_max_amount start
            if line.split(';')[0] == 'region_max_amount':
                head = line.split(';')[0]
                region_max_amount = int(input.readline().split(";")[0])
                self.rules[head] = region_max_amount

            # region_max_amount end
            line = input.readline()
            line = input.readline()
            # workdays start
            if line.split(';')[0] == 'workdays':
                head = line.split(';')[0]
                line = input.readline()
                if '\n' in line: line = line.replace('\n', '')
                self.rules[head] = [int(value) for value in line.split(';') if value != '']

            # workdays end

            line = input.readline()
            line = input.readline()
            # holidays start
            if line.split(';')[0] == 'holidays':
                from datetime import date
                from datetime import timedelta
                head = line.split(';')[0]
                self.rules[head] = list()
                line = input.readline()
                holidays = list()
                while line.split(";")[0]:
                    if '\n' in line: line = line.replace('\n', '')
                    start_day = date(int(line.split(';')[0].split('-')[2]), int(line.split(';')[0].split('-')[1]),
                                     int(line.split(';')[0].split('-')[0]))

                    holidays.append(start_day)
                    if line.split(';')[1]:
                        end_day = date(int(line.split(';')[1].split('-')[2]), int(line.split(';')[1].split('-')[1]),
                                       int(line.split(';')[1].split('-')[0]))
                        for x in range(int((end_day - start_day).days)):
                            holidays.append((start_day + timedelta(days=x + 1)))
                    self.rules[head] = holidays

                    line = input.readline()

            # holidays end
            line = input.readline()
            # holidays_trainers start
            if line.split(';')[0] == "holidays_trainers":
                from datetime import date
                from datetime import timedelta
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[1] or line.split(";")[2]:
                    if '\n' in line: line = line.replace('\n', '')
                    if line.split(";")[1]:
                        sub_head = line.split(';')[1]
                        self.rules[head][sub_head] = list()
                    else:
                        start_day = date(int(line.split(';')[2].split('-')[2]),
                                         int(line.split(';')[2].split('-')[1]),
                                         int(line.split(';')[2].split('-')[0]))
                        holidays_trainers = list()
                        holidays_trainers.append(start_day)
                        if line.split(';')[3]:
                            end_day = date(int(line.split(';')[3].split('-')[2]),
                                           int(line.split(';')[3].split('-')[1]),
                                           int(line.split(';')[3].split('-')[0]))
                            for x in range(int((end_day - start_day).days)):
                                holidays_trainers.append((start_day + timedelta(days=x + 1)))
                        self.rules[head][sub_head] = holidays_trainers
                    line = input.readline()
            # holidays_trainers end
            line = input.readline()
            # trainer_max_week
            if line.split(';')[0] == 'trainer_max_week':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = int(line.split(';')[1])
                    self.rules[head][val] = values
                    line = input.readline()
            line = input.readline()

            if line.split(';')[0] == 'trainer_week_gap':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = int(line.split(';')[1])
                    self.rules[head][val] = values
                    line = input.readline()

            line = input.readline()

            if line.split(';')[0] == 'inadmissible_trainings':
                head = line.split(';')[0]
                self.rules[head] = dict()
                line = input.readline()
                while line.split(";")[0]:

                    if '\n' in line: line = line.replace('\n', '')
                    val = line.split(';')[0]
                    values = line.split(';')[1:]
                    self.rules[head][val] = [value for value in values if value != '']
                    line = input.readline()

            break

        input.close()

    def getPreviousTraining(self,training):
        if not training: return
        for trainer in self.rules["Trainings"]:
            if training in self.rules["Trainings"][trainer]:
                if self.rules["Trainings"][trainer][training]["previous"]:
                    return self.rules["Trainings"][trainer][training]["previous"]
                else:
                    continue
        return

    def isRolePossible(self,role, roles):
        res = True
        for r in roles:
            if r.lower() not in self.rules['roles'][role.lower()]:
                res = False
        return res

    def isRegionManagerPossible(self,participant,participants,demand,training):
        res = True
        if int(self.rules['Trainings']['trainer#1'][training]['roles_rules'])!=0:
            role = str(demand.people[participant]['Должность']).lower()
            region = str(demand.people[participant]['регион']).lower()
            for prt in participants:
                rg=str(demand.people[prt]['регион']).lower()
                if rg==region:
                    rl = str(demand.people[prt]['Должность']).lower()
                    if rl in self.rules['Region_Manager_roles']:
                        if role in self.rules['Region_Manager_roles'][rl]:
                            res = False
                    if role in self.rules['Region_Manager_roles']:
                        if rl in self.rules['Region_Manager_roles'][role]:
                            res = False
        return res

    def isMaxParticipantsPossible(self,amount,training):
        if training == 'Oratorical skills' and amount == 8:
            p=1
        res = False
        if amount<int(self.rules['Trainings']['trainer#1'][training]['tmp_amount']):
            res = True
        return res

    def isMaxFromRegionPossible(self,participant,participants,demand):
        res = True
        amount = 0
        region = str(demand.people[participant]['регион']).lower()
        for prt in participants:
            rg = str(demand.people[prt]['регион']).lower()
            if rg == region:
                amount+=1
        if amount>=int(self.rules['region_max_amount']):
            res = False
        return res

    def makeTempFoldAmount(self):
        import random

        for training in self.rules['Trainings']['trainer#1']:
            amount = (int(self.rules['Trainings']['trainer#1'][training]['max'])-int(self.rules['Trainings']['trainer#1'][training]['minmin']))//int(self.rules['Trainings']['trainer#1'][training]['fold'])+1
            if (int(self.rules['Trainings']['trainer#1'][training]['max'])-int(self.rules['Trainings']['trainer#1'][training]['minmin'])) % int(self.rules['Trainings']['trainer#1'][training]['fold']) != 0:
                print(training+' max('+self.rules['Trainings']['trainer#1'][training]['max']+')-min('+self.rules['Trainings']['trainer#1'][training]['minmin']+')/fold('+self.rules['Trainings']['trainer#1'][training]['fold']+') is not int!')
            amountList=list()
            for i in range(1,amount+1):
                amountList.append(int(self.rules['Trainings']['trainer#1'][training]['minmin'])+int(self.rules['Trainings']['trainer#1'][training]['fold'])*(i-1))
            self.rules['Trainings']['trainer#1'][training]['tmp_amount'] = amountList[random.randint(0,amount-1)]

    def isPossibleForCalendarDates(self,training,week_start_date):
        import datetime
        week_start_date = datetime.datetime.combine(week_start_date,datetime.datetime.min.time())
        return True if ((True if self.rules['Trainings']['trainer#1'][training]['start_day'] == ''
                            else week_start_date >= datetime.datetime.strptime(self.rules['Trainings']['trainer#1'][training]['start_day'],'%d-%m-%Y'))
                         and
                        (True if self.rules['Trainings']['trainer#1'][training]['end_day'] == ''
                              else week_start_date < datetime.datetime.strptime(self.rules['Trainings']['trainer#1'][training]['end_day'],'%d-%m-%Y'))
                         ) else False

