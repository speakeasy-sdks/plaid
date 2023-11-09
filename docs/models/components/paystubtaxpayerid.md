# PayStubTaxpayerID

Taxpayer ID of the individual receiving the paystub.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `additional_properties`                         | Dict[str, *Any*]                                | :heavy_minus_sign:                              | N/A                                             |
| `id_mask`                                       | *Optional[str]*                                 | :heavy_check_mark:                              | ID mask; i.e. last 4 digits of the taxpayer ID. |
| `id_type`                                       | *Optional[str]*                                 | :heavy_check_mark:                              | Type of ID, e.g. 'SSN'.                         |