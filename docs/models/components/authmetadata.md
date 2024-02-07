# AuthMetadata

Metadata that captures information about the Auth features of an institution.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `supported_methods`                                                                          | [Optional[components.AuthSupportedMethods]](../../models/components/authsupportedmethods.md) | :heavy_check_mark:                                                                           | Metadata specifically related to which auth methods an institution supports.                 |
| `additional_properties`                                                                      | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |