
print ('Welcome to the Combinator!', '\n')
num_of_lists = int(input ('How many lists of items should I run through?'))

user_data = []
for list_index in range(num_of_lists):
    string_input = input('Enter items in list separated by comas:')
    user_data.append(string_input.split(',')) #a list of lists

print ('Your lists are:')
for user_list in user_data:
    print (user_list)

combinations = []   #Stores the list of results
# A recursive function to permutate through all the items in the lists
# and add them to the results
def combine (terms, accum): #terms is a list of lists, accum is a list
    last = (len(terms) == 1)
    for i in range(len(terms[0])):
        item = []
        item.extend(accum)
        item.append(terms[0][i])
        if last:
            combinations.append(item)
        else:
            combine(terms[1:], item)

print('Combining items... ... ...')
combine (user_data, [])
print ('Created', len(combinations), 'possible combinations:')
for combination in combinations:
    print (combination)
