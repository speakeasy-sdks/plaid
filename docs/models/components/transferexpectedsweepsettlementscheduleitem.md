# TransferExpectedSweepSettlementScheduleItem

Defines an expected sweep date and amount.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `sweep_settlement_date`                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The settlement date of a sweep for this transfer.                            |
| `swept_settled_amount`                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The accumulated amount that has been swept by `sweep_settlement_date`.       |
| `additional_properties`                                                      | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |