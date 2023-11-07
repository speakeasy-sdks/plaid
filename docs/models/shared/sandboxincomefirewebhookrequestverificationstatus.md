# SandboxIncomeFireWebhookRequestVerificationStatus

`VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.

`VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.

`VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.


## Values

| Name                                      | Value                                     |
| ----------------------------------------- | ----------------------------------------- |
| `VERIFICATION_STATUS_PROCESSING_COMPLETE` | VERIFICATION_STATUS_PROCESSING_COMPLETE   |
| `VERIFICATION_STATUS_PROCESSING_FAILED`   | VERIFICATION_STATUS_PROCESSING_FAILED     |
| `VERIFICATION_STATUS_PENDING_APPROVAL`    | VERIFICATION_STATUS_PENDING_APPROVAL      |