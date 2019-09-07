# Tutorial dari https://youtu.be/AhSvKGTh28Q

List = [1,2,'a',3.14]

# ListComprehensions = [expr for val in collection ]

# Without list comprehensions

squares = []
for i in range(1,101):
    squares.append(i**2)

print(squares)

# With list comprehensions

squares2 = [i**2 for i in range(1,101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1,101)]
print(remainders11)

movies = ['Star Wars', 'Gandhi', 'Casablanca', 'Shawshank Redemption', 
          'Toy Story', 'Gone with the wind', 'Citizine Kane', "It's a wonderful life", 
          'The wizard of Oz', 'Gattaca', 'Rear window', 'Ghostbusters', 'To kill a mockingbird',
          'Good will hunting', '2001: A space odyssey', 'Raiders of the lost ark', 'Groundhog day',
          'Close encounters of the third kind']

gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)
print(gmovies)

rmovies = [title for title in movies if title.startswith('C')]
print(rmovies)

movies2 = [('Citizen Kane', 1941), ('Spirited Away', 2001), ("It's a wonderful life", 1946), ('Gattaca', 1997),
           ('No country for old man', 1997), ("Rear window", 1954), ('The Lord of Rings: The fellowshing of the rings', 2001),
           ('Groundhog day', 1993), ('Close encounters of the third kind', 1977), ('The royal tennenbaums', 2001),
           ('The aviator', 2004), ('Raiders of the lost ark', 1981)]

pre2k = [title for (title, year) in movies2 if year < 2000]
print(pre2k)

# Scalar multiplication

v = [2, -3, 1]
print(4*v)

w = [4*x for x in v]
print(w)

# Cartesian Products
# if A and B are sets, then the Cartesian Products is the sets of pairs (a,b)
# wheres 'a' is in A and 'b' is in B

# A x B = {(a,b) | a E A, b E B}

# Example
# A = {1,3}
# B = {x,y}
# Then the Cartesian Products is :
# A x B = {(1,x), (1,y), (3,x), (3,y)}

C = [1, 3, 5, 7]
D = [2, 4, 6, 8]

cartesian_products = [(a,b) for a in C for b in D]
print(cartesian_products)
