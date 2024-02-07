# RiskCheckStolenIdentity

Field containing the data used in determining the outcome of the stolen identity risk check.

Contains the following fields:

`score` - A score from 0 to 100 indicating the likelihood that the user is a stolen identity.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `score`                                                                             | *int*                                                                               | :heavy_check_mark:                                                                  | A score from 0 to 100 indicating the likelihood that the user is a stolen identity. | 0                                                                                   |
| `additional_properties`                                                             | Dict[str, *Any*]                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |                                                                                     |