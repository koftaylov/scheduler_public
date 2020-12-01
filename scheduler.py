# -*- coding: utf-8 -*-
import random
from func import printDict
from TrainerCalendar import TrainerCalendar
from People import People
from Logger import Logger
from Rules import Rules
from Trainings import Trainings
from sys import getsizeof
from send_mail import send_mail_attach
import datetime
import copy


# print('It\'s version with unfold amounts participant.')
# print('The result will be save to XLSX file.')

# if input("Continue? y or n: ").lower() != 'y':
#     exit(0)


receiver_email = "koftaylov@gmail.com"
subject = "Result schedule"
body = """
        The result of scheduler is in attachment.
        
        
        Your scheduler!
        """

logger = Logger()
logger.setLevel(1)
logger.log('--> Start scheduler3',1)
printflag = True

issendmail = input("Send mail? (False): ")
issendmail = True if issendmail == 'True' else False

attempts = input("Enter amount of attempts (100): ")
attempts = int(attempts) if attempts != '' and attempts.isdecimal() and int(attempts)>0 else 100

break_amount_percent = input("Enter break percents (85): ")
break_amount_percent = int(break_amount_percent)/100 if break_amount_percent != '' and break_amount_percent.isdecimal() and int(break_amount_percent)<=1 and int(break_amount_percent)>0 else 0.85

break_seconds = input("Enter break seconds (3600): ")
break_seconds = int(break_seconds) if break_seconds !='' and break_seconds.isdecimal() and int(break_seconds)>0 else 3600


year = input("Enter year (2019): ")
year = int(year) if year != '' and year.isdecimal() and int(year) >= 2017 and int(year) < 2030 else 2019

print("Loading data...")

trainer1 = "trainer#1"

# logger.log('start load demand',2)
demand = People()
demand.loadFromXLS(workbook='demand_'+str(year)+'.xlsm', worksheet='demand')
# print('demand') if printflag else None
# printDict(demand.people,"\t") if printflag else None

# logger.log('start load history',2)
history = People()
history.loadFromXLS('demand_'+str(year)+'.xlsm', worksheet='histor')
# print('history') if printflag else None
# printDict(history.people,"\t") if printflag else None

# logger.log('start load rules',2)
rules = Rules()
rules.loadFromCSV('rules2_'+str(year)+'.csv')
# print('rules') if printflag else None
# printDict(rules.rules) if printflag else None
# print('rules end') if printflag else None
# logger.log('delete demand trainig if it is in history',2)
deleted = demand.removeIfTRainigIsInOtherList(history.people)
# print('Deleted trainings - is in History '+str(len(deleted))+': '+str(deleted)) if printflag else None

# logger.log('delete trainigs without demands and add order',2)
deleted2 = demand.deleteIfDependenceIsNotInHistry(history,rules)
# printDict(demand.people,"\t") if printflag else None
# print('Deleted trainings 2: '+str(deleted2)) if printflag else None

# logger.log('make trainings-people object and load',2)
prts_for_trainings = Trainings(rules)
prts_for_trainings.loadTrainingsFromPeople(demand)
# print('prts_for_trainings') if printflag else None
# printDict(prts_for_trainings.prts_for_trainings,"\t") if printflag else None
# print('printPrtsForTrainingsCount') if printflag else None
# prts_for_trainings.printPrtsForTrainingsCount() if printflag else None

# logger.log('make list of trainings',2)
demand.makeListOfTrainings()
# print('list Of Trainings of Demand') if printflag else None
# print(demand.listOfTrainings) if printflag else None

# logger.log('make list of history trainings',2)
history.makeListOfTrainings()
# print('list Of Trainings of History') if printflag else None
# print(history.listOfTrainings) if printflag else None

# print(demand.countOfListOfTrainings()) if printflag else None
# print('There are ' + str(prts_for_trainings.countTotalPrtsForTrainings()) + ' requests.')

break_amount= int(break_amount_percent*prts_for_trainings.countTotalPrtsForTrainings())
# print(break_amount) if printflag else None
total_trainings = prts_for_trainings.countTotalPrtsForTrainings()
best_order = list()
best_calendar = list()
best_score = 1
best_iter=0
best_time = 0
best_score_iter = 0
#listOfAttempts = dict()
cal_for_tr_1 = TrainerCalendar(year,trainer1,rules.rules)

# print(cal_for_tr_1.cln_trainer) if printflag else None
# print('trainings for cal_tr_1') if printflag else None
# printDict(cal_for_tr_1.trainings) if printflag else None
# print('part weeks') if printflag else None
# printDict(cal_for_tr_1.participantweeks)
start_time =datetime.datetime.now()
# logger.log('start '+str(attempts)+' iterations',1)
# print('start '+str(attempts)+' iterations') if printflag else None
changed_min=False
try:
    for j in range(attempts):
        rules.makeTempFoldAmount()
        # logger.log('attempt '+str(j),2)
        # print('attempt '+str(j)) if printflag else None

        copy_cal_for_tr_1=copy.deepcopy(cal_for_tr_1)

        order = list()
        final_list = list()
        copy_initial_list = demand.listOfTrainings.copy()
        waitingList=list()
        for i in range(len(copy_initial_list)):
            rn = random.randint(0, len(copy_initial_list) - 1)
            order.append(copy_initial_list[rn])
            del copy_initial_list[rn]

        # logger.log('order madden',2)
        # print('order madden') if printflag else None
        # print('order:') if printflag else None
        # print(order) if printflag else None
        # logger.log('begin iterations by order', 2)
        # print('begin iterations by order') if printflag else None
        it=0
        for k in order:
            it+=1
            # print('k: '+str(k)) if printflag else None
            # logger.log('iteration '+ str(it), 2)

            participant = k.split('|')[0]
            training = k.split('|')[1]

            # logger.log('iteration '+str(it) + ': trying to add training for participant', 2)
            # print('iteration '+str(it) + ': trying to add '+str(training)+' for '+str(participant)) if printflag else None
            res = copy_cal_for_tr_1.addParticipantToTraining(participant,training,demand,rules,history)
            # logger.log('iteration '+str(it) + ' result of adding: '+str(res),2)
            # print('iteration '+str(it) + ' result of adding: '+str(res)) if printflag else None

            if not res:
                waitingList.append(participant+'|'+training)
                # print('add '+str(participant)+'|'+str(training)+' to waiting list') if printflag else None


        # print('cal before deleting') if printflag else None
        # printDict(copy_cal_for_tr_1.trainings) if printflag else None
        # print('deleting training with less min') if printflag else None
        # logger.log('iteration ' + str(it) + ': delete small trainings', 2)
        copy_cal_for_tr_1.deleteSmallTrainings(rules)

        # print('final: trainings') if printflag else None
        # printDict(copy_cal_for_tr_1.trainings) if printflag else None
        # print('final: participants list') if printflag else None
        # print(copy_cal_for_tr_1.participantslist) if printflag else None
        # print('score: '+str(len(copy_cal_for_tr_1.participantslist)) + ' from ' +str(len(demand.listOfTrainings))) if printflag else None
        score = len(copy_cal_for_tr_1.participantslist)

        if score > best_score:
            best_score = score
            best_order = final_list
            best_score_iter = j
            best_cal = copy.deepcopy(copy_cal_for_tr_1)
            best_iter = j
            best_time = (datetime.datetime.now() - start_time).seconds
            filename = best_cal.saveToXLS(demand,best_score,total_trainings)
        # print(str(j) + ': score is: ' + str(score) + ' -> best: ' + str(best_score) + ' / ' + str(total_trainings) + ' = ' + str(
        #     round(best_score / total_trainings * 100, 1)) + '%: ' + str(
        #     (datetime.datetime.now() - start_time).seconds) + ' sec: best in: ' + str(best_iter) + ' iter., ' + str(
        #     best_time) + ' sec') if printflag else None
        if score >= break_amount:
            print("--break by score")

            break
        if (datetime.datetime.now() - start_time).seconds>break_seconds:
            print("--break by time")

            break
        t1=datetime.datetime.now()
except KeyboardInterrupt:
    # print("Break. Saving file...")
    # logger.log('Making XLS', 1)
    # best_cal.saveToXLS(demand,best_score)
    # logger.log('End scheduler3', 1)
    exit(0)

# print('Finished. Saving file...')

# logger.log('Making XLS',1)

# best_cal.saveToXLS(demand,best_score)

# logger.log('End scheduler3',1)
if issendmail:
    send_mail_attach(receiver_email, subject, body, filename)

