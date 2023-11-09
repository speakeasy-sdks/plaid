# CreditPayStubEarnings

An object representing both a breakdown of earnings on a pay stub and the total earnings.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                             | Dict[str, *Any*]                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `breakdown`                                                                                         | List[[components.PayStubEarningsBreakdown](../../models/components/paystubearningsbreakdown.md)]    | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `total`                                                                                             | [components.PayStubEarningsTotal](../../models/components/paystubearningstotal.md)                  | :heavy_check_mark:                                                                                  | An object representing both the current pay period and year to date amount for an earning category. |