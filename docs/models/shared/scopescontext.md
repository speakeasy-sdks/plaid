# ScopesContext

An indicator for when scopes are being updated. When scopes are updated via enrollment (i.e. OAuth), the partner must send `ENROLLMENT`. When scopes are updated in a post-enrollment view, the partner must send `PORTAL`.


## Values

| Name         | Value        |
| ------------ | ------------ |
| `ENROLLMENT` | ENROLLMENT   |
| `PORTAL`     | PORTAL       |