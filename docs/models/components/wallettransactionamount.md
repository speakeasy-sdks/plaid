# WalletTransactionAmount

The amount and currency of a transaction


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `additional_properties`                                                                  | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `iso_currency_code`                                                                      | [components.WalletISOCurrencyCode](../../models/components/walletisocurrencycode.md)     | :heavy_check_mark:                                                                       | An ISO-4217 currency code, used with e-wallets and transactions.                         |
| `value`                                                                                  | *float*                                                                                  | :heavy_check_mark:                                                                       | The amount of the transaction. Must contain at most two digits of precision e.g. `1.23`. |