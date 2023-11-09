# CreditPayStubEmployee

Data about the employee.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `additional_properties`                                                            | Dict[str, *Any*]                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `address`                                                                          | [components.CreditPayStubAddress](../../models/components/creditpaystubaddress.md) | :heavy_check_mark:                                                                 | Address on the pay stub.                                                           |
| `marital_status`                                                                   | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | Marital status of the employee - either `SINGLE` or `MARRIED`.                     |
| `name`                                                                             | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | The name of the employee.                                                          |
| `taxpayer_id`                                                                      | [components.PayStubTaxpayerID](../../models/components/paystubtaxpayerid.md)       | :heavy_check_mark:                                                                 | Taxpayer ID of the individual receiving the paystub.                               |