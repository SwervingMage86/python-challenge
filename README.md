# python-challenge

# PyBank

# Step 1:

First thing I did was import the os and csv modules and delcare a path to be able to read the csv file.

# Step 2:

I used a with statement to open the csv file and used a for loop inside a sum function to count the number of rows.
I ended up with an error because I had a string in the rows yet I was starting with an integer of 1.
I corrected this by skipping the header with the next function. 
I printed the count at this point to verify it was counting all the rows. Then was able to clean up the print statement from there.

# Step 3:

I attempted to use another for loop to go through the rows and add up all the values in the second column using a sum function, starting with a variable of net=0. However I kept getting errors.
I then tried to add all the values of the second column to a list, eliminating the net variable and summing them from there. This worked but my values kept coming out as 0.
I solved this by creating another with statement to read the file again, skip the header again, and loop through rows apppending values to monthly profit list.
Printing sum of this list gave me the solution I was looking for. Then cleaned up the print statement.

# Step 4:

Finding the monthly change was really tricky and took me the most amount of time.
Without going through all of my frustrated attempts, I was finally able to figure out that setting the first month to the first value of the list I could use a for loop to go through the monthly profit statement I created.
From there I used an if/else statement to pull the data I wanted by basically saying if the value of a row equals the same value of the first row, set it as a previous month variable.
If this was not true then add the value of the current month subtracted by the set previous month to a new list then reset the current month as the previous month variable so the loop would continue correctly.
Again, this was frustrating and took me some time to figure out.
Once I had my new list I found average change by setting a variable to equal the sum of my new list and dividing it by my count of rows(minus 1).
I had to use minus one since the change of the first month wasn't needed and I had one less value in this list then the number of recorded months.
I printed this to make sure it was coming out correct then cleaned up the print statement. 

# Step 5:

To find the greatest profit and loss changes I used the max and min functions.
Printed to verify, then cleaned it up.
To match this up with the month I used and index function to find where in the list the max and min were occuring
I printed this to verify it was returning correctly.
I then assigned this to a variable so it would be easier to print to validate it.
I then went back to my for loop where I assigned the monthly profits to a list and decided to created a list of the other column (months) so I could reference it.
I pulled from the matching index of my month list, unfortunately at first this didn't come out how I wanted, it was one month behind.  Then I remembered my change in profit list had one less value, so I had to add one to the index number to pull the correct month.
I assigned this value its own variable to make it easier to print.
I printed then printed to validate accuracy

# Step 6:

I cleaned up how the results printed in the terminal then wrote a seperate with statement to write the results in a text file in another folder.

# PyPoll

# Step 1:

I imported the os and csv files and opened the file to read the csv

# Step 2:

I counted the rows the same way as the previous code to get the total vote count
Printed to verify and cleaned.

# Step 3:

Again, I had trouble getting another for loop to run without reopening the file again
I then made another for loop using an if statement to append votes for each candidates to separate lists.
At first I was just using one candidate to validate accuracy of the code, but I had nested another for loop inside my first for loop to count up all the votes for a particular candidate.
This was taking FOREVER!
I moved the count loop outside of the first for loop and this ran WAY faster.
I finished addind the rest of the candidates.
Printed the values to verify.

# Step 4:

I added formulas to determine the percentage change and added a round function in the statement so I wasn't coming out with an annoying amount of decimal places.
I cleaned up this print statement.

# Step 5:

I made two seperate lists, one for the count of each candidate and one for each candidate's names.
I had to ensure that the indexes matched respectively so that when I referenced the index of the max of the vote list, it would output the correct candidate as winner.
Printed and cleaned.

# Step 6:

Made sure print statements were clean and then outputed results to terminal as well as seperate file.