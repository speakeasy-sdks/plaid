# SandboxPublicTokenCreateRequestIncomeVerificationBankIncome

Specifies options for Bank Income. This field is required if `income_verification` is included in the `initial_products` array and `bank` is specified in `income_source_types`.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `days_requested`                                                  | *Optional[int]*                                                   | :heavy_minus_sign:                                                | The number of days of data to request for the Bank Income product |