from email.policy import EmailPolicy


def strings_challenges():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    #this function is designed to return the number of non-repeated letters in a word
    def unique_english_letters(word):
        #I understood I needed a counter
      count = 0 
      #I understood I needed a for loop to iterate throgh the letters variable
      for letter in letters:
          #I became confused here because  I didn't understand how to use the if statement. The if statement should reference the word, not letters.
        # if letter == letters:
        if letter in word:
            #I was also confused about how to count. I was under the impression that a variable would be added itself using +=.
        #   count += count
            count += 1
      return count
    print(unique_english_letters("mississippi"))
    print(unique_english_letters("Apple"))
    
    # Write your count_char_x function here:
    def count_char_x(word, x):
        count = 0 
        for letter in word:
          #I only missed that this if statement should be ==
        # if letter in x:
            if letter == x:
                count += 1
        #misplaced the return 
        return count
    print(count_char_x("mississippi", "s"))
    print(count_char_x("mississippi", "m"))
    
    # Write your count_multi_char_x function here:
    def count_multi_char_x(word, x):
        #split function breaks up word according to x
      splits = word.split(x)
      #returns the list of what was split numerically, - returns what was removed
      return(len(splits)-1) 
    print(count_multi_char_x("mississippi", "iss"))
    print(count_multi_char_x("apple", "pp"))    
    
    # Write your substring_between_letters function here:
    def substring_between_letters(word, start,end):
        #each function takes care of find the start and end points of the word. 
        #Since I didn't know about these functions I had to learn in this function.
      start_ind = word.find(start)
      end_ind = word.find(end)
      #checks what's between the start and end.
      if start_ind > -1 and end_ind > -1:
          #Since slicing is inclusive:exclusive the additional 1 is required for starting.
        return(word[start_ind+1:end_ind])
      return word
    print(substring_between_letters("apple", "p", "e"))
    print(substring_between_letters("apple", "p", "c"))
    
    def x_length_words(sentence, x):
        #this breaks the sentence down into an array. 
      words = sentence.split(" ")
      #this iterates through the array measuring it against integer provided
      for word in words: 
        if len(word) < x:
          return False
        else: return True
    print(x_length_words("i like apples", 2))
    print(x_length_words("he likes apples", 2))
    
def strings_advanced_challenges():
    #Checks for name being in sentence
    def check_for_name(sentence, name):
        #This was my solution
    #   if name.lower() in sentence.lower():
    #     return True
    #   else: return False
      #alternatively the method could be written as 
      return name.lower() in sentence.lower()
    print(check_for_name("My name is Jamie", "Jamie"))
    print(check_for_name("My name is jamie", "Jamie"))
    print(check_for_name("My name is Samantha", "Jamie"))
    
    def every_other_letter(word):
      #I couldn't understand how to iterate by 2. Missing 0 indicating the starting point, since range takes 3 parameters.
        empty_string = ""
        for i in range(0, len(word), 2):
        #this string will store the characters,so the append method is required, yet it can't be used because of the AttributeError
        #I don't understand how to use + to add the characters to the empty string.
            empty_string += word[i]
        return empty_string
    print(every_other_letter("Codecademy"))
    print(every_other_letter("Hello world!"))
    
    def reverse_string(word):
      rev_string = ""
      #All I needed to change was the range from the previous function. 
      #I tried solving the problem incrementally but in this case that didn't work as the solution is a whole one. 
      #Using -1, len(word) only got the first letter, yet I couldn't understand how to get the remaining characters. 
      for i in range(len(word) -1, -1, -1):
        rev_string += word[i]
      return rev_string
    print(reverse_string("Codecademy"))
    print(reverse_string("Hello world!"))
    
    def make_spoonerism(word1, word2):
        #New variables aren't required since the characters can be assessed by indexes
        return word2[0] + word1[1:] + " " + word1[0] + word2[1:]
    print(make_spoonerism("Codecademy", "Learn"))
    print(make_spoonerism("Hello", "world!"))
    print(make_spoonerism("a", "b"))
    
    # Write your add_exclamation function here:
    def add_exclamation(word):
        #Forgot len() method
      while len(word) < 20:
        #Forgot = w/+
        word += "!"
      return word
    print(add_exclamation("Codecademy"))
    print(add_exclamation("Codecademy is the best place to learn"))
    
def dict_challenge():
    def sum_values(my_dictionary):
      numsum = 0 
      for value in my_dictionary.values():
          #Only have the variables backwards
        numsum += value
      return numsum
    print(sum_values({"milk":5, "eggs":2, "flour": 3}))    
    print(sum_values({10:1, 100:2, 1000:3}))
    
    def sum_even_keys(my_dictionary):
        evensum = 0
        for key in my_dictionary.keys():
            #Confused on how to use if statement. 
            if key % 2 == 0:
                #My confusion was misunderstanding that the iteration is happening to the keys not the values
                evensum += my_dictionary[key]
        return evensum
    #prints 2
    print(sum_even_keys({1:5, 2:2, 3:3}))
    #prints 6
    print(sum_even_keys({10:1, 100:2, 1000:3}))

    def add_ten(my_dictionary):
      for key in my_dictionary.keys():
        my_dictionary[key] += 10
      return my_dictionary
    # should print {1:15, 2:12, 3:13}
    print(add_ten({1:5, 2:2, 3:3}))
    # should print {10:11, 100:12, 1000:13}
    print(add_ten({10:1, 100:2, 1000:3}))
    
    def values_that_are_keys(my_dictionary):
      value_keys = []
      for value in my_dictionary.values():
        if value in my_dictionary:
          value_keys.append(value)
      return value_keys
    # should print [1, 4]
    print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
    # should print ["a"]
    print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
    
    def max_key(my_dictionary):
      largest_key = float("-inf")
      largest_value = float("-inf")
      for key, value in my_dictionary.items():
        if value > largest_value:
          largest_value = value
          largest_key = key
      return largest_key
    # should print 1
    print(max_key({1:100, 2:1, 3:4, 4:10}))
    # should print "c"
    print(max_key({"a":100, "b":10, "c":1000}))
dict_challenge()

def advanced_dict_challenge():
    def word_length_dictionary(words):
      empty = {}
      for word in words:
        empty[word] = len(word)
      return empty
    # should print {"apple":5, "dog": 3, "cat":3}
    print(word_length_dictionary(["apple", "dog", "cat"]))
    # should print {"a": 1, "": 0}
    print(word_length_dictionary(["a", ""]))
    
    #I don't fully grasp this method. I understand that it's counting the words in dictionary, but how?
    def frequency_dictionary(words):
        #this stores the values that are returned since nothing is being removed, only counted
      emp_dict = {}
      #iterates through each word or simply put counting
      for word in words:
          #Just discovered the not in syntax w/this challenge 
        if word not in emp_dict:
            #emp_dict is storing the values that aren't duplicates as 0
          emp_dict[word] = 0
          #I'm not sure why this is an indent behind the initial, but this variable is adding to the count.
        emp_dict[word] += 1
      return emp_dict
    # should print {"apple":2, "cat":1, 1:1}
    print(frequency_dictionary(["apple", "apple", "cat", 1]))
    # should print {0:5}
    print(frequency_dictionary([0,0,0,0,0]))
    
    #The first challenge I SOLVED ON MY OWN. :)
    def unique_values(my_dictionary):
        #return the # of unique values from each list
      empty_list = []
      for value in my_dictionary.values():
        if value not in empty_list:
          empty_list.append(value)
      return len(empty_list)
    # should print 2
    print(unique_values({0:3, 1:1, 4:1, 5:3}))
    # should print 1
    print(unique_values({0:3, 1:3, 4:3, 5:3}))
    
    #This challenge was the last and hardest.
    def count_first_letter(names):
      letters = {}
      #iteration is happening through multiple dictionaries
      for key in names:
          #the index accesses the first letter
        first_letter = key[0] 
        if first_letter not in letters:
            #set the value of letters to 0
          letters[first_letter] = 0 
          #I understand this is where the iteration is happening, however, I don't comprehend what's stored in names[key] before the iteration
        letters[first_letter] += len(names[key])
      return letters
    # should print {"S": 4, "L": 3}
    print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
    # should print {"S": 7}
    print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))