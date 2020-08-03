# Election_Analysis

## Overview of Election Audit
For Deliverables one and tow we had to modify our initial code to include data pertaining to county turnout. With fairly basic and rudimentary additions to the code, we were able to achieve this. Almost none of the existing code that focused on the number of votes for each candidate needed to be changed at all. 

### Changes Made
We essentially had to do the same things for counties that was initially in the code for candidates. This included making a "county votes" dictionary and a list to hold the names of all of our counties. Likewise, I used indexing to initialize the variable for county name at index 2. 

![Screen Shot 2020-08-02 at 8 53 15 PM](https://user-images.githubusercontent.com/66881241/89144505-d6494b80-d502-11ea-9bd7-d0a1295d9de6.png)

Then we used several conditionals like we did with candidates to add new counties to the list while tallying votes to said counties in the counties dictionary as we looped through the rows on the csv file.

![Screen Shot 2020-08-02 at 8 53 43 PM](https://user-images.githubusercontent.com/66881241/89144466-bc0f6d80-d502-11ea-96db-ce810108c776.png)

Similarly, to print out the largest county by votes, we had to create variables for largest county, county votes, and county percentages which  we assigned to the appropriate county and then printed to the terminal as well as wrote to the election results file.

![Screen Shot 2020-08-02 at 8 53 56 PM](https://user-images.githubusercontent.com/66881241/89144409-8ff3ec80-d502-11ea-93df-89da561457e3.png)

There were some differences between what I printed on the terminal and what was written to the txt file. Making these changes warranted some tinkering with \n in strategic locations.

## Election Audit Results
The results of the election were that Denver county had the largest county turnout followed by Jefferson county and then Arapahoe. 82.8% of the votes came from Denver, 10.5% came from Jefferson, and 6.7% came from Arapahoe. This is generally what I would expect.

## Election Audit Summary

### Challenges
There were some bumps along the way. I kept getting an indentation error, however, over time I came to understand this is really just a syntax error. The changes I made to fix this error almost never involved indentation and almost always involved some sort of incorrect syntax. Getting the terminal print and the txt file just how they needed to be with the spaces and dashes was difficult, but I was able to adapt and eventually got it just right. I was new to file paths at the beginning of this module, so working with them in the code certainly presented challenges of its own but I now have a robust understanding of this concept and how to keep it working in my code even when I change the location of my files.

### Summary
The changes we made to make this election audit include county information wasa relatively painless and straightforward. It involved repeating what we did initially in the code with the candidates which speaks to the usefullness of this code pattern involving the use of lists and dictionaries to tally numbers in relation to names. 

![Screen Shot 2020-08-02 at 8 52 45 PM](https://user-images.githubusercontent.com/66881241/89144535-ebbe7580-d502-11ea-9cac-bc91921a3f2a.png)

Similarly, the method of assigning a visual presentation of the data and then assigning it to a variable that we later print is likely a method of coding that makes this code all the more readable and sleek.
