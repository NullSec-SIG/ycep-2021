CONFIG = {"FLAG": "{4mating-is_d4ngeros}"}
cont = True
blacklist = ['recv', 'stdout', 'exec', 'eval', 'init', 'hamster', 'i love blacklisting']

class Person(object):
    
    def __init__(self, name, profile):
        self.name = name
        self.profile = profile
        
                

print(' _               _             \n\
| |             | |                \n\
| |__   __ _  __| | __ _  ___ _ __ \n\
|  _ \ / _` |/ _` |/ _` |/ _ \ |__|\n\
| |_) | (_| | (_| | (_| |  __/ |   \n\
|_.__/ \__,_|\__,_|\__, |\___|_|   \n\
                    __/ |          \n\
                   |___/           \n')

while cont:
    choice = input('This is the Beta for Badger v0.4a!\n1) Create profile\n2) View badge\n3) Patch Notes\n4) Exit\n')
    print()
    if choice == '1':
        name = input("Enter name: ")
        print('Welcome {}! Enter a short biography for your profile:'.format(name))
        profile = input()
        create = True
        person = Person(name, profile)

        
    elif choice == '2':
         #ry:
             print('╔════════════════════════════════════════════════')
             print('║Name : {}'.format(person.name).format(person=person))
             print('║Bio  : {}'.format(person.profile).format(person=person))
             print('╚════════════════════════════════════════════════')
         #except:
             #print('An error occured!')
    elif choice == '3':
        print('Update 0.4a:')
        print('The choice to format your profile has been added!\n')
        print('Example profile: Hi! Im {person.name}, nice to meet you!\n')
        print('Further implementations coming soon!')
        
    elif choice == '4':
        cont = False
    else:
        print('Invalid Choice!')

    print()
    

