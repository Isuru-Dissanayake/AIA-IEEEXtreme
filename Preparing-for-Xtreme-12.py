import math

test = int(input())
sub_to_book = {}
sub_taken = {}
book_data = {}
subjects = []
for cases in range(test):
    data = list(map(str,input().split()))
    book_data[cases] = data
    for i in range(1,len(data)):
        if data[i] in subjects:
            sub_to_book[data[i]].append(cases)
        else:
            sub_to_book[data[i]] = [cases]
            subjects.append(data[i])
            sub_taken[data[i]] = False
time = 0
for i in range(len(subjects)):
    sub = subjects[i]
    if not sub_taken[sub]:
        print (sub)
        books = sub_to_book[sub]
        book_ind = 0
        book_time = math.inf
        for j in range(len(books)):
            if book_time > int(book_data[books[j]][0]):
                book_ind = books[j]
                book_time = int(book_data[books[j]][0])
        print (book_ind)
        sub_read_count = 0
        for j in range(1,len(book_data[book_ind])):
            if sub_taken[book_data[book_ind][j]] == True:
                sub_read_count += 1
            else:
                sub_taken[book_data[book_ind][j]] = True
print (time)
            
            

