# Pizza Project
***
### Installation
To start this application: 
- download all files
- run the client.py file

### Brief Description
This app gives the opportunity to create and log into your account as customer or admin, and then make a pizza order, view order history, sign out of account or add pizza, remove pizza, view purchase history, view menu and sign out of account, respectively.
Application enables to navigate between next pages:

#### Main Page
Allows to go to "Sign in" page by pressing Sign In button, and to "Sign Up" page by pressing Sign Up button

#### Sign Up Page
Once the page appeared, customer should fill 5 entries taking into account some constraints

|Entry|Restrictions|
|-----|-----|
|Name|minimum length = 3|
|Surname|minimum length = 3|
|E-mail| minimum length = 9; should contain no numbers; there should be at least 1 letter before and after "@" and "." . For example: someone@gmail.com|
|Password|minimum length = 5|
|Repeat Password|should be the same as password|

***current regex for email which can be improved: [a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+**
This page contains two buttons:
- if you click Home, it will return you back to the Main Page
- if you click Enter, you will be redirected to your customer account

#### Sign In Page
If you have signed up before, then you can press Sign In button in Main Page and go to Sign In page. Here the customer should fill two entries: the email and password. If the information provided doesn't match with the information from database then the pop-up menu will appear. However, if the information is correct and you have pressed Enter, you can see your Customer Account page. Home button will redirect you to the Main Page as in Sign Up page.
***Here if the next data is written, then you will be navigated to Admin Account Page:**
* **email: admin@gmail.com**
* **password: admin**

#### Customer Account Page
In this page, the customer is provided with 3 options: 
1. viewing history of orders (by pressing Go to History button) - will navigate to **History Page** and this page will display all the orders made, their cost and date of order. Horizontal and vertical scrollbars are provided to see the whole string and all orders, relatively.
2. making order (by pressing Make Order button) - will go to Menu Page
3. signing out(by pressing Sign Out button) - will return you to Main Page

#### Menu Page
Here 3 buttons will be displayed:
- My account - returns you to your account
- Ready Pizzas - prompts Ready Pizzas Page
- Custom Pizzas - prompts Custom pizzas Page
#### Ready Pizzas Page
Here, you would be able to see all the pizzas available, their ingredients and cost. To buy pizza, you should press relative image of pizza, otherwise, you can return to your account by pressing the only button here.
*Note that when admin adds new pizza to database, new pizza appears here
#### Custom Pizzas Page
This page allows you to choose the size of pizza and topping that you want to add. After the customer clicked the checkbox of desired item, Submit button should be pressed to add pizza to database. Newly ordered pizza can be seen in Customer History and Admin History.
#### Admin Account Page
Admin can perform 5 actions: add pizza, remove pizza, view menu, view orders and sign out of account. To be able to do that, buttons with the same names should be pressed.
#### Add New Pizza Page
The Page requres to fill 2 entries:
1. Pizza Name - should not have the name of already available pizza
2. Pizza Image Path - **this should be an absolute path of .png image**

Afterwards, ingredients should be checkboxed and Submit button should be pressed. The cost of newly created pizza would be calculated and all the data would be stored in database.

#### Remove Pizza Page
If admin wants to remove pizza from menu, then he/she should press the image of needed pizza, and, once the pizza is removed from menu, pop-up window wil appear and inform about it. The next time you navigate to this page removed pizza will not be shown.
#### View Whole Menu Page
Displays ready pizza information with ingredients, as well as available topping information and their costs.
#### View All Orders
Displays the information about all the customer orders in the form of string. Vertical and horiziontal scrollbars are provided to view the whole string.
