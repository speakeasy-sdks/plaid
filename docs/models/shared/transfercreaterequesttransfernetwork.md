# ~~TransferCreateRequestTransferNetwork~~

The network or rails used for the transfer.

For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ACH`          | ach            |
| `SAME_DAY_ACH` | same-day-ach   |
| `RTP`          | rtp            |