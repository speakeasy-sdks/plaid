# Wallet

An object representing the e-wallet


## Fields

| Field                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `additional_properties`                                                                                                                                                                                                                          | Dict[str, *Any*]                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `balance`                                                                                                                                                                                                                                        | [components.WalletBalance](../../models/components/walletbalance.md)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                               | An object representing the e-wallet balance                                                                                                                                                                                                      |
| `numbers`                                                                                                                                                                                                                                        | [components.WalletNumbers](../../models/components/walletnumbers.md)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                               | An object representing the e-wallet account numbers                                                                                                                                                                                              |
| `recipient_id`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | The ID of the recipient that corresponds to the e-wallet account numbers                                                                                                                                                                         |
| `status`                                                                                                                                                                                                                                         | [components.WalletStatus](../../models/components/walletstatus.md)                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                               | The status of the wallet.<br/><br/>`UNKNOWN`: The wallet status is unknown.<br/><br/>`ACTIVE`: The wallet is active and ready to send money to and receive money from.<br/><br/>`CLOSED`: The wallet is closed. Any transactions made to or from this wallet will error. |
| `wallet_id`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | A unique ID identifying the e-wallet                                                                                                                                                                                                             |