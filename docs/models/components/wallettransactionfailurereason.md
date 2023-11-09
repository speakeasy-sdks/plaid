# WalletTransactionFailureReason

The error code of a failed transaction. Error codes include:
`EXTERNAL_SYSTEM`: The transaction was declined by an external system.
`EXPIRED`: The transaction request has expired.
`CANCELLED`: The transaction request was rescinded.
`INVALID`: The transaction did not meet certain criteria, such as an inactive account or no valid counterparty, etc.
`UNKNOWN`: The transaction was unsuccessful, but the exact cause is unknown.


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `EXTERNAL_SYSTEM` | EXTERNAL_SYSTEM   |
| `EXPIRED`         | EXPIRED           |
| `CANCELLED`       | CANCELLED         |
| `INVALID`         | INVALID           |
| `UNKNOWN`         | UNKNOWN           |