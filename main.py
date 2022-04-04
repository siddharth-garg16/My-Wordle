from valid_words import valid_words
import wordle
import os

os.system("cls") if os.name == "nt" else os.system("clear")

begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
"""

print(begin_message.replace("#", f"{wordle.Color.YELLOW}#{wordle.Color.BASE}"))

if __name__ == "__main__":
    
    while True:
        guess = wordle.GuessWord(w_str = input(f'[{wordle.GuessWord.counter}]> '))

        if guess.is_valid():
            guess.apply_guesses()
            guess.check_perfect_guess()
            guess.jump_turn()
            guess.check_game_loss()
