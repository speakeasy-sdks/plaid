# CreditBankIncomeTransaction

The transactions data for the end user's income source(s).


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                                     | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The settled value of the transaction, denominated in the transactions's currency as stated in `iso_currency_code` or `unofficial_currency_code`.<br/>Positive values when money moves out of the account; negative values when money moves in.<br/>For example, credit card purchases are positive; credit card payment, direct deposits, and refunds are negative. |
| `check_number`                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The check number of the transaction. This field is only populated for check transactions.                                                                                                                                                                                                                                                                   |
| `date_`                                                                                                                                                                                                                                                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted.<br/>Both dates are returned in an ISO 8601 format (YYYY-MM-DD).                                                                                                                                                            |
| `iso_currency_code`                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The ISO 4217 currency code of the amount or balance.                                                                                                                                                                                                                                                                                                        |
| `name`                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The merchant name or transaction description.                                                                                                                                                                                                                                                                                                               |
| `original_description`                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The string returned by the financial institution to describe the transaction.                                                                                                                                                                                                                                                                               |
| `pending`                                                                                                                                                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | When true, identifies the transaction as pending or unsettled.<br/>Pending transaction details (name, type, amount, category ID) may change before they are settled.                                                                                                                                                                                        |
| `transaction_id`                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.                                                                                                                                                                                                                                                       |
| `unofficial_currency_code`                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                          | The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.<br/>Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.                                                                 |