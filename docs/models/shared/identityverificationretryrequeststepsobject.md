# IdentityVerificationRetryRequestStepsObject

Instructions for the `custom` retry strategy specifying which steps should be required or skipped.


Note:


This field must be provided when the retry strategy is `custom` and must be omitted otherwise.

Custom retries override settings in your Plaid Template. For example, if your Plaid Template has `verify_sms` disabled, a custom retry with `verify_sms` enabled will still require the step.

The `selfie_check` step is currently not supported on the sandbox server. Sandbox requests will silently disable the `selfie_check` step when provided.


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `documentary_verification`                                                                                     | *bool*                                                                                                         | :heavy_check_mark:                                                                                             | A boolean field specifying whether the new session should require or skip the `documentary_verification` step. |
| `kyc_check`                                                                                                    | *bool*                                                                                                         | :heavy_check_mark:                                                                                             | A boolean field specifying whether the new session should require or skip the `kyc_check` step.                |
| `selfie_check`                                                                                                 | *bool*                                                                                                         | :heavy_check_mark:                                                                                             | A boolean field specifying whether the new session should require or skip the `selfie_check` step.             |
| `verify_sms`                                                                                                   | *bool*                                                                                                         | :heavy_check_mark:                                                                                             | A boolean field specifying whether the new session should require or skip the `verify_sms` step.               |