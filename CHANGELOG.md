## 0.1.10 - 27th March 2024
### Added
- Implemented rerun_scope and automatic fragment detection (contributed by @tabedzki)

## 0.1.9 - 2nd August 2024
### Added
- Key for each elements in filters, so that multiple DynamicFilters can be used in one app (contribution by @vikashgraja)
- reset_filters function (contribution by @ragchuck)

## 0.1.8 - 1st August 2024
### Added
- Key for each elements in filters, so that multiple DynamicFilters can be used in one app (contribution by @vikashgraja)
- reset_filters function (contribution by @ragchuck)

## 0.1.6 - 27th March 2024
### Added
- Sorted alphabetically filter labels

## 0.1.5 - 28th December 2023
### Added by kzielins <Krzysztof Zielinski> kzislinsk@gmail.com
- Hierarchical filter selectors
- Independent filters with diffrent sessions name

## 0.1.3 - 28th September 2023
### Added
- Ability to specify filter location in display_filters(). The filters can be either displayed in sidebar, main area or columns.
- Error handling of invalid arguments in display_filters().

### Changed
- Renamed filter_except() to filter_df(). The function returns a filtered df.

### Deprecated
-

### Removed
-

### Fixed
- The StreamlitApiException that occured when selected values did not exist in the dataset.
- Possibility to have more than one filter
