import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print success message
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        print("Failed to connect to the database: {}".format(error))

if __name__ == "__main__":
    create_database()


Task 2: Create Tables
task_2.sql

USE alx_book_store;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS authors (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE IF NOT EXISTS order_details (
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, book_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

ALTER TABLE books
ADD CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES authors(id);
