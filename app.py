import streamlit as st
import pandas as pd
import pickle

# Method to load the clustered dataframe
def load_clustered_data():
    clustered_df = pd.read_csv('combined_data.csv')
    return clustered_df

# Streamlit app function
def main():
    # st.title("📰 **News Article Clustering**")
    # st.write("---")
    st.markdown(
        """
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

        /* Style for the custom title */
        .custom-title {
            font-family: 'Roboto', sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 20px;
        }

  /* Style for the custom header */
        .custom-header {
            font-family: 'Roboto', sans-serif;
            font-size: 28px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin: 20px 0;
        }

        /* Style for horizontal line */
        .custom-hr {
            border: 2px solid #333;
            margin: 20px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Custom styled title
    st.markdown('<h1 class="custom-title">📰 News Article Clustering</h1>', unsafe_allow_html=True)
    

    # Load the clustered dataframe
    data = load_clustered_data()

    # Displaying clusters and related stories
    categories = ['Business', 'Politics', 'Sports', 'Entertainment']

    st.sidebar.header("🔍 **Filter Options**")
    selected_category = st.sidebar.selectbox("Select a Category", categories)

    st.markdown(f'<h2 class="custom-header">{selected_category} Articles</h2>', unsafe_allow_html=True)

    category_cluster_mapping = {'Business': 0, 'Politics': 1, 'Sports': 2, 'Entertainment': 3}
    selected_cluster = category_cluster_mapping[selected_category]

    cluster_articles = data[data['Cluster'] == selected_cluster]

    for idx, row in cluster_articles.iterrows():
          st.markdown(
            f"""
            <p style="font-family: Arial, sans-serif;">
                <strong style="font-size: 16px;">Title:</strong> {row['Title']}<br>
                <strong style="font-size: 16px;">Category:</strong> {row['Category']}<br>
                <strong style="font-size: 16px;">Source:</strong> {row['Source']}<br>
                <strong style="font-size: 16px;">URL:</strong> <a href="{row['Link']}" style="color: #1f77b4;">{row['Link']}</a>
            </p>
            """,
            unsafe_allow_html=True
        )

          st.markdown(
            """
            <hr style="border: 1px solid #ccc;">
            """,
            unsafe_allow_html=True
        )

# Running the app
if __name__ == "__main__":
    main()
