# WatchlistScreeningRequestSearchTerms

Search inputs for creating a watchlist screening


## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `country`                                                                                                            | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form. | US                                                                                                                   |
| `date_of_birth`                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                         | :heavy_minus_sign:                                                                                                   | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).                                                              | 1990-05-29                                                                                                           |
| `document_number`                                                                                                    | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | The numeric or alphanumeric identifier associated with this document.                                                | C31195855                                                                                                            |
| `legal_name`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The legal name of the individual being screened.                                                                     | Aleksey Potemkin                                                                                                     |
| `watchlist_program_id`                                                                                               | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | ID of the associated program.                                                                                        | prg_2eRPsDnL66rZ7H                                                                                                   |