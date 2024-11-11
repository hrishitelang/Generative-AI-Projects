from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

# To retrieve query from SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
"""
You are an expert in converting English questions to SQL query!
The SQL database has the name student and has the following columns: Name, Class, Section and Marks \n\n
For Example - How many entries of records are present in the SQL command will be something like this 
SELECT COUNT(*) FROM student;
\nExample 2: Tell me all the students studying in Data Science class, the SQL command will be something like this:
SELECT * FROM student WHERE class = "Data Science";
Also the SQL code should not have ``` in beginning or end and sql word in the output
"""
]

## Streamlit App
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to retrieve SQL data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is:")
    for row in data:
        st.write(row)
else:
    st.write("No records found.")