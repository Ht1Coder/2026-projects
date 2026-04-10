import csv
import time
import random
import os

os.system('cls' if os.name == 'nt' else 'clear') #clears screen
def authentication():
    global username #Make username a global variable 
    User_file = "user.csv" #Allows user.csv to be variable
    username = input(''' _____       _                                     
| ____|_ __ | |_ ___ _ __   _   _  ___  _   _ _ __ 
|  _| | '_ \| __/ _ \ '__| | | | |/ _ \| | | | '__|
| |___| | | | ||  __/ |    | |_| | (_) | |_| | |   
|_____|_| |_|\__\___|_|     \__, |\___/ \__,_|_|   
 _   _ ___  ___ _ __ _ __   |___/_ __ ___   ___ _  
| | | / __|/ _ \ '__| '_ \ / _` | '_ ` _ \ / _ (_) 
| |_| \__ \  __/ |  | | | | (_| | | | | | |  __/_  
 \__,_|___/\___|_|  |_| |_|\__,_|_| |_| |_|\___(_)  ''') # Ask for the username
    username.lower() #makes it lowercase
    os.system('cls' if os.name == 'nt' else 'clear') #clears screen
    user_found = False #Checks if there is a username
    with open(User_file, "r") as file: #reads file
       reader = csv.reader(file) 
       for row in reader:
           if row[0] == username:
               user_found = True
               break

    if user_found:
        print(''' _                _                                          __       _   
| |    ___   __ _(_)_ __    ___ _   _  ___ ___ ___  ___ ___ / _|_   _| |  
| |   / _ \ / _` | | '_ \  / __| | | |/ __/ __/ _ \/ __/ __| |_| | | | |  
| |__| (_) | (_| | | | | | \__ \ |_| | (_| (_|  __/\__ \__ \  _| |_| | |_ 
|_____\___/ \__, |_|_| |_| |___/\__,_|\___\___\___||___/___/_|  \__,_|_(_)
__        __|___/                           _                _            
\ \      / /__| | ___ ___  _ __ ___   ___  | |__   __ _  ___| | __        
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | '_ \ / _` |/ __| |/ /        
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | |_) | (_| | (__|   < _       
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_.__/ \__,_|\___|_|\_( )      
                                                                 |/       ''', username) #When user is found it tell them the login was successful
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''' _   _                             _      __                       _   
| | | |___  ___ _ __   _ __   ___ | |_   / _| ___  _   _ _ __   __| |  
| | | / __|/ _ \ '__| | '_ \ / _ \| __| | |_ / _ \| | | | '_ \ / _` |  
| |_| \__ \  __/ |    | | | | (_) | |_  |  _| (_) | |_| | | | | (_| |_ 
 \___/|___/\___|_|    |_| |_|\___/ \__| |_|  \___/ \__,_|_| |_|\__,_(_)  ''') #tell them user is not found
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = input(''' __        __          _     _                       _ _ _          _        
\ \      / /__  _   _| | __| |  _   _  ___  _   _  | (_) | _____  | |_ ___  
 \ \ /\ / / _ \| | | | |/ _` | | | | |/ _ \| | | | | | | |/ / _ \ | __/ _ \ 
  \ V  V / (_) | |_| | | (_| | | |_| | (_) | |_| | | | |   <  __/ | || (_) |
   \_/\_/ \___/ \__,_|_|\__,_|  \__, |\___/ \__,_| |_|_|_|\_\___|  \__\___/ 
  __ _  __| | __| |   __ _   _ _|___/____      __  _   _ ___  ___ _ _|__ \  
 / _` |/ _` |/ _` |  / _` | | '_ \ / _ \ \ /\ / / | | | / __|/ _ \ '__|/ /  
| (_| | (_| | (_| | | (_| | | | | |  __/\ V  V /  | |_| \__ \  __/ |  |_|   
 \__,_|\__,_|\__,_| _\__,_| |_| |_|\___| \_/\_/    \__,_|___/\___|_|  (_)   
 _   _  ___  ___   / / __   ___                                             
| | | |/ _ \/ __| / / '_ \ / _ \                                            
| |_| |  __/\__ \/ /| | | | (_) |                                           
 \__, |\___||___/_/ |_| |_|\___/                                            
 |___/                                                                      ''').lower() #gives the option to make a new user
        if choice == "yes":
             os.system('cls' if os.name == 'nt' else 'clear')
             username = input('''  _____       _                                    
| ____|_ __ | |_ ___ _ __   _ __   _____      __  
|  _| | '_ \| __/ _ \ '__| | '_ \ / _ \ \ /\ / /  
| |___| | | | ||  __/ |    | | | |  __/\ V  V /   
|_____|_|_|_|\__\___|_|__  |_| |_|\___|_\_/\_/_ _ 
| | | / __|/ _ \ '__| '_ \ / _` | '_ ` _ \ / _ (_)
| |_| \__ \  __/ |  | | | | (_| | | | | | |  __/_ 
 \__,_|___/\___|_|  |_| |_|\__,_|_| |_| |_|\___(_) ''')
             with open(User_file, "a", newline="") as file: #Adds the new user to the file
              writer = csv.writer(file)
              writer.writerow([username])
              os.system('cls' if os.name == 'nt' else 'clear')
             print('''  _   _                           _     _          _                      
| | | |___  ___ _ __    __ _  __| | __| | ___  __| |                     
| | | / __|/ _ \ '__|  / _` |/ _` |/ _` |/ _ \/ _` |                     
| |_| \__ \  __/ |    | (_| | (_| | (_| |  __/ (_| |                     
 \___/|___/\___|_|     \__,_|\__,_|\__,_|\___|\__,_|    __   __          
 ___ _   _  ___ ___ ___  ___ ___ / _|_   _| | |_   _    \ \ / /__  _   _ 
/ __| | | |/ __/ __/ _ \/ __/ __| |_| | | | | | | | |    \ V / _ \| | | |
\__ \ |_| | (_| (_|  __/\__ \__ \  _| |_| | | | |_| |_    | | (_) | |_| |
|___/\__,_|\___\___\___||___/___/_|  \__,_|_|_|\__, (_)   |_|\___/ \__,_|
                                        _      |___/                 _   
  __ _ _ __ ___   _ __   _____      __ | | ___   __ _  __ _  ___  __| |  
 / _` | '__/ _ \ | '_ \ / _ \ \ /\ / / | |/ _ \ / _` |/ _` |/ _ \/ _` |  
| (_| | | |  __/ | | | | (_) \ V  V /  | | (_) | (_| | (_| |  __/ (_| |  
 \__,_|_|  \___| |_| |_|\___/ \_/\_/   |_|\___/ \__, |\__, |\___|\__,_|  
(_)_ __                                         |___/ |___/              
| | '_ \                                                                 
| | | | |_                                                               
|_|_| |_(_)                                                               ''')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''  ____                                                 _ _ _ 
|  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___   __      _(_) | |
| |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \  \ \ /\ / / | | |
|  __/| | | (_) | (_| | | | (_| | | | | | |  \ V  V /| | | |
|_|   |_|  \___/ \__, |_|_ \__,_|_|_|_| |_|   \_/\_/ |_|_|_|
  ___| | ___  ___|___/  (_)_ __   | ___|                    
 / __| |/ _ \/ __|/ _ \ | | '_ \  |___ \                    
| (__| | (_) \__ \  __/ | | | | |  ___) |                   
 \___|_|\___/|___/\___| |_|_| |_| |____/                    
 ___  ___  ___ ___  _ __   __| |___                         
/ __|/ _ \/ __/ _ \| '_ \ / _` / __|                        
\__ \  __/ (_| (_) | | | | (_| \__ \_ _ _                   
|___/\___|\___\___/|_| |_|\__,_|___(_|_|_)                   ''') #closes the program
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''   ____ _           _                         
 / ___| | ___  ___(_)_ __   __ _             
| |   | |/ _ \/ __| | '_ \ / _` |            
| |___| | (_) \__ \ | | | | (_| |            
 \____|_|\___/|___/_|_| |_|\__, |            
 _ __  _ __ ___   __ _ _ __|___/ _ __ ___    
| '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \   
| |_) | | | (_) | (_| | | | (_| | | | | | |_ 
| .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_(_)
|_|              |___/                        ''')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

authentication() 
def choose_song(): #gets all the data from the song.csv file
    songlist = []
    songs = "mysong.csv"
    with open(songs, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            songlist.append(row)
        choice = random.choice(songlist)
        choice_song_name = choice[0]
        choice_song_author = choice[1]
        choice_song_duration = choice[2]
        return choice_song_name, choice_song_author, choice_song_duration
        
def song_info(): #print all the data from the song.csv file
    choice_song_name, choice_song_author, choice_song_duration = choose_song()
    first_letter = next(zip(*choice_song_name.split()))
    word_list = choice_song_name.split()  
    letter_count = []
    for word in word_list:
      letter_count.append(len(word))
    print(f"This is the song duration {choice_song_duration}")  #prints the song duration
    print(f"This is the name of the author {choice_song_author}") #prints the song author
    print(f"This is the first letter of every word {first_letter}") #prints the first letter of everyword
    print(f"This is the amount of letters in each word {letter_count}") #prints the letter count
    guess = input("What is your guess for the song name: ").lower() #gets input for song name
    return guess, choice_song_name
def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''    ____                        ____  _             _   _             
 / ___| __ _ _ __ ___   ___  / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
| |  _ / _` | '_ ` _ \ / _ \ \___ \| __/ _` | '__| __| | '_ \ / _` |
| |_| | (_| | | | | | |  __/  ___) | || (_| | |  | |_| | | | | (_| |
 \____|\__,_|_|_|_| |_|\___| |____/ \__\__,_|_| _ \__|_|_| |_|\__, |
(_)_ __   |___ /   ___  ___  ___ ___  _ __   __| |___         |___/ 
| | '_ \    |_ \  / __|/ _ \/ __/ _ \| '_ \ / _` / __|              
| | | | |  ___) | \__ \  __/ (_| (_) | | | | (_| \__ \              
|_|_| |_| |____/  |___/\___|\___\___/|_| |_|\__,_|___/              ''') #starts the game
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    lives = 3
    global score # makes score global
    score = 0
    while lives > 0:
        guess, choice_song_name = song_info()
        if guess.lower() == choice_song_name.lower():
          score += 1
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"Your score is {score}")#current score
          print(f"Your lives is: {lives}")#current lives
        else:
            if lives > 1: 
                lives -= 1 
                os.system('cls' if os.name == 'nt' else 'clear') 
                print(f"Your score is {score}") #current score
                print(f"Your lives is: {lives}")#current lives
            else:
                lives -= 1 # takes away a life
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Your final score is {score}") #tell what score you have
                print(f"Your lives is: {lives}") #tell you that you have to no lives
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                
game()

def leaderboard_display(): #displaying leaderboard functipn
    global leaderboard
    leaderboard = "leaderboard.csv"
    with open(leaderboard, "a", newline="") as file: #adds data to the leaderboard file
     writer = csv.writer(file)
     writer.writerow([score, username])
    leader = []
    with open(leaderboard, "r") as file: #reads the leaderboard file
        reader = csv.reader(file)
        for row in reader:
            if row[0].isdigit(): #checks if the score is a digit
                leader.append([int(row[0]), row[1]]) #adds the scores to the leaderboard list
    leader.sort(reverse=True) #sorts the leaderboard in terms of score
    print("Top five leaderboard:")
    if len(leader) <= 5: #prints the leaderboard if there is 5 or less people
        for data in leader:
            print(data)
    else: 
        for data in leader[0:5]: #prints the top five scores in the leaderboard
            print(data)
   
leaderboard_display()
