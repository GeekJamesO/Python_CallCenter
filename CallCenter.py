# Assignment: Call Center


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
        self.queueSize += 1
        for index in range(0, len(self.calls)):
            if self.calls[index].timeOfCall > newCall.timeOfCall:
                self.calls.insert(index, newCall)
                return self
        self.calls.append(newCall)
        return self

    def find(self, phone):
        for index in range(0,len(self.calls)):
            if (self.calls[index].callerPhoneNumber == phone):
                return index
        return None

    def info (self):
        print "  -- Call Center information: --"
        for aCall in self.calls:
            aCall.display()
        print "  --------------------------"
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

newcall1 = Call(123,"Abe Ache", "(425) 555-1111", "December 31, 1999 23:59:59.000000", "Drunken 'happy..  new.. yarg...'" )
newcall2 = Call(124,"Brownie Blown", "(425) 555-2222", "January 1, 12000 09:00:00.000000", "Abe is passed out on my deck." )
newcall3 = Call(125,"Chuck Clucker", "(425) 555-3333", "December 30, 1999 10:00:00.000000", "Need new years cocktails for Abe." )
newcall4 = Call(126,"Duke Dracko", "(425) 555-4444", "January 01, 2000 12:00:00.000000", "See, I told you the Y2k thing was a hoax." )
print ("Add to call center with 4 calls.")
cc = CallCenter().add(newcall1).add(newcall2).add(newcall3).add(newcall4).info()

removedEntry = cc.remove()  #defaults to position zero..
print "remove first entry : ", removedEntry.callerName
cc.info()
todo = cc.removeByPhoneNumber("(425) 555-2222")
print "Remove a call by the phone number.  (425) 555-2222  -->", todo.callerName
cc.info()
