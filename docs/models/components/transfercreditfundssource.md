# TransferCreditFundsSource

Specifies the source of funds for the transfer. Only valid for `credit` transfers, and defaults to `sweep` if not specified. This field is not specified for `debit` transfers.

`sweep` - Sweep funds from your funding account
`prefunded_rtp_credits` - Use your prefunded RTP credit balance with Plaid
`prefunded_ach_credits` - Use your prefunded ACH credit balance with Plaid


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `SWEEP`                 | sweep                   |
| `PREFUNDED_RTP_CREDITS` | prefunded_rtp_credits   |
| `PREFUNDED_ACH_CREDITS` | prefunded_ach_credits   |