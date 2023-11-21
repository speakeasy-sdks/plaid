# TransferAuthorization

Contains the authorization decision for a proposed transfer.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `created`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The datetime representing when the authorization was created, in the format `2006-01-02T15:04:05Z`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `decision`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [components.TransferAuthorizationDecision](../../models/components/transferauthorizationdecision.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <br/>A decision regarding the proposed transfer.<br/><br/>`approved` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `ITEM_LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.<br/><br/>`declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details. |
| `decision_rationale`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[components.TransferAuthorizationDecisionRationale]](../../models/components/transferauthorizationdecisionrationale.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `guarantee_decision`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[components.TransferAuthorizationGuaranteeDecision]](../../models/components/transferauthorizationguaranteedecision.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details.                                                                                                                                                                                                                                                                              |
| `guarantee_decision_rationale`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Optional[components.TransferAuthorizationGuaranteeDecisionRationale]](../../models/components/transferauthorizationguaranteedecisionrationale.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Plaid’s unique identifier for a transfer authorization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `proposed_transfer`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [components.TransferAuthorizationProposedTransfer](../../models/components/transferauthorizationproposedtransfer.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Details regarding the proposed transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `signal_insights`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[components.SignalInsights]](../../models/components/signalinsights.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Signal insights including scores and attributes. This response is offered as an add-on to `/transfer/authorization/create`. To request access to these fields please contact your Plaid account manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |