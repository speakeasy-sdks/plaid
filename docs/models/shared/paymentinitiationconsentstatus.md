# PaymentInitiationConsentStatus

The status of the payment consent.

`UNAUTHORISED`: Consent created, but requires user authorisation.

`REJECTED`: Consent authorisation was rejected by the user and/or the bank.

`AUTHORISED`: Consent is active and ready to be used.

`REVOKED`: Consent has been revoked and can no longer be used.

`EXPIRED`: Consent is no longer valid.


## Values

| Name           | Value          |
| -------------- | -------------- |
| `UNAUTHORISED` | UNAUTHORISED   |
| `AUTHORISED`   | AUTHORISED     |
| `REVOKED`      | REVOKED        |
| `REJECTED`     | REJECTED       |
| `EXPIRED`      | EXPIRED        |