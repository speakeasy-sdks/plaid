# SignalPaymentMethod

The payment method to complete the transaction after the risk assessment. It may be different from the default payment method.

`SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day

`NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors

`STANDARD_ACH`: standard ACH by NACHA

`REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow

`DEBIT_CARD`: if the default payment is over debit card networks

`MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods

Possible values: `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`



## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `SAME_DAY_ACH`             | SAME_DAY_ACH               |
| `NEXT_DAY_ACH`             | NEXT_DAY_ACH               |
| `STANDARD_ACH`             | STANDARD_ACH               |
| `REAL_TIME_PAYMENTS`       | REAL_TIME_PAYMENTS         |
| `DEBIT_CARD`               | DEBIT_CARD                 |
| `MULTIPLE_PAYMENT_METHODS` | MULTIPLE_PAYMENT_METHODS   |