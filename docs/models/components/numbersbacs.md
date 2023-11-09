# NumbersBACS

Identifying information for transferring money to or from a UK bank account via BACS.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `additional_properties`                                  | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      |
| `account`                                                | *str*                                                    | :heavy_check_mark:                                       | The BACS account number for the account                  |
| `account_id`                                             | *str*                                                    | :heavy_check_mark:                                       | The Plaid account ID associated with the account numbers |
| `sort_code`                                              | *str*                                                    | :heavy_check_mark:                                       | The BACS sort code for the account                       |