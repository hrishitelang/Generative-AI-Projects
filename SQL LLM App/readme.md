
# Text-to-SQL LLM Application Using Google Gemini Pro

## **Overview**
This project demonstrates an **end-to-end application** using **Google Gemini Pro** to convert natural language text into **SQL queries** and retrieve data from an **SQL database**. By leveraging generative AI, we simplify querying databases for users unfamiliar with SQL syntax, enabling seamless interaction with structured data.

---

## **Features**
1. **Text-to-SQL Conversion**: Converts natural language inputs into SQL queries using Google Gemini Pro.
2. **Database Integration**: Retrieves data from a SQLite database using dynamically generated queries.
3. **Streamlit Interface**: Provides an intuitive web-based interface for user interaction.
4. **Support for Complex Queries**: Handles advanced SQL queries, including joins, aggregations, and subqueries.

---

## **Tools and Technologies**
- **Google Gemini Pro**: For generating SQL queries from text inputs.
- **Streamlit**: For creating a user-friendly frontend interface.
- **SQLite**: Lightweight local database for storing and retrieving data.
- **Python-dotenv**: For managing environment variables, including API keys.

---

## **Workflow**

### **1. Database Setup**
- **Database**: A SQLite database (`student.db`) is created with the following schema:
  ```sql
  CREATE TABLE student (
      name TEXT,
      class TEXT,
      section TEXT,
      marks INTEGER
  );
  ```
- **Data Insertion**: Records are inserted programmatically into the database, including:
  - Example: `INSERT INTO student VALUES ('Krish', 'Data Science', 'A', 90);`

### **2. Application Flow**
1. **User Input**:
   - Users provide questions in natural language, such as:
     - "Tell me all the student names."
     - "Provide the average marks of all students."
2. **Query Generation**:
   - Google Gemini Pro converts the input text into a corresponding SQL query.
   - Example Input: "Provide the average marks of all students."
   - Generated SQL Query: `SELECT AVG(marks) FROM student;`
3. **Database Interaction**:
   - The generated SQL query is executed on the SQLite database to retrieve results.
4. **Result Display**:
   - Results are displayed in the Streamlit interface.

---

## **Setup Instructions**

### **1. Environment Setup**
1. Create a Python virtual environment:
   ```bash
   conda create -n text_to_sql python=3.9
   conda activate text_to_sql
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add the **Google Gemini Pro API Key** to a `.env` file:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

### **2. Running the Application**
1. Create and populate the database:
   ```bash
   python sql_setup.py
   ```
2. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## **Key Functionalities**

### **Database Management (`sql_setup.py`)**
- **SQLite3** is used to:
  - Create the database and schema.
  - Insert sample data into the database.
- Example Data:
  | Name      | Class          | Section | Marks |
  |-----------|----------------|---------|-------|
  | Krish     | Data Science   | A       | 90    |
  | Sudhanshu | Data Science   | B       | 100   |
  | Darius    | Data Science   | A       | 86    |

### **Google Gemini Integration (`app.py`)**
1. **Prompt Design**:
   - Custom prompt to guide the LLM on how to interpret text inputs as SQL queries:
     ```text
     You are an expert in converting English questions into SQL queries.
     The SQL database has the following schema: name, class, section, marks.
     Example Input: "Tell me all students in the Data Science class."
     Example Output: `SELECT * FROM student WHERE class = 'Data Science';`
     ```
2. **Model Configuration**:
   - Google Gemini Pro is configured using the API key stored in `.env`.
   - Queries are generated using the `generate_content` function.

### **Query Execution**
- The application retrieves results by executing the generated SQL queries on the SQLite database using Python's `sqlite3` library.

### **Streamlit Interface**
- **Input Box**: Users input their questions in natural language.
- **Submit Button**: Executes the query and displays results in real-time.

---

## **Sample Queries and Outputs**

| Input Question                                  | Generated SQL Query                                  | Output                                      |
|------------------------------------------------|----------------------------------------------------|--------------------------------------------|
| "Tell me all student names."                   | `SELECT name FROM student;`                        | Krish, Sudhanshu, Darius                   |
| "Provide the average marks of all students."   | `SELECT AVG(marks) FROM student;`                 | 92.0                                       |
| "Provide the student name with the highest marks." | `SELECT name, MAX(marks) FROM student;`            | Sudhanshu                                  |
| "Show the marks of students in class A."       | `SELECT name, marks FROM student WHERE section='A';` | Krish: 90, Darius: 86                      |

---

## **Future Enhancements**
- **Database Flexibility**: Extend support for MySQL and PostgreSQL.
- **Improved Query Interpretation**: Add support for ambiguous or multi-intent queries.
- **Error Handling**: Implement checks for invalid inputs or SQL syntax errors.
- **Real-Time Integration**: Connect to live databases for dynamic data retrieval.
- **Advanced Querying**: Enable multi-table joins and nested subqueries.

---

## **References**
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini Pro](https://makersuite.google.com/)
- [SQLite3 Documentation](https://www.sqlite.org/docs.html)

---

With this application, you can easily convert natural language queries into SQL and interact with your databases seamlessly!
