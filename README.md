# Election_Analysis

## Overview of Election Audit
For Deliverables one and tow we had to modify our initial code to include data pertaining to county turnout. With fairly basic and rudimentary additions to the code, we were able to achieve this. Almost none of the existing code that focused on the number of votes for each candidate needed to be changed at all. 

![Screenshot_of_Terminal](https://user-images.githubusercontent.com/66881241/89145499-d3038f00-d505-11ea-96a1-382391c401c9.png)


### Changes Made
We essentially had to do the same things for counties that was initially in the code for candidates. This included making a "county votes" dictionary and a list to hold the names of all of our counties. Likewise, I used indexing to initialize the variable for county name at index 2. 

![Screen Shot 2020-08-02 at 8 53 15 PM](https://user-images.githubusercontent.com/66881241/89144505-d6494b80-d502-11ea-9bd7-d0a1295d9de6.png)

Then we used several conditionals like we did with candidates to add new counties to the list while tallying votes to said counties in the counties dictionary as we looped through the rows on the csv file.

![Screen Shot 2020-08-02 at 8 53 43 PM](https://user-images.githubusercontent.com/66881241/89144466-bc0f6d80-d502-11ea-96db-ce810108c776.png)

Similarly, to print out the largest county by votes, we had to create variables for largest county, county votes, and county percentages which  we assigned to the appropriate county and then printed to the terminal as well as wrote to the election results file.

![Screen Shot 2020-08-02 at 8 53 56 PM](https://user-images.githubusercontent.com/66881241/89144409-8ff3ec80-d502-11ea-93df-89da561457e3.png)

There were some differences between what I printed on the terminal and what was written to the txt file. Making these changes warranted some tinkering with \n in strategic locations.

## Election Audit Results
- Total Votes: 369,711

Winner of the Election:
- Diana DeGette

Votes By Candidate:
- 85,213 votes (23.0%) for Charles Casper Stockham
- 272,892 votes (73.8%) for Diana DeGette
-11,606 votes (3.1%) for Raymon Anthony Doane

The results of the election by county:
* Denver county had the largest county turnout 
* Jefferson county had the second largest
* Arapahoe had the third largest. 

The Percentage Breakdown by County:
- 82.8% of the votes came from Denver. 
- 10.5% came from Jefferson.
- 6.7% came from Arapahoe. 

## Election Audit Summary

### Challenges
There were some bumps along the way. I kept getting an indentation error, however, over time I came to understand this is really just a syntax error. The changes I made to fix this error almost never involved indentation and almost always involved some sort of incorrect syntax. Getting the terminal print and the txt file just how they needed to be with the spaces and dashes was difficult, but I was able to adapt and eventually got it just right. I was new to file paths at the beginning of this module, so working with them in the code certainly presented challenges of its own but I now have a robust understanding of this concept and how to keep it working in my code even when I change the location of my files. The changes we made to make this election audit include county information was relatively painless and straightforward. It involved repeating what we did initially in the code with the candidates which speaks to the usefullness of this code pattern involving the use of lists and dictionaries to tally numbers in relation to names. 

![Screen Shot 2020-08-02 at 8 52 45 PM](https://user-images.githubusercontent.com/66881241/89144535-ebbe7580-d502-11ea-9cac-bc91921a3f2a.png)


### Summary
This script can be used for any election so long as the format of the csv file used has the same information in the same columns as the election_results.csv used in this analysis. Furthermore, the csv file must be in the same location relative to this python script in order to function properly. Some other minor changes will need to be made to the Python script regarding the file paths of the csv it is using and the file you will want to have the results written to. This is an easy process and this script will be an election option to use for further elections in the future.
