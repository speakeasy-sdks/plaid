# Party

A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `individual`                                                                       | [components.PartyIndividual](../../models/components/partyindividual.md)           | :heavy_check_mark:                                                                 | Documentation not found in the MISMO model viewer and not provided by Freddie Mac. |
| `roles`                                                                            | [components.Roles](../../models/components/roles.md)                               | :heavy_check_mark:                                                                 | Documentation not found in the MISMO model viewer and not provided by Freddie Mac. |
| `taxpayer_identifiers`                                                             | [components.TaxpayerIdentifiers](../../models/components/taxpayeridentifiers.md)   | :heavy_check_mark:                                                                 | The collection of TAXPAYER_IDENTIFICATION elements                                 |
| `additional_properties`                                                            | Dict[str, *Any*]                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                |