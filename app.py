from flask import Flask, redirect, url_for, render_template, request
from math import floor, tan, pi

def _sieve(limit):
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i, v in enumerate(is_prime) if v]

primes = _sieve(4_000_000)

def split(word): 
    return [char for char in word]

def ispositive(num):
  return num >= 0

def gcf(x, y, z):
	return gcd(gcd(abs(x), abs(y)), abs(z))

def commaremove(mainlist):
  return [intconvert(str(x).replace(",", "")) for x in mainlist]

def intconvert(num):
  try:
    num = float(num)
  except:
    return str(num)
  if num == floor(num):
    return int(num)
  else:
    return float(num)

def modmakestring(lst):
  return "".join(str(x) for x in lst)

def commasgone(string):
  string = string.replace(",", "")
  return string


def nummyhelp(string):
  if string.count(".") > 1 or string.count("-") > 1:
    return False
  return True

def checknum(word):
  numchars = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "-"]
  mylist = split(str(word))
  for i in range(len(mylist)):
    count = 0
    for t in range(len(numchars)):
      if mylist[i] != numchars[t]:
        count += 1
      else:
        count = 0
      if count > (len(numchars) - 1):
        return False
  if nummyhelp(word) == False:
    return False
  return True

def addth(mynum):
  if mynum % 100 in (11, 12, 13):
    return str(mynum) + "th"
  if mynum % 10 == 1:
    return str(mynum) + "st"
  if mynum % 10 == 2:
    return str(mynum) + "nd"
  if mynum % 10 == 3:
    return str(mynum) + "rd"
  return str(mynum) + "th"

def makestring(lst):
  return ", ".join(str(x) for x in lst)

def dashedmakestring(lst):
  return "&".join(str(x) for x in lst)

def removespaces(mylist):
  return [x for x in mylist if x != ""]

def findandchangenums(string):
  number = []
  lists = string.split()
  for i in range(len(lists)):
    if checknum(lists[i]) == True:
      lists[i] = intconvert(commasgone(lists[i]))
      number.append(lists[i])
      lists[i] = str(lists[i])
  return number

def pullnums(string):
  mylist = string.split()
  for i in range(len(mylist)):
    mylist[i] = str(mylist[i])
    quicksplit = split(mylist[i])
    quicknums = []
    for t in range(len(quicksplit)):
      if checknum(quicksplit[t]) == True:
        quicknums.append(quicksplit[t])
    mylist[i] = intconvert(modmakestring(quicknums)) 
  return findandchangenums(makestring(removespaces(mylist)))


def pullclosenums(string):
  numbers = ""
  mylist = split(string)
  for i in range(len(mylist)):
    mylist[i] = str(mylist[i])
    if checknum(mylist[i]) == True:
      numbers = numbers + mylist[i]
    else:
      numbers += " "
  seclist = commaremove(numbers.split())
  retlist = []
  for i in range(len(seclist)):
    if type(seclist[i]) != str:
      retlist.append(seclist[i])
  return retlist

def checkint(num):
  try:
    num = float(num)
  except:
    return False
  if num == floor(num):
    return True
  else:
    return False

def insertcommas(num):
  if checkint(num) == True:
    num = int(num)
  else:
    return str(num)
  if len(split(str(num))) < 4:
    return str(num)
  Negative = True
  if num >= -num:
    Negative = False
  num = abs(num)
  mylist = split(str(num))
  mylist.reverse()
  ret = ""
  for i in range(len(mylist) - 1):
    ret = ret + mylist[i]
    if i % 3 == 2:
      ret += ","
  ret = ret + mylist[len(mylist) - 1]
  theret = split(ret)
  theret.reverse()
  if Negative == False:
    return modmakestring(theret)
  else:
    return "-" + modmakestring(theret)

def sqrt(num):
  return intconvert(num**0.5)

def gcd(a,b):
    return a if not b else gcd(b, a%b)

def onecheck(n):
  if intconvert(n) == 1:
    n = ""
  return n

def zerocheck(n):
  if intconvert(n) == 0:
    n = ""
  return n

def addorsub(num):
  try:
    num = float(num)
  except:
    return "+ " + insertcommas(num)
  if num >= -num:
    return "+ " + insertcommas(intconvert(num))
  if num < -num:
    return "- " + insertcommas(intconvert(abs(num)))

def simpleradicalformat(n):
    if n < -n:
      n = -n
    g = n
    primesfact = []
    primesfact2 = []
    count = 0
    index = 0
    while primes[index] ** 2 <= n:
      while n % (primes[index]**2) == 0:
        n = n // (primes[index]**2)
        primesfact2.append(primes[index]**2)
        primesfact.append(primes[index])
        count = count + 1
      index += 1
    if n != 1 and sqrt(n) == floor(sqrt(n)):
      primesfact2.append(int(n))
      primesfact.append(int(sqrt(n)))
      count = count + 1
    index1 = 0
    coeff = 1
    in_root = g
    while index1 < count:
      in_root = in_root // primesfact2[index1]
      coeff = coeff * primesfact[index1]
      index1 = index1 + 1
    answer = [coeff, in_root, index + 1]
    return answer

def quad(a, b, c):
  a, b, c = intconvert(a), intconvert(b), intconvert(c)
  finret = ""

  d = int((b**2) - (4 * a *c))

  finret += ("\n\n\nThen we can identify the disciminant by doing b² - 4ac\n")
  finret += (insertcommas(b**2) + " - 4(" + insertcommas(a) + ")(" + insertcommas(c) + ")")
  finret += ("\nAnd we get " + insertcommas(d))
  finret += ("\n\n\n")

  if d == 0 and b > -b:
    finret += ("\nBecause, as you can see, the discriminant is zero...")
    finret += ("\nthis is a double root. The answer is -" + str(intconvert(sqrt(c))))
    return finret

  if d == 0 and b < -b:
    finret += ("\nBecause, as you can see, the discriminant is zero...")
    finret += ("\nthis is a double root. The answer is " +  str(intconvert(sqrt(c))))
    return finret

  b = -b

  posorneg = True

  if d < 0:
    v = str("i√")

  if d > 0:
    v = str("√")
    o = float(sqrt(d))
    posorneg = False

  simpleradical = []

  try:
    simpleradical = simpleradicalformat(d)
  except IndexError:
    finret += ("\nAnd sorry this number is a bit too big for us to simplify\nso we will just finish the problem taking the square root of the disciminant\nand solve with the rest of the formula\n")
    if d> 0:
      o = float(sqrt(d))
      finret += ("x = " + str(intconvert((b - o)/ (2 * a))) + ",  " + str(intconvert((b + o)/(2 * a))))
    if d < 0:
      d = -d
      o = float(sqrt(d))
      finret += ("x = " + str(intconvert(b/ (2 * a))) + " ± " + str(intconvert(o/ (2 * a))) + "i" )
    return finret

  coeffecient = intconvert(simpleradical[0])

  in_root = intconvert(simpleradical[1])

  indexforfun = intconvert(simpleradical[2])

  r = gcd((2*a), b)
  l = gcd(r, (coeffecient))

  finret += ("\nAnd then we need to simplify the square root of the discriminant we just found " + insertcommas(d))
  if posorneg == True:
    finret += ("\nClearly, first we want to take out the negative, leaving us with i")
  finret += ("\nNotice that " + insertcommas(abs(d)) + " is just divisble by " + insertcommas(coeffecient ** 2))
  finret += ("\nWe can take that number out and find the square root of it which is " + insertcommas(coeffecient))
  finret += ("\nWe are left with " + insertcommas(coeffecient) + v + insertcommas(in_root))
  finret += ("\n\n\n")

  finret += ("Lastly, we need to use the rest of the Quadratic Formula\nand put our simplified radical in place of the squareroot of the discimnant\n\n")
  finret += ("x = " + insertcommas(intconvert(b)) + " ± " + insertcommas(coeffecient) + v + insertcommas(in_root))
  finret += ("\n    ━━━━━━━━━━━━━")
  finret += ("\n       "  + insertcommas(intconvert(2 * a)))
  finret += ("\n\n\n")

  finret += ("\n\nAnd then we can simplify this further")
  finret += ("\nWe can divide all the terms by " + insertcommas(l) + " and do our final simplification")
  finret += ("\nLeaving us with....")
  finret += ("\n\n\n")

  def rootyhelp(n):
    if in_root == 1:
      return ""
    else:
      return n

  def superhelpy(n):
    if in_root == 1 and coeffecient == 1:
      return "l"
    return n

  finret += ("x = " + insertcommas(zerocheck(intconvert((b/l)))) + " ± " + insertcommas(onecheck(superhelpy(intconvert(coeffecient / l)))) + rootyhelp(v) + insertcommas(rootyhelp(in_root)))
  if ((2 * a)/l) != 1:
    finret += ("\n    ━━━━━━━━━━━━━")
    finret += ("\n       "  + insertcommas(intconvert((2 * a)/l)))
  finret += ("\n\n")
  if d> 0:
    finret += ("x = " + str(zerocheck(intconvert((b - o)/ (2 * a)))) + ",  " + str(intconvert((b + o)/ (2 * a))))
  if d < 0:
    d = -d
    o = float(sqrt(d))
    finret += ("x = " + str(zerocheck(intconvert(b/ (2 * a)))) + " ± " + str(intconvert(o/ (2 * a))) + "i" )

  finret += ("\n\nAlso please note that we had to check through the first " + insertcommas(indexforfun) + " prime\nnumbers, sometimes multiple times, to do this problem. And we only have about 285,000.")
  return finret


def makepolynomialmodified(nums, divsor):
	retstring = ""
	for i in range(len(nums) - 2):
	  if nums[i] != 0:
	    retstring += addorsub(onecheck(nums[i])) + "x" + str(onecheck(len(nums) - 2 - i)).translate(SUP) + " "
	if len(nums) > 1:
	  retstring += addorsub(nums[len(nums) - 2]) + " "
	if nums[len(nums) - 1] != 0:
	  retstring += "+ (" + str(nums[len(nums) - 1]) + " / x " + addorsub(-divisor) + ")"
	test = split(retstring)
	if test[0] == "+":
	  return retstring[1:].strip()
	return retstring

def makepolynomial(nums):
	retstring = ""
	for i in range(len(nums) - 1):
	  if nums[i] != 0:
	    retstring += addorsub(onecheck(nums[i])) + "x" + str(onecheck(len(nums) - 1 - i)).translate(SUP) + " "
	retstring += addorsub(nums[len(nums) - 1]) + " "
	test = split(retstring)
	if test[0] == "+":
	  return retstring[1:].strip()
	return retstring

def makestringwithspaces(list):
	string = "   "
	for i in range(len(list) - 1):
	  string = string + str(list[i]) + "   "
	string = string + str(list[len(list) - 1] )
	return string

def myspacesrighttheere(string):
	retstring = ""
	quicksplit = split(str(string))
	if len(quicksplit) >= 5:
	  return retstring
	for i in range(5 - len(quicksplit)):
	  retstring += " "
	return retstring

def synthetic(nums, divisor):
  finretstring = ""
  botlist = [0]
  retlist = []
  allsteps = "Here is a description of the steps I took: \n\n1. I first put a zero on the bottom\n\n"
  for i in range(len(nums)):
    retlist.append(intconvert(nums[i] + botlist[i]))
    allsteps += str(i + 2) + ". I added " + str(nums[i]) + " and " + str(botlist[i]) + " and got " + str(retlist[i])
    botlist.append(retlist[i] * divisor)
    if i != len(nums) - 1:
      allsteps += "\n After I put it at the bottom, I multiplied " + str(retlist[i]) + " times " + str(divisor) + " getting " + str(botlist[i + 1]) + "\n\n"
  botlist = botlist[:-1]

  mybottomstring = "     "

  for i in range(len(split(makestringwithspaces(nums)))):
    mybottomstring += "━━"
  botlist = intconvertlist(botlist)

  finretstring += ("\n\n")
  finretstring += (myspacesrighttheere(divisor)+ str(divisor) +"|" + makestringwithspaces(nums))
  finretstring += ("\n     |" + makestringwithspaces(botlist))
  finretstring += ("\n" + mybottomstring)
  finretstring += ("\n     " + makestringwithspaces(retlist))
  finretstring += ("\n\n\n")
  try:
    finretstring += (makepolynomial(nums) + " when divided by x " + addorsub(-divisor) + " is \n\n")
    finretstring += (makepolynomialmodified(retlist, divisor))
    finretstring += ("\n\nTherefore, f(" + str(divisor) + ") = " + str(retlist[len(retlist) - 1]))
  except:
    finretstring += ("you either messed up bad or the answer is 0 so...either way ur a bot")
  finretstring += "\n\n\n" + allsteps
  return finretstring

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def leasttogreatest(mylist):
  return sorted(mylist)




def rootfact(n):
  indiv = 1
  sumdiv = 1
  nsave = n
  numsave = n
  while floor(n/sumdiv) == n/sumdiv:
    nsave = nsave / sumdiv
    sumdiv = sumdiv * indiv
    indiv += 1
  else:
    indiv = indiv - 1
    sumdiv = sumdiv / indiv
    indiv = indiv - 1
  factthing = indiv
  multiplier = intconvert(n/sumdiv)
  if multiplier != 1:
    return(str(multiplier) + " times " + str(factthing) +"! " + " = " + str(numsave))
  else:
    return((str(factthing) + "! " + " = " + str(numsave)))

def factorial(num):
  ret = 1
  for i in range(1, num + 1):
    ret = ret * i
  return ret

def primefactor(num):
  retlist = []
  for i in range(len(primes)):
    #I divide by primes as long as the number isn't down to one or I have more primes
    if num == 1:
      break
    while num % primes[i] == 0:
      num = num // primes[i]
      retlist.append(primes[i])
      #add them to my list
  if num != 1:
    #this checks if I ever actually finished
    retlist.append(num)
    if num > (primes[-1] ** 2):
      return retlist, False
      #If i didn't I return False to make not of that below
  return retlist, True

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def removecopies(mylist):
  mylist = list(dict.fromkeys(mylist))
  return mylist

def primefactorstyled(num):
  numsave = num
  mylist = primefactor(num)[0]
  info = primefactor(num)[1]
  plainlist = removecopies(mylist)
  powerlist = []
  for i in range(len(plainlist)):
    powerlist.append(mylist.count(plainlist[i]))
  retstring = ""
  for i in range(len(plainlist)):
    retstring += insertcommas(plainlist[i])
    if powerlist[i] != 1:
      retstring += str(powerlist[i]).translate(SUP)
    if i != len(plainlist) - 1:
      retstring += " ⋅ "
  if info == False:
    retstring = "*last digit may not be prime*  " + str(numsave) + " = " + retstring
    return retstring
  return  str(numsave) + " = " + retstring


def numoffactors(num):
  mylist = primefactor(num)[0]
  info = primefactor(num)[1]
  plainlist = removecopies(mylist)
  powerlist = []
  for i in range(len(plainlist)):
    powerlist.append(mylist.count(plainlist[i]))
  sum = 1
  for i in range(len(powerlist)):
    sum = sum * (powerlist[i] + 1)
  if info == False:
    retsting = "We cannot accurately tell you how many factors our number has.\nBut if we had to guess we would say:\n"
    retsting += str(sum)
  else:
    retsting = "This number has " + str(sum) + " factors"
  return retsting, sum

def primefactordata(num):
  mylist = primefactor(num)[0]
  plainlist = removecopies(mylist)
  #list of numbers without duplicates
  powerlist = []
  #list of exponent powers
  for i in range(len(plainlist)):
    powerlist.append(mylist.count(plainlist[i]))
    #I go back to my original prime factorization and count all of the same numbers
    #Then I add it to my powerlist
  return plainlist, powerlist

def multiplylist(mylist):
  mylist = list(mylist)
  retnum = 1
  for i in range(len(mylist)):
    mylist[i] = float(mylist[i])
    retnum = retnum * mylist[i]
  return retnum

def findfactors1(num):
  mylist = primefactordata(num)[0]
  powerlist = primefactordata(num)[1]
  singlepowers = []
  for i in range(len(powerlist)):
    shortlist = []
    for t in range(powerlist[i] + 1):
      shortlist.append(mylist[i] ** t)
    singlepowers.append(shortlist)
  return singlepowers

def sumoffactors(num):
  mylist = findfactors1(num)
  finlist = []
  for i in range(len(mylist)):
    finlist.append(sum(mylist[i]))
  return intconvert(multiplylist(finlist))


def findfactors2(num):
  mylist = findfactors1(num)
  retlist = []
  for i in range(len(mylist)):
    for t in range(len(mylist[i])):
      retlist.append(mylist[i][t])
  return removecopies(retlist)

def findfactors(num):
	try:
	  mylist = findfactors2(num)
	  mainlist = []
	  for t in range(len(mylist) + 1):
	    for i in combinations(mylist, t):
	      mainlist.append(i)
	  retlist = []
	  for i in range(len(mainlist)):
	    retlist.append(multiplylist(mainlist[i]))
	  finretlist = []
	  for i in range(len(retlist)):
	    if retlist[i] <= num and num % retlist[i] == 0:
	      finretlist.append(int(retlist[i]))
	  finretlist = removecopies(finretlist)
	  if len(finretlist) != numoffactors(num)[1]:
	    return "There may be an error - " + makestring(leasttogreatest(finretlist))
	  return makestring(leasttogreatest(finretlist))
	except:
		return "Overflow Error - do you really need that many factors???"

def findfactorslist(num):
  mylist = findfactors2(num)
  mainlist = []
  for t in range(len(mylist) + 1):
    for i in combinations(mylist, t):
      mainlist.append(i)
  retlist = []
  for i in range(len(mainlist)):
    retlist.append(multiplylist(mainlist[i]))
  finretlist = []
  for i in range(len(retlist)):
    if retlist[i] <= num and num % retlist[i] == 0:
      finretlist.append(int(retlist[i]))
  return leasttogreatest(removecopies(finretlist))

def combosoflist(mylist):
  retlist = []
  for i in range(floor(len(mylist) / 2)):
    quicklist = []
    quicklist.append(mylist[i])
    quicklist.append(mylist[len(mylist) - i - 1])
    retlist.append(quicklist)
  if len(mylist) % 2 == 1:
    quicklist = [mylist[floor(len(mylist) / 2)]]
    quicklist.append(mylist[floor(len(mylist) / 2)])
    retlist.append(quicklist)
  return retlist

