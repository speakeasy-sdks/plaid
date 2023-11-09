# Email

An object representing an email address


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `additional_properties`                                                       | Dict[str, *Any*]                                                              | :heavy_minus_sign:                                                            | N/A                                                                           |
| `data`                                                                        | *str*                                                                         | :heavy_check_mark:                                                            | The email address.                                                            |
| `primary`                                                                     | *bool*                                                                        | :heavy_check_mark:                                                            | When `true`, identifies the email address as the primary email on an account. |
| `type`                                                                        | [components.Type](../../models/components/type.md)                            | :heavy_check_mark:                                                            | The type of email account as described by the financial institution.          |