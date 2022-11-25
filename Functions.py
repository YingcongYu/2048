class game():
    def __init__(self):
        # create a variable matrix so all functions can directly call it
        self.matrix = []
        # use number 0, 1, 2, 3 to represent the status of the game
        # 0 means the game is ongoing
        # 1 means the game reaches 2048
        # 2 means the game is failed
        # 3 means the player wants to exit the game
        self.status = 0
    
    def add_2(self):
        # generate random coordinates to place 2 in a random cell
        import random
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        # only place 2 in an empty cell
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = 2
        else:
            self.add_2()
    
    def initialize(self):
        # use 0 to represent empty
        self.matrix = [[0]*4 for i in range(4)]
        # reset status
        self.status = 0
        # add two 2s to the matrix
        for i in range(2):
            self.add_2()
    
    def check(self):
        target = 0
        movable = 0
        for i in range(4):
            for j in range(4):
                # find the current maximum value of the matrix
                target = max(target, self.matrix[i][j])
                # if there is any 0 in the matrix, there must be movable steps
                if self.matrix[i][j] == 0:
                    movable = 1
                    continue
                # no need to check the last number
                if j == 3 and i == 3:
                    break
                # special judgement for the last column and the last row
                elif j == 3:
                    if self.matrix[i][j] == self.matrix[i+1][j]:
                        movable = 1
                elif i == 3:
                    if self.matrix[i][j] == self.matrix[i][j+1]:
                        movable = 1
                # for other rows, if there is any same number on the current number's right or down position, there must be movable steps
                else:
                    if self.matrix[i][j] == self.matrix[i][j+1] or self.matrix[i][j] == self.matrix[i+1][j]:
                        movable = 1
        # if 2048 is reached, change status to 1
        if target >= 2048:
            self.status = 1
        # if there is no movable step, change status to 2
        elif movable == 0:
            self.status = 2

    # moving to each of the four directions needs a corresponding function
    # moving to any of the four directions is actually the same case
    # use coordinates to locate numbers in the matrix
    def move_up(self):
        for j in range(4):
            # use fast and slow pointers to help identify various scenarios
            fast = 1
            slow = 0
            while fast < 4:
                # move the fast pointer until it reaches a non-zero
                if self.matrix[fast][j] == 0:
                    fast += 1
                else:
                    # if the slow pointer points at a zero, exchange the number between fast and slow
                    # only move the fast pointer because nothing has been done to that new slow number yet
                    if self.matrix[slow][j] == 0:
                        self.matrix[slow][j], self.matrix[fast][j] = self.matrix[fast][j], self.matrix[slow][j]
                        fast += 1
                    # if both numbers are the same, add them together at the slow position
                    # change the fast number to 0 because it has been used
                    # move both pointers
                    elif self.matrix[slow][j] == self.matrix[fast][j]:
                        self.matrix[slow][j] += self.matrix[fast][j]
                        self.matrix[fast][j] = 0
                        slow += 1
                        fast += 1
                    # if both numbers are not the same, exchange the fast number with the place one index ahead of the slow pointer
                    # this position must be the fast pointer itself or 0 because the fast pointer has already checked it before
                    # move both pointers
                    else:
                        self.matrix[slow+1][j], self.matrix[fast][j] = self.matrix[fast][j], self.matrix[slow+1][j]
                        slow += 1
                        fast += 1
        # add a new 2 to the matrix after each move
        self.add_2()
    
    # same logic as move_up, except iterating the j coordinate backward
    def move_down(self):
        for j in range(4):
            fast = 2
            slow = 3
            while fast > -1:
                if self.matrix[fast][j] == 0:
                    fast -= 1
                else:
                    if self.matrix[slow][j] == 0:
                        self.matrix[slow][j], self.matrix[fast][j] = self.matrix[fast][j], self.matrix[slow][j]
                        fast -= 1
                    elif self.matrix[slow][j] == self.matrix[fast][j]:
                        self.matrix[slow][j] += self.matrix[fast][j]
                        self.matrix[fast][j] = 0
                        slow -= 1
                        fast -= 1
                    else:
                        self.matrix[slow-1][j], self.matrix[fast][j] = self.matrix[fast][j], self.matrix[slow-1][j]
                        slow -= 1
                        fast -= 1
        self.add_2()
    
    # same logic as move_up, except iterating the i coordinate
    def move_left(self):
        for i in range(4):
            fast = 1
            slow = 0
            while fast < 4:
                if self.matrix[i][fast] == 0:
                    fast += 1
                else:
                    if self.matrix[i][slow] == 0:
                        self.matrix[i][slow], self.matrix[i][fast] = self.matrix[i][fast], self.matrix[i][slow]
                        fast += 1
                    elif self.matrix[i][slow] == self.matrix[i][fast]:
                        self.matrix[i][slow] += self.matrix[i][fast]
                        self.matrix[i][fast] = 0
                        slow += 1
                        fast += 1
                    else:
                        self.matrix[i][slow+1], self.matrix[i][fast] = self.matrix[i][fast], self.matrix[i][slow+1]
                        slow += 1
                        fast += 1
        self.add_2()
    
    # same logic as move_up, except iterating the i coordinate backward
    def move_right(self):
        for i in range(4):
            fast = 2
            slow = 3
            while fast > -1:
                if self.matrix[i][fast] == 0:
                    fast -= 1
                else:
                    if self.matrix[i][slow] == 0:
                        self.matrix[i][slow], self.matrix[i][fast] = self.matrix[i][fast], self.matrix[i][slow]
                        fast -= 1
                    elif self.matrix[i][slow] == self.matrix[i][fast]:
                        self.matrix[i][slow] += self.matrix[i][fast]
                        self.matrix[i][fast] = 0
                        slow -= 1
                        fast -= 1
                    else:
                        self.matrix[i][slow-1], self.matrix[i][fast] = self.matrix[i][fast], self.matrix[i][slow-1]
                        slow -= 1
                        fast -= 1
        self.add_2()