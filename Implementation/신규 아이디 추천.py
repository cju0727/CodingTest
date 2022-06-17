import re

def solution(new_id):
    #print(new_id)
    
    #1
    new_id = new_id.lower()
    
    #2
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    
    #3
    new_id = re.sub('\.{2,}', '.', new_id)

    #4
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    
    #5
    if len(new_id) == 0:
        new_id = "a"
    
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    
    #7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
        
    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))