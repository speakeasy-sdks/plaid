# TransferRefundStatus

The status of the refund.

`pending`: A new refund was created; it is in the pending state.
`posted`: The refund has been successfully submitted to the payment network.
`settled`: Credits have been refunded to the Plaid linked account.
`cancelled`: The refund was cancelled by the client.
`failed`: The refund has failed.
`returned`: The refund was returned.


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `POSTED`    | posted      |
| `CANCELLED` | cancelled   |
| `FAILED`    | failed      |
| `SETTLED`   | settled     |
| `RETURNED`  | returned    |