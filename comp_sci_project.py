# Mentor Google Sheet

import gspread
import pandas as pd
from google.auth import default
from google.colab import auth
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
spreadsheet = gc.open_by_key('1B_3tx6u48CIEar-zRHSeIvgGza9tvttdmgA8gxAojN8')
worksheet = spreadsheet.get_worksheet(0)
df = pd.DataFrame(worksheet.get())
# Code for making the first row as header. Remove if not needed.
df.columns = df.iloc[0]
df = df.drop(0)
df.head()

mentor_responses = df

class Mentor:
  def __init__(self, name, major, minor, undeclared, living, beechwood, clubs, greeklife, athlete, personaltime, social, lgbtq, ethnicgroup, sharedidentity, bond, communication, availability):
    self.name = name
    self.major = major
    self.minor = minor
    self.undeclared = undeclared
    self.living = living
    self.beechwood = beechwood
    self.clubs = clubs
    self.greeklife = greeklife
    self.athlete = athlete
    self.personaltime = personaltime
    self.social = social
    self.lgbtq = lgbtq
    self.ethnicgroup = ethnicgroup
    self.sharedidentity = sharedidentity
    self.bond = bond
    self.communication = communication
    self.availability = availability

mentors = []

for index, row in mentor_responses.iterrows():
    name = (row["Preferred First Name"] + " " + row["Last Name"])
    phone = (row["Phone Number"])
    email = (row["Email"])
    pronouns = (row["What are your preferred pronouns?"])
    grade = (row["What is your grade level for the upcoming year (2026/27)"])
    major = (row["What is your major(s)?"])
    minor = (row["What is your minor(s)?"])
    undeclared = (row["Did you enter Monmouth University undeclared?"])
    majorswitch = (row["Have you changed your major since being at Monmouth?"])
    living = (row["During your first year, did you live on campus or commute?"])
    beechwood = (row["Did you live in Beechwood (Honors Housing) your freshman year?"])
    clubs = (row["What clubs/student orgs/team are you involved in at Monmouth?"])
    greeklife = (row["Are you involved in Greek Life?"])
    athlete = (row["Are you a college varsity athlete?"])
    personaltime = (row["What do you do in your personal time separate from school-supported activities? (Select up to 3)"])
    birthday = (row["When is your birthday?"])
    social = (row["How would you describe your social style?"])
    lgbtq = (row["Are you a member of the LGBTQ+ community?"])
    ethnicgroup = (row["Do you feel particularly connected to an ethnic background/religion/cultural group/LGBTQ+ community/heritage and would like to connect with your mentee over this? "])
    groupmonmouth = (row["If you are a member of any ethnicity based groups on campus, which one(s)?"])
    strengths = (row["What do you consider your biggest strengths as a peer mentor? (Select up to 3)"])
    outsidemajor = (row["Would you be comfortable mentoring a student outside of your major?"])
    sharedidentity = (row["Would you prefer to mentor a student who shares your gender identity?"])
    bond = (row["What areas could you most easily bond over with your mentor?\n\n(Select up to 3)"])
    other = (row["Is there anything else you would like us to consider when creating mentor-mentee pairings?"])
    communication = (row["How would you prefer to communicate with your mentees?\n\n(Select all that apply)"])
    availability = (row["How available are you generally for checking in with your mentee?"])

    mentor = Mentor(name, major, minor, undeclared, living, beechwood, clubs, greeklife, athlete, personaltime, social, lgbtq, ethnicgroup, sharedidentity, bond, communication, availability)
    mentors.append(mentor)

count = 0
print(f"\nMentor Names")
for mentor in mentors:
  count = count + 1
  print(f"Mentor {count}: {mentor.name}")

  # Mentee Google Sheet

import gspread
import pandas as pd
from google.auth import default
from google.colab import auth
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
spreadsheet = gc.open_by_key('1B_3tx6u48CIEar-zRHSeIvgGza9tvttdmgA8gxAojN8')
worksheet = spreadsheet.get_worksheet(1)
df = pd.DataFrame(worksheet.get())
# Code for making the first row as header. Remove if not needed.
df.columns = df.iloc[0]
df = df.drop(0)
df.head()

mentee_responses = df

#Mentee Responses

class Mentee:  #storing all this info inside mentor)
  def __init__(self, name, major, minor, undeclared, living, beechwood, clubs, greeklife, athlete, personaltime, social, lgbtq, ethnicgroup, sharedidentity, bond, communication, availability):
    self.name = name
    self.major = major
    self.minor = minor
    self.undeclared = undeclared
    self.living = living
    self.beechwood = beechwood
    self.clubs = clubs
    self.greeklife = greeklife
    self.athlete = athlete
    self.personaltime = personaltime
    self.social = social
    self.lgbtq = lgbtq
    self.ethnicgroup = ethnicgroup
    self.sharedidentity = sharedidentity
    self.bond = bond
    self.communication = communication
    self.availability = availability

mentees = []

