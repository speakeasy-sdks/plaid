# BankTransferSweep

BankTransferSweep describes a sweep transfer.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `amount`                                                             | *str*                                                                | :heavy_check_mark:                                                   | The amount of the sweep.                                             |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The datetime when the sweep occurred, in RFC 3339 format.            |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Identifier of the sweep.                                             |
| `iso_currency_code`                                                  | *str*                                                                | :heavy_check_mark:                                                   | The currency of the sweep, e.g. "USD".                               |
| `additional_properties`                                              | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |