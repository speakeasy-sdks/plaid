# LinkTokenCreateRequestIncomeVerificationBankIncome

Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `days_requested`                                                  | *int*                                                             | :heavy_check_mark:                                                | The number of days of data to request for the Bank Income product |
| `enable_multiple_items`                                           | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Whether to enable multiple Items to be added in the Link session  |