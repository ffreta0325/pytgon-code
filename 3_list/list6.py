#現在想進行 4 位數字的 Bulls and Cows 遊戲, 請你寫一個函數 result(answer, guess) 回傳 guess 和 answer 的比較結果.

#例如: result('1234', '4321') 回傳 '0A4B', result('4657', '9658') 回傳 '2A0B', result('9876', '6879') 回傳 '2A2B'
def result(answer,guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
    
       for idx_gue, val_gue in enumerate(guess):

           if idx_ans==idx_gue:
              if val_ans==val_gue:
                 A+=1
              else:
                 B+=1
           
           #print(idx_ans, val_ans, idx_gue, val_gue)
           #print(str(A)+"A"+str(B)+"B")
    return str(A)+"A"+str(B)+"B"

print(result('1234','4321'))
print(result('4657','9658'))
print(result('9876','6879'))

    #for idx_ans, val_ans in enumerate(answer):
    #if answer[idx_ans] == guess[idx_ans]
    #A+=1
    #elsf val_ans in guess:
    #B+=1