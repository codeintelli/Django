!WHAT WE ARE USING IN THIS PROJECT 
1. HTML
2. CSS
3. JavaScript
4. Bootstrap 5
5. JQuery
6. AJAX
7. FONTAWESOME/BOX-ICON
8. OWL CAROUSEL
9. PYTHON
10. DJANGO
11. PAYPAL PAYMENT INTEGRATION/PAYTM
12. DIGITAL OCEAN (HOSTING/HEROKU/NETLIFY)


!TOPIC COVERED

1. create model
2. model property
3. choice field
4. register model admin
5. class based view
6. function based view
7. template inheritance
8. using template engine
9. using static file
10. DTL
11. Handling Json Data
12. Image Upload
13. Writing URL
14. Rendering custom template for Auth
15. Form
16. Config media
17. config email


!DATABASE TABLE DETAILS

* CUSTOMER
user : ForeignKey
name
locality
city
zipcode
state



* USER
username
password
first_name


* PRODUCT
title
selling price
discount price
desc
brand
category
product-image



* ORDERPLACED
user: ForeignKey
customer
product
quantity
orderd_date
status


* CART
user
product
quantity