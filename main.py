
#length is the minimum length of seq1 or seq2 after shifting either of them (and inserting "-" in the shifted cells)
def find_match(seq1,seq2,length):
    
    match = 0
    for i in range(0,length):
        if seq1[i] == seq2[i]:
            match += 1

    return match

#length is the minimum length of seq1 or seq2 after shifting either of them (and inserting "-" in the shifted cells)
def find_chain(seq1,seq2,length):
    
    longest_chain = 0
    match = 0
    for i in range(0,length):
        if seq1[i] == seq2[i]:
            match += 1
            longest_chain = max(longest_chain, match)
        else:
            match = 0

    return longest_chain

def find_match_by_shifting_seq1(seq1, seq2, max_shift, chain = False):
    max_score = 0
    for shift in range(0,max_shift+1):
        shifted_seq1 = '-' * shift + seq1

        smaller_length = min(len(shifted_seq1), len(seq2))
        
        #chain or subsequence?
        if chain:
            score = find_chain(shifted_seq1,seq2,smaller_length)    
        else:
            score = find_match(shifted_seq1,seq2,smaller_length)
        max_score = max(max_score, score)

        print(f'For shift {shift}, score: {score}')
    return max_score

def find_match_by_shifting_seq2(seq1, seq2, max_shift, chain = False):
    max_score = 0
    for shift in range(0,max_shift+1):
        shifted_seq2 = "-" * shift + seq2

        smaller_length = min(len(shifted_seq2), len(seq1))
        
        #chain or subsequence?
        if chain:
            score = find_chain(shifted_seq2,seq1,smaller_length)
        else:
            score = find_match(shifted_seq2,seq1,smaller_length)
        max_score = max(max_score, score)

        print(f'For shift {shift}, score: {score}')
    return max_score

def file_input():
    sequence_one = ''
    sequence_two = ''

    while len(sequence_one) == 0 or len(sequence_two) == 0:
        print('')
        file_name = input("Please input the filename (that contains the two sequences in two lines): ")
        file_name.strip() #strip trailing and leading whitespaces

        try:
            with open(file_name,"r") as file:
                lines = file.readlines()
                sequence_one = lines[0][:-1] #trim the new line
                sequence_two = lines[1][:-1] #trim the new line
                #find_match_by_shifting_seq2(sequence_one,sequence_two,max_shift,chain=True)
        except FileNotFoundError:
            print(f"The file {file_name} doesn't exist!")

    print('')
    return sequence_one, sequence_two

def console_input():
    print('')
    sequence_1 = input("Enter the first sequence: ")
    sequence_2 = input("Enter the second sequence: ")
    print('')

    return sequence_1, sequence_2

def menu():
    print("Hello! Welcome to DNA Sequence Matching Program :-)")
    print("First, start by entering the maximum no. of shifts you would want the sequences to have.")
    print('')

    max_shift = -1

    while max_shift < 0:
        try:
            max_shift = int(input("Enter a positive number of your choice as the maximum shift: "))
            if max_shift <= 0:
                print('Max shift count must be positive!')
        except ValueError:
            print('Max shift count must be an integer number!')       
        
    
    print('')
    print("Now, let me know How do you want to input the pair of sequence?")
    print('')

    input_choice = -1

    while input_choice!=1 and input_choice!=2:
        try:
            input_choice = int(input("Enter 1 for console input, 2 for file input: "))
            if input_choice!=1 and input_choice!=2:
                print('The options are 1 or 2!')
        except ValueError:
            print('Entered value is not an integer number!')       


    if input_choice == 1:
        sequence1, sequence2 = console_input() 
    else:
        sequence1, sequence2 = file_input()

    return max_shift, sequence1, sequence2

def main():
    max_shift, sequence_one, sequence_two = menu()
    
    print("The pair of sequence:")
    print(sequence_one)
    print(sequence_two)
    print("---------------------")

    find_match_by_shifting_seq1(sequence_one,sequence_two,max_shift,chain=True)
    #find_match_by_shifting_seq2(sequence_one,sequence_two,max_shift,chain=True)
    
main()