# CreditBankStatementUploadBankAccountPeriod

An object containing data on the overall period of the statement.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `end_date`                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The end date of the statement period in ISO 8601 format (YYYY-MM-DD).        |
| `ending_balance`                                                             | *Optional[float]*                                                            | :heavy_check_mark:                                                           | The ending balance of the bank account for the period.                       |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The start date of the statement period in ISO 8601 format (YYYY-MM-DD).      |
| `starting_balance`                                                           | *Optional[float]*                                                            | :heavy_check_mark:                                                           | The starting balance of the bank account for the period.                     |