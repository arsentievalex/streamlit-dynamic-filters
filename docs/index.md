Streamlit Dynamic Filters
Streamlit Dynamic Filters is a Python library that brings advanced, dynamic filtering capabilities to Streamlit applications. It allows users to easily filter data based on multiple criteria with filters that automatically update to reflect the current state of the data.

Installation
bash
Copy code
pip install streamlit-dynamic-filters
Usage
Basic Example
Here's a simple example to get started with Streamlit Dynamic Filters:

python
Copy code
import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

# Sample data
data = {
    'Category': ['Fruit', 'Vegetable', 'Fruit', 'Vegetable'],
    'Item': ['Apple', 'Carrot', 'Banana', 'Broccoli']
}
df = pd.DataFrame(data)

# Initialize DynamicFilters
dynamic_filters = DynamicFilters(df, ['Category', 'Item'])

# Display the filters and the dataframe
dynamic_filters.display_filters()
dynamic_filters.display_df()
Advanced Usage
Hierarchical Filtering
For hierarchical data (e.g., Country > State > City), use DynamicFiltersHierarchical:

python
Copy code
from streamlit_dynamic_filters import DynamicFiltersHierarchical

# Assuming df is a DataFrame with hierarchical data
dynamic_filters = DynamicFiltersHierarchical(df, ['Country', 'State', 'City'])
dynamic_filters.display_filters()
dynamic_filters.display_df()
Filters in Sidebar
Place filters in the sidebar:

python
Copy code
dynamic_filters.display_filters(location='sidebar')
Customizing Number of Columns
Display filters in multiple columns:

python
Copy code
dynamic_filters.display_filters(location='columns', num_columns=2)
Contributing
Contributions to the streamlit-dynamic-filters library are welcome. Please follow the standard fork, branch, and pull request workflow.

License
This project is licensed under the MIT License.

Support
For support and questions, please open an issue in the GitHub repository.
