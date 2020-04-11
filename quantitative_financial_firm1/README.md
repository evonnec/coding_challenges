### Task:  
  
- Calculate the following based on the attached files and cost rules below.  
- Total number of orders  
- Total number of shares traded  
- Total notional value in CHF traded  
- Total trading fees incurred  
  
Please also provide any code, files, or documents used to find the solutions.  Feel free to use any approach (Python, C#, R, Excel etc..), as long as you can show how you got your results.  
  
#### Attached Files:  
- SIX_Trades.csv is a file of trades and partial trades  
- SIXBlueChips.csv contains a list of all SIX Swiss Blue Chip companies  
  
#### Cost Rules:  
Each order is charged trading fees which are the sum of a fixed portion and a variable rate based on the notional value executed.  
  
Use the attached stock list to determine whether a stock is a blue chip or not.  
  
#### Fee Schedule:  
- Each order is charged a fixed fee of .01 CHF. If an order has multiple executions (for example two partial fills), this fee is not charged twice.  
- Each order for a blue chip stock is charged a value based fee of 1 basis point.  
- Each order for non-blue chip stocks is charged a value based fee of 2 basis points.  
- Each order for a non-blue chip stock is subject to a minimum charge of 1 CHF (for example if the calculated fee for an order is .01 fixed + .5 CHF value based = .51 CHF, it will be charged 1 CHF instead)

### Coding Decisions Choices:
  
- I first implemented the challenge using VBA in Excel as at the time I was more comfortable with it. However I didn't love my implementation of an edge case as the for loops and while wends are not good practice for every single thing, generally speaking.  
  
- After submission, I at some point found a pocket of time and implemented the same in Python and Pandas using a Jupyter Notebook. This was far easier as there are reliable libraries that simply just do the thing you ask of it, and quickly too. After doing so, it appeared I did not account for something in an edge case in my VBA implementation, which isn't all surprising.  
  
- Lesson learned, don't try to reinvent the wheel with subpar tooling. Go for the tools that don't require extra headache to implement correctly, even if you don't know those tools as well. Good libraries are everything.  
  