# AccountIdentityVerificationStatus

The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.

`pending_automatic_verification`: The Item is pending automatic verification

`pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the micro-deposit.

`automatically_verified`: The Item has successfully been automatically verified	

`manually_verified`: The Item has successfully been manually verified

`verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.

`verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.	
	


## Values

| Name                             | Value                            |
| -------------------------------- | -------------------------------- |
| `AUTOMATICALLY_VERIFIED`         | automatically_verified           |
| `PENDING_AUTOMATIC_VERIFICATION` | pending_automatic_verification   |
| `PENDING_MANUAL_VERIFICATION`    | pending_manual_verification      |
| `MANUALLY_VERIFIED`              | manually_verified                |
| `VERIFICATION_EXPIRED`           | verification_expired             |
| `VERIFICATION_FAILED`            | verification_failed              |