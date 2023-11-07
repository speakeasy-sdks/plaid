# EntityScreeningHitEmailsItems

Analyzed emails for the associated hit


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `additional_properties`                                                                          | Dict[str, *Any*]                                                                                 | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `analysis`                                                                                       | [Optional[components.MatchSummary]](../../models/shared/matchsummary.md)                         | :heavy_minus_sign:                                                                               | Summary object reflecting the match result of the associated data                                |
| `data`                                                                                           | [Optional[components.EntityScreeningHitEmails]](../../models/shared/entityscreeninghitemails.md) | :heavy_minus_sign:                                                                               | Email address information for the associated entity watchlist hit                                |