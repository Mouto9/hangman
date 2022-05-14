from numpy import result_type
import random

def hangman():
    #wordはランダム
    word_list = ["Python","Web","HTML","WordPress"]
    random_number = random.randint(0,3)
    word = word_list[random_number]
    #間違えた回数
    wrong = 0
    stages = [  "",
                "_________        ",
                "|                ",
                "|       |        ",
                "|       0        ",
                "|      /|\       ",
                "|      / \       ",
                "                 "
                ]
    #wordのlist化
    rletters = list(word)
    #まだ明かされていないところ
    board = ["_"] * len(word)
    #勝敗
    win = False
    print("ハングマンへようこそ")
    #間違えた回数<ハングマンの絵
    while wrong < len(stages) - 1:
            print("\n")
            msg = "1文字を予想してね："
            char = input(msg)
            #含まれていたらboardを明かす、listも$に変える
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
            else:
                wrong += 1
            #空白を間に挟む
            print(" ".join(board))
            #絵を見せる
            e = wrong + 1
            print("\n".join(stages[0:e]))
            #勝利条件
            if "_" not in board:
                print("win");
                #正解文字
                print(" ".join(board))
                win = True
                break
    #敗北時
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("lose:{}".format(word))

hangman()