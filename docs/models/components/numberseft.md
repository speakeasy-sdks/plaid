# NumbersEFT

Identifying information for transferring money to or from a Canadian bank account via EFT.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `account`                                                | *str*                                                    | :heavy_check_mark:                                       | The EFT account number for the account                   |
| `account_id`                                             | *str*                                                    | :heavy_check_mark:                                       | The Plaid account ID associated with the account numbers |
| `branch`                                                 | *str*                                                    | :heavy_check_mark:                                       | The EFT branch number for the account                    |
| `institution`                                            | *str*                                                    | :heavy_check_mark:                                       | The EFT institution number for the account               |
| `additional_properties`                                  | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      |