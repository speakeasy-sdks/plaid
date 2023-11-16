# TransferTestClock

Defines the test clock for a transfer.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `additional_properties`                                                                   | Dict[str, *Any*]                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `test_clock_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | Plaid’s unique identifier for a test clock.                                               |
| `virtual_time`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_check_mark:                                                                        | The virtual timestamp on the test clock. This will be of the form `2006-01-02T15:04:05Z`. |