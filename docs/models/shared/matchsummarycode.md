# MatchSummaryCode

An enum indicating the match type between data provided by user and data checked against an external data source.


`match` indicates that the provided input data was a strong match against external data.

`partial_match` indicates the data approximately matched against external data. For example, "Knope" vs. "Knope-Wyatt" for last name.

`no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.

`no_data` indicates that Plaid was unable to find external data to compare against the provided input data.

`no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.


## Values

| Name            | Value           |
| --------------- | --------------- |
| `MATCH`         | match           |
| `PARTIAL_MATCH` | partial_match   |
| `NO_MATCH`      | no_match        |
| `NO_DATA`       | no_data         |
| `NO_INPUT`      | no_input        |