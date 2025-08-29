# This is a comment that will be ignored
'''
This is a multi-line comment
'''

def main():
    helloWorld()
    printSomething("something")
    printSomething("something","other")
    sameLineAsFxn("weird")
    includesSemiolonSyntax("semicolon")
    moreSemicolonSyntax("more semicolon")
    thisOneHasASpaceIndent("space indent")
    weirdComment("weird comment")

def helloWorld():
    print("hello")

def printSomething(something):
    print(something)
    if something == "something":
        print("it's something!")
    print("and then back to this block")

def printSomething(something, other):
    print(something + " or " + other)
    '''comment''' ; print("after comment")

def sameLineAsFxn(something): something = something + " another thing" ; print(something)

def includesSemiolonSyntax(something):
    print(something + " more weird things") ; print("and again")
    print("done with weird syntax")

def moreSemicolonSyntax(something):
    print(something + " more weird things"); print("and again") ; print("next is a new line")
    print("done with weird syntax")

def thisOneHasASpaceIndent(something):
 print(something + " started with a space")

def weirdComment(something): # this comment should be ignored ; print("not printed")
    print(something + " should be printed")  
    '''
    This is a multi-line string that is not assigned to a variable
    It should be ignored by the parser'''
    print("done with weird comment")

if __name__ == "__main__":
    main()