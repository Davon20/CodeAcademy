sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

#Dictionaires can be made of any combination of values from strings, numbers, or lists.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

def dictionaries():
    def add_keys():
        animals_in_zoo = {}
        animals_in_zoo["zebras"] = 8
        animals_in_zoo["monkeys"] = 12
        animals_in_zoo["dinosaurs"] = 0
    
    def add_more_keys():
        user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
        #The update method allows for the addition of multiple keys at once
        user_ids.update({"theLooper": 138475, "stringQueen": 85739})
        
    def overwrite_keys():
        oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
        oscar_winners.update({"Supporting Actress": "Viola Davis"})
        oscar_winners["Best Picture"] = "Moonlight"
        
    def dict_lists():
        drinks = ["espresso", "chai", "decaf", "drip"]
        caffeine = [64, 40, 0, 120]
        zipped_drinks = zip(drinks, caffeine)
        drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
        print(drinks_to_caffeine)
        
    def dict_music_playlist():
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
        
    def access_dict():
        zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
        #This accessing the elements in accordance to the keys
        print(zodiac_elements["earth"])
        print(zodiac_elements["fire"])
        
    def conditional_dict():
        zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

        zodiac_elements["energy"] = "Not a Zodiac element"

        if "energy" in zodiac_elements:
          print(zodiac_elements["energy"])
          
    def try_and_except_dict():
        caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
        caffeine_level["matcha"] = 30
        try: 
          print(caffeine_level["matcha"])
        except KeyError:
          print("Unknown Caffeine Level")
          
    def dict_get():
        user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
        tc_id = user_ids.get("teraCoder")
        print(tc_id)

        stack_id = user_ids.get("superStackSmash", 100000)
        print(stack_id)

    def dict_delete():
        available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
        health_points = 20
        health_points += available_items.pop("stamina grains", 0)
        health_points += available_items.pop("power stew", 0)
        health_points += available_items.pop("mystic bread", 0)
        print(available_items, health_points)
    
    def dict_full_key_access():
        user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
        num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

        users = user_ids.keys()
        lessons = num_exercises.keys()

        print(users, lessons)
    
    def dict_full_value_access():
        num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
        total_exercises = 0 
        for num in num_exercises.values():
          total_exercises += num
          print(total_exercises)
    
    def dict_full_access():
        pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

        for occupation, percentage in pct_women_in_occupation.items():
          print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
    
    def dict_full_use():
        tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 
                 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 
                 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 
                 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 
                 20:	"Judgement", 21:	"The World", 22: "The Fool"}

        spread = {}
        spread["past"] = tarot.pop(13)
        spread["present"] = tarot.pop(22)
        spread["future"] = tarot.pop(10)

        for key, value in spread.items():
          print("Your " + (key) + " is the " + (value) + " card.")
          
    def dict_practice():
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
        letter_to_points = {key:value for key, value in zip(letters, points)}
        letter_to_points[" "] = 0
        print(letter_to_points)

        def score_word(word):
          point_total = 0 
          for letter in word:
            point_total += letter_to_points.get(letter, 0)
          return point_total
        
        browine_points = score_word("BROWNIE")
        print(browine_points)
        
        player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
        player_to_points = {}

        for player, words in player_to_words.items():
            player_points = 0 
            for word in words:
                player_points += score_word(word)
            player_to_points[player] = player_points 
        print(player_to_points)

        def play_word(player, word):
            player_to_words[player].append(word)
        play_word("player1", "CODE")
        print(player_to_words)
        print(player_to_points)
    dict_practice()
dictionaries()