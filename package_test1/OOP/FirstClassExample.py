class Main:
    def __init__(self):
        print("Main constructor called")
        self.members = ['Sparrow', 'Robin', 'Duck']


    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)
    def __str__(self):
        return self.members[0];
