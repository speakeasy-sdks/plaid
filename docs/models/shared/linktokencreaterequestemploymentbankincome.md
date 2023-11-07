# LinkTokenCreateRequestEmploymentBankIncome

Specifies options for initializing Link for use with Bank Employment. This field is required if `employment` is included in the `products` array and `bank` is specified in `employment_source_types`.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `days_requested`                                                       | *int*                                                                  | :heavy_check_mark:                                                     | The number of days of data to request for the Bank Employment product. |