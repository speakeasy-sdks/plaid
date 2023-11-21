# ClientProvidedEnhancedTransaction

A client-provided transaction that Plaid has enhanced.


## Fields

| Field                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                           | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                               |
| `amount`                                                                                                                                                                                                                                                                                                          | *float*                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                | The value of the transaction, denominated in the account's currency, as stated in `iso_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. |
| `description`                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                | The raw description of the transaction.                                                                                                                                                                                                                                                                           |
| `enhancements`                                                                                                                                                                                                                                                                                                    | [components.Enhancements](../../models/components/enhancements.md)                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                | A grouping of the Plaid produced transaction enhancement fields.                                                                                                                                                                                                                                                  |
| `id`                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                | Unique transaction identifier to tie transactions back to clients' systems.                                                                                                                                                                                                                                       |
| `iso_currency_code`                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                | The ISO-4217 currency code of the transaction.                                                                                                                                                                                                                                                                    |