# README file of Question 4

## Question

Taking into account the student’s progress and goals, what is the best set of kanji / vocab to teach to them next?

## Strategy

**Dependencies: Need "cleaned_link.csv", result from Question 1**

These files can be run in any order so long as Question1 has been run. Output is inline.

* FindLevelCorrelations.ipynb Compare sources and sequences to try to determine the optimal learning sequence to follow to learn how to read a given source. 
* QueryByLevel.ipynb Given that the user has completed some level of kanji from a learning sequence (such as "N5" or "Grade 6"), tell them what kanji to learn next.
