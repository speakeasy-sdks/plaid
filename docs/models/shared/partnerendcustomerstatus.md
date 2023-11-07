# PartnerEndCustomerStatus

The status of the given end customer.

`UNDER_REVIEW`: The end customer has been created and enabled in the non-Production environments. The end customer must be manually reviewed by the Plaid team before it can be enabled in production, at which point its status will automatically transition to `PENDING_ENABLEMENT` or `DENIED`.

`PENDING_ENABLEMENT`: The end customer is ready to be enabled in the Production environment. Call the `/partner/customer/enable` endpoint to enable the end customer in Production.

`ACTIVE`: The end customer has been enabled in all environments.

`DENIED`: The end customer has been created and enabled in the non-Production environments, but it did not pass review by the Plaid team and therefore cannot be enabled in the Production environment. Talk to your Account Manager for more information.


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `UNDER_REVIEW`       | UNDER_REVIEW         |
| `PENDING_ENABLEMENT` | PENDING_ENABLEMENT   |
| `ACTIVE`             | ACTIVE               |
| `DENIED`             | DENIED               |