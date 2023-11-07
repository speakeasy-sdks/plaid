# SenderBACSNullable

The account number and sort code of the sender's account, if specified in the `/payment_initiation/payment/create` call.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `account`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | The account number of the account. Maximum of 10 characters. |
| `sort_code`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | The 6-character sort code of the account.                    |