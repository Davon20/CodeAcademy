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

def final_project():
  daily_sales = \
  """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
  09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
  white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
  ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
  ;,;   $5.13   ;,; white   ;,; 09/15/17,
  Eduardo George   ;,;$20.39;,; white&yellow 
  ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
  purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
  purple&yellow ;,;09/15/17,   Shaun Brock;,; 
  $17.98;,;purple&yellow ;,; 09/15/17 , 
  Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
  Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
  Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
  09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
  white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
  ;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
  $8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
  09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
  green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
  ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
  Israel Cummings;,;   $11.86   ;,;black;,;  
  09/15/17,   June Doyle   ;,;   $22.29 ;,;  
  black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
  $8.35;,;   white&black&yellow   ;,;   09/15/17,   
  Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
  ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
  ;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
  ;,; 09/15/17   ,Hubert Miles;,;   $3.59   
  ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
  ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
  black   ;,;   09/15/17 , Audrey Ferguson ;,; 
  $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
  $17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
  Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
  09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
  yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
  yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
  ;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
  $14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
  ;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
  black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
  ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
  $8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
  ;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
  ,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
  09/15/17 , Melody Moran ;,;   $30.84   
  ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
  $12.31 ;,; green&yellow&black;,;   09/15/17 ,
  Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
  ,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
  09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
  white&yellow&black ;,;09/15/17   ,   Dale Brady   
  ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
  Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
  ,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
  09/15/17, Angelica Garza;,;$11.60;,;white&black   
  ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
  white&black&red ;,;09/15/17   ,   Rex Hudson   
  ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
  ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
  Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
  ;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
  green&purple&yellow ;,;09/15/17   ,Stanley Holland 
  ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
  Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
  ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
  red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
  green&red ;,;   09/15/17   ,Irving Patterson 
  ;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
  Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
  Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
  Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
  ,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
  Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
  , Beatrice Newman ;,;$22.45   ;,;white&purple&red 
  ;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
  red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
  black&red;,; 09/15/17,   Javier Bailey   ;,;   
  $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
  Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
  ,   Traci Craig ;,;$0.65;,; green&yellow;,; 
  09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
  green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
  ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
  ;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
  Leonard Guerrero ;,;   $1.86   ;,;yellow  
  ;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
  09/15/17   ,Donna Ball ;,; $28.10  ;,; 
  yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
  $9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
  $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
  ;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
  Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
  ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
  green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
  green&yellow;,;09/15/17,Malcolm Morales ;,;   
  $24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
  Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
  ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
  , Leticia Manning;,;$15.70 ;,; green&purple;,; 
  09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
  09/15/17,Lewis Glover;,;   $13.66   ;,;   
  green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
  ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
  ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

  #------------------------------------------------
  # Start coding below!
  daily_sales_replaced = daily_sales.replace(";,;", "+")
  daily_transactions = daily_sales_replaced.split(",")
  # print(daily_transactions)

  daily_transactions_split = []
  for transaction in daily_transactions: 
    daily_transactions_split.append(transaction.split("+"))
    # print(daily_transactions_split)
    
  transactions_clean = []
  for transaction in daily_transactions_split:
    transaction_clean = []
    for data_point in transaction:
      transaction_clean.append(data_point.replace("\n", " ").strip(" "))
      transactions_clean.append(transaction_clean)
    # print(transactions_clean)
    
  customers = []
  sales = []
  thread_sold = []
  for transaction in transactions_clean:
    customers.append(transaction[0])
    sales.append(transaction[1])
    thread_sold.append(transaction[2])
    
  total_sales = 0 
  for sale in sales: 
    total_sales += float(sale.strip("$"))
    
  thread_sold_split = []
  for sale in thread_sold:
    for color in sale.split("&"):
      thread_sold_split.append(color)
    
  def color_count(color):
    color_total = 0 
    for thread_color in thread_sold_split:
      if color == thread_color:
        color_total += 1
    return color_total
  
  print(color_count("white"))

  colors = ['red','yellow','green','white','black','blue','purple']
  for color in colors:
    print("Thread Shed sold {0} threads of {1} thread today.".format(color_count(color), color))
final_project()