import streamlit as st
import pandas as pd
from faker import Faker
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a seed for reproducibility
np.random.seed(42)
# to hide warning messages
st.set_option('deprecation.showPyplotGlobalUse', False)

# Function to generate fake employee data
def generate_fake_data(num_records=100):
    fake = Faker()
    data = {
        'Name': [fake.name() for _ in range(num_records)],
        'Age': [fake.random_int(min=22, max=60) for _ in range(num_records)],
        'Salary': [np.random.randint(50000, 120000) for _ in range(num_records)],
        'Work Experience (Years)': [np.random.randint(0, 15) for _ in range(num_records)],
        'Department': [fake.job() for _ in range(num_records)],
        'Gender': [fake.random_element(elements=('Male', 'Female')) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to create Streamlit app
def main():
    st.title("Employee Data Visualization")

    # Generate fake employee data
    num_records = st.slider("Select the number of records", min_value=50, max_value=500, value=100)
    employee_data = generate_fake_data(num_records)

    # Display the raw data
    st.subheader("Raw Employee Data")
    st.write(employee_data)

    # Basic statistics
    st.subheader("Basic Statistics")
    st.write(employee_data.describe())

    # Age distribution histogram
    st.subheader("Age Distribution")
    plt.figure(figsize=(8, 6))
    sns.histplot(employee_data['Age'], bins=20, kde=True)
    st.pyplot()

    # Salary distribution by department
    st.subheader("Salary Distribution by Department")
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Department', y='Salary', data=employee_data)
    st.pyplot()

    # Work experience vs Salary scatter plot
    st.subheader("Work Experience vs Salary")
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Work Experience (Years)', y='Salary', hue='Gender', data=employee_data)
    st.pyplot()

    # Gender distribution pie chart
    st.subheader("Gender Distribution")
    gender_counts = employee_data['Gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)



    # Salary range slider
    st.subheader("Salary Range Filter")
    salary_range = st.slider("Select a Salary Range", min_value=50000, max_value=120000, value=(50000, 120000))
    filtered_data = employee_data[(employee_data['Salary'] >= salary_range[0]) & (employee_data['Salary'] <= salary_range[1])]
    st.write(filtered_data)

if __name__ == "__main__":
    main()

