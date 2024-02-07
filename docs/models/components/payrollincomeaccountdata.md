# PayrollIncomeAccountData

An object containing account level data.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *Optional[str]*                                                                        | :heavy_check_mark:                                                                     | ID of the payroll provider account.                                                    |
| `pay_frequency`                                                                        | *Optional[str]*                                                                        | :heavy_check_mark:                                                                     | The frequency at which an individual is paid.                                          |
| `rate_of_pay`                                                                          | [components.PayrollIncomeRateOfPay](../../models/components/payrollincomerateofpay.md) | :heavy_check_mark:                                                                     | An object representing the rate at which an individual is paid.                        |
| `additional_properties`                                                                | Dict[str, *Any*]                                                                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |