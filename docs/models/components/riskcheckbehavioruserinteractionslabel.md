# RiskCheckBehaviorUserInteractionsLabel

Field describing the overall user interaction signals of a behavior risk check. This value represents how familiar the user is with the personal data they provide, based on a number of signals that are collected during their session.

`genuine` indicates the user has high familiarity with the data they are providing, and that fraud is unlikely.

`neutral` indicates some signals are present in between `risky` and `genuine`, but there are not enough clear signals to determine an outcome.

`risky` indicates the user has low familiarity with the data they are providing, and that fraud is likely.

`no_data` indicates there is not sufficient information to give an accurate signal.


## Values

| Name      | Value     |
| --------- | --------- |
| `GENUINE` | genuine   |
| `NEUTRAL` | neutral   |
| `RISKY`   | risky     |
| `NO_DATA` | no_data   |