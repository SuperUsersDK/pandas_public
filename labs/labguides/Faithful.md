### K-means clustering med scipy

## Old Faithful Geyser Data

# Description:

     Waiting time between eruptions and the duration of the eruption
     for the Old Faithful geyser in Yellowstone National Park, Wyoming,
     USA.

# Format:

     A data frame with 272 observations on 2 variables.

  *     [,1]  eruptions  numeric  Eruption time in mins 
  *     [,2]  waiting    numeric  Waiting time to next eruption (in mins) 

For more clustering data does it not makes sense to calculate means, median, spread, etc. for the full dataset.

Data from the Geyser "Old Faithful" is an example on 2-cluster data. "Old Faithful" is in the Yellowstone Nation Park, Wyoming, USA.

# Exercises:
1. Read the CSV-file called "Faithful.csv" into a dataframe
2. Plot the observations as a scatter plot. The X-axis must show eruptions. The Y-axis must be waiting.
3. Add another column called "Group". The values in groups must be which group the observation is located in when using k-means with two centers.
4. Plot the observations as a scatter plot with different colors based on the on the value in "Group" column.
5. Calculate the mean for both columns, both for all rows and and based on groups

For fler-clustering data giver gennemsnit, median, spredning etc. ikke mening for det fulde datasæt.
Data fra geyseren "Old Faithful" er et eksempel på 2-cluster data.
"Old Faithful" befinder i Yellowstone Nation Park, Wyoming, USA.

# Opgaver
  * Indlæs csv-filen "Faithful.csv" ind i data-frame.
  * Afbild de 272 observationer med europtions på x-aksen og waiting på y-aksen.
  * Tilføj en ekstra søjle med navn "Gruppe". Værdierne i "Gruppe", som udregnes vha.
    k-means cluster med to centre.
  * Afbild de 272 obersvationer med forskellige farver baseret på værdien i "Gruppe"
  * Beregn gennemsnitlig værdier for waiting og eruptions for hele datasæt og for 
    hver af de to grupper.



