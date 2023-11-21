# SignalInsights

Signal insights including scores and attributes. This response is offered as an add-on to `/transfer/authorization/create`. To request access to these fields please contact your Plaid account manager.


## Fields

| Field                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                             | Dict[str, *Any*]                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                 |
| `scores`                                                                                                                                                                                                                                                                                            | [Optional[components.SignalScores]](../../models/components/signalscores.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Risk scoring details broken down by risk category.                                                                                                                                                                                                                                                  |
| `warnings`                                                                                                                                                                                                                                                                                          | List[[components.SignalWarning](../../models/components/signalwarning.md)]                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | If bank information was not available to be used in the Signal model, this array contains warnings describing why bank data is missing. If you want to receive an API error instead of Signal scores in the case of missing bank data, file a support ticket or contact your Plaid account manager. |