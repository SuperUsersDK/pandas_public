# Flights - a data science case story

The file `datasets/flights.csv` contains data about flights between the airports in Houston: IAH (George Bush Intercontinental) and HOU (Houston Hobby) in the year 2011.

1. Read the file 'flights.csv' into a pandas dataframe. Remember to parse dates correctly.
   Hint: Use a list of lists to use more than one column for the date parser. Or a dictonary
   Check that you have read 227496 rows and 19 columns.

2. How many flights where leaving Houston on the 1st of january?

3. How many flights did American Airlines (AA) and United Airlines (UA) have leaving Houston?

4. How many flights (in percent) were delayed (DepDelay) more than 60 minutes?

5. Add a column called Speed that must contain the result of the calculation: `Distance/Airtime*60`

6. Add a column called AvgDelay. It must contain the average delay on the arrival (ArrDelay) grouped on the destination (Dest).

7. Sort the dataframe on AvgDelay with the smallest values first. Show the first six rows.
   The output should be:
```
   BKG -16.2
   BFL -13.2
   GRK -8.3
   MTJ -0.451
   HDN 0.0865
   SNA 0.358
```
Visualize all the output.


8. Add a column which must contain the number of flights per day. Call the column FlightCount.

9. Sort the dataframe on FlightCount with the largest values first. Sort afterwards on Month and DayOfMonth. Show the first six rows.
   The output should be:
```
   Month DayOfMonth flight_count
   8     4           706
   8     11          706
   8     12          706
   8     5           705
   8     3           704
   8     10          704
```

10. How many in percent in average per airliner was cancelled (Cancelled) or diverted (Diverted)?
    You should get 1.85 pct cancelled for American Airlines (AA) and 0.185 pct diverted for American Airlines (AA)
    Visualize your result for all airlines.



   
