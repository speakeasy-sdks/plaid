# PaymentInitiationOptionalRestrictionBacs

An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `account`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | The account number of the account. Maximum of 10 characters. |
| `sort_code`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | The 6-character sort code of the account.                    |