def i ():
    print("             *********************               ")
    for i in range (11) :
        print("                      *                      ")
    print("             *********************               ")


def love_symbol():

   ''' for i in range(0, 5):
        print(" " * (15 - i), end=" ")

        for j in range(0, i ):
           print( "*",  end=" ")
        i += 1
        print()'''

   # define size n = even only
   n = 8

   # so this heart can be made n//2 part left,
   # n//2 part right, and one middle line
   # i.e; columns m = n + 1
   m = n + 1

   # loops for upper part
   for i in range(n // 2 - 1):
       for j in range(m):

           # condition for printing stars to GFG upper line
           if i == n // 2 - 2 and (j == 0 or j == m - 1):
               print("*", end=" ")

           # condition for printing stars to left upper
           elif j <= m // 2 and ((i + j == n // 2 - 3 and j <= m // 4) \
                                 or (j - i == m // 2 - n // 2 + 3 and j > m // 4)):
               print("*", end=" ")

           # condition for printing stars to right upper
           elif j > m // 2 and ((i + j == n // 2 - 3 + m // 2 and j < 3 * m // 4) \
                                or (j - i == m // 2 - n // 2 + 3 + m // 2 and j >= 3 * m // 4)):
               print("*", end=" ")

           # condition for printing spaces
           else:
               print(" ", end=" ")
       print()

   # loops for lower part
   for i in range(n // 2 - 1, n):
       for j in range(m):

           # condition for printing stars
           if (i - j == n // 2 - 1) or (i + j == n - 1 + m // 2):
               print('*', end=" ")


           # condition for printing spaces
           else:
               print(' ', end=" ")

       print()


def u_symbol():
    print()
    print()
    for i in range (6):
        print(" "*15 , '*'," " * 10, '*')

    print (" "*15, '*'*14)

i()
love_symbol()
u_symbol()