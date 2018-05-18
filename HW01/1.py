a = -3 + 4 * 15
print('')
print('a = -3 + 4 * 15')
print('a', str(a), type(a))

b = "a + 3" * 2
print('')
print('b = "a + 3" * 2')
print('b', str(b), type(b))

c = ( int( "3" ) - a ) ** 2 / ( 1.5 - 1.6e3 )
print('')
print('c = ( int( "3" ) - a ) ** 2 / ( 1.5 - 1.6e3 )')
print('c', str(c), type(c))

d = b[ -1] * [ int( "2" ) , 1.1 , 3 ] [ 2 ]
print('')
print('d = b[ -1] * [ int( "2" ) , 1.1 , 3 ] [ 2 ]')
print('d', str(d), type(d))

e = float( str( 15671 * 16.3 ) [6 -6:6] + "2e2 " )
print('')
print('e = float( str( 15671 * 16.3 ) [6 -6:6] + "2e2 " )')
print('e', str(e), type(e))

f = id( e ) % 3 and True
print('')
print('f = id( e ) % 3 and True')
print('f', str(f), type(f))

b , h = ( f - 2 , not bool( a ) )
print('')
print('b , h = ( f - 2 , not bool( a ) )')
print('b', str(b), type(b))
print('h', str(h), type(h))

g = not h and True and ( ( ( not bool( 0 ) ) ) )
print('')
print('g = not h and True and ( ( ( not bool( 0 ) ) ) )')
print('g', str(g), type(g))

RESULT = """
a = -3 + 4 * 15
a 57 <class 'int'>

b = "a + 3" * 2
b a + 3a + 3 <class 'str'>

c = ( int( "3" ) - a ) ** 2 / ( 1.5 - 1.6e3 )
c -1.8242101970597435 <class 'float'>

d = b[ -1] * [ int( "2" ) , 1.1 , 3 ] [ 2 ]
d 333 <class 'str'>

e = float( str( 15671 * 16.3 ) [6 -6:6] + "2e2 " )
e 255437200.0 <class 'float'>

f = id( e ) % 3 and True
f True <class 'bool'>

b , h = ( f - 2 , not bool( a ) )
b -1 <class 'int'>
h False <class 'bool'>

g = not h and True and ( ( ( not bool( 0 ) ) ) )
g True <class 'bool'>
"""
