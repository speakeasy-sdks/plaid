# NumbersInternationalNullable

Identifying information for transferring money to or from an international bank account via wire transfer.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `account_id`                                                 | *str*                                                        | :heavy_check_mark:                                           | The Plaid account ID associated with the account numbers     |
| `bic`                                                        | *str*                                                        | :heavy_check_mark:                                           | The Bank Identifier Code (BIC) for the account               |
| `iban`                                                       | *str*                                                        | :heavy_check_mark:                                           | The International Bank Account Number (IBAN) for the account |