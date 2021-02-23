The original program only works with key lengths of 7.
I have expanded the program in crackV2.py to accept and decrypt key
lengths of 5 to 9 without issue. The program requires 
a user to do the frequency analysis by themselves and 
then enter the key they compute (after closing graph window)
The program should be able to strip out most non ascii characters
but can be finicky. I have included cipher text that correctly
decrypts into "Harry Potter" plaintext. Also note that for some
reason strings copied from html webpages and pasted directly into
the command line seem to break the program. Still working out why. If
I paste into a .txt and delete new lines it seems to work. Final note,
this program relies on large inputs to find common trigrams so strings of a few
sentences wont work. 
P.S if I get the time I will be refactoring this heavily 
to adhere to OOP and the like.
Thanks!