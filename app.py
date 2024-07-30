import streamlit as st
import pandas as pd

# Method to load the clustered dataframe
def load_clustered_data():
    return pd.read_csv('combined_data.csv')

# Streamlit app function
def main():
    st.set_page_config(page_title="News Article Clustering", layout="wide")
    
    st.title("📰 **News Article Clustering**")
    st.sidebar.header("🔍 **Filter Options**")

    # Load the clustered dataframe
    data = load_clustered_data()

    # Define categories and create a sidebar selector
    categories = ['Business', 'Politics', 'Sports', 'Entertainment']
    selected_category = st.sidebar.selectbox("Select a Category", categories)
    
    st.header(f"### {selected_category} Articles")
    
    category_cluster_mapping = {'Business': 0, 'Politics': 1, 'Sports': 2, 'Entertainment': 3}
    selected_cluster = category_cluster_mapping[selected_category]
    
    # Filter the articles based on the selected cluster
    cluster_articles = data[data['Cluster'] == selected_cluster]

    # Create a container for the articles
    with st.container():
        for idx, row in cluster_articles.iterrows():
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 10px; background-color: #f9f9f9;">
                    <h4 style="margin: 0; color: #333;">**Title:** {row['Title']}</h4>
                    <p style="margin: 5px 0; color: #555;">**Category:** {row['Category']}</p>
                    <p style="margin: 5px 0; color: #555;">**Source:** {row['Source']}</p>
                    <p style="margin: 5px 0; color: #007bff;">**URL:** <a href="{row['Link']}" target="_blank" style="text-decoration: none; color: #007bff;">Read More</a></p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Running the app
if __name__ == "__main__":
    main()
