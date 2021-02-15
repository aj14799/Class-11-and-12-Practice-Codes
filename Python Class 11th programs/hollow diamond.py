def HollowDiamond():
    l = int(input("Enter odd Value:"))
    if l%2==0:
        print("Don't give Even value")
    try:
        l = int(input("Enter odd Value:"))
    except:
        print("Error type again")
            

    # Initialize first row; this will create a list with a
    # single element, the first row containing a single star
    rows = ['*']

    # Add half of the rows; we loop over the odd numbers from
    # 1 to l, and then append a star followed by `i` spaces and
    # again a star. Note that range will not include `l` itself.
    for i in range(1, l, 2):
        rows.append('*' + ' ' * i + '*')

    # Mirror the rows and append; we get all but the last row
    # (the middle row) from the list, and inverse it (using
    # `[::-1]`) and add that to the original list. Now we have
    # all the rows we need. Print it to see what's inside.
    rows += rows[:-1][::-1]

    # center-align each row, and join them
    # We first define a function that does nothing else than
    # centering whatever it gets to `l` characters. This will
    # add the spaces we need around the stars
    align = lambda x: ('{:^%s}' % l).format(x)

    # And then we apply that function to all rows using `map`
    # and then join the rows by a line break.
    diamond = '\n'.join(map(align, rows))

    # and print
    print(diamond)
HollowDiamond()