def bigx(a, b, c):
  myproduct = a * c
  mysum = b
  prodsave = myproduct
  myproduct = abs(myproduct)
  possibles = findfactorslist(myproduct)
  combos = combosoflist(possibles)
  for i in range(len(combos)):
    if combos[i][0] + combos[i][1] == mysum and (combos[i][0]) * (combos[i][1]) == prodsave:
      return combos[i][0], combos[i][1]
    if -combos[i][0] + combos[i][1] == mysum and (-combos[i][0]) * (combos[i][1]) == prodsave:
      return -combos[i][0], combos[i][1]
    if combos[i][0]  - combos[i][1] == mysum and (combos[i][0]) * (-combos[i][1]) == prodsave:
      return combos[i][0], -combos[i][1]
    if -combos[i][0] - combos[i][1] == mysum and (-combos[i][0]) * (-combos[i][1]) == prodsave:
      return -combos[i][0], -combos[i][1]
  return False

def quicksimp(a, b):
  gcf = gcd(a, b)
  a = a // gcf
  b = b // gcf
  if ispositive(b) == True and ispositive(a) != True:
  	a, b = -a, -b
  return a, b

def finquadfactors(a, b, c):
  mytuple = bigx(a, b, c)
  first, second = mytuple[0], mytuple[1]
  return quicksimp(a, first), quicksimp(a, second)

def quadcute(a, b, c):
  sets = finquadfactors(a, b, c)
  fira, firp, seca, secp = sets[0][0], sets[0][1], sets[1][0], sets[1][1],
  return "(" + onecheck(str(fira)) + "x " + addorsub(firp) + ")(" + onecheck(str(seca)) + "x " + addorsub(secp) + ")"

def finquadfactorsnosimp(a, b, c):
  mytuple = bigx(a, b, c)
  first, second = mytuple[0], mytuple[1]
  return (a, first), (a, second)

def quadcutenosimp(a, b, c):
  sets = finquadfactorsnosimp(a, b, c)
  fira, firp, seca, secp = sets[0][0], sets[0][1], sets[1][0], sets[1][1],
  return "(" + onecheck(str(fira)) + "x " + addorsub(firp) + ")(" + onecheck(str(seca)) + "x " + addorsub(secp) + ")"

def fracthelp(a):
  if a == 1:
    return ""
  else:
    return "/" + str(a)

def fractiondisplay(a, b):
  a, b = quicksimp(a, b)
  if ispositive(a) == True and ispositive(b) == True or ispositive(a) == False and ispositive(b) == False:
    return str(abs(a)) + fracthelp(abs(b))
  else:
    return "-" + str(abs(a)) + fracthelp(abs(b))


def quadtotal(a, b, c, Input):
  retstring = ""
  a, b, c = float(a), float(b), float(c)

  if a == 0:
    return "bot"

  longchain1 = insertcommas(intconvert(a)) + "x² " + addorsub(intconvert(b)) + "x " + addorsub(intconvert(c)) + " = 0"

  mymultiplier = 1

  if checkint(a) == False or checkint(b) == False or checkint(c) == False:
      while checkint(a) == False or checkint(b) == False or checkint(c) == False:
        a = round(a * 10, 8)
        b = round(b * 10, 8)
        c = round(c * 10, 8)
        mymultiplier = round(mymultiplier * 10, 8)

  a = intconvert(a)
  b = intconvert(b)
  c = intconvert(c)


  grtcommonfactor = gcf(a, b, c)

  if ispositive(a) == False:
    grtcommonfactor = -grtcommonfactor

  mymultiplier = (mymultiplier/grtcommonfactor)

  a = int(a/grtcommonfactor)
  b = int(b/grtcommonfactor)
  c = int(c/grtcommonfactor)

  longchain2 = insertcommas(a) + "x² " + addorsub(b) + "x " + addorsub(c) + " = 0"

  retstring += "Our first step is to turn " + longchain1 + " into " + longchain2 + "\nYou can do this by multiplying both sides by " + insertcommas(intconvert(mymultiplier)) + "\nor dividing both sides by " + insertcommas(intconvert(1 / mymultiplier))

  try:
    result = quadcute(a, b, c)
  except:
    return retstring + quad(a, b, c)

  if Input == "True":
    return retstring + quad(a, b, c)

  retstring += ("\n\nFrom here, we want to try and factor this quadratic. We need two numbers that add to " + str(b) + " and multiply to " + str(a * c) + "\n\nTo do this, we need to look at the factors of " + str(abs(a * c)) + ", which are:\n" + makestring(findfactorslist(abs(a * c))) + "\n\n\nFrom this list, the two that we can find that add to " + str(b) + " are " + (str(bigx(a, b, c)).replace("(","")).replace(")", ""))

  retstring += ("\n\n\nNow that we know those two values, we can put them in the format of (ax + p)(ax + q). Doing this, we come up with:  " + str(quadcutenosimp(a, b, c)) + "\n\nNow we can cancel out the greatest common factor of each, finding our final set of binomial factors. Note that what we divided by multiplied to " + str(a) + "\nAnd dividing and tacking on the inital value we divided, we get: \n" + str(onecheck(intconvert(1 / mymultiplier))) + str(quadcute(a, b, c)))

  fira, firp = finquadfactors(a, b, c)[0]
  seca, secp = finquadfactors(a, b, c)[1]


  retstring += "\n\n\n\nIf we would like to finish solving this quadratic, all we would need to do is set our result equal to zero:\n" + str(onecheck(intconvert(1 / mymultiplier))) + str(quadcute(a, b, c)) + " = 0. \n\nWe want to then divide by our inital multipler " + str(intconvert(1 / mymultiplier)) + " effectively just canceling it out, leaving us with just " + str(quadcute(a, b, c)) + " = 0.\n\nThe next step is to set both of these binomials equal to zero:\n" + str(quadcute(a, b, c)).replace(")", ") = 0\n") + "\n\nSolving, we get:\n" + str(fira) + "x = -(" + str(firp) + ") \n" + str(seca) + "x = -(" + str(secp) + ")"


  retstring += "\nDividing by " + str(fira) + " and " + str(seca) + " on both sides gives us:\n\nx = " + fractiondisplay(-firp, fira) + ", " + fractiondisplay(-secp, seca) + " or in decimal form " + str(-firp / fira) + ", " + str(-secp / seca)
  return retstring


def productoffactors(num):
	try:
		ret = int(num**(numoffactors(num)[1] / 2))
	except:
		return "Overflow ERROR - too large a number, so much so you probably don't need it"
	return ret


def displaynuminfo(num):
	try:
		num = int(num)
	except:
		return "ERROR"
	retstring = "\nThe first bit of information we will just give is something you can calculate with a calulator\n\n"
	retstring += insertcommas(num) + " squared is: " +  insertcommas(num**2)  + "\nAnd the square root: " + str(num**0.5) + "\nAnd finally the cube root: " + str(num**(1/3))
	retstring += "\n\n\n\nHopefully, if you needed any of that information that helped.\nNow we wil try to find the prime factorization of our number which will let us find the number of factors, etc\n\n"
	retstring += "So to find the prime factorization, you really just need to split the number up into primes as you see them, until you can multiply only by primes to do this.\n"
	retstring += "When we do this, we end up with:\n\n" + primefactorstyled(num)
	retstring += "\n\n\n\nUsing this, we can find the number of this number by adding one to all of the exponents and multiplying them together. When we do this we come up with:\n" + numoffactors(num)[0]
	if num < 30:
		retstring += "\n\n\n\nAdditionally, " + str(num) + "! = " + insertcommas(factorial(num)) + "\n\nConversly, your number written in the form of a * b! is " +  rootfact(num)
	retstring += "\n\n\nAdditionally, " + str(num) + " written in the form of a * b! is:\n\n" +  rootfact(num)
	retstring += "\n\n\n\n\nNext, we can find sets of each prime factors, for instance, 2^3 would give us, 1, 2, 4, 8.\n\nIf we take the sum of all these sets and multiply them together, we can find the sum of all the factors: " + insertcommas(sumoffactors(num)) + "\n\n\n\nWe can also find the product of the factors, by taking our number to the power of the number of factors it has divided by 2. \nDoing this we end up with:\n" + insertcommas(productoffactors(num)) +  "\n\n\n\n\nUsing this, the last thing we can discover when we match up the prime\nfactorization is all of the factors:\n" + findfactors(num)
	return retstring



