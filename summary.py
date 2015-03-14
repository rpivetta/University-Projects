'''
# summary.py. Sixth programming project for CIS 211 (WQ 2015).


# Author: Ricardo Pivetta.

# This module fill all the requirements for project six, no extras.

'''
import sqlite3
import sys
from datetime import *

if __name__ == "__main__":
  #setting the connection with the sql
  con = sqlite3.connect('sakila211.db')
  cursor = con.cursor()

  date_format = "%Y-%m-%d %H:%M:%S.%f"
  date_format_display = '%m-%d-%Y'
  total = 0
  #getting the arguments
  lname = sys.argv[1]
  year = sys.argv[2]
  month = sys.argv[3]

  #running the query to select everything that I need from the database
  query = "select customer.first_name, film.title, customer.last_name, rental.rental_date, film.rental_rate, rental.return_date, film.rental_duration " \
          "  from customer "\
          "  join rental "\
          "    on customer.customer_id = rental.customer_id "\
          "  join inventory "\
          "    on rental.inventory_id = inventory.inventory_id "\
          "  join film "\
          "    on inventory.film_id = film.film_id "\
          " where customer.last_name like '{0}' "\
          "   and strftime('%Y', rental_date) = '{1}' "\
          "   and strftime('%m', rental_date) like '%{2}'"
  cursor.execute(query.format(lname,year,month))
  row = cursor.fetchall()

  print('')
  print('--------- Sakila DVD Rentals --------- ')
  print('')
  print("Monthly report for {0} {1}\n".format(row[0][0], lname))
  print('')

  #for each row in data, check the rental and return date, and also sum the price
  for i in range(len(row)):
    rented = datetime.strptime(row[i][3], date_format)  #getting the rental date
    returned = datetime.strptime(row[i][5], date_format) #getting the return date
    total = total + row[i][4] #sum of the total rental price
    print('{0:<20} {1:<12} {2:<10}'.format(row[i][1],rented.strftime(date_format_display),row[i][4]))  #displaying rental

  #checking, printing and summing the late fees
    diff = returned - rented
    if diff.days > row[i][6]:
      print('          **late fee {0} {1:6}'.format(returned.strftime(date_format_display),row[i][4]))
      total = total + row[i][4]

  #printing the total to pay
  print("\nMonthly total: %.2f" % total)