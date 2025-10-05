import random

#Function to select  the winner
def win(player,computer):
    if player == computer:
        print("\nIt's a tie!...")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
         print("\n*****You Wins*****")
    else:
        print("\n*****Computer Wins*****")
        
#Function to play the game
def play():
    choices=['rock','paper','scissor']
    player_choice=input("Enter your choice: rock,paper, or scissor :").lower()

    if player_choice not in choices:
        player_choice=print("Invalid choice...")
        return
    computer_choice= random.choice(choices)
    print(f"You chose : {player_choice.upper()}")
    print(f"Computer chose : {computer_choice.upper()}")
     
    winner=win(player_choice,computer_choice)

#Main function      
def main():
    print(" Rock, Paper, Scissors Game ")
    print("------------------------------------------\n")
    print("Winning Rules:\n Rock vs Paper -> Paper Wins\n Paper vs Scissor -> Scissor Wins \n Rock vs Scissor -> Rock Wins\n")
    print ("\nLets start the game.....")
   
    while True:
        play()
      # Play again option
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        
        if play_again != "yes":
            print("Thanks for playing!")
            break
       
main()