def heron(a, b, c):
  retstring = ""
  try:
    a = float(a)
    b = float(b)
    c = float(c)
  except ValueError:
    return "try again"

  semi = ((a + b + c) / 2)

  mainhelp = (semi * (semi - a) * (semi - b) * (semi - c))

  if a == b and b == c:
    retstring += ("This is an equilaterial triangle. Please use the formula a squared root 3 over four. But we will still show you how to use Heron's for this\n\n")

  multiplier = 1

  if checkint(a) == False or checkint(b) == False or checkint(c) == False:
      while checkint(a) == False or checkint(b) == False or checkint(c) == False:
        a = round(a * 10, 8)
        b = round(b * 10, 8)
        c = round(c * 10, 8)
        multiplier = round(multiplier * 10, 8)

  grtcommonfactor = gcf(a, b, c)

  divisor = grtcommonfactor

  a = int(a/grtcommonfactor)
  b = int(b/grtcommonfactor)
  c = int(c/grtcommonfactor)

  retstring += ("So the first step here, if we plan to put our final answer in simplified\nradical form, is to use the concept of similar triangles. We are going to find the\narea of the smallest similar triangle with integer side lengths and then adjust our area based on the scale factor, squaring it because it we want the area. To do this,\nwe can multiply all of the sides by " + insertcommas(multiplier) + " and divide them both by " + insertcommas(divisor))


  if (a + b) <= c or (c + b) <= a or (a + c) <= b:
    retstring += ("\n\n\nThis triangle does not exist. The sum of any two sides of a triangle must be greater than the third side. As you can see, that is not the case here.")
    return retstring

  main = ((a + b + c)*(a + b - c)*(a - b + c)*(-a + b + c))

  myvalues = str(a) + ", " + str(b) + ", " + str(c)

  retstring +=("\n\n\n\nThe next step that we take is to plug our side lengths, " + myvalues +", into Heron's Formula. We will use\na modified version of the formula: ​1⁄4√((a + b + c)*(a + b - c)*(a - b + c)*(-a + b + c))\nto ensure our result stays integral\n\n\nPlugging in our values, not including the square root or the one-fourth, we end up with:\n" + insertcommas(main))

  def rootyhelp(n):
    if in_root == 1:
      return ""
    else:
      return n

  def superhelpy(n):
    if firstinroot == 1 and firstoutroot == 1:
      return "l"
    return n

  def bottomhelp(string):
    if denominator == 1:
      return ""
    return string

  v = str("√")

  try:
    simpleradical = simpleradicalformat(main)
  except:
    retstring +=("\n\nThe area of your triangle is " + insertcommas(sqrt(mainhelp)))
    retstring +=("\n\nSorry this number is a bit to big for us to calculate the simplified radical form of")
    return retstring

  coeff = intconvert(simpleradical[0])
  in_root = intconvert(simpleradical[1])
  index = intconvert(simpleradical[2])

  retstring +=("\n\n\n\nNow we need to simplify this radical.\n")
  retstring +=("Notice that " + insertcommas(main) + " is just divisble by " + insertcommas(coeff ** 2))
  retstring +=("\n\nWe can take that number out and find the square root of it which is " + insertcommas(coeff))
  coeff = intconvert(coeff * (divisor**2))

  retstring += ("\n\nAnd from here we need to multiply this coeffecient by what we divided by,\nwhich is " + insertcommas(divisor) + " and we get " + insertcommas(coeff))
  retstring +=("\nWe are left with (" + insertcommas(coeff) + v + insertcommas(in_root) + ") / (4 * " + insertcommas(multiplier **2) + ") left over from our\nmodified formula and multiplying to find integral values\n\n\n")


  firstinroot = intconvert(in_root)
  grtcommon = gcd(coeff, ((multiplier**2)* 4))

  firstoutroot = intconvert(coeff / grtcommon)

  denominator = intconvert(((2 * multiplier)**2)/grtcommon)

  retstring +=("And then we can simplify our final expression further\n")
  retstring +=("We can divide all the terms by " + insertcommas(grtcommon) + " and do our final simplification\n")
  retstring +=("Leaving us with....\n\n")

  retstring +=("\nThe area of your triangle is " + insertcommas(sqrt(mainhelp)))
  retstring +=("\nAnd in simplified radical form (" + insertcommas(onecheck(superhelpy(firstoutroot))) + "√" + insertcommas(firstinroot) + ") " + bottomhelp("/") + insertcommas(onecheck(denominator)))

  retstring +=("\n\n\nAlso please note that we had to check through the first " + insertcommas(index) + " prime\nnumbers, sometimes multiple times, to do this problem. And we only have about 285,000.")
  return retstring

def MAD(num):
  retstring = ""

  count = len(num)

  mean = sum(num) / count

  deviation = [abs(x - mean) for x in num]

  sumd = sum(deviation)

  num.sort()
  numsave = num

  def medhelp(n):
    n = intconvert(n)
    if n != floor(n):
      return str((numsave[intconvert(n - 0.5)] + numsave[intconvert(n + 0.5)]) / 2)
    else:
      return str(numsave[n])

  def freq(List): 
      return max(set(List), key = List.count)

  retstring += ("\n\n")
  retstring +=("Mean/average = "  + str(intconvert(mean)))
  retstring +=("\n\nMean Absolute Deviation = " + str(intconvert(sumd / count)))
  retstring +=("\n\nPercent Deviation = " + str(intconvert(abs(((sumd / count) / mean) * 100))) + "%")
  retstring +=("\n\nRange = " + str(numsave[len(numsave) - 1] - numsave[0]))
  retstring +=("\n\nMedian = " + str(intconvert(medhelp((len(numsave) - 1) / 2))))
  if len(list(dict.fromkeys(numsave))) != len(numsave):
    retstring +=("\n\nMode = " + str(freq(numsave)))
    retstring +=("\n\n   - Mode will be the lowest, most frequent number: may not include all possible modes")
  retstring +=("\n\nAnd your set had " + str(count) + " numbers:\n")
  retstring +=(makestring(numsave))
  return retstring


def checknumsbase(word):
  numchars = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "-",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  mylist = split(str(word))
  for i in range(len(mylist)):
    count = 0
    for t in range(len(numchars)):
      if mylist[i] != numchars[t]:
        count += 1
      else:
        count = 0
      if count > (len(numchars) - 1):
        return False
  if nummyhelp(word) == False:
    return False
  return True

def pullclosenumsbase(string):
  numbers = ""
  mylist = split(string)
  for i in range(len(mylist)):
    mylist[i] = str(mylist[i])
    if checknumsbase(mylist[i]) == True:
      numbers = numbers + mylist[i]
    else:
      numbers += " "
  return numbers.split()

