# CreditSessionPayrollIncomeResult

The details of a digital payroll income verification in Link


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `institution_id`                                          | *Optional[str]*                                           | :heavy_minus_sign:                                        | The Plaid Institution ID associated with the Item.        |
| `institution_name`                                        | *Optional[str]*                                           | :heavy_minus_sign:                                        | The Institution Name associated with the Item.            |
| `num_paystubs_retrieved`                                  | *Optional[int]*                                           | :heavy_minus_sign:                                        | The number of paystubs retrieved from a payroll provider. |
| `num_w2s_retrieved`                                       | *Optional[int]*                                           | :heavy_minus_sign:                                        | The number of w2s retrieved from a payroll provider.      |