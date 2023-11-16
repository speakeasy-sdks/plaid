# PaymentProfileStatus

The status of the given Payment Profile.

`READY`: This Payment Profile is ready to be used to create transfers using `/transfer/authorization/create` and `/transfer/create`.

`PENDING`: This Payment Profile is not ready to be used. You’ll need to call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field to initiate the account linking experience.

`REMOVED`: This Payment Profile has been removed.


## Values

| Name      | Value     |
| --------- | --------- |
| `PENDING` | PENDING   |
| `READY`   | READY     |
| `REMOVED` | REMOVED   |