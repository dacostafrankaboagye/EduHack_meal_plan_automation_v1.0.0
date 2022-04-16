


with open('db.txt', 'r') as db:
    for i in db.readlines():
        a = i.strip()
        if bool(a) == True:
            with open('formattedDB.txt', 'a') as fdb:
                fdb.write(a)
                fdb.write('\n')
    
