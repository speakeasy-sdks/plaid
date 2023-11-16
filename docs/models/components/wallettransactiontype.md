# WalletTransactionType

The type of the transaction. The supported transaction types that are returned are:
`BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.

`PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.

`PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).

`REFUND:` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).

`FUNDS_SWEEP`: an automated transaction which debits funds from an e-wallet to a designated client-owned account.


## Values

| Name            | Value           |
| --------------- | --------------- |
| `BANK_TRANSFER` | BANK_TRANSFER   |
| `PAYOUT`        | PAYOUT          |
| `PIS_PAY_IN`    | PIS_PAY_IN      |
| `REFUND`        | REFUND          |
| `FUNDS_SWEEP`   | FUNDS_SWEEP     |