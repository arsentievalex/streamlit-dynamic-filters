# Dynamic Multi Select Filters for Streamlit
[![Open Demo App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dynamic-filters-demo.streamlit.app/)

Custom component to create dynamic multiselect filters in Streamlit. 
The filters apply to a dataframe and adjust their values based on the user selection (similar to Google Sheets slicers or Only Relevant Values in Tableau).

How to install and use the package:
1. Install the package using [pip](https://pypi.org/project/streamlit-dynamic-filters/):
    ```pip install streamlit-dynamic-filters```
2. Import the `DynamicFilters` class:
    ```from streamlit_dynamic_filters import DynamicFilters```
3. Create an instance of the `DynamicFilters` class and pass the dataframe and the list of fields that will serve as filters:

    ```dynamic_filters = DynamicFilters(df, filters=['col1', 'col2', 'col3', 'col4'])```
4. Display the filters in your app:
    ```dynamic_filters.display_filters()```
5. Display the filtered dataframe:
    ```dynamic_filters.display_df()```


Sample usage:

```
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
    }

df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['Region', 'Country', 'City'])

with st.sidebar:
    dynamic_filters.display_filters()

dynamic_filters.display_df()
```

Demo GIF:
<img src="https://i.postimg.cc/mDG8BfK4/multiselect-demo.gif"/>   
