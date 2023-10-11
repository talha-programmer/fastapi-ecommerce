## Sample E-commerce System
Backend only e-commerce system implemented in Fastapi and Python 3.11. The system provides features such including products management, inventory management, insights on 
revenue and sales, sample data generation for testing etc.

### Dependencies:
- Python 3.11
- Poetry: A package manager for Python. `pip install poetry`
- MySQL

### Setup Instructions
- Clone the project and CD into the project directory
- Create a new Virtual Environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate
    ```
- Install project dependencies: `poetry install`
- Create a new database for this project in your MySQL server
- Provide the username, password and database name in the db URL inside `db/db_setup.py` and `alembic.ini` files
- Run the migrations and seeders: `alembic upgrade head`. It will create the tables and also seed the data for testing
- Run the Uvicorn dev server by providing the name of starter file: `uvicorn main:app --reload`
- Now the backend app will be running on `localhost:8000`
- You can test all the API endpoints by opening `localhost:8000/docs` if the server was started at 8000 port


### Database Schema
1. Categories Table:
  - Stores the name of the category
  - Has One to Many relationship with proucts
   
2. Products Table:
   - Main table for products, having information about the product such as title, price, discount, stock, category id etc.
   - Only one foreign key `category_id`
   - It has Belongs To relationship with Category and One to Many relationship with Orders and Inventories

3. Inventories Table:
   - Table to store and track inventory related updates for a specific product.
   - When stock increases, the `quantity` column of inventories table contains a positive value.
   - When stock decreases, the `quantity` column contains a negative value
   - Only one foreign key `product_id`
   - It has Belongs To relationship with Product
   - Stores the complete track about each change done in the inventory including the timestamps as well
  
4. Orders Table:
   - Stores all information regading the sales of the store. Including: quantity, discount applied, product price, time and date of order placement
   - Only one foreign key `product_id`
   - It has Belongs To relationship with Product

### Endpoints 
You can check the details about the endpoints after running the project and going to `/docs` route


### Additional Question & Answer
- If there are libraries essential for the project configuration, list them and explain the reason.
    - Listed in Dependencies section
- If there are libraries that you think might be necessary for project configuration, list them and explain the reason.
    - Nil
- The timezone of the data and the user's timezone may be different from your located timezone. What should be considered when handling Datetime using
  Python and Database? (Explanation or code example)
    - In the database, the datetime fields are always stored in UTC timezone as a standard. If there is a need to show these fields to the user in local timezone, then we can
      convert the fields to the local timezone of the users by getting the timezone through the IP Address of the user.
    - One way of converting to the local timezone is by providing Accessors to modify the values of the datetime fields in the `Timestamp` class of the `db/models/mixins.py` file.
    - We can get the timezone of the user through an external API