def numbertobaselist(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def baselistcuter(n, b):
  #something from base 10 to new base with proper formatting - string
  nsave = n
  n = abs(n)
  mylist = numbertobaselist(n, b)
  for i in range(len(mylist)):
    if mylist[i] >= 10:
      mysave = mylist[i] - 10
      try:
        mylist[i] = letters[mysave]
      except:
        mylist[i] = "(" + str(mylist[i]) + ")"
  if ispositive(nsave) == False:
    return "-" + modmakestring(mylist)
  return modmakestring(mylist)

def reversecutieparenthesis(mylist):
  retlist = []
  for i in range(len(mylist)):
    try:
      retlist.append(int(mylist[i]))
    except:
      retlist.append(letters.index(mylist[i]) + 10)
  return retlist


def reversecutieclean(mystring):
  mystring = str(mystring)
  mylist = split(mystring)
  retlist = []
  for i in range(len(mylist)):
    try:
      retlist.append(int(mylist[i]))
    except:
      retlist.append(letters.index(mylist[i]) + 10)
  return retlist

def makecutie(mylist):
  for i in range(len(mylist)):
    if mylist[i] >= 10:
      mysave = mylist[i] - 10
      try:
        mylist[i] = letters[mysave]
      except:
        mylist[i] = "(" + str(mylist[i]) + ")"
  return modmakestring(mylist)

def tobaseten(mylist, b):
  b = int(b)
  return sum(int(v) * (b ** i) for i, v in enumerate(reversed(mylist)))


def tobasetenview(mylist, b):
  retstring = ""
  for i, value in enumerate(reversed(mylist)):
    term = str(int(value)) + " ⋅ " + str(b) + str(i).translate(SUP)
    if i != 0:
      term += " + "
    retstring = term + retstring
  return retstring

def makecuteletterstonums(mylist):
  retstring = ""
  for i in range(len(mylist)):
    retstring += "(" + str(mylist[i]) + ")"
  return retstring

#retstring = ("This is a base converter. We will ask for your number, its base, and the base you want it in.\nWe use A-Z to represent 10 - 35. If you need values greater than 35 or don't want\nto use letters, please enter with parenthesis for clarity. Ex - (67)(45)(A)(11)(5)\n")

def basedisplay(a, b, c):
  a = str(a)
  b = int(b)
  c = int(c)
  retstring = "\nOur first step is to convert the number you entered, " + a + ", to base 10. To do this, we will rewrite our numbers in terms of powers of our base, of course converting our letters into numerical values\nAdding and multiplying out will give us our number in base 10, simply because we are naturally adding and multiplying in base 10.\n\n\n"

  if a.count("(") != 0:
    mylist = (reversecutieparenthesis(pullclosenumsbase(a)))
  else:
    mylist = (reversecutieclean(a))

  toten = tobaseten(mylist, b)

  retstring += a + " = " + makecuteletterstonums(mylist) + "\n\nWhen we do this, we get:\n" + tobasetenview(mylist, b) + "\n\nThis equals " + insertcommas(toten) + "\n\n\nAnd from here we need to convert " + insertcommas(toten) + " to base " + insertcommas(c)

  retstring += "\n\nTo do this, we can use upsidedown division, where we continually divide by our base, taking the remainder at each interval. When we complete this, we get:\n\n" + baselistcuter(toten, c)

  retstring += "\n\n\nTherefore: " + makecutie(mylist) + " in base " + insertcommas(b) + " converted to base " + insertcommas(c) + " is " + baselistcuter(toten, c)

  return retstring

def perm(num, part):
  if checkint(num) == False or checkint(part) == False:
    return ValueError
  num, part = int(num), int(part)
  product = 1
  for i in range(part):
    product *= (num - i)
  return product

def permwithmultiply(num, part):
  if checkint(num) == False or checkint(part) == False:
    return "There is an error"
  num, part = int(num), int(part)
  product = 1
  retstring = ""
  for i in range(part):
    product *= (num - i)
    if i != (part - 1):
      retstring += str(num - i) + " ⋅ "
    else:
      retstring += str(num - i)
  return retstring

def permwithallwork(num, part):
  if checkint(num) == False or checkint(part) == False:
    return "There is an error"
  num, part = int(num), int(part)
  product = 1
  retstring = "\n\n\nIn order to do " + insertcommas(num)  + "P" + insertcommas(part) + ", we need to start with " + insertcommas(num) + " and multiply that by each previous number a total of " + insertcommas(part) + " times.\n\nSetting this up, we see:\n\n"
  quickstring = ""
  for i in range(part):
    product *= (num - i)
    if i != (part - 1):
      quickstring += str(num - i) + " ⋅ "
    else:
      quickstring += str(num - i)
  retstring += quickstring + "\n\nThis gives us:\n\n" + insertcommas(intconvert(product))
  return retstring

def comb(num, part):
  if checkint(num) == False or checkint(part) == False:
    return ValueError
  num, part = int(num), int(part)
  if num / 2 < part:
    part = num - part
  product = 1
  for i in range(part):
    product *= (num - i)
  return int(product / factorial(part))

def combwithmultiply(num, part):
  if checkint(num) == False or checkint(part) == False:
    return ValueError
  num, part = int(num), int(part)
  if num / 2 < part:
    part = num - part
  return "(" + permwithmultiply(num, part) + ") / (" + permwithmultiply(part, part) + ")"

def combwithallwork(num, part):
  if checkint(num) == False or checkint(part) == False:
    return "There is an error"
  num, part = int(num), int(part)
  retstring = ""
  if num / 2 < part:
    retstring += "\n\n\nFirst, we need to change " + insertcommas(num) + " choose " + insertcommas(part) + " into " + insertcommas(num) + " choose " + insertcommas(num - part) + " because they are equivalent and everything cancels out."
    part = num - part
  retstring += "\n\n\nWe need to begin with " + insertcommas(num) + " and multiply that by each previous number a total of " + insertcommas(part) + " times and then divide by " + insertcommas(part) + " factorial times.\n\nSetting this up, we see:\n\n" + combwithmultiply(num, part) + "\n\nGiving us " + insertcommas(num) + "C" + insertcommas(part) + " = " + insertcommas(comb(num, part))
  return retstring


def permandcomb(userdata):
  origuserinput = userdata
  userdata = userdata.lower()

  userdata = userdata.replace("-", "+ -")
  userdata = userdata.replace("/", "* /")

  totals = userdata.split("+")

  for i in range(len(totals)):
    totals[i] = totals[i].split("*")

  retstring = "You entered: " + origuserinput + "\n\nOkay, lets start by finding the value of each of your combination/permutation statements."

  for i in range(len(totals)):
    product = 1
    for t in range(len(totals[i])):
      if totals[i][t].count("p") != 0:
        num = perm(pullclosenums(totals[i][t])[0], pullclosenums(totals[i][t])[1])
        retstring += permwithallwork(pullclosenums(totals[i][t])[0], pullclosenums(totals[i][t])[1])
      else:
        num = comb(pullclosenums(totals[i][t])[0], pullclosenums(totals[i][t])[1])
        retstring += combwithallwork(pullclosenums(totals[i][t])[0], pullclosenums(totals[i][t])[1])
      if totals[i][t].count("/") != 0:
        num = intconvert(1 / num)
        retstring += "\n\nNow we are going to take the reciprocal of that number, so we can just multiply instead: " + str(num)
      product = product * num
    if totals[i][0].count("-") != 0:
      totals[i] = -1 * intconvert(product)
    else:
      totals[i] = intconvert(product)

  finalanswer = sum(totals)

  retstring += "\n\nWhen we multiply everything that needs to multiplied, we have these terms remaining: " + makestring(totals) + "\n\nAnd when we add these all together, we end up with: \n" + insertcommas(finalanswer)
  return retstring

def fractiondisplaypythag(a, b, inroot):
  inroot = int(inroot)
  a, b = quicksimp(a, b)
  if ispositive(a) == True and ispositive(b) == True or ispositive(a) == False and ispositive(b) == False:
    return str(onecheck(abs(a))) + "√" + str(inroot) + str(fracthelp(abs(b)))
  else:
    return "-" + str(onecheck(abs(a))) + "√" + str(inroot) + str(fracthelp(abs(b)))

def pythag(a, b, solvinginput):
  retstring = ""
  a, b = float(a), float(b)

  solvefor = solvinginput

  quicklist = [a, b]
  a, b = leasttogreatest(quicklist)

  retstring += "\nOk, we are solving for the " + solvefor + " and we have the two lengths " + str(intconvert(a)) + ", " + str(intconvert(b)) + "\n\nThe first step will be to scale these lengths by a viable scale factor in order to make our calculations easier"

  mymultiplier = 1

  asave = a
  bsave = b

  if checkint(a) == False or checkint(b) == False:
      while checkint(a) == False or checkint(b) == False:
        a = round(a * 10, 8)
        b = round(b * 10, 8)
        mymultiplier = round(mymultiplier * 10, 8)

  a = intconvert(a)
  b = intconvert(b)

  divisor = gcd(a, b)

  a = a // divisor
  b = b // divisor

  retstring += "\n\nWe can multiply both sides by " + str(intconvert(mymultiplier / divisor)) + " or divide by " + str(intconvert(divisor / mymultiplier)) + " giving us the lengths " + str(a) + " and " + str(b)

  if solvefor == "hypotenuse":
    adjtotal = int((a**2) + (b**2))
    total = float((bsave**2) + (asave**2))

    retstring += "\n\n\nNow we need to plug our values into our formula a2 + b2 = c2".translate(SUP) + ", where we have a and b and need to solve for c.\n\nPlugging in our values, we see that c squared equals: " + str(adjtotal)

    coeff, in_root, index = simpleradicalformat(adjtotal)

    answer = fractiondisplaypythag(int(coeff * divisor), mymultiplier, in_root)

  elif solvefor == "leg":
    adjtotal = int((b**2) - (a**2))
    total = float((bsave**2) - (asave**2))

    retstring += "\n\n\nNow we need to plug our values into our modified formula a2 = c2 - b2".translate(SUP) + ", where we have b and c and need to solve for a.\n\nPlugging in our values, we see that a squared equals: " + str(adjtotal)

    coeff, in_root, index = simpleradicalformat(adjtotal)

    answer = fractiondisplaypythag(int(coeff * divisor), mymultiplier, in_root)

  retstring += "\n\nNow we need to simplify the √" + str(adjtotal) + " giving us: " + str(coeff) + "√" + str(in_root) + "\n\n\nFinally, we need to reapply the scale factor that we used, leaving us with a final answer of\n" + answer + "\n\nYour " + solvefor + " length is " + answer + "\n\nor in decimal form: " + str(intconvert(sqrt(total))) + "\n\n" + str(index) + " is the number of primes it got to in our list of 283146 primes"
  return retstring


def intconvertlist(mylist):
  return [intconvert(x) for x in mylist]

def pos(num):
  return num >= 0

def findfactorsall(num):
  retlist = []
  if num == 0:
    return [0]
  num = abs(num)
  for i in range(1, num + 1):
    if num % i == 0:
      retlist.append(-i)
      retlist.append(i)
  return retlist

def findfactorspos(num):
  retlist = []
  if num == 0:
    return [0]
  num = abs(num)
  for i in range(1, num + 1):
    if num % i == 0:
      retlist.append(i)
  return retlist

def syn(nums, divisor): 
  botlist = [0]
  retlist = []
  for i in range(len(nums)):
    retlist.append(intconvert(nums[i] + botlist[i]))
    botlist.append(retlist[i] * divisor)
  botlist = botlist[:-1]
  return retlist


def syntheticsteps(nums, divisor):
  finretstring = ""
  botlist = [0]
  retlist = []
  allsteps = "Here is a description of the steps I took: \n\n1. I first put a zero on the bottom\n\n"
  for i in range(len(nums)):
    retlist.append(intconvert(nums[i] + botlist[i]))
    allsteps += str(i + 2) + ". I added " + str(nums[i]) + " and " + str(botlist[i]) + " and got " + str(retlist[i])
    botlist.append(retlist[i] * divisor)
    if i != len(nums) - 1:
      allsteps += "\n After I put it at the bottom, I multiplied " + str(retlist[i]) + " times " + str(divisor) + " getting " + str(botlist[i + 1]) + "\n\n"
  botlist = botlist[:-1]

  mybottomstring = "     "

  for i in range(len(split(makestringwithspaces(nums)))):
    mybottomstring += "━━"
  botlist = intconvertlist(botlist)

  finretstring += ("\n\n")
  finretstring += (myspacesrighttheere(divisor)+ str(divisor) +"|" + makestringwithspaces(nums))
  finretstring += ("\n     |")
  finretstring += ("\n     |" + makestringwithspaces(botlist))
  finretstring += ("\n" + mybottomstring)
  finretstring += ("\n     " + makestringwithspaces(retlist))
  finretstring += ("\n\n")
  if retlist[-1] == 0:
    finretstring += "Therefore, this is a zero because the remainder is zero"
  else:
     finretstring += "Since there is a remainder, this is not a zero"
  return finretstring

def possiblezeros(mylist):
  retlist = []
  if mylist[-1] != 0:
    p = findfactorsall(mylist[-1])
  else:
    p = findfactorsall(mylist[-2])
    retlist.append(0)
  q = findfactorspos(mylist[0])
  for i in range(len(p)):
    for t in range(len(q)):
      retlist.append(intconvert(p[i] / q[t]))
  return retlist

def plugin(mylist, value):
  finnum = 0
  degree = len(mylist) - 1
  for i in range(len(mylist)):
    finnum += mylist[i] * (value**(degree - i))
  return finnum

def zerocheckpolynomial(nums, divisor):
  mylist = syn(nums, divisor)
  if mylist[-1] == 0:
    return True
  return False

def findzeros(nums, possibles):
  retlist = []
  for i in range(len(possibles)):
    if zerocheckpolynomial(nums, possibles[i]) == True:
      retlist.append(possibles[i])
  return retlist

def roundlist(mylist):
  return [round(x, 5) for x in mylist]

def checkintlist(mylist):
  for i in range(len(mylist)):
    if checkint(mylist[i]) == False:
      return False
  return True


def gcdoflist(data):
  data = [x for x in data if x != 0]
  combos = combinations(data, 2)
  mycombos = list(combos)
  retlist = []
  for i in range(len(mycombos)):
    retlist.append(abs(gcd(mycombos[i][0], mycombos[i][1])))
  print(retlist)
  return min(retlist)



def allrationalroots(mystring):
  usernums = pullclosenums(mystring)

  i = 0
  while usernums[i] == 0:
  	i += 1
  usernums = usernums[i:]

  if len(usernums) < 2:
    return "Enter more than one value"

  usernumsave = usernums

  multiplier = 1
  while checkintlist(usernums) == False:
    usernums = [round(x * 10, 7) for x in usernums]
    multiplier *= 10

  gcdofinput = gcdoflist(usernums)

  if ispositive(usernumsave[0]) == False:
  	gcdofinput = - gcdofinput

  nums = [x // gcdofinput for x in usernums]

  multiplier /= gcdofinput

  divider = 1 / multiplier


  even = True
  if len(nums) % 2 == 0:
    even = False

  up = False
  if pos(nums[0]) == True:
    up = True

  try:
    zeros = findzeros(nums, possiblezeros(nums))
  except:
    return "There was an Error"

  degree = len(nums) - 1

  retstring = "\n\nf(x) = " + makepolynomial(nums)
  if multiplier != 1:
    retstring += "\n\nBefore we start any calculations, we first want to multiply the entire polynomial " + makepolynomial(usernumsave) + "= 0 by " + str(intconvert(multiplier)) + " or divide by " + str(intconvert(divider)) + " to get " + makepolynomial(nums) + " = 0"
  if nums[-1] != 0:
    retstring += "\n\nFirst we want to find p and q, all of the factors of the first coeffecient and\nthe last. Let's start by finding all of the factors of " + str(nums[-1]) + " includign the negatives.\n\n"
    retstring += "\nWhen we do this, we get:\n" + makestring(findfactorsall(nums[-1]))
  else:
    retstring += "\n\nFirst we want to find p and q, all of the factors of the first coeffecient and\nthe last. Let's start by finding all of the factors of " + str(nums[-2]) + " includign the negatives.\n\n"
    retstring += "When we do this, we get:\n" + makestring(findfactorsall(nums[-2]))
  retstring += "\n\nAnd then we find all the factors of " + str(nums[0]) + " and we get\n\n" + makestring(findfactorsall(nums[0]))

  retstring += "\n\nThe next step is to divide all of these two sets of factors to come up with a list of\npossible zeros\n\nWhen we do this, we get:\n" + makestring(roundlist(possiblezeros(nums)))

  retstring += "\n\nNow we have reached the part where we need to do synthetic divison with each\none of these possible zeros (or until the equation becomes easily factoriable)\nin order to determine whether they are actually zeros.\n\n"

  zeroslist = possiblezeros(nums)
  for i in range(len(zeroslist)):
    retstring += "\n" + syntheticsteps(nums, zeroslist[i])
    if i != len(zeroslist) - 1:
      retstring += "\n\nAnd on to the next zero:\n\n"

  numofzeros = len(zeros)

  retstring += "\n\n\n\n\nLooking back, we found " + str(numofzeros) + " zeros"

  retstring += "\n\n\nHere are the " + str(numofzeros) + " zeros we found out of the " + str(degree) + " there should be(may be double root): \n\n"
  try:
    retstring += makepolynomial(nums)
    retstring += "\n\nx = " + makestring(zeros)
  except:
    return retstring

  retstring += "\n\n\nOk from here we need to find our relative maximum and minimum points.\nDoing this will be hard or impossible if we have not found all of our zeros\n"

  def makecorofx(mylist):
    mystring = ""
    for i in range(len(mylist)):
      mystring += "(" + str(mylist[i]) + ", 0)  "
    return mystring

  def makecor(mylist, mylist2):
    mystring = ""
    for i in range(len(mylist)):
      mystring += "(" + str(mylist[i]) + ", " + str(mylist2[i]) + ")  "
    return mystring

  def thingstoplugin(mylist):
    retlist = []
    for i in range(len(mylist) - 1):
      retlist.append(intconvert(0.5 * (mylist[i] + mylist[i + 1])))
    return retlist

  if numofzeros == 1:
    retstring += "\n\nOkay, since we only have one zero, the only point we have is " + makecorofx(zeros)
    retstring += "\n\nAnd we obviously have (0, " + str(nums[-1]) + "), the y-intercept\nAnd thats about as far as we can go"
  else:
    retstring += "So we found " + str(numofzeros) + " zeros leaving us with these points:\n" + makecorofx(zeros)
    retstring += "\nAnd we obviously have (0, " + str(nums[-1]) + "), the y-intercept\nAnd thats about as far as we can go\n"
    retstring += "\n\nNow we need to find the minimum and maximum points, which will be what you find\nwhen you plug in the x values in between the zeros."

    xcorvalues = thingstoplugin(zeros)
    retstring += "\nFinding the averages of the zeros, we will plug-in:  " + makestring(xcorvalues)
    ycorvalues = []
    for i in range(len(xcorvalues)):
      ycorvalues.append(intconvert(plugin(nums, xcorvalues[i])))

    retstring += "\n\n\nAfter doing that, the points that we came up with are:\n" + makecor(xcorvalues, ycorvalues)
    retstring += "\n\n\n\nAnd that's it. We have our zero coordinates:\n" + makecorofx(zeros) + "\nAnd our maximum and minimum points:\n" + makecor(xcorvalues, ycorvalues)
    if even == True:
      if up == True:
        retstring += "\n\n\nBe sure to plot these points and remember this is a even graph(td)\nthat will go upwards, aka is positive"
      else:
        retstring += "\n\\nnBe sure to plot these points and remember this is a even graph(td)\nthat will go downards, aka is negative"
    else:
      if up == True:
        retstring += "\n\n\nBe sure to plot these points and remember this is a odd graph(disco)\nthat will go upwards, aka is positive"
      else:
        retstring += "\n\n\nBe sure to plot these points and remember this is a odd graph(disco)\nthat will go downards, aka is negative"
  return retstring

def makelistint(mylist):
  return [int(item) for item in mylist]

def addnumslist(mylist):
  retstring = ""
  if float(mylist[-1]) < -float(mylist[-1]):
    mylist[-1] = "(" + insertcommas(mylist[-1]) + ")"
  for i in range(len(mylist) - 1):
    mylist[i] = insertcommas(mylist[i])
    if mylist[i].count("-") != 0:
      mylist[i] = "(" + insertcommas(mylist[i]) + ")"
    retstring += mylist[i] + " + "
  return retstring + insertcommas(mylist[-1])




def addparenthesis(mylist):
  #puts parenthesis
  retstring = ""
  for i in range(len(mylist)):
    retstring += "(" + str(mylist[i]) + ")"
  return retstring

def basedisplaytoten(mylist, b):
  retstring =  addparenthesis(mylist) + " in base " + str(b) + " = " + tobasetenview(mylist, b) + "\n\n = " + insertcommas(tobaseten(mylist, b))
  return retstring


def baseoperate(userdata, userfinalbase):
  origuserinput = userdata
  userdata = userdata.replace(" ", "")
  userdata = userdata.replace("-", "+ -")
  userdata = userdata.replace("/", "* /")
  userfinalbase	= int(userfinalbase	)

  totals = userdata.split("+")

  for i in range(len(totals)):
    totals[i] = totals[i].split("*")

  retstring = "You entered: " + origuserinput + "\n\nLet's start by finding the values of each of your numbers in base 10.\n\n\n"

  for i in range(len(totals)):
    product = 1
    for t in range(len(totals[i])):
      totals[i][t] = totals[i][t].strip()
      if totals[i][t].count("(") != 0:
        totals[i][t] = totals[i][t].split("b")
        if totals[i][t][0].count("-") != 0:
          posmultiply = -1
          totals[i][t][0] = totals[i][t][0].replace("-", "")
        else:
          posmultiply = 1
        if totals[i][t][0].count("/") != 0:
          divmultiply = True
          totals[i][t][0] = totals[i][t][0].replace("/", "")
        else:
          divmultiply = False
        mylist = reversecutieparenthesis(pullclosenumsbase(totals[i][t][0]))
      else:
        totals[i][t] = totals[i][t].split("b")
        if totals[i][t][0].count("-") != 0:
          posmultiply = -1
          totals[i][t][0] = totals[i][t][0].replace("-", "")
        else:
          posmultiply = 1
        if totals[i][t][0].count("/") != 0:
          divmultiply = True
          totals[i][t][0] = totals[i][t][0].replace("/", "")
        else:
          divmultiply = False
        mylist = reversecutieclean(totals[i][t][0])

      base = totals[i][t][-1]

      num = tobaseten(mylist, base) * posmultiply

      retstring += str(basedisplaytoten(mylist, base)) + "\n\n"

      if divmultiply == True:
        product = intconvert(product / num)
      else:
        product *= num

    totals[i] = intconvert(product)

  final = intconvert(sum(totals))


  retstring += "\n\n\nAfter multiplying and dividing, we are left with: \n" + addnumslist(totals) + "\n\n = " + insertcommas(final)


  if userfinalbase != 10 and checkint(final) == True:
    retstring += "\n\n\nAnd converting " + str(final) + " to base " + str(userfinalbase) + " gives us: " + baselistcuter(final, userfinalbase)

  return retstring


def fractiondisplayslope(a, b):
  a, b = quicksimp(a, b)
  a, b = intconvert(a), intconvert(b)
  if ispositive(a) == True and ispositive(b) == True or ispositive(a) == False and ispositive(b) == False:
    return str(abs(a)) + fracthelp(abs(b))
  else:
    return "-" + str(abs(a)) + fracthelp(abs(b))

def negorpos(num):
  num = str(num)
  if num.count("-") != 0:
    return num.replace("-", "- ")
  elif num != 0:
    return "+ " + num
  return num


def gcfoffour(a, b, c, d):
  return gcd(gcd(gcd(a, b), c), d)


def slopeform(x1, y1, x2, y2):
  retstring = "Your two points are (" + str(intconvert(x1)) + ",  " + str(intconvert(y1)) + ")   and   (" + str(intconvert(x2)) + ",  " + str(intconvert(y2)) + ")\n\n"
  multiplier = 1
  if checkint(x1) == False or checkint(x2) == False or checkint(y1) == False or checkint(y2) == False:
      while checkint(x1) == False or checkint(x2) == False or checkint(y1) == False or checkint(y2) == False:
        x1 = round(x1 * 10, 8)
        x2 = round(x2 * 10, 8)
        y1 = round(y1 * 10, 8)
        y2 = round(y2 * 10, 8)
        multiplier *= 10

  mygcf = gcfoffour(x1, x2, y1, y2)

  x1, x2 = intconvert(x1 / mygcf), intconvert(x2 / mygcf)

  y1, y2 = intconvert(y1 / mygcf), intconvert(y2 / mygcf)

  b = fractiondisplayslope(((y1 * (x2 - x1) - x1 * (y2 - y1)) * mygcf), (x2 - x1) * multiplier)

  slope = fractiondisplayslope(y2 - y1, x2 - x1)
  slopedecimal = intconvert(round(((y2 - y1)/ (x2 - x1)), 5))
  bdecimal = intconvert(round((((y1 * (x2 - x1) - x1 * (y2 - y1)) * mygcf) / ((x2 - x1) * multiplier)), 5))

  retstring += "y = " + str(onecheck(slope)) + "x " + str(zerocheck(negorpos(b)))
  if checkint(bdecimal) != True or checkint(slopedecimal) != True:
    retstring += "\n\nAnd in decimal form: " + "y = " + str(onecheck(slopedecimal)) + "x " + str(zerocheck(negorpos(bdecimal)))
  return retstring


def derivefunction(mylist):
  if len(mylist) == 1:
    return [0]
  if len(mylist) == 2:
    return [mylist[0]]
  result = []
  for i in range(len(mylist) - 1):
    result.append(mylist[i] * (len(mylist) - i - 1))
  return result

def derive(mylist, dernum):
  mypoly = makepolynomial(mylist)
  if dernum < 50 and dernum > 0:
	  for i in range(dernum):
	    mylist = derivefunction(mylist)
  else:
  	mylist = [0]
  return "The " + addth(dernum) + " derivative of\n\n" + mypoly + " = " + makepolynomial(mylist)

def radsimplifywithwork(num):
  num = abs(num)
  num = float(num)
  denominator = 1
  while checkint(num) == False:
      num = round(num * 100, 8)
      denominator *= 10
  numerator, inroot, nada = simpleradicalformat(num)
  return "\nFirst, we must scale this to be an integer value. To do that we will multiply by " + insertcommas(denominator ** 2) + " and create a denominator equal to this value and leaving us with:\n√" + insertcommas(num) +  " / " + insertcommas(denominator ** 2)  + "\n\n\nFrom here, we will simplify the radical on both the top and bottom. Looking at the denominator first, the square root of " + insertcommas(denominator ** 2) + " is just \n" + insertcommas(denominator) + ".\n\nIn order to simply the numerator, we can take out a " + insertcommas(numerator**2) + " leaving us with\n" + insertcommas(numerator) + "√" + insertcommas(inroot) + "\n\n\nHowever, now we need to simplify the entire expression, leaving us with: \n\n" + fractiondisplaypythag(numerator, denominator, inroot)

def areaofpolygon(num, side):
  area = round(((side ** 2) * num) / (4 * tan(pi / num)), 5)
  if num < 3:
  	return "Try Again"
  return "The area of your " + insertcommas(num) + " - gon with a side length of " + insertcommas(side) + " = " + insertcommas(area)


def sigfigcounter(num):
  num = str(num)
  num = num.replace("-", "")
  test = float(num)
  mylist = split(num)
  i = 0
  while mylist[i] == 0:
    i += 1
  mylist = mylist[i:]
  if mylist.count(".") == 0:
    mylist.reverse()
    i = 0
    while int(mylist[i]) == 0:
      i += 1
    mylist = mylist[i:]
    mylist.reverse()
  elif floor(test) == 0:
    i = 0
    while mylist[i] == "0" or mylist[i] == ".":
      i += 1
    mylist = mylist[i:]
  try:
    mylist.remove(".")
  except ValueError:
    test = "fries"
  return num + " has " + str(len(mylist)) + " significant figures\n\nThey are:\n" + makestring(mylist)


def finalcalc(currentgrade, wantgrade, percent):
  currentgrade, wantgrade, percent = intconvert(currentgrade), intconvert(wantgrade), intconvert(percent)
  percent = percent / 100
  if percent >= 1 or percent <= 0 or currentgrade < 0 or wantgrade <= 0:
    return "Invalid inputs - check that percent is between 1-99 and grades are positive"
  finalgrade = round(((wantgrade - ((1 - percent) * currentgrade))/percent), 2)
  return "If your current grade is " + str(intconvert(currentgrade)) + "% and your final is worth " + str(intconvert(percent * 100)) + "% of your grade,\nyou need a " + str(intconvert(finalgrade)) + "% on your final in order to get a " + str(intconvert(wantgrade)) + "% in your class."

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/shortcalcs/")
def shortcalcs():
	return render_template("shortcalcs.html")

@app.route("/ContactUs/")
def about():
	return render_template("contactus.html")

@app.route("/data/", methods=["POST", "GET"])
def datahome():
	if request.method == "POST":
		mydata = request.form["data"]
		try:
			mydata = pullnums(mydata)
			urladd = dashedmakestring(mydata)
		except:
			return redirect(url_for("datahome"))
		return redirect(url_for("dataresults", data = urladd))
	else:
		return render_template("dataindex.html")

@app.route("/data/<data>", methods=["POST", "GET"])
def dataresults(data):
	mylist = data.split("&")
	for i in range(len(mylist)):
		mylist[i] = intconvert(mylist[i]) 
	try:
		result = MAD(mylist)
	except:
		return redirect(url_for("datahome"))
	finresults = result.split("\n")
	return render_template("datadisplay.html", content=finresults)


@app.route("/numinfo/", methods=["POST", "GET"])
def numinfohome():
	if request.method == "POST":
		mydata = request.form["data"]
		try:
			mydata = (pullnums(mydata))[0]
		except:
			return redirect(url_for("numinfohome"))
		return redirect(url_for("numinforesults", data = mydata))
	else:
		return render_template("numinfoindex.html")

@app.route("/numinfo/<data>", methods=["POST", "GET"])
def numinforesults(data):
	try:
		result = int(commasgone(data))
	except:
		return redirect(url_for("numinfohome"))
	if result == 0:
		return redirect(url_for("numinfohome"))
	results = displaynuminfo(result)
	finresults = results.split("\n")
	try:
		return render_template("numinfodisplay.html", content=finresults)
	except:
		return redirect(url_for("numinfohome"))


@app.route("/synthetic/", methods=["POST", "GET"])
def synthetichome():
	if request.method == "POST":
		try:
			mydata = request.form["data"]
			rvalue = request.form["rvalue"]
			mydata = pullnums(mydata)
			urladd = dashedmakestring(mydata)
		except:
			return redirect(url_for("synthetichome"))
		return redirect(url_for("syntheticresults", data = urladd, rvalue = rvalue))
	else:
		return render_template("syntheticindex.html")

@app.route("/synthetic/<data>/<rvalue>", methods=["POST", "GET"])
def syntheticresults(data, rvalue):
	mylist = data.split("&")
	for i in range(len(mylist)):
		mylist[i] = intconvert(mylist[i])
	divisor = intconvert(rvalue)
	try:
		result = synthetic(mylist, divisor)
	except:
		return redirect(url_for("synthetichome"))
	finresults = result.split("\n")
	try:
		return render_template("syntheticdisplay.html", content=finresults)
	except:
		return redirect(url_for("synthetichome"))

@app.route("/quad/", methods=["POST", "GET"])
def quadhome():
	if request.method == "POST":
		try:
			adata = float(request.form["data1"])
			bdata = float(request.form["data2"])
			cdata = float(request.form["data3"])
			try:
				Input = request.form["Input"]
			except:
				Input = "False"
		except:
			return redirect(url_for("quadhome"))
		return redirect(url_for("quadanswerpage", a=adata, b=bdata, c=cdata, Input =Input))
	else:
		return render_template("index.html")


@app.route("/quad/<a>/<b>/<c>/<Input>", methods=["POST", "GET"])
def quadanswerpage(a, b, c, Input):
	hi = (quadtotal(a, b, c, Input))
	result = hi.split("\n")
	try:
		return render_template("display.html", content=result)
	except:
		return redirect(url_for("quadhome"))


@app.route("/base/", methods=["POST", "GET"])
def basehome():
	if request.method == "POST":
		try:
			a = str(request.form["data1"])
			a = a.strip()
			b = int(request.form["data2"])
			c = int(request.form["data3"])
		except:
			return redirect(url_for("basehome"))
		return redirect(url_for("baseanswerpage", a = a, b=b, c=c))
	else:
		return render_template("baseconverter.html")


@app.route("/base/<a>/<b>/<c>", methods=["POST", "GET"])
def baseanswerpage(a, b, c):
	try:
		a = a.strip()
		b = int(b)
		c = int(c)
		hi = (basedisplay(a, b, c))
		result = hi.split("\n")
		return render_template("basedisplay.html", content=result)
	except:
		return redirect(url_for("basehome"))

@app.route("/heron/", methods=["POST", "GET"])
def heronhome():
	if request.method == "POST":
		try:
			adata = float(request.form["data1"])
			bdata = float(request.form["data2"])
			cdata = float(request.form["data3"])
		except:
			return redirect(url_for("heronhome"))
		return redirect(url_for("heronanswerpage", a=adata, b=bdata, c=cdata))
	else:
		return render_template("heronindex.html")


@app.route("/heron/<a>/<b>/<c>", methods=["POST", "GET"])
def heronanswerpage(a, b, c):
	hi = (heron(a, b, c))
	result = hi.split("\n")
	return render_template("herondisplay.html", content=result)

@app.route("/combine/", methods=["POST", "GET"])
def combinehome():
	if request.method == "POST":
		userstring = request.form["data"]
		userstring = userstring.replace("/", "!")
		return redirect(url_for("combineresults", userstring = userstring))
	else:
		return render_template("Combinationsindex.html")

@app.route("/combine/<userstring>", methods=["POST", "GET"])
def combineresults(userstring):
	try:
		userstring = userstring.replace("!", "/")
		result = permandcomb(str(userstring))
	except:
		return redirect(url_for("combinehome"))
	finresults = result.split("\n")
	try:
		return render_template("Combinationsdisplay.html", content=finresults)
	except:
		return redirect(url_for("combinehome"))

@app.route("/pythagorean/", methods=["POST", "GET"])
def pythaghome():
	if request.method == "POST":
		try:
			adata = float(request.form["data1"])
			bdata = float(request.form["data2"])
			solvinginput = str(request.form["solvefor"])
		except:
			return redirect(url_for("pythaghome"))
		return redirect(url_for("pythaganswerpage", a=adata, b=bdata, solvinginput = solvinginput))
	else:
		return render_template("pythagindex.html")


@app.route("/pythagorean/<a>/<b>/<solvinginput>", methods=["POST", "GET"])
def pythaganswerpage(a, b, solvinginput):
	stupidvar = 1
	try:
		stupidvar += 1
	except:
		return redirect(url_for("pythaghome"))
	hi = (pythag(a, b, solvinginput))
	result = hi.split("\n")
	return render_template("pythagdisplay.html", content=result)

@app.route("/rationalroots/", methods=["POST", "GET"])
def rationalrootshome():
	if request.method == "POST":
		try:
			mydata = request.form["data"]
			mydata = pullnums(mydata)
			urladd = dashedmakestring(mydata)
		except:
			return redirect(url_for("rationalrootshome"))
		return redirect(url_for("rationalrootsresults", data = urladd))
	else:
		return render_template("rationalrootsindex.html")

@app.route("/rationalroots/<data>", methods=["POST", "GET"])
def rationalrootsresults(data):
	try:
		result = allrationalroots(data)
	except:
		return redirect(url_for("rationalrootshome"))
	finresults = result.split("\n")
	try:
		return render_template("rationalrootsdisplay.html", content=finresults)
	except:
		return redirect(url_for("rationalrootshome"))

@app.route("/baseoperations/", methods=["POST", "GET"])
def baseoperationshome():
	if request.method == "POST":
		try:
			userstring = str(request.form["data"]).replace("/", "!")
			userbase = int(request.form["base"])
			return redirect(url_for("baseoperationsresults", userstring = userstring, userbase = userbase))
		except:
			return redirect(url_for("baseoperationshome"))
	else:
		return render_template("baseoperationsindex.html")

@app.route("/baseoperations/<userstring>/<userbase>", methods=["POST", "GET"])
def baseoperationsresults(userstring, userbase):
	try:
		userstring = userstring.replace("!", "/")
		result = baseoperate(userstring, userbase)
	except:
		return redirect(url_for("baseoperationshome"))
	finresults = result.split("\n")
	return render_template("baseoperationsdisplay.html", content=finresults)

@app.route("/shortcalcs/slope/", methods=["POST", "GET"])
def slopeformhome():
	if request.method == "POST":
		try:
			x1 = float(request.form["x1"])
			x2 = float(request.form["x2"])
			y1 = float(request.form["y1"])
			y2 = float(request.form["y2"])
			return redirect(url_for("slopeformresults", x1 = x1, y1 = y1, x2 = x2, y2 = y2))
		except:
			return redirect(url_for("slopeformhome"))
	else:
		return render_template("slopeindex.html")

@app.route("/shortcalcs/slope/<x1>/<y1>/<x2>/<y2>", methods=["POST", "GET"])
def slopeformresults(x1, y1, x2, y2):
	try:
		x1, y1, x2, y2 = intconvert(x1), intconvert(y1), intconvert(x2), intconvert(y2)
		result = slopeform(x1, y1, x2, y2)
	except:
	 	return redirect(url_for("slopeformhome"))
	finresults = result.split("\n")
	return render_template("slopedisplay.html", content = finresults)

@app.route("/shortcalcs/derivative/", methods=["POST", "GET"])
def derivehome():
	if request.method == "POST":
		try:
			mylist = pullclosenums(request.form["poly"])
			dernum = float(request.form["dernum"])
			mystring = dashedmakestring(mylist)
			return redirect(url_for("deriveresults", mystring = mystring, dernum = dernum))
		except:
			return redirect(url_for("derivehome"))
	else:
		return render_template("deriveindex.html")

@app.route("/shortcalcs/derivative/<mystring>/<dernum>", methods = ["POST", "GET"])
def deriveresults(mystring, dernum):
	mylist = intconvertlist(mystring.split("&"))
	dernum = intconvert(dernum)
	try: 
		result = derive(mylist, dernum)
	except:
		return redirect(url_for("derivehome"))
	return render_template("derivedisplay.html", content = result.split("\n"))

@app.route("/shortcalcs/radical/", methods=["POST", "GET"])
def radicalhome():
	if request.method == "POST":
		try:
			num = float(request.form["num"])
			return redirect(url_for("radicalresults", num = num))
		except:
			return redirect(url_for("radicalhome"))
	else:
		return render_template("radicalindex.html")

@app.route("/shortcalcs/radical/<num>", methods=["POST", "GET"])
def radicalresults(num):
	try:
		return render_template("radicaldisplay.html", content = radsimplifywithwork(intconvert(num)).split("\n"))
	except:
		return redirect(url_for("radicalhome"))

@app.route("/shortcalcs/areaofpolygon/", methods=["POST", "GET"])
def areaofpolygonhome():
	if request.method == "POST":
		try:
			num = int(request.form["num"])
			side = float(request.form["side"])
			return redirect(url_for("areaofpolygonresults", num = num, side = side))
		except:
			return redirect(url_for("areaofpolygonhome"))
	else:
		return render_template("areaofpolygonindex.html")

@app.route("/shortcalcs/areaofpolygon/<num>/<side>", methods=["POST", "GET"])
def areaofpolygonresults(num, side):
	try:
		return render_template("areaofpolygondisplay.html", content = areaofpolygon(intconvert(num), intconvert(side)).split("\n"))
	except:
		return redirect(url_for("areaofpolygonhome"))

@app.route("/shortcalcs/sigfigs/", methods=["POST", "GET"])
def sigfigshome():
	if request.method == "POST":
		try:
			num = str(request.form["num"])
			return redirect(url_for("sigfigsresults", num = num))
		except:
			return redirect(url_for("sigfigshome"))
	else:
		return render_template("sigfigsindex.html")

@app.route("/shortcalcs/sigfigs/<num>", methods=["POST", "GET"])
def sigfigsresults(num):
	try:
		return render_template("sigfigsdisplay.html", content = sigfigcounter(num).split("\n"))
	except:
		return redirect(url_for("sigfigshome"))

@app.route("/shortcalcs/final/", methods=["POST", "GET"])
def finalhome():
	if request.method == "POST":
		try:
			currentgrade = float(request.form["currentgrade"])
			wantgrade = float(request.form["wantgrade"])
			percent = float(request.form["percent"])
			return redirect(url_for("finalresults", currentgrade = currentgrade, wantgrade = wantgrade, percent = percent))
		except:
			return redirect(url_for("finalhome"))
	else:
		return render_template("finalindex.html")

@app.route("/shortcalcs/final/<currentgrade>/<wantgrade>/<percent>", methods=["POST", "GET"])
def finalresults(currentgrade, wantgrade, percent):
	try:
		return render_template("finaldisplay.html", content = finalcalc(currentgrade, wantgrade, percent).split("\n"))
	except:
		return redirect(url_for("finalhome"))


if __name__ == "__main__":
  app.run(debug=True)