
# DynamicFilters Class Documentation

`DynamicFilters` is a class in the `streamlit-dynamic-filters` library designed to create dynamic multi-select filters in Streamlit applications. Below is a detailed explanation of its methods, arguments, and usage examples.

## Class Initialization

### `__init__(self, df, filters, filters_name='filters')`
Initializes the DynamicFilters object with a dataframe and a list of filters.

#### Parameters:
- `df` (`DataFrame`): The pandas DataFrame on which filters are applied.
- `filters` (`list` of `str`): List of column names in `df` for which filters are to be created.
- `filters_name` (`str`, optional): The key name for storing filters in the Streamlit session state. Default is `'filters'`.

#### Example:
```python
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = {'Category': ['Fruit', 'Vegetable'], 'Item': ['Apple', 'Carrot']}
df = pd.DataFrame(data)
dynamic_filters = DynamicFilters(df, ['Category', 'Item'])
```

## Methods

### `check_state(self)`
Initializes the session state with filters if not already set.

### `filter_df(self, except_filter=None)`
Filters the dataframe based on session state values except for the specified filter.

#### Parameters:
- `except_filter` (`str`, optional): The filter name to be excluded from the current filtering operation.

#### Returns:
- `DataFrame`: Filtered dataframe.

#### Example:
```python
filtered_df = dynamic_filters.filter_df(except_filter='Item')
```

### `display_filters(self, location=None, num_columns=0, gap="small")`
Renders dynamic multiselect filters for user selection.

#### Parameters:
- `location` (`str`, optional): Location to display filters. Can be `'sidebar'`, `'columns'`, or `None` (defaulting to main area).
- `num_columns` (`int`, optional): Number of columns to display filters in when `location` is `'columns'`. Must be 0 (default) or a positive integer.
- `gap` (`str`, optional): Gap between columns when `location` is `'columns'`. Can be `'small'`, `'medium'`, or `'large'`.

#### Example:
```python
dynamic_filters.display_filters(location='sidebar')
```

### `display_df(self, **kwargs)`
Renders the filtered dataframe in the main area.

#### Keyword Arguments:
- `kwargs`: Additional keyword arguments to pass to `streamlit.dataframe`.

#### Example:
```python
dynamic_filters.display_df()
```

## Usage Notes

- Ensure that the Streamlit app is rerun when filter selections are changed to update the displayed dataframe.
- The class dynamically updates the session state to reflect the current filter selections.
