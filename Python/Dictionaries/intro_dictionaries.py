sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

#Dictionaires can be made of any combination of values from strings, numbers, or lists.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

#Adding A Key
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

#Adding Multiple Keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
    #The update method allows for the addition of multiple keys at once
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

#Overwrite Keys
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"

#Dictionary Comprehension
#Takes a pair from the iterator of tuples, Names the elements in the pair key and value, then Creates a key : value item in the students dictionary
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)

#Testing Dict Application
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
#Creates the key: value pairs of the lists above for music
plays = {key:value for key, value in zip(songs, playcounts)}
#Adds a new song and play count
plays["Purple Haze"] = 1
#Updates existing song and plays
plays.update({"Respect": 94})
#Creates a category of the music and an empty list 
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)