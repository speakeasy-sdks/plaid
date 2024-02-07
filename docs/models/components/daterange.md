# DateRange

A date range with a start and end date


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `beginning`                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).                      | 1990-05-29                                                                   |
| `ending`                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).                      | 1990-05-29                                                                   |
| `additional_properties`                                                      | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | N/A                                                                          | {"ending":"1966-06-30","beginning":"1966-06-01"}                             |