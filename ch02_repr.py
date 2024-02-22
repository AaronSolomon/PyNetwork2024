# {!r} Convert with repr()
s = "NKUST"
t = "I'm fine."
u = "single quote(') and double quote(" + '"' + ")"
n = 2018
fmt = "{0}\n{0!r}"
print( fmt.format(s) )
print( fmt.format(t) )
print( fmt.format(u) )
print( fmt.format(n) )
