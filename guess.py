di={
    "FRUITS":{ # --> Fruits is the cateroy 
        1:"PINEAPPLE", # Here ( 1,2,3 ) are level 1 , next three are level 2 and rest 3 are level 3
        2:"BANANA",
        3:"ORANGE",

        4:"DRAGONFRUIT",
        5:"POMEGRANATE",
        6:"LITCHI",

        7:"RASPBERRY",
        8:"GRAPE",
        9:"AVACADO"

    },
    "ANIMALS":{
        1:"HORSE",
        2:"DONKEY",
        3:"GOAT",

        4:"LION",
        5:"CHEETAH",
        6:"SQUIRREL",

        7:"LIGER",
        8:"TIGON",
        9:"REDPANDA"
    }
}

def score_display(score): #--> function to display score which takes score as a parameter
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                   End of this short game ! ")
    print("Total score was 150")
    print("Your total score was",score)
    if(score==150):
        print("You have Big Brain")
    elif(score>=100 and score<150):
        print("You are smart")
    elif(score>=50 and score<100):
        print("Good try")
    else:
        print("Try harder !")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    again=input("Wanna play again ?")
    if(again.upper()=="YES"):
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        intro() # Asking to replay the game ! 
    else:
        print("GOODBYE!")
        
def user_guess(source): # ---> Function to display hint , count score , and ask and check the answers
    global categorie
    score=0
    word_count=1 # This is for keeping track of number of words
    list_keys=[key for key,value in source.items()] # List with all the keys from dictionary named "Hint"
    while(word_count<=3):
        guess_count=1
        print("                                 Word no : "+str(word_count)) # Shows word number
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(1,4):
            print("Hint no : "+str(i) ,source[list_keys[word_count-1]][i]) # Displays the hint from the dictionary with keys from list named list_keys
            answer=input("Enter the word :")
            if(answer.replace(" ","").upper()==list_keys[word_count-1]): # Checking if the answer is correct
                print("-------------------------------------------------------------------------------------------------------------------------------------------")
                print("Correct Answer")
                word_count+=1 # Adds 1 to the number of words if answer is correct by breaking the loop
                if(guess_count==1):
                    score+=50
                    print("+50 added to score")
                    break
                elif(guess_count==2):
                    print("+30 added to score")
                    score+=30
                    break
                elif(guess_count==3):
                    print("+10 added to score")
                    score+=10
                    break
                else:
                    break
            else:
                print("Incorrect answer")
                guess_count+=1
                print("-------------------------------------------------------------------------------------------------------------------------------------------")
                if(guess_count>3):
                    word_count+=1
                    break
    score_display(score)




def guessing_game(): # --> Asking the user for categorie and hardness of their choice
    print("Following are the list of categories : ")
    for key,value in di.items():
        print(key)
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    categorie=input("Choose a given categorie : ").upper()
    hardness=int(input("Choose the level of hardness ( 1,2,3 ): "))
# level_1 , level_2 , level_3 are the lists created for provicing hints for each item in a category
    if(hardness==1):
        level_1(categorie,di)
    elif(hardness==2):
        level_2(categorie,di)
    elif(hardness==3):
        level_3(categorie,di)
    else:
        print("Invalid choice")

def level_1(categorie,di):
    if(categorie=="FRUITS"):    
        Hints={
            di[categorie][1]:{1:"It's a tropical fruit known for its sweet and tangy flavor. It's often used in desserts, salads, and as a topping for pizzas.",
        2:"Starts with 'P' ",
        3:"Its exterior is covered in a rough, spiky skin, while the inside contains juicy, yellow flesh with a core of tougher, fibrous materiale"},

        di[categorie][2]:{1:"It's a tropical fruit with a curved shape and yellow skin.",
        2:" It's a good source of potassium and other essential nutrients.' ",
        3:"Starts with 'B' "},

        di[categorie][3]:{1:"It's commonly juiced for its refreshing taste, and its zest is used in cooking and baking.",
        2:"It's rich in vitamin C and is often associated with breakfast",
        3:"It's a citrus fruit known for its round shape and orange-colored skin."},
   }
    elif(categorie=="ANIMALS"):
        Hints={
            di[categorie][1]:{1:" Known for its strength, speed, and intelligence; has a long mane and tail.",
            2:"Large, four-legged mammal commonly used for riding, racing, and pulling carts. ",
            3:"starts with 'H'"},

        di[categorie][2]:{1:"Domesticated member of the horse family, known for its sturdy build and long ears.",
        2:"Often used as a working animal for carrying loads or pulling carts due to its strength and endurance.  ",
        3:" Known for its braying sound, which is distinct from the neighing of horses."},

        di[categorie][3]:{1:"Domesticated mammal with a shaggy coat, often found in various sizes and colors",
        2:" commonly kept for milk, meat, and fiber.",
        3:"Starts with 'G' "},
             }

    user_guess(Hints)

