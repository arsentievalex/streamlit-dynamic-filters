# Dynamic Multi Select Filters for Streamlit
[![Open Demo App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dynamic-filters-demo.streamlit.app/)

Custom component to create dynamic multiselect filters in Streamlit. 
The filters apply to a dataframe and adjust their values based on the user selection (similar to Google Sheets slicers or Only Relevant Values in Tableau). 

Basic documentation is available at [https://arsentievalex.github.io/streamlit-dynamic-filters/](https://arsentievalex.github.io/streamlit-dynamic-filters/)

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


#### Sample usage with sidebar filters:

```
import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi']
}

df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])

with st.sidebar:
    st.write("Apply filters in any order 👇")

dynamic_filters.display_filters(location='sidebar')

dynamic_filters.display_df()
```

Demo GIF:
<img src="https://i.postimg.cc/x1zDwgwh/dynamic-filters-demo-1.gif"/>   

#### Sample usage with columns:

```
import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi']
}

df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])

st.write("Apply filters in any order 👇")

dynamic_filters.display_filters(location='columns', num_columns=2, gap='large')

dynamic_filters.display_df()
```

Demo GIF:
<img src="https://i.postimg.cc/gkLTjjg6/dynamic-filters-demo-2.gif"/>   

