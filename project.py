import random

name = ""
age = 0
job = ""
height = 0
smartness = 0
has_speech = False

names = []
jobs = []

for i in range(10):
    name = input(f"Put in a name ({i}/10 names):")
    names.append(name)

for i in range(10):
    job = input(f"Put in a job ({i}/10 names):")
    jobs.append(job)

name = random.choice(names)
job = random.choice(jobs)
age = random.randint(10, 30)
height = random.random() * 10
smartness = random.randint(0, 10)
hasspeech = random.choice([True, False])

print("New NPC:\t", name)
print("Job:\t", job)
print("Age:\t", age)
print("Height:\t", height)
print("Inteligence:\t", smartness)
print("Can Speak:\t", hasspeech)