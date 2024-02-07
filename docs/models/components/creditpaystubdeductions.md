# CreditPayStubDeductions

An object with the deduction information found on a pay stub.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `breakdown`                                                                                          | List[[components.PayStubDeductionsBreakdown](../../models/components/paystubdeductionsbreakdown.md)] | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `total`                                                                                              | [components.PayStubDeductionsTotal](../../models/components/paystubdeductionstotal.md)               | :heavy_check_mark:                                                                                   | An object representing the total deductions for the pay period                                       |
| `additional_properties`                                                                              | Dict[str, *Any*]                                                                                     | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |