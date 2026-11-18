# Mentor Responses

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