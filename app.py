import streamlit as st
import pandas as pd

# Method to load the clustered dataframe
def load_clustered_data():
    return pd.read_csv('combined_data.csv')

# Streamlit app function
def main():
    st.set_page_config(page_title="News Article Clustering", layout="wide")
    
    st.title("News Article Clustering")
    st.sidebar.header("Filter Options")

    # Load the clustered dataframe
    data = load_clustered_data()

    # Define categories and create a sidebar selector
    categories = ['Business', 'Politics', 'Sports', 'Entertainment']
    selected_category = st.sidebar.selectbox("Select a Category", categories)
    
    st.header(f"{selected_category} Articles")
    
    category_cluster_mapping = {'Business': 0, 'Politics': 1, 'Sports': 2, 'Entertainment': 3}
    selected_cluster = category_cluster_mapping[selected_category]
    
    # Filter the articles based on the selected cluster
    cluster_articles = data[data['Cluster'] == selected_cluster]

    # Create a container for the articles
    with st.container():
        for idx, row in cluster_articles.iterrows():
            st.write(f"**Title:** {row['Title']}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Source:** {row['Source']}")
            st.write(f"**URL:** [Read More]({row['Link']})")
            st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation

# Running the app
if __name__ == "__main__":
    main()
