# PartnerEndCustomerSecrets

The secrets for the newly created end customer in non-Production environments.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `additional_properties`                                        | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            |
| `development`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | The end customer's secret key for the Development environment. |
| `sandbox`                                                      | *Optional[str]*                                                | :heavy_minus_sign:                                             | The end customer's secret key for the Sandbox environment.     |