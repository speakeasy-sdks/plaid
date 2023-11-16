# ACHClass

Specifies the use case of the transfer. Required for transfers on an ACH network.

`"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

`"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

`"tel"` - Telephone-Initiated Entry

`"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet


## Values

| Name  | Value |
| ----- | ----- |
| `CCD` | ccd   |
| `PPD` | ppd   |
| `TEL` | tel   |
| `WEB` | web   |