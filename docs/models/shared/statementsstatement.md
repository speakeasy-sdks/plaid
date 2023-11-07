# StatementsStatement

A statement's metadata associated with an account


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `additional_properties`                                                      | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `month`                                                                      | *int*                                                                        | :heavy_check_mark:                                                           | Month of the year. Possible values: 1 through 12 (January through December). |
| `statement_id`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | Plaid's unique identifier for the statement.                                 |
| `year`                                                                       | *int*                                                                        | :heavy_check_mark:                                                           | Year. Possible values: 2010-{current_year}.                                  |