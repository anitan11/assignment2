Author: Anita Ruud Nilsen
Contact: anitarn5@gmail.com

This file is placed in this directory because I thought it was a good logical position.

An university assignment - Assignment 2

This application is made to make the calculation of how much energy a horse needs easier. It is part of
the learnpythonthehardway.org-exercises. But instead of making a game, I made this application. This is 
because I wanted to make something else than everybody else, and have the opportunity to include different
segments of code.

I have used most of my time to get this last exercise to work. Therefore all the errors that I have
fixed in exercise 52 will still be present in the earlier exercises.

The theory behind this application is something I learned during my years on an agriculture school some 
years ago, and it was presented verbal to the class. That is why I don't have any references to the theory.

My last problem was that the calculations came out wrong. I figured out what I had done wrong. I remembered
that a horses weight can not be calculated from the horses hight. You need to make a measurement around 
the horses chest, where girt is lying. Then take this measurement in cm and multiply it by 6,25 and 
subtract 625.

chest scope * 6,25 - 625

I fixed this by adding a new field in the form, and the user has to figure out the horses weight on 
their own.

I think I could have done a lot more with this application, like adding CSS, create error messages and 
so on. But I also think that I had to limit it to get it done since we have more assignments to do.

One thing I didn't figure out is how to import classes from another folder. That is why there is a
modules.py-file in both the bin-direcorty and the program-directory.