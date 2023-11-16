# PayrollRiskSignalsItem

Object containing fraud risk data pertaining to the Item linked as part of the verification.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                            | Dict[str, *Any*]                                                                                   | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `item_id`                                                                                          | *str*                                                                                              | :heavy_check_mark:                                                                                 | The `item_id` of the Item associated with this webhook, warning, or error                          |
| `verification_risk_signals`                                                                        | List[[components.DocumentRiskSignalsObject](../../models/components/documentrisksignalsobject.md)] | :heavy_check_mark:                                                                                 | Array of payroll income document authenticity data retrieved for each of the user's accounts.      |