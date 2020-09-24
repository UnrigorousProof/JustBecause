import csv

presidentResults = "1976-2016-president.csv"
houseResults = "1976-2018-house.csv"
senateResults = "1976-2018-senate_1.csv"

def grade(dictionary):
  stateGrades = {}
  for state, votes in dictionary.items():
    grade = []
    for vote in votes:
      if "democrat" in vote:
        grade.append(-1)
      elif "republican" in vote:
        grade.append(1)
      else:
        grade.append(0)
    stateGrades[state] = grade
  return stateGrades

  
def getPresidentialResults():
  StateHistory = {}

  with open(presidentResults, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
      
    votes = {}
    for count, row in enumerate(csvreader):
      if count == 0:
        continue

      
      State = row[2]
      voteID = str(row[0]) + "-" + str(row[3]) + "-" + str(row[4]) + "-" + str(row[5] + "-" + row[1])
      if voteID not in votes.keys():
        votes[voteID] = []
      
      votes[voteID].append([row[8], row[10]])
    
    StateHistory = {}
    #for each election find the winning party  
    for key, values in votes.items():
      max= 0 
      maxParty = ""
      
      if int(key[0:4]) < 2000:
        continue

      for party, val in values:
        if int(val) > max:
          maxParty = party
          max = int(val)

      state = key[key.rfind("-")+1:]
      if state not in StateHistory.keys():
          StateHistory[state] = []
      StateHistory[state].append(maxParty)
      
  return StateHistory


def getSenateResults():
  StateHistory = {}

  with open(senateResults, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
      
    votes = {}
    for count, row in enumerate(csvreader):
      if count == 0:
        continue

      
      State = row[2]
      voteID = str(row[0]) + "-" + str(row[3]) + "-" + str(row[4]) + "-" + str(row[5] + "-" + row[1])

      if voteID not in votes.keys():
        votes[voteID] = []
      
      votes[voteID].append([row[11], row[14]])
    
    StateHistory = {}
    #for each election find the winning party  
    for key, values in votes.items():
      max= 0 
      maxParty = ""
      
      if int(key[0:4]) < 2000:
        continue

      for party, val in values:
        if int(val) > max:
          maxParty = party
          max = int(val)

      state = key[key.rfind("-")+1:]
      if state not in StateHistory.keys():
          StateHistory[state] = []
      StateHistory[state].append(maxParty)
      
  return StateHistory


def getHouseResults():
  StateHistory = {}

  with open(houseResults, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
      
    votes = {}
    for count, row in enumerate(csvreader):
      if count == 0:
        continue
      
      State = row[2]
      voteID = str(row[0]) + "-" + str(row[3]) + "-" + str(row[4]) + "-" + str(row[5]) + "-" + str(row[7]) + "-" + row[1]

      if voteID not in votes.keys():
        votes[voteID] = []
      
      votes[voteID].append([row[12], row[15]])
    
    StateHistory = {}
    #for each election find the winning party  
    for key, values in votes.items():
      max= 0 
      maxParty = ""
      
      if int(key[0:4]) < 2000:
        continue

      for party, val in values:
        if int(val) > max:
          maxParty = party
          max = int(val)

      state = key[key.rfind("-")+1:]
      if state not in StateHistory.keys():
          StateHistory[state] = []
      StateHistory[state].append(maxParty)
      
  return StateHistory
  
  
presidentGrades = grade(getPresidentialResults())
senateGrades = grade(getSenateResults())
houseGrades = grade(getHouseResults())

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
members = {'Alabama':7, 'Alaska':1, 'Arizona':9, 'Arkansas':4, 'California':53, 'Colorado':7, 'Connecticut':5, 'Delaware':1, 'Florida':27, 'Georgia':14, 'Hawaii':2, 'Idaho':2, 'Illinois':18, 'Indiana':9, 'Iowa':4, 'Kansas':4, 'Kentucky':6, 'Louisiana':6, 'Maine':2, 'Maryland':8, 'Massachusetts':9, 'Michigan':14, 'Minnesota':8, 'Mississippi':4, 'Missouri':8, 'Montana':1, 'Nebraska':3, 'Nevada':4, 'New Hampshire':2, 'New Jersey':12, 'New Mexico':3, 'New York':27, 'North Carolina':13, 'North Dakota':1, 'Ohio':16, 'Oklahoma':5, 'Oregon':5, 'Pennsylvania':18, 'Rhode Island':2, 'South Carolina':7, 'South Dakota':1, 'Tennessee':9, 'Texas':36, 'Utah':4, 'Vermont':1, 'Virginia':11, 'Washington':10, 'West Virginia':3, 'Wisconsin':8, 'Wyoming':1}

for state in states:
  grades = []
  sum = 0
  total = 0
  d = {-1:0,0:0,1:0}
  for val in presidentGrades[state]:
    grades.append(val)
    sum += val
    total += 1
    d[val] += 1
  for val in senateGrades[state]:
    grades.append(val)
    sum += val/2
    total += 1/2
    d[val] += 1
  for val in houseGrades[state]:
    grades.append(val)
    sum += val/members[state]
    total += 1/members[state]
    d[val] += 1
  
  print(state, d, sum / total)
