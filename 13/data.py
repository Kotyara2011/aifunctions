# Import the pyodbc module
import pyodbc

# Define a function to connect to a data source and return a cursor object
def connect_data_source(dsn, uid, pwd):
    # Create a connection string with the data source name, user id and password
    conn_str = f"DSN={dsn};UID={uid};PWD={pwd}"
    # Connect to the data source using the connection string
    conn = pyodbc.connect(conn_str)
    # Create a cursor object from the connection
    cursor = conn.cursor()
    # Return the cursor object
    return cursor

# Define a function to extract target audience information from an ad account
def get_target_audience(cursor, account_id):
    # Execute a SQL query to select the target audience attributes from the ad account table
    cursor.execute(f"SELECT age_range, gender, location, interests FROM ad_account WHERE id = {account_id}")
    # Fetch the first row of the query result
    row = cursor.fetchone()
    # If the row is not None, return a dictionary with the target audience attributes
    if row:
        target_audience = {
            "age_range": row[0],
            "gender": row[1],
            "location": row[2],
            "interests": row[3]
        }
        return target_audience
    # Otherwise, return None
    else:
        return None

# Define a function to extract platform information from an ad account
def get_platform(cursor, account_id):
    # Execute a SQL query to select the platform name from the ad account table
    cursor.execute(f"SELECT platform FROM ad_account WHERE id = {account_id}")
    # Fetch the first row of the query result
    row = cursor.fetchone()
    # If the row is not None, return the platform name as a string
    if row:
        platform = row[0]
        return platform
    # Otherwise, return None
    else:
        return None

# Define a function to extract product features from a product catalog
def get_product_features(cursor, product_id):
    # Execute a SQL query to select the product name, description, price and image url from the product table
    cursor.execute(f"SELECT name, description, price, image_url FROM product WHERE id = {product_id}")
    # Fetch the first row of the query result
    row = cursor.fetchone()
    # If the row is not None, return a dictionary with the product features
    if row:
        product_features = {
            "name": row[0],
            "description": row[1],
            "price": row[2],
            "image_url": row[3]
        }
        return product_features
    # Otherwise, return None
    else:
        return None

# Define a function to extract branding guidelines from an asset library
def get_branding_guidelines(cursor, brand_id):
    # Execute a SQL query to select the brand name, logo url, color scheme and font style from the brand table
    cursor.execute(f"SELECT name, logo_url, color_scheme, font_style FROM brand WHERE id = {brand_id}")
    # Fetch the first row of the query result
    row = cursor.fetchone()
    # If the row is not None, return a dictionary with the branding guidelines
    if row:
        branding_guidelines = {
            "name": row[0],
            "logo_url": row[1],
            "color_scheme": row[2],
            "font_style": row[3]
        }
        return branding_guidelines
    # Otherwise, return None
    else:
        return None

