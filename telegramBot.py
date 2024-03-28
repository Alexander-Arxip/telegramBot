












print("НОВОЕ ОБНОВЛЕНИЕ ЧТО БЫ ГИТ ХАБ УВИДЕЛ")

print("ЭТОТ ТЕКСТ ДОБАВЛЕН В ГИТ ХАБЕ ЧТО БЫ ОН ПЕРЕДАЛСЯ НА ЛОКАЛЬНЫЙ МОЙ ПАЙ ЧАРМ")

print("это ТРЕТЬЕ ОБНОВЛЕНИЕ-ИЗМЕНЕНИЕ КОДА в гит хабе. ")

print("это  ЧЕТВЕРТОЕ изменение кода В МОЕМ пай чарме. Потом Сделать Пушь что бы сервер гит хаб увидел ")

print(" это ПЯТОЕ изменение кода в пай чарме. Его надо передать в новую ветку ветка_1 на гит хаб ")

print(" это ШЕСТОЕ измение кода. Создал в пай чарме ВЕТКУ и передаю из нее на гит хаб ")


print('это ИЗМЕНЕНИЕ вноситься из ВИЗУАЛ СТУДИО на сервер гит хаб')

print('это изменение вносится в гит хабе и переноситься НА МОЙ ВИЗУАЛ СТУДИО ')

"""



# функция которая рисует доску 3х3.
def draw_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        print('-------')

      # функция которая позволяет пользователю делать ход.
def ask_and_make_move(player, board):
    x,y = ask_move(player, board)
    make_move(player, board, x, y )
    '''
    x,y = input(f"{player}, enter x and y coordinati (e.g. 0 0): " ).strip().split()
    x,y = int(x), int(y)
    if (0 <= x <=2) and (0<= y <= 2) and (board[x][y] ==  " "):
        board[x][y] = player
    else:
        print('Eto mesto zanato. Poprobyiye eshe raz.')
        ask_and_make_move(player,board)
    '''

      # функция позволяет пользователю ввести координаты хода
def ask_move(player, board):
    x,y = input(f"{player}, enter x and y coordinati (e.g. 0 0): " ).strip().split()
    x, y = int(x), int(y)
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return ( x,y )
    else:
        print('Kletka zanata. Vvedite koordinatu esho raz.')
        return ask_move(player, board)

       # функция позволяет пользователю делать ход
def make_move(player, board, x,y):
    if board[x] [y] != "  ":
        print('Izvenite. Kletka zanata')
        return False
    board[x] [y] = player
    return True

   # функция проверяющая стал ли ход выйгрышным.

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player ]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board [0] [0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return  True
    return False

     # функция которая управляет ходом игры.

def tic_toe():
    while True:                  # цикл (Пока) -> Тру, значит -> бесконечный цикл игры
        board = [ [ ' ' for i in range(3)] for j in range (3) ]
        player = 'X'
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):    # проверка выйграли ли игрок
                print( f"{player} you Victory!" )
                break
            tie_game = False                # проверка на вариант -- ничья
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = True
            if not tie_game:
                break
            player = '0' if player == 'X' else 'X'
        resrart = input('Hotite eshe raz sigrat ???  (y/n) ')
        if resrart.lower() != 'y':
            break


"""
















