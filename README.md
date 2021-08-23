# surfs_up

## Overview of the analysis: 
The purpose of this analysis is to gather more information about temperature statistics for June and December in order to determine if running a surf shop is sustainable year around.

### Deliverables:
1. Determine the Summary Statistics for June
2. Determine the Summary Statistics for December

## Resources:
* Python
* Pandas functions and methods
* SQLAlchemy 
* hawaii.sqlite database

### Goal:
Using Python, Pandas functions and methods, and SQLAlchemy, filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the months of June and December. Convert these temperatures to a list, create a DataFrame, and generate the summary statistics.

## Results: 
1. Determine the Summary Statistics for June

* In June there was a total count of 1700, mean of 74.9, min of 64.0 and max of 85.0
<img width="120" alt="Deliverable1" src="https://user-images.githubusercontent.com/85847344/130370830-9995ec78-6fc8-4b9d-973f-737e28f8bfd3.png">

2. Determine the Summary Statistics for December
* In December we had a total count of 1517, mean of 71.0, min of 56.0 and max of 83.0
<img width="113" alt="Deliverable2" src="https://user-images.githubusercontent.com/85847344/130370833-b77e86c6-782e-4505-afea-62036ca8a5a3.png">

* As seen from the images above...
  * the average tempurature only differs by about 4 degrees over 6 months. 
  * the coldest the tempurature reaches is about 56 degrees F in the month of December.
  * the count shows that there are clearly enough data points to provide a sufficient analysis
 
* Standard deviation is 3.25 in June and 3.75 in December, which makes a .5 difference in the two different seasons. This therefore proves tempurature would not be the issue in running a surf shop year around.

## Summary: 
Based on the data, there is a clear analysis of what the tempurature would be like year around. Although, there are other attributes to the weather that could affect the successfulness of this surfshop. An example of this is precipitation. This shows that there can be additional quieries to run in order to have a better understanding of whether or not people can come and visit the shop. If given more access to more data from the area, then even more quieries could be run. From there, this will help decide how to build the shop and, furthermore, what areas would make this a more prominent location for visitors to come.
