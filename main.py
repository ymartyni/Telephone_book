db  = {123 : 'test', 555 : 'new'}

while True:
    print '-------------------'
    print '1.Create new phone'
    print '2.Search by phone'
    print '3.Search by name'
    print '4.Delete by phone'
    print '5.Delete by name'
    print '6.Show all'
    print '0.Exit'
    print '--------------------'

    choice = int (raw_input())

    if choice == 1:
        print 'Creating new phone in phonebook.....'
        name = raw_input('Please type name: ')
        phone = int(raw_input('Please type phone: '))
        db[phone] = name
        print "{} : {}".format(phone,name)

    elif choice == 2:
        phone = int(raw_input('serch number'))
        for key, value in db.items():
            if phone == key:
                print "{} : {}".format(key, value)

    elif choice == 3:
        name = raw_input('serch by name')
        for key, value in db.items():
            if name == value:
                print "{} : {}".format(key, value)


    elif choice == 4:
        phone = int(raw_input('delete number '))
        for key, value in db.items():
            if phone == key:
                print "{} : {}".format(key, value)
                del db[key]

    elif choice == 5:
        name = raw_input('Please write name for delete: ')
        for key, value in db.items():
            if name == value:
                print "{} : {}".format(key, value)
                del db[key]
        #del db[key]
        #print '{}: Name was deleted'.format(name)
        #print 'Name: ' + name + ' was deleted'

    elif choice == 6:
        for key, value in db.items():
            print "{} : {}".format(key, value)
    # db  = {
    # 'test': 123,
    # 'new' : 555,
    # '123' : 'Yura'}

    elif choice == 0:
            break





