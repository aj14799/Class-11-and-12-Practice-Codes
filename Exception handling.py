#Exception Handling
class myError(Exception):
    pass
MyError1 = myError("Negative making not allowed")
MyError2 = myError("Maximum marks are 100")
try:
    marks = float(raw_input("Enter marks :"))
    if marks < 0:
        raise MyError1
    elif marks > 100:
        raise MyError2
    elif marks > 40:
        print "Promoted to next class"
    else:
        print "Your re-examination is scheduled"

except myError, e:
    print e.message, "; Marks entered:", marks

    
    
    
