# WatchlistScreeningEntityHitListResponse

Paginated list of entity watchlist screening hits


## Fields

| Field                                                                                                                                       | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 | Example                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                     | Dict[str, *Any*]                                                                                                                            | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |                                                                                                                                             |
| `entity_watchlist_screening_hits`                                                                                                           | List[[components.EntityWatchlistScreeningHit](../../models/components/entitywatchlistscreeninghit.md)]                                      | :heavy_check_mark:                                                                                                                          | List of entity watchlist screening hits                                                                                                     |                                                                                                                                             |
| `next_cursor`                                                                                                                               | *Optional[str]*                                                                                                                             | :heavy_check_mark:                                                                                                                          | An identifier that determines which page of results you receive.                                                                            | eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM                                                                                             |
| `request_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |                                                                                                                                             |