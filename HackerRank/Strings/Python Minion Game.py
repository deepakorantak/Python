def minion_game(string):
    # your code goes here

    if len(string) > 0 and len(string) <= 10**6:

        vowels = {'A', 'I', 'O', 'U', 'E', 'a', 'i', 'o', 'u', 'e'}
        stuart_score = 0
        kevin_score = 0

        for i in range(len(string)):
            if string[i] in vowels:
                kevin_score += len(string) - i
            else:
                stuart_score += len(string) - i   
        
        if stuart_score > kevin_score:
            result = 'Stuart '+ str(stuart_score)
        elif kevin_score > stuart_score:
            result = 'Kevin '+ str(kevin_score)
        else:
            result = 'Draw'

        print(result)    



if __name__ == '__main__':
    s = input()
    minion_game(s)