# 📚 Student Management System (CRUD App)

A **Student Management System** built using **Streamlit** and **MySQL** that allows users to **Create, Read, Update, and Delete (CRUD)** student records through an interactive web interface.

---

## 🚀 Features

- 📖 **View Students**
  - Display all student records in a table
  - Search for a student by ID
  - View total student count

- ➕ **Add Student**
  - Add new student records
  - Prevents duplicate student IDs

- ✏️ **Update Student**
  - Update student name and age
  - Select student easily using dropdown

- ❌ **Delete Student**
  - Delete student records safely
  - Confirmation warning before deletion

- 🎯 Clean UI with sidebar navigation  
- 🎈 Success animations using Streamlit balloons

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** MySQL  
- **Libraries Used:**
  - `streamlit`
  - `mysql-connector-python`
  - `pandas`

---

## 🗄️ Database Setup

Create a MySQL database and table using the following SQL:

```sql
CREATE DATABASE Student_db;

USE Student_db;

CREATE TABLE Student (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
