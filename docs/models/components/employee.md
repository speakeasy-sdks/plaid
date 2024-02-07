# Employee

Data about the employee.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `address`                                                                | [components.PaystubAddress](../../models/components/paystubaddress.md)   | :heavy_check_mark:                                                       | Address on the paystub                                                   |
| `name`                                                                   | *Optional[str]*                                                          | :heavy_check_mark:                                                       | The name of the employee.                                                |
| `additional_properties`                                                  | Dict[str, *Any*]                                                         | :heavy_minus_sign:                                                       | N/A                                                                      |
| `marital_status`                                                         | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Marital status of the employee - either `single` or `married`.           |
| `taxpayer_id`                                                            | [Optional[components.TaxpayerID]](../../models/components/taxpayerid.md) | :heavy_minus_sign:                                                       | Taxpayer ID of the individual receiving the paystub.                     |