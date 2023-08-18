import streamlit as st
import pandas as pd


class DynamicFilters:
    """
    A class to create dynamic multi-select filters in Streamlit.

    ...

    Attributes
    ----------
    df : DataFrame
        The dataframe on which filters are applied.
    filters : dict
        Dictionary with filter names as keys and their selected values as values.

    Methods
    -------
    check_state():
        Initializes the session state with filters if not already set.
    filter_except(except_filter=None):
        Returns the dataframe filtered based on session state excluding the specified filter.
    display():
        Renders the dynamic filters and the filtered dataframe in Streamlit.
    """

    def __init__(self, df, filters):
        """
        Constructs all the necessary attributes for the DynamicFilters object.

        Parameters
        ----------
            df : DataFrame
                The dataframe on which filters are applied.
            filters : list
                List of columns names in df for which filters are to be created.
        """
        self.df = df
        self.filters = {filter_name: [] for filter_name in filters}
        self.check_state()

    def check_state(self):
        """Initializes the session state with filters if not already set."""
        if 'filters' not in st.session_state:
            st.session_state.filters = self.filters

    def filter_except(self, except_filter=None):
        """
        Filters the dataframe based on session state values except for the specified filter.

        Parameters
        ----------
            except_filter : str, optional
                The filter name that should be excluded from the current filtering operation.

        Returns
        -------
            DataFrame
                Filtered dataframe.
        """
        filtered_df = self.df.copy()
        for key, values in st.session_state.filters.items():
            if key != except_filter and values:
                filtered_df = filtered_df[filtered_df[key].isin(values)]
        return filtered_df

    def display_filters(self):
        """
        Renders the dynamic multiselect filters.

        When any filter value changes, it triggers an update to adjust other filter options based on the current selection.
        """
        filters_changed = False

        # Sidebar Filters
        for filter_name in st.session_state.filters.keys():
            filtered_df = self.filter_except(filter_name)
            options = filtered_df[filter_name].unique().tolist()

            selected = st.multiselect(f"Select {filter_name}", options,
                                      default=st.session_state.filters[filter_name])
            if selected != st.session_state.filters[filter_name]:
                st.session_state.filters[filter_name] = selected
                filters_changed = True

        if filters_changed:
            st.experimental_rerun()

    def display_df(self):
        """Renders the filtered dataframe in the main area."""
        # Display filtered DataFrame
        st.dataframe(self.filter_except())


