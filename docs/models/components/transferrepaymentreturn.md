# TransferRepaymentReturn

Represents a return on a Guaranteed ACH transfer that is included in the specified repayment.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `amount`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | The value of the returned transfer.                                   |
| `event_id`                                                            | *int*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the corresponding `returned` transfer event. |
| `iso_currency_code`                                                   | *str*                                                                 | :heavy_check_mark:                                                    | The currency of the repayment, e.g. "USD".                            |
| `transfer_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the guaranteed transfer that was returned.   |
| `additional_properties`                                               | Dict[str, *Any*]                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |