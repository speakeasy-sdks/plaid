# PaymentScheme

Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.

`LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.

`LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.

`SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

`SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.


## Values

| Name                           | Value                          |
| ------------------------------ | ------------------------------ |
| `LESS_THAN_NIL_GREATER_THAN_`  | <nil>                          |
| `LOCAL_DEFAULT`                | LOCAL_DEFAULT                  |
| `LOCAL_INSTANT`                | LOCAL_INSTANT                  |
| `SEPA_CREDIT_TRANSFER`         | SEPA_CREDIT_TRANSFER           |
| `SEPA_CREDIT_TRANSFER_INSTANT` | SEPA_CREDIT_TRANSFER_INSTANT   |