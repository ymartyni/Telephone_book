# 1. create new phone
# 2. search by phone
# 3. search by name
# 4. delete by phone
# 5. delete by name
# 6. show all

db  = {}
#dictionary
while True:
    print '---------------------------------'
    print '1. Create new phone'
    print '6. Show all'
    print '---------------------------------'

    choice = int(raw_input())

    if choice == 1:
        print 'Creating new phone in phonebook...'
        name = raw_input('Please type name: ')
        phone = int(raw_input('Please type phone'))
        db[name] = phone
        print "{} : {}".format(name, phone)

    elif choice == 6:
        for key, value in db.items():
            print "{} : {}".format(key, value)







