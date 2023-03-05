# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and 
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.

echo "extracting data"

cut -d":" -f1,3,6 /etc/passwd > extracted_data.txt

echo "transformaing data"

tr ":" "," < extracted_data.txt > transformed_data.csv

echo "loading data"

echo "\c template1;\COPY users FROM '/home/project/transformed_data.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=localhost

echo '\c template1 \\SELECT * from users;' | psql --username=postgres --host=localhost