def level_2(categorie,di):
    if(categorie=="FRUITS"):
        Hints={
        di[categorie][4]:{1:"Tropical fruit with vibrant pink or yellow skin.",
        2:"Flesh is white or red with black seeds, tastes sweet like kiwi. ",
        3:" Hybrid fruit Rich in antioxidants, vitamins, and fiber; often used in smoothies and salads."},

        di[categorie][5]:{1:"This fruit Symbolizes fertility and abundance in many cultures worldwide",
        2:" Fruit with a tough outer skin and juicy, red seeds inside. ",
        3:"Name starts with 'P' "},

        di[categorie][6]:{1:" A small tropical fruit from the soapberry family",
        2:"Known as the Queen of Fruits",
        3:" It  has an oblong shape, bright red skin, and sweet and juicy pulp."},
   }
    elif(categorie=="ANIMALS"):
        Hints={
        di[categorie][4]:{1:"symbols of strength, courage, and royalty in many cultures.",
        2:"Its scientific name is Panthera leo ",
        3:"Starts with 'L' "},

        di[categorie][5]:{1:"Carnivorous animals with long legs and dinstinctive black tear marks from eyes to mouth",
        2:" This cat has relatively poor stamina and relies on short bursts of speed to catch its prey ",
        3:"Holds the title of the fastest land animal, capable of reaching speeds up to 75 miles per hour (120 kilometers per hour) "},

        di[categorie][6]:{1:"Small rodent with bushy tail, often seen climbing trees",
        2:"Known for storing nuts in burrows or tree hollows.",
        3:"Quick and agile, often seen darting across branches."},
   }
    user_guess(Hints)
    

def level_3(categorie,di):
    if(categorie=="FRUITS"):
        Hints={
        di[categorie][7]:{1:"Small, round fruit with a vibrant red color.",
        2:" Tart and sweet flavor, often used in desserts and jams. ",
        3:" Grows on bushes and is known for its distinctive druplet structure. ( starts with 'R')"},

        di[categorie][8]:{1:"Rich source of vitamin C tasting both sour and sweet",
        2:"Found in cluster with variety of colours , black and green being the major ones ",
        3:"Used widely to make wines' "},

        di[categorie][9]:{1:"Oval-shaped fruit with a green, bumpy skin.",
        2:"Creamy, pale green flesh with a nutty flavor.",
        3:"Rich in healthy fats, vitamins, and minerals; popular in salads and guacamole."},}
    elif(categorie=="ANIMALS"):
        Hints={
            di[categorie][7]:{1:"Hybrid Larger than both parent species, known for its massive size.",
        2:"Rare in the wild, primarily found in captivity due to different habitats of parent species ",
        3:"Hybrid big cat, offspring of a lion and a tigress."},

        di[categorie][8]:{1:" Resembles a smaller version of a lion with tiger-like stripes",
        2:" Rare in the wild, primarily found in captivity due to different habitats of parent species. ",
        3:" Hybrid big cat, offspring of a tiger and a lioness."},

        di[categorie][9]:{1:"Native to the eastern Himalayas and southwestern China.",
        2:"Small, tree-dwelling mammal with reddish-brown fur.",
        3:"Eats mainly bamboo, and is often mistaken for a raccoon due to its similar appearance."},
   }
    user_guess(Hints)

def intro():
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                     Welcome to this fancy guessing game !")
    print("                                     Following are the rules of this game:")
    print(""" 
    1) In this game you are supposed to guess a word out of the given categories .
    2) There are three levels to this game , where the hardness increases with increase in level
    3) You will be provided 3 hints related to a particular word for guessing .
    4) If you guess the word within the first hint , you will be awarded with 50 points .
    5) Similarly , 30 points for second try and 10 points for third try !
    6) There is a time limit of 30 seconds to guess each word . ( under construction )
    7) You will get zero points in the following conditions : 
         a) If you run out of time
         b) If you leave a guess blank 
         c) If you skip the question  
         
                            Good luck !
      """)
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    choice=input("Wanna get started(yes/no) ? ")
    if(choice.upper()=="YES"):
        guessing_game()
    elif(choice.upper()=="NO"):
        print("Get out then !")
    else:
        print("Invalid choice")
        ask=input("Try again ?")
        if(ask.upper()=="YES"):
            guessing_game()
        else:
            print("Bye then")
intro()

