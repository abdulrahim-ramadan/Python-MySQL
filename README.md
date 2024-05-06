# Python-MySQL Project: Exploring the World of Databases with Python 🐍📊

\`\`\`python
pip install mysql-connector-python
\`\`\`

## How to Use the Project

\`\`\`bash
# Set up the database
mysql> CREATE DATABASE mydatabase;
mysql> USE mydatabase;
mysql> CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255));
\`\`\`

\`\`\`python
# Update connection info in config.py
host = "localhost"
user = "yourusername"
password = "yourpassword"
database = "mydatabase"
\`\`\`

\`\`\`python
# Run the program
python main.py
\`\`\`

## Contributing

\`\`\`bash
git clone https://github.com/abdulrahim-ramadan/Python-MySQL.git
# Make changes and submit a pull request!
\`\`\`

## Project License

This project is licensed under the [MIT License](LICENSE).
