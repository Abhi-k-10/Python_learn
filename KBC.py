import random


#KBC Programme 


username = input("Enter your Name to Continue : ")

#List of Qustions
Ques = [ "Q: What block-building survival game is famous for creepers and crafting?" ,
         "Q: Which popular programming language is widely used for building AI and simple 2D games?",
         "Q: Which core markup language provides the basic structural foundation for web GUIs?",
         "Q: What Debian-derived Linux distribution is designed specifically for ethical hacking?",
         "Q: Which centralized counseling authority manages engineering college seat allocation in India?",
         "Q: What decade's nostalgic, vintage aesthetic is known for heavy film grain and warm tones?" ,
         "Q: On which video-sharing platform do gaming creators typically upload their content?",
         "Q: What everyday wireless networking technology is frequently used to practice password cracking?" ]


#List of answers 
Ans = ["Minecraft" , 
       "Python",
       "HTML",
       "Kali",
       "JoSAA",
       "90s",
       "YouTube",
       "Wi-Fi"]

#Function for intiation
def initiatorKBC():
    print(f"Hello {username}, Welcome to the Game of Kaun Banega KarorePati , Presented By Abhik !")
    Display = random.choice(Ques)
    Options = [random.sample(Ans , 1) , random.sample(Ans , 1) , random.sample(Ans , 1) ,]
    
    print(Display) 
    print(Options)
    UserInput = input(f"{username} Enter Your Answer as it is : ")

    if UserInput in Options:
        if Options.index(Ans) == Display.index(Ques):
            print("Answer is Correct")
        else :
            print("Wrong Answer")

    else :
        print("Options were wrong")

initiatorKBC()
