guests = ['carla','gus','ricky']
print(guests)
print("I've found a bigger table, so i'll invite 3 more guest")
guests.insert(0, "paula")
guests.insert(int(len(guests)/2), "rulo")
guests.append("maria")
print(guests)
messages = "Hey " + guests[0].capitalize() + " come over to my house, let's have some dinner\n"
messages = messages + "Hi " + guests[1].capitalize() + " i'll have dinner with " + guests[0].capitalize() + " and " + guests[2].capitalize() + ", you're invited too\n"
messages = messages + guests[2].capitalize() + " ma men, come to mine's, we'll eat something\n"
messages = messages + "Oi " + guests[3].capitalize() + " come to my house we'll eat something\n"
messages = messages + "Che " + guests[4].capitalize() + " veni a comer algo, que viene mucha gente\n"
messages = messages + guests[5].capitalize() + " veni a comer a la noche"
print("-----------------------------------------------------\n" + messages + "\n-----------------------------------------------------")