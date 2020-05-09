import shelve


try:
    db = shelve.open('pickle.db', writeback=True)
    db['actions'] =             # create new key or update key with new value
    actions = db['actions']     # Get local VOLATILE copy of key
    k_flag = 'action' in db     # Check if key is in DB dictionary
except IOError:
    print(f'Error opening pickle.db file! Ensure it is actually there and not currently open by something')
except KeyError as err:
    print(f'Object: ({err}) not found. DB file is likely empty')
finally:
    db.close()


def getDatabase():
    try:
        db = shelve.open('pickle.dbm')
        print(db.keys()) 
        actions = db['actions'] 
    except:
        print(f'error!')
    finally:
        db.close()


def createDatabase(name):
    db = shelve.open('pickle.db')
    db['actions'] = [
        {
            'click_x': '244',
            'click_y': '299'
        },
    ]