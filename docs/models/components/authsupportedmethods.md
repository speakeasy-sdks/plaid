# AuthSupportedMethods

Metadata specifically related to which auth methods an institution supports.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `automated_micro_deposits`                          | *bool*                                              | :heavy_check_mark:                                  | Indicates if automated microdeposits are supported. |
| `instant_auth`                                      | *bool*                                              | :heavy_check_mark:                                  | Indicates if instant auth is supported.             |
| `instant_match`                                     | *bool*                                              | :heavy_check_mark:                                  | Indicates if instant match is supported.            |
| `additional_properties`                             | Dict[str, *Any*]                                    | :heavy_minus_sign:                                  | N/A                                                 |