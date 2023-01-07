def main():
    question = (input('What is the answer for the Question of Life...? ')).lower().strip()
    if correct_answer(question) is True:
         print('Yes')
    else: 
         print('No')

def correct_answer(x):
    return True if x == '42' or x == 'forty-two' or x == 'forty two' else False


main()