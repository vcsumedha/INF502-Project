
def find_match(seq1,seq2,length):
    #this function is called with same lengthed sequence
    match = 0
    for i in range(0,length):
        if seq1[i] == seq2[i]:
            match += 1

    return match

    limit = min(len(seq1),len(seq2))

def find_match_by_shifting_seq1(seq1, seq2, max_shift):
    max_match = 0
    for shift in range(0,max_shift+1):
        shifted_seq1 = " " * shift + seq1

        smaller_length = min(len(shifted_seq1), len(seq2))
        match = find_match(shifted_seq1,seq2,smaller_length)

        print(f'For shift {shift}, match found: {match}')

def find_match_by_shifting_seq2(seq1, seq2, max_shift):
    max_match = 0
    for shift in range(0,max_shift+1):
        shifted_seq2 = " " * shift + seq2

        smaller_length = min(len(shifted_seq2), len(seq1))
        match = find_match(shifted_seq2,seq1,smaller_length)

        print(f'For shift {shift}, match found: {match}')

def main():

    max_shift = -1

    while max_shift < 0:
        try:
            max_shift = int(input("How much maximum shift you want? "))
        except ValueError:
            print('Please provide integer number as the maximum shift count')
            continue
        
        if max_shift < 0:
            print('Please provide a positive number as the maximum shift count')
    
    try:
        filename = 'input.txt'
        with open(filename,"r") as file:
            lines = file.readlines()
            sequence_one = lines[0][:-1] #trim the new line
            sequence_two = lines[1][:-1] #trim the new line
            print(sequence_one)
            print(sequence_two)

            #find_match_by_shifting_seq1(sequence_one,sequence_two,max_shift)
            find_match_by_shifting_seq2(sequence_one,sequence_two,max_shift)
    except FileNotFoundError:
        print(f"Please make sure the file {filename} exists in the same directory")


    

main()