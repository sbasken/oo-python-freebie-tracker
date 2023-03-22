import ipdb
from lib import *

#code here
apple = Company( 'Apple, Inc.', 1976 ) 
ibm = Company( 'IBM', 1911 )
google = Company( 'Google Search', 1998 )

adam = Dev( 'Adam' )
emily = Dev( 'Emily' )
joe = Dev( 'Joe' )

f1 = Freebie( emily, apple, "sticker", 3 )
f2 = Freebie( adam, ibm, "pen", 5 )
f3 = Freebie( emily, google, "magnet", 6 )

ipdb.set_trace()
