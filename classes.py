class Point: #class name wit capital letter
    # defining functions belonging to a class
    def draw(self):
        print('draw')

# point = Point()
# point.draw()


#constructor  and instance methods
class MyPoint: 
    default_color = 'blue' # class attribute, the same for all instances of a class
    #magic method, constructor, executed when we definie new poin object
    #self is a reference to current object
    def __init__(self, x, y):
        self.x = x #setting x attribute, can be different for every instance
        self.y = y #setting y instance attribute

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

# point = MyPoint(1,2)
"""
point.  >> you can pick draw method as well as attribute x and y

"""
# print(point.x) # zwraca 1

# point.z = 10 # you can definie another atributes outside, it will be shared along all instances



#class methods
class MyPoint2: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    @classmethod #decorator
    def zero(cls): #definig class method
        return cls(0, 0) # initial values like MyPoint(0,0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point2 = MyPoint2.zero()
print(point2)
point2.draw()

'''
Magic methods __nazwa__

in order to compare if objects are the same, eg:
point3 = MyPoint2(1,2)
point4 = MyPoint2(1,2)

def __eq__(sel, other):
    return self.x == other.x and self.y == self.y

in order to check if point3 > point4:

def __gt__(sel, other):
    return self.x > other.x and self.y > self.y

aritmatic operators:

def __add__(self, other):
    return My.point(self.x+ other.x, self.y+ other.y)

'''

'''
creating custom container
'''
class TagCloud:

    # we are using buil-in data structure: dictionaty
    def __init__(self):
        self.__tags = {}

    #checking if we have tag if not setting it to 1
    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) +1
    
    # to gen number by writing cloud["python"]
    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(), 0)
    
    # to set number by writing cloud["python"] = 5
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    # to get number of items
    def __len__(self):
        return len(self.__tags)
    #  to make it iterable
    def __iter__(self):
        iter(self.__tags)

cloud = TagCloud()
cloud.add('Python')
cloud.add('python')
cloud.add('Python')
print(cloud["python"])
print(cloud.__tags)