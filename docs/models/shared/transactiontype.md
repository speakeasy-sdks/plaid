# ~~TransactionType~~

Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.

`digital:` transactions that took place online.

`place:` transactions that were made at a physical location.

`special:` transactions that relate to banks, e.g. fees or deposits.

`unresolved:` transactions that do not fit into the other three types.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Values

| Name         | Value        |
| ------------ | ------------ |
| `DIGITAL`    | digital      |
| `PLACE`      | place        |
| `SPECIAL`    | special      |
| `UNRESOLVED` | unresolved   |