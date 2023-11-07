# ItemStatusNullable

An object with information about the status of the Item.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                      | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `investments`                                                                                | [Optional[components.ItemStatusInvestments]](../../models/shared/itemstatusinvestments.md)   | :heavy_minus_sign:                                                                           | Information about the last successful and failed investments update for the Item.            |
| `last_webhook`                                                                               | [Optional[components.ItemStatusLastWebhook]](../../models/shared/itemstatuslastwebhook.md)   | :heavy_minus_sign:                                                                           | Information about the last webhook fired for the Item.                                       |
| `transactions`                                                                               | [Optional[components.ItemStatusTransactions]](../../models/shared/itemstatustransactions.md) | :heavy_minus_sign:                                                                           | Information about the last successful and failed transactions update for the Item.           |