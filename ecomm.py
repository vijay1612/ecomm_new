import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("This is an app for E-commerce")
    st.sidebar.title("You can upload your file here")
    upload_file = st.sidebar.file_uploader("Upload your file", type=["csv", "xlsx"])
    if upload_file is not None:
        try:
            if upload_file.name.endswith("csv"):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("Data uploaded successfully")

            st.subheader("i am going to show you the data details, head 5")
            st.dataframe(data.head())

            st.subheader("lets see some more data from dataset")
            st.write("shape of the data", data.shape)
            st.write("the column name inside data is", data.columns)
            st.write("missing values into column", data.isnull().sum())

            st.subheader("here i will show you bit of stats")
            st.write(data.describe())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
