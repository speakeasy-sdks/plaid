# Application

Metadata about the application


## Fields

| Field                                                                                                                                           | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `application_id`                                                                                                                                | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect.   |
| `application_url`                                                                                                                               | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | The URL for the application's website                                                                                                           |
| `city`                                                                                                                                          | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing the city of the client’s headquarters.                                                                                    |
| `company_legal_name`                                                                                                                            | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing the name of client’s legal entity.                                                                                        |
| `country_code`                                                                                                                                  | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing the country code of the client’s headquarters.                                                                            |
| `display_name`                                                                                                                                  | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A human-readable name of the application for display purposes                                                                                   |
| `join_date`                                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                    | :heavy_check_mark:                                                                                                                              | The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. |
| `logo_url`                                                                                                                                      | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A URL that links to the application logo image.                                                                                                 |
| `name`                                                                                                                                          | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | The name of the application                                                                                                                     |
| `postal_code`                                                                                                                                   | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing the postal code of the client’s headquarters.                                                                             |
| `reason_for_access`                                                                                                                             | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string provided by the connected app stating why they use their respective enabled products.                                                  |
| `region`                                                                                                                                        | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing the region of the client’s headquarters.                                                                                  |
| `use_case`                                                                                                                                      | *Optional[str]*                                                                                                                                 | :heavy_check_mark:                                                                                                                              | A string representing client’s broad use case as assessed by Plaid.                                                                             |