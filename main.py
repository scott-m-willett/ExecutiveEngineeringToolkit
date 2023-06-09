# Author: Scott Willett
# Version: 2023-05-29 (v0.1)
#
# Name: Executive Engineering Toolkit
# Description: A coding tool to help communicate with a non-technical decision maker (an executive)

# A module that helps us to create banners
import pyfiglet

# This is our banner for the program
# https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
print(pyfiglet.figlet_format("Executive Engineering Toolkit", font = "letters"))

# This is our task.
print(pyfiglet.figlet_format("Task"))
task = """
Think about how you could persuade a CIO in an organisation which still has mandated regular password changes"
- to not do that, and instead to adopt the standard. We're going to assume the CIO isn't technical.
"""
print(task)

# Understanding of the business.
print(pyfiglet.figlet_format("Context"))
context = """
Business name: Dunder Mifflin Paper Co, Scranton Branch
Description: A branch for a private corporation, selling paper in Scranton"
Business type: Medium Enterprise
Risk Appetite: Low
Risk Language: ISO 31000, information on the risk matrix on intranet portal
CIO Name: Jan Levinson
"""
print(context)

# Initial attempt at the task
print(pyfiglet.figlet_format("Initial Attempt"))
attempt_one = """ 
Insert your attempt here
"""
print(attempt_one)

# The crown jewels. Identify our critical assets that relate to the task
print(pyfiglet.figlet_format("The Crown Jewels"))
crown_jewels = """
Billing system
Sales system
Office 365 tenant
"""
print(crown_jewels)

# Business Impact - Reframe what we’re communicating, using what our audience cares about.
print(pyfiglet.figlet_format("Business Impact"))
business_impact = """
Can either of these be realised if we don't implement our solution? Is there significant risk?
- Data breach
- Ransomware

Could consequences to SCORE happen if we don't implement our solution? Is there significant risk?

SCORE
- Safety
- Compliance
- Operations
- Reputation
- Economy (revenue)
"""
print(business_impact)

# Executive perspective - our audience is very busy, and it is understandable that difficult problems can move to the back of the queue.
print(pyfiglet.figlet_format("Executive Perspective"))
perspective = """
Our audience is very busy with many things happening at once. It is easy for our request to fall to the back of the queue.

Check our message is tailored so it is:
- Concise and relevant
- Has a clear ask / request
- Easy to make a decision
"""
print(perspective)

# Create a narrative
print(pyfiglet.figlet_format("Narrative"))
narrative = """
I have created a story that engages my audience.
I am prepared to tell my own story.
"""
print(narrative)

# Based on the 4 birds approach to understanding personality
print(pyfiglet.figlet_format("Personality"))
personality = """
The personality of the CIO is an eagle. I need to be relevant and clear in my message.
"""
print(personality)

# Case studies to back you up
print(pyfiglet.figlet_format("Case Studies"))
case_studies = """
I will research use case studies the optus, medibank, and latitude breaches to back me up if I need it.
"""
print(case_studies)

# Consider what we have learned about changing minds.
print(pyfiglet.figlet_format("Changing Minds"))
changing_minds = """
Consider the following to help change someones mind:
- You need to understand someone, their perspective, and their side of the issue. 
- Pick sources your audience deems trustworthy. 
- Actively listen, pay attention to their emotions, and honour / respect them.
- Prop someone up, make them feel good about themselves, and not threatened
- A lot of people will conform when a group has a contrary opinion to their own.
- We might have to play the long game with our message – changing minds is hard!
"""
print(changing_minds)

# Imagery and anologies
print(pyfiglet.figlet_format("Message"))
imagery = """
I have a handful of images and analogies available to communicate concepts that resonate with my audience.
"""
print(imagery)

# Preparing your first draft
print(pyfiglet.figlet_format("Message"))
message = """
I have prepared a message that is:
- Concise
- Relevant to what my audience cares about
- Is backed up by evidence, costs, and more detail if required
- Has a call to action that makes it easy to make a decision
"""
print(message)


# Delivering the message
print(pyfiglet.figlet_format("Delivery"))
delivery = """
- I have thought about how I can connect with my audience - thinks I can talk or joke about.
- I have thought about how I present myself
- I have spent time learning and practicing speaking for impact
"""
print(delivery)

# Reflect on your message and delivery
print(pyfiglet.figlet_format("Reflection"))
reflection = """
I have looked inwards and at my message, regardless of the result of my message. I have reflected on my message and delivery.
"""
print(reflection)

# Attempt the exercise again
print(pyfiglet.figlet_format("Second Attempt"))
attempt_one = """ 
Insert your second attempt here
"""
print(attempt_one)