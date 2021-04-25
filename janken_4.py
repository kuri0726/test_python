import random



class Jnaken:
    hands = ['グー','チョキ','パー']
    def __init__(self,number):
        self.n = number
        self.hands[self.n]

    def pon(self):
        return self.hands[self.n]
       
    def __lt__(self,c2):
        if self.n < c2.n:
            return True          

    def __gt__(self,c2):
        if self.n > c2.n:
            return True
    def __repr__(self):
        return self.hands[self.n]
        
class Player:
    def __init__(self,name):
        self.name = name
        self.win = 0

    def __repr__(self):
        return self.name

class Game:
    def __init__(self):
        name1 = input('プレイヤー１の名前')
        name2 = input('プレイヤー２の名前')
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def draw(self,p1n,p1h,p2n,p2h):
        xx = '{} は {} を、{} は {} を出しました！'
        xx = xx.format(p1n,p1h,p2n,p2h)
        print(xx)

    def win_lose(self,p1n,p1w,p2n,p2w):
        ww = '現在 {} は {}勝、{} は {}勝'
        ww = ww.format(p1n,p1w,p2n,p2w)
        print(ww)
    
    def play_game(self):
        while 0<= self.p2.win - self.p1.win <= 2 or 0<= self.p1.win - self.p2.win <= 2:
            print('\n')
            print('じゃんけんをはじめます！')
            print('3勝差付けた方が勝ち！！')
            p1n = self.p1
            p2n = self.p2
            p1w = self.p1.win
            p2w = self.p2.win
            self.win_lose(p1n,p1w,p2n,p2w)
            x = random.randint(0,2)
            number = int(input('好きな手を入力してください（０：グー　１：チョキ　２：パー）:'))
            janken_1 = Jnaken(number)
            janken_2 = Jnaken(x)
            p1h = janken_1
            p2h = janken_2
            self.draw(p1n,p1h,p2n,p2h)
                        
            if number == 0 and x == 2:
                print('このラウンドは '+str(self.p2) +' の勝ち！')
                self.p2.win += 1
            if number == 1 and x == 0:
                print('このラウンドは '+str(self.p2) +' の勝ち！')
                self.p2.win += 1
            if number == 2 and x == 1:
                print('このラウンドは '+str(self.p2) +' の勝ち！')
                self.p2.win += 1
            if number == 0 and x == 1:
                print('このラウンドは '+str(self.p1) +' の勝ち！')
                self.p1.win += 1
            if number == 1 and x == 2:
                print('このラウンドは '+str(self.p1) +' の勝ち！')
                self.p1.win += 1
            if number == 2 and x == 0:
                print('このラウンドは '+str(self.p1) +' の勝ち！')
                self.p1.win += 1
            if number == 0 and x == 0:
                print('引き分け！')
            if number == 1 and x == 1:
                print('引き分け！')
            if number == 2 and x == 2:
                print('引き分け！')
                
        if self.p2.win > self.p1.win:
            print('\n')
            print('この試合 '+str(self.p2) +' の勝ち！')
        if self.p1.win > self.p2.win:
            print('\n')
            print('この試合 '+str(self.p1) +' の勝ち！')


   
game = Game()
game.play_game()
