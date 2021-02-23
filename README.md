The original program only works with key lengths of 7.
I have expanded the program to accept and decrypt key
lengths of 5 to 9 without issue. The program requires 
a user to do the frequency analysis by themselves and 
then enter the key they compute (after closing graph window)
The program should be able to strip out non ascii characters
but can be finicky. I have included cipher text that correctly
decrypts into "Harry Potter" plaintext. Also note that for some
reason strings copied from html webpages and pasted directly into
the command line seem to break the program. Still working out why.