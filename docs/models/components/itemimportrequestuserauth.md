# ItemImportRequestUserAuth

Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `auth_token`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Authorization token Plaid will use to aggregate this user’s accounts |
| `user_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Opaque user identifier                                               |