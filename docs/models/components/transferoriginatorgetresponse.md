# TransferOriginatorGetResponse

Defines the response schema for `/transfer/originator/get`


## Fields

| Field                                                                                                                                       | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                     | Dict[str, *Any*]                                                                                                                            | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `originator`                                                                                                                                | [components.DetailedOriginator](../../models/components/detailedoriginator.md)                                                              | :heavy_check_mark:                                                                                                                          | Originator and their status.                                                                                                                |
| `request_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |