# TransferStatus

The status of the transfer.

`pending`: A new transfer was created; it is in the pending state.
`posted`: The transfer has been successfully submitted to the payment network.
`settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.
`cancelled`: The transfer was cancelled by the client.
`failed`: The transfer failed, no funds were moved.
`returned`: A posted transfer was returned.


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `POSTED`    | posted      |
| `SETTLED`   | settled     |
| `CANCELLED` | cancelled   |
| `FAILED`    | failed      |
| `RETURNED`  | returned    |