# scheduler.py
  The program is designed to form a training schedule based on the list of desired trainings and certain rules: time limits, job restrictions, participants' regions and others.
  

## Algorithm
  Due to the complexity of the rules and the multitude of staff to schedule for, the best approach, in my opinion, is random brute force.
  At each step of the enumeration, a list of training participants (Vasya-project management, Petya-Excel) is randomly generated for all employees and all their trainings. Next, we go through this random list and try to add a participant to an existing training, or if this type of training has not yet been planned (or if we could not add it due to restrictions in the rules), add a new training to the schedule and add a participant to it.
  After passing through all the participants, we count the number of participants who were added to the schedule and compare with the maximum achieved value - if more, we found the next best option. We save it and move on to the next random set. The program has several limitations: the number of iterations (how many random sets we will process), the percentage of person-trainings that we managed to fit into the schedule, the time, and also stops by CTRL + C.
  
___
## Classes
### Logger
A class for logging actions, in fact, you can make a function.

### Rules
A class for storing the rules reference book and working with it.

### Trainings
Class for keeping a list of people for each type of training.

### People
List of requested trainings and training history. For each employee present in the list of requested trainings, from 1 to 3 types of tregings are indicated for which the employee signed up. For each employee present in the list of attended trainings, there are tregings that the employee attended in previous years.

| Region | City | Surname and Name of the employee | Position | Line Manager | KAM 1 | KAM 2 | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KAM1 | Moscow | Ivanov Ivan | KAM | Petrov Petr | 1 | 1 | ... |
| KAM1 | Moscow | Petrov Petr | JKAM | Ivanov Ivan || 1 | ... |
| KAM1 | Moscow | Sidorov Sidr | KAM | Ivanov Ivan | 1 || ... |
| KAM1 | Moscow | Annova Anna | KAM | Ivanov Ivan ||| ... |


### TrainerCalendar
Trainings Schedule
____
