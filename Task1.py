try :
    marks={'John': 85,'Smith': 92,'Emma': 78, 'Noah': 88, 'Olivia': 95, 'Jmaes': 74, 'Taylor': 91 }
    a=input('Enter the student\'s name: ')
    print(a,'\'s marks: ',marks[a],sep="")
except KeyError:
    print('Student not found.')