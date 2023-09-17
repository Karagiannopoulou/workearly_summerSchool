# Final assignment
1. Firstly, I have opened the MySQL Workbench program and imported the dataset as requested.
   Then, I performed the SQL query that appeared with the name "finance_liquor_sales_limitedbyYEAR.sql".
   As can be seen, I selected all the columns in the dataset and filtered the data records according to the date range (2016-2019).
   Finally, I ordered the dataset based on dates and exported it as instructed in the tutorial.
   
2. I used PyCharm (Python IDE) and the pandas library to analyse the dataset. The code snippet denoted as "finalAssignment.py"
   I created a new column, called "percentage", which will contain the percentage of sales for each product,
   divided by the sum of sales of the stores located in the same zip code (i.e., area).
   I created a second dataframe, containing only the columns that were necessary, and identified the index of the product
   and had the highest sales.
   Finally, with the iloc function, I managed to extract only the rows declared as the most popular products,
   an outcome that was saved in CSV format () so as to be able to get imported into Tableau.

3. In the public Tableau, I imported the CSV as a text file.
   I included in rows and columns, the longitude, and latitude in order to generate a geographic map.
   I fixed 27 names of cities that couldn't be identified automatically.
   Eventually, I represented the sales as classified elements, altering the size of the circle based on the amount of sales.
   The values of stores and cities were represented as labels, and the items were differentiated based on colour.
   All the processing chain and the output result can be found in xx and xx files. 

    
   
    
   

