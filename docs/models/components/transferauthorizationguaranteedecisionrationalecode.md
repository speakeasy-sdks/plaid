# TransferAuthorizationGuaranteeDecisionRationaleCode

A code representing the reason Plaid declined to guarantee this transfer:

`RETURN_BANK`: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this transfer.

`RETURN_CUSTOMER`: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to guarantee this transfer.

`GUARANTEE_LIMIT_REACHED`: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number or rate of guarantees that applies to this transfer.

`RISK_ESTIMATE_UNAVAILABLE`: A risk estimate is unavailable for this Item.

`REQUIRED_PARAM_MISSING`: Required fields are missing.


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `RETURN_BANK`               | RETURN_BANK                 |
| `RETURN_CUSTOMER`           | RETURN_CUSTOMER             |
| `GUARANTEE_LIMIT_REACHED`   | GUARANTEE_LIMIT_REACHED     |
| `RISK_ESTIMATE_UNAVAILABLE` | RISK_ESTIMATE_UNAVAILABLE   |
| `REQUIRED_PARAM_MISSING`    | REQUIRED_PARAM_MISSING      |