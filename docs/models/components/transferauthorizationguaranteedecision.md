# TransferAuthorizationGuaranteeDecision

Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details.


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `GUARANTEED`     | GUARANTEED       |
| `NOT_GUARANTEED` | NOT_GUARANTEED   |