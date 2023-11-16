# TransferRepayment

A repayment is created automatically after one or more guaranteed transactions receive a return. If there are multiple eligible returns in a day, they are batched together into a single repayment.

Repayments are sent over ACH, with funds typically available on the next banking day.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `additional_properties`                                               | Dict[str, *Any*]                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `amount`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | Decimal amount of the repayment as it appears on your account ledger. |
| `created`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_check_mark:                                                    | The datetime when the repayment occurred, in RFC 3339 format.         |
| `iso_currency_code`                                                   | *str*                                                                 | :heavy_check_mark:                                                    | The currency of the repayment, e.g. "USD".                            |
| `repayment_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | Identifier of the repayment.                                          |