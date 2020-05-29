
import numpy as np

iMax= 5
jMax = 5
i_index = 1
j_index = 1
moveNumber = 0
board = np.zeros((iMax, jMax), dtype=int)


def nextMove():
    def getAvailableMove():
        return (true, )

    pass


def showBoard():
    for i in range(iMax):
        for j in range(jMax):
            print(board[i][j], end='')
        print('\n')


if __name__ == "__main__":

    answer = input('Do you want to set the initial position (y/n (empty): ')
    if answer.lower() == 'y':
        iTmp = input('Please enter start position in row (i): ')
        jTmp = input('Please enter start position in column (j): ')
        try:
            if not (1 <= int(iTmp) <= iMax and 1 <= int(jTmp) <= jMax):
                print('Sorry wrong position(s). starting from 1,1')
            else:
                i_index = iTmp
                j_index = jTmp
        except Exception as e:
            print('Sad, error in data type. Aborting')
            exit(-1)
    if nextMove():
        moveNumber += 1
        showBoard()
    else:
        if moveNumber == iMax * jMax:
            print('Mission completed')
        else:
            print('Cannot move more, mission fails')

