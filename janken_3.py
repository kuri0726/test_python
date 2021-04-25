print('じゃんけんをはじめます！')
hands = ['グー','チョキ','パー']

import random


while True:
    number = int(input('好きな手を入力してください（０：グー　１：チョキ　２：パー）:'))
    x = random.randint(0,2)
    if 0 <= number <=2:
        print('あなたが出した手は「'+hands[number]+'」です。')
        print('相手は「'+hands[x]+'」を出しました。')
        if x == 0 and number == 2:
            print('あなたの勝ち！！！！')
            print('\n')
        elif x == 1 and number == 0:
            print('あなたの勝ち！！！！')
            print('\n')
        elif x == 2 and number == 1:
            print('あなたの勝ち！！！！')
            print('\n')
        elif x == number:
            print('あいこ！！！！')
            print('\n')
        else:
            print('あなたの負け！！！！')
            print('\n')
    else:
        print('0~2の整数を入力してください')
        print('\n')
