#Strings & Conditions
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
  
#String Challenge
def username_generator(first_name, last_name):
  #Create a username using the first 3 & 4 characters of first & last names
  if len(first_name) < 3: user_name = first_name
  else: user_name = first_name[0:3]
  if len(last_name) < 4:user_name += last_name
  else: user_name += last_name[0:4]
  print(user_name) 

def password_generator(user_name):
  password = ""
  #Adjusts the position of user_name by 1 to create password
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  print(password)
  
#String Slicing
def author_slicing():
  authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
  author_names = authors.split(',')
  #creates a new list to store the values
  author_last_names = []
  #iterates through the list of names
  for name in author_names:
    #appends name to empty list, then splits name according to first index
    author_last_names.append(name.split()[1])
  print(author_last_names)
  
#String Joining
def joinging():
    party_list = ["John Bishop", "James McAvoy", "Bill Williams", "Grace Sherlock", "Jean Grayson"]
    party_list = " ".join(party_list)

def stripped_strings():
    love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
    love_maybe_lines_stripped = []
    #Remove whitespace from list
    for lines in love_maybe_lines:
        #Inserts the removed whitespace text into empty list
        love_maybe_lines_stripped.append(lines.strip())
        #Creates new line within new list
        love_maybe_full = "\n".join(love_maybe_lines_stripped)
    print(love_maybe_full)

def replacing_strings():
    toomer_bio = " Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands."
    #Replace method changes the text in a string by taking the string as is then the string it's to become. 
    toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
    
def finding_strings():
    god_wills_it_line_one = "The very earth will disown you"
    #Finds the index of the string given as an argument
    disown_placement = god_wills_it_line_one.find("disown")
    print(disown_placement)
    
def formatting_strings():
    def poem_title_card(title, poet):
        #Escaping quotations reqires backslashes before the beginning quote and the space before the final quotation
        return "The poem \"{}\" is written by {}.".format(title, poet)
    print(poem_title_card("I Hear America Singing", "Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
    #Format is assigning the arguments to themselves so the order doesn't hinder the readability & utility of the code
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, 
    author=author, title=title, original_work=original_work)
    return poem_desc
#This variable stores the function containing the assigned variables. 
my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")


def review_string_methods():
    highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
    #Step 2
    print(highlighted_poems)
    highlighted_poems_list = highlighted_poems.split(",")
    #Step 3
    print(highlighted_poems_list)
    #Step 4
    highlighted_poems_stripped = []
    for i in highlighted_poems_list:
      highlighted_poems_stripped.append(i.strip())
    #Step 5
    print(highlighted_poems_stripped)
    #Step 6 
    highlighted_poems_details = []
    #Step 7 
    for j in highlighted_poems_stripped:
      highlighted_poems_details.append(j.split(":"))
    #Step 8 
    titles = []
    poets = []
    dates = [] 
    #Step 9 
    for k in highlighted_poems_details:
        titles.append(k[0])
        poets.append(k[1])
        dates.append(k[2])
    #Step 10
    for l in highlighted_poems_details[0]:
        print("The poem {} was published by {} in {}.".format(titles, poets, dates))
    
review_string_methods()