# PaymentInitiationOptionalRestrictionBacs

An object containing a BACS account number and sort code. If an IBAN is not provided or if you need to accept domestic GBP-denominated payments, BACS data is required.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `account`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | The account number of the account. Maximum of 10 characters. |
| `sort_code`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | The 6-character sort code of the account.                    |