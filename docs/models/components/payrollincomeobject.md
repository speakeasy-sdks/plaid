# PayrollIncomeObject

An object representing payroll data.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *Optional[str]*                                                            | :heavy_check_mark:                                                         | ID of the payroll provider account.                                        |
| `form1099s`                                                                | List[[components.Credit1099](../../models/components/credit1099.md)]       | :heavy_check_mark:                                                         | Array of tax form 1099s.                                                   |
| `pay_stubs`                                                                | List[[components.CreditPayStub](../../models/components/creditpaystub.md)] | :heavy_check_mark:                                                         | Array of pay stubs for the user.                                           |
| `w2s`                                                                      | List[[components.CreditW2](../../models/components/creditw2.md)]           | :heavy_check_mark:                                                         | Array of tax form W-2s.                                                    |
| `additional_properties`                                                    | Dict[str, *Any*]                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |