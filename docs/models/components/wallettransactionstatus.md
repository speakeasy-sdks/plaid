# WalletTransactionStatus

The status of the transaction.

`AUTHORISING`: The transaction is being processed for validation and compliance.

`INITIATED`: The transaction has been initiated and is currently being processed.

`EXECUTED`: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.

`SETTLED`: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.

`FAILED`: The transaction failed to process successfully. This is a terminal status.

`BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.


## Values

| Name          | Value         |
| ------------- | ------------- |
| `AUTHORISING` | AUTHORISING   |
| `INITIATED`   | INITIATED     |
| `EXECUTED`    | EXECUTED      |
| `SETTLED`     | SETTLED       |
| `BLOCKED`     | BLOCKED       |
| `FAILED`      | FAILED        |