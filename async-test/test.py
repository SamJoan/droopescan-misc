from twisted.internet import reactor, defer
from twisted.web.client import getPage

global err_count
err_count = 0
def printPage(page):
    print 'gotresult'

def printError(err):
    global err_count
    err_count += 1
    print err

jobs = []
for i in range(1000):
    jobs.append(getPage('http://crp.droope.org/?a').addCallbacks(printPage,
                                          printError))

def done(ignored):
    reactor.stop()
defer.gatherResults(jobs).addCallback(done)

reactor.run()

print(err_count)