for index, row in mentee_responses.iterrows(): #assigning a response to the class Mentee
    name = (row["Preferred First Name"] + " " + row["Last Name"])
    phone = (row["Phone Number"])
    email = (row["Email"])
    pronouns = (row["What are your preferred pronouns?"])
    major = (row["What is your planned major? (If undeclared, please select undeclared)"])
    minor = (row["Do you have a planned or possible minor? Please select below, if not select: No."])
    living = (row["Will you be living on campus or commuting from home?"])
    hometown = (row["What is your hometown and state?"])
    beechwood = (row["Do you plan to live in Beechwood (Honors Housing) your freshman year?"])
    dorms = (row["If living on campus but not Beechwood Hall, what dorm do you plan to live in?"])
    clubs = (row["What clubs/student orgs/team are you interested in joining at Monmouth?"])
    greeklife = (row["Are you interested in joining Greek Life?"])
    athlete = (row["Are you a college varsity athlete?"])
    personaltime = (row["What do you do in your personal time separate from school-supported activities? (Select up to 3)"])
    social = (row["How would you describe your social style? 1 being introvert and 5 being extrovert."])
    lgbtq = (row["Are you a member of the LGBTQ+ community?"])
    ethnicgroup = (row["Do you feel particularly connected to an ethnic background/religion/cultural group/LGBTQ+ community/heritage and would like to connect with your mentor over this? Select yes, no, or non-applicable"])
    hopetogain = (row["What are you hoping to gain most from the Peer Mentoring Program? (Select up to 3)"])
    sharedidentity = (row["Would you prefer to be matched with a mentor who shares your gender identity?"])
    bond = (row["What areas are you hoping to bond over with your mentor?\n\n(Select up to 3)"])
    other = (row["Is there anything else you would like us to consider when creating mentor-mentee pairings?"])
    communication = (row["How would you prefer to communicate with your mentor?"])
    availability = (row["How available would you like your mentor to be?"])

    mentee = Mentee(name, major, minor, undeclared, living, beechwood, clubs, greeklife, athlete, personaltime, social, lgbtq, ethnicgroup, sharedidentity, bond, communication, availability)

    mentees.append(mentee)

count = 0
print(f"\nMentee Names")
for mentee in mentees:
  count = count + 1
  print(f"Mentee {count}: {mentee.name}")

  #Scoring System + Fuzzy Matching

!pip install rapidfuzz
from rapidfuzz import fuzz
import re

def get_keywords(answer):

  answer = str(answer).lower()
  answer = re.sub(r'[^\w\s]', ' ', answer)

  stop_words = ["i", "am", "the", "a", "an", "and","to", "of", "in", "with", "my", "want", "like", "enjoy", "that","for", "is", "it", "club", "clubs"]
  words = answer.split()
  keywords = []

  for word in words:
      if word not in stop_words:
        keywords.append(word)

  return keywords

def fuzzy_match(answer1, answer2):
  clubs1 = answer1.lower().replace(" and ", ",").split(",")
  clubs2 = answer2.lower().replace(" and ", ",").split(",")

  points = 0

  for club1 in clubs1:
    for club2 in clubs2:
      if club1.strip() != "" and club2.strip() != "":
        similarity = fuzz.ratio(club1.strip(), club2.strip())

        if similarity >= 85:
          points = points + 1
          break

  return points

def match_score(mentor, mentee):
  score = 0

  if mentor.major == mentee.major:
    score = score + 2

  if mentor.minor == mentee.minor:
    score = score + 1

  if mentor.undeclared == "Yes" and mentee.major == "Undeclared":
    score = score + 1

  if mentor.living == mentee.living:
    score = score + 2

  if mentor.beechwood == mentee.beechwood:
    score = score + 1

  score = score + fuzzy_match(mentor.clubs, mentee.clubs)

  if mentor.greeklife == mentee.greeklife:
    score = score + 1

  if mentor.athlete == mentee.athlete:
    score = score + 1

  mentor_answers = mentor.personaltime.split(", ")
  mentee_answers = mentee.personaltime.split(", ")

  for answer in mentor_answers:
    if answer != "" and answer in mentee_answers:
      score = score + 2

  if mentor.social == mentee.social:
    score = score + 1

  if mentor.lgbtq == mentee.lgbtq:
    score = score + 1

  if mentor.ethnicgroup == mentee.ethnicgroup:
    score = score + 1

  if mentor.sharedidentity == mentee.sharedidentity:
    score = score + 1

  mentor_answers = mentor.bond.split(", ")
  mentee_answers = mentee.bond.split(", ")

  for answer in mentor_answers: #if answer is equals mentee answers
    if answer != "" and answer in mentee_answers:
      score = score + 1

  if mentor.communication == mentee.communication:
    score = score + 1

  if mentor.availability == mentee.availability:
    score = score + 1

  return score

print(mentor.name)
print(mentee.name)

match_score(mentor, mentee)

# Matching Scores

for mentee in mentees:
  print(f"\nMentee: {mentee.name}")

  for mentor in mentors:
    score = match_score(mentor, mentee)
    print(f"Mentor: {mentor.name} - Score: {score}")

# Group Formation
num_mentors = int(input("Enter the number of mentors: ")) #idk if this works
num_mentees = int(input("Enter the number of mentees: "))

def compatibility():

  for mentor in mentors:
    mentor.group = []

  assigned = []

  for i in range(len(mentees)):
    highest_score = -1 #greater than 0
    best_mentor = None #emptys spot
    best_mentee = None #emptys spot

    for mentee in mentees:
      if mentee not in assigned:

        for mentor in mentors:
          if len(mentor.group) < 4:
            score = match_score(mentor, mentee)

            if score > highest_score: #is this score better than the highest score yet
              highest_score = score
              best_mentor = mentor #make that mentor best mentor
              best_mentee = mentee #makes that mentee best mentee

    if best_mentor is not None: #all mentees should have a best mentee at this point but if not it will print their name
      best_mentor.group.append(best_mentee.name) #
      assigned.append(best_mentee)
    else:
      print(f"No space available for {mentee.name}")

  for mentor in mentors:
    print(f"\nMentor: {mentor.name}")

    for name in mentor.group:
      print(name)

compatibility()

# Fuzzy Matching Check

for mentee in mentees:
  print(f"\nMentee: {mentee.name}")
  print(f"Clubs: {mentee.clubs}")

  for mentor in mentors:
    points = fuzzy_match(mentor.clubs, mentee.clubs)

    print(f"Mentor: {mentor.name}")
    print(f"Clubs: {mentor.clubs}")
    print(f"Club Points: {points}")