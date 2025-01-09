import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Interactive Chart Generator with Matplotlib and Seaborn")

# Step 1: Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV format):", type=["csv"])
if uploaded_file:
    # Step 2: Read the dataset
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.write(df.head())

    # Step 3: Display column names with checkboxes
    st.header("Select Columns for X and Y Axes")
    x_column = st.selectbox("Select X Axis Column", options=df.columns)
    y_column = st.selectbox("Select Y Axis Column", options=df.columns)

    # Step 4: Select chart type
    st.header("Select Chart Type")
    chart_type = st.selectbox(
        "Chart Type",
        options=["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"]
    )

    # Step 5: Generate the chart
    if st.button("Generate Chart"):
        fig, ax = plt.subplots(figsize=(10, 6))  # Prepare the plot

        # Chart logic based on selected type
        if chart_type == "Bar Chart":
            sns.barplot(x=x_column, y=y_column, data=df, ax=ax)
            ax.set_title(f"{y_column} by {x_column}")
        elif chart_type == "Line Chart":
            sns.lineplot(x=x_column, y=y_column, data=df, ax=ax)
            ax.set_title(f"{y_column} over {x_column}")
        elif chart_type == "Scatter Plot":
            sns.scatterplot(x=x_column, y=y_column, data=df, ax=ax)
            ax.set_title(f"Scatter Plot of {y_column} vs {x_column}")
        elif chart_type == "Histogram":
            sns.histplot(df[x_column], kde=True, ax=ax)
            ax.set_title(f"Histogram of {x_column}")

        # Display the plot
        st.pyplot(fig)
