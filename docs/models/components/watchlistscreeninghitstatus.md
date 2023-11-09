# WatchlistScreeningHitStatus

The current state of review. All watchlist screening hits begin in a `pending_review` state but can be changed by creating a review. When a hit is in the `pending_review` state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as `confirmed` or `dismissed` it will no longer be updated so that the state is as it was when the review was first conducted.


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `CONFIRMED`      | confirmed        |
| `PENDING_REVIEW` | pending_review   |
| `DISMISSED`      | dismissed        |