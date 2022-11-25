# import the Functions file
import Functions

# create an object play
play = Functions.game()
# initialize the game
play.initialize()

# end the loop once the player chooses to exit the game
while play.status <= 2:
    # show the matrix
    for i in play.matrix:
        print(i)
    # when 2048 is reached
    if play.status == 1:
        while True:
            # collect input and restrict it to numbers only
            try:
                # use \n to organize the text and make it more friendly to read
                restart = int(input("Congratulations! You've reached 2048! Do you want to play for another round? \n (1) YES \n (2) NO \n Option: "))
            except:
                # ask for a proper input if there is any error
                print('You can only choose within the available options.')
                continue
            # initialize the game again if the player chooses option 1
            if restart == 1:
                play.initialize()
                # break the loop otherwise it never ends
                break
            # change the status to 3 if the player chooses option 2
            elif restart == 2:
                play.status = 3
                # break the loop otherwise it never ends
                break
            else:
                # ask for a proper input among the available options
                print('You can only choose within the available options.')
    # when there is no movable steps
    elif play.status == 2:
        while True:
            # collect input and restrict it to numbers only
            try:
                # use \n to organize the text and make it more friendly to read
                restart = int(input("Opps! Game is over! Do you want to play for another round? \n (1) YES \n (2) NO \n Option: "))
            except:
                # ask for a proper input if there is any error
                print('You can only choose within the available options.')
                continue
            # initialize the game again if the player chooses option 1
            if restart == 1:
                play.initialize()
                # break the loop otherwise it never ends
                break
            # change the status to 3 if the player chooses option 2
            elif restart == 2:
                play.status = 3
                # break the loop otherwise it never ends
                break
            else:
                # ask for a proper input among the available options
                print('You can only choose within the available options.')
    else:
        while True:
            # collect input and restrict it to numbers only
            try:
                # use \n to organize the text and make it more friendly to read
                # add an Exit option so the player can end the game at any moment
                move = int(input('What is your next step? \n (1) Up \n (2) Down \n (3) Left \n (4) Right \n (5) Exit \n Option: '))
            except:
                # ask for a proper input if there is any error
                print('You can only choose within the available options.')
            if move == 1:
                # if it is impossible to move this step, the while loop in the function will cause an error
                try:
                    play.move_up()
                    # break the loop otherwise it never ends
                    break
                except:
                    # warn and ask for a different move
                    print('This is not a valid move! Try with another one.')
            elif move == 2:
                # if it is impossible to move this step, the while loop in the function will cause an error
                try:
                    play.move_down()
                    # break the loop otherwise it never ends
                    break
                except:
                    # warn and ask for a different move
                    print('This is not a valid move! Try with another one.')
            elif move == 3:
                # if it is impossible to move this step, the while loop in the function will cause an error
                try:
                    play.move_left()
                    # break the loop otherwise it never ends
                    break
                except:
                    # warn and ask for a different move
                    print('This is not a valid move! Try with another one.')
            elif move == 4:
                # if it is impossible to move this step, the while loop in the function will cause an error
                try:
                    play.move_right()
                    # break the loop otherwise it never ends
                    break
                except:
                    # warn and ask for a different move
                    print('This is not a valid move! Try with another one.')
            # change the status to 3 if the player chooses option 5
            elif move == 5:
                play.status = 3
                # break the loop otherwise it never ends
                break
            else:
                # ask for a proper input among the available options
                print('You can only choose within the available options.')
        # check if there is any movable steps and if 2048 is reached after each move
        play.check()