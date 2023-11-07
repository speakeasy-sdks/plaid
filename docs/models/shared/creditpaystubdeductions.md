# CreditPayStubDeductions

An object with the deduction information found on a pay stub.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `additional_properties`                                                                          | Dict[str, *Any*]                                                                                 | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `breakdown`                                                                                      | List[[components.PayStubDeductionsBreakdown](../../models/shared/paystubdeductionsbreakdown.md)] | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `total`                                                                                          | [components.PayStubDeductionsTotal](../../models/shared/paystubdeductionstotal.md)               | :heavy_check_mark:                                                                               | An object representing the total deductions for the pay period                                   |