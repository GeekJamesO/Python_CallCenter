# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you
# need a way to track that call. One of your program's requirements is to store
# calls in a queue while callers wait to speak with a call center employee.
#
# You will create two classes. One class should be Call, the other CallCenter.
#
# Call Class
# Create your call class with an init method. Each instance of Call() should have:
#     Attributes:
#         unique id
#         caller name
#         caller phone number
#         time of call
#         reason for call
#     Methods:
#         display: that prints all Call attributes.
#
# CallCenter Class
# Create your call center class with an init method. Each instance of CallCenter()
# should have the following attributes:
#     Attributes:
#         calls: should be a list of call objects
#         queue size: should be the length of the call list
#     Methods:
#         add: adds a new call to the end of the call list
#         remove: removes the call from the beginning of the list (index 0).
#         info: prints the name and phone number for each call in the queue as well as the length of the queue.
#
# You should be able to test your code to prove that it works. Remember to build
# one piece at a time and test as you go for easier debugging!
#
# Ninja Level: add a method to call center class that can find and remove a call
# from the queue according to the phone number of the caller.
#
# Hacker Level: If everything is working properly, your queue should be sorted
# by time, but what if your calls get out of order? Add a method to the call
# center class that sorts the calls in the queue according to time of call in
# ascending order.

class Call:
    def __init__(self, uniqueId, callerName, callerPhoneNumber, timeOfCall, reasonForCall):
        self.uniqueId = uniqueId
        self.callerName = callerName
        self.callerPhoneNumber = callerPhoneNumber
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall
    def display(self):
        print "    unique id:       {0}".format(self.uniqueId)
        print "    caller name:     {0}".format(self.callerName)
        print "    caller phone #:  {0}".format(self.callerPhoneNumber)
        print "    time of call:    {0}".format(self.timeOfCall)
        print "    reason for call: {0}".format(self.reasonForCall)
        return self;
# #testCode
# newcall = Call(123,"Joe Blow", "(425) 555-1212", "December 31, 1999 23:59:59.000000", "Drunken 'happy..  new.. yarg...'" )
# newcall.display()

class CallCenter:
    def __init__(self):
        self.calls = []
        self.queueSize = 0

    def add(self, newCall):
        self.calls.append(newCall)
        self.queueSize += 1
        return self

    def find(self, phone):
        index = 0;
        for aCall in self.calls:
            if (aCall.callerPhoneNumber == phone):
                return index
            else:
                pass;
            index += 1
        return None

    def info (self):
        print "Call Center information:"
        for aCall in self.calls:
            aCall.display()
            print "-----------------------"
        print "There are {0} call(s) in the queue.".format(self.queueSize)
        return self

    def remove(self, location=0):
        if self.queueSize < 1:
            return None
        else:
            oldValue = self.calls.pop(location)
            self.queueSize -= 1
            return oldValue
    def removeByPhoneNumber(self, PhoneNumber):
        index = self.find(PhoneNumber)
        if (None != index):
            return self.remove(index)
        else:
            return None

    # def sortByDate(self):
    #     this.calls.sorted(key=lambda, key=attrgetter('timeOfCall'))
    #     return self;

newcall1 = Call(123,"Abe Ache", "(425) 555-1111", "December 31, 1999 23:59:59.000000", "Drunken 'happy..  new.. yarg...'" )
newcall2 = Call(123,"Brownie Blown", "(425) 555-2222", "January 1, 12000 09:00:00.000000", "Abe is passed out on my deck." )
newcall3 = Call(123,"Chuck Clucker", "(425) 555-3333", "December 30, 1999 10:00:00.000000", "Need new years cocktails for Abe." )
newcall4 = Call(123,"Duke Dracko", "(425) 555-4444", "January 01, 2000 12:00:00.000000", "See, I told you the Y2k thing was a hoax." )
cc = CallCenter().add(newcall1).add(newcall2).add(newcall3).add(newcall4).info()

todo = cc.remove()
cc.info()
todo = cc.removeByPhoneNumber("(425) 555-3333")
cc.info()
