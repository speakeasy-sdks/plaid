# NumbersInternationalIBAN

Account numbers using the International Bank Account Number and BIC/SWIFT code format.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `bic`                                                                          | *str*                                                                          | :heavy_check_mark:                                                             | The Business Identifier Code, also known as SWIFT code, for this bank account. |
| `iban`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | International Bank Account Number (IBAN).                                      |
| `additional_properties`                                                        | Dict[str, *Any*]                                                               | :heavy_minus_sign:                                                             | N/A                                                                            |