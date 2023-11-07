# CreditPayrollIncomeRefreshRequestOptions

An optional object for `/credit/payroll_income/refresh` request options.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `item_ids`                                                                                             | List[*str*]                                                                                            | :heavy_minus_sign:                                                                                     | An array of `item_id`s to be refreshed. Each `item_id` should uniquely identify a payroll income item. |
| `webhook`                                                                                              | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | The URL where Plaid will send the payroll income refresh webhook.                                      |