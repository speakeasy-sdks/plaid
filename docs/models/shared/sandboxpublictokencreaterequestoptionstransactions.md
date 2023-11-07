# SandboxPublicTokenCreateRequestOptionsTransactions

An optional set of parameters corresponding to transactions options.


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `end_date`                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                          | :heavy_minus_sign:                                                                                    | The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. |
| `start_date`                                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                          | :heavy_minus_sign:                                                                                    | The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.    |