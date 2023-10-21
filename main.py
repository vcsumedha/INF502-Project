
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
            
            print("The pair of sequence:")
            print(sequence_one)
            print(sequence_two)
            print("---------------------")

            find_match_by_shifting_seq1(sequence_one,sequence_two,max_shift,chain=True)
            #find_match_by_shifting_seq2(sequence_one,sequence_two,max_shift,chain=True)
    except FileNotFoundError:
        print(f"Please make sure the file {filename} exists in the same directory")


    

main()