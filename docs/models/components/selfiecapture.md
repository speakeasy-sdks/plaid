# SelfieCapture

The image or video capture of a selfie. Only one of image or video URL will be populated per selfie.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `image_url`                                                                     | *Optional[str]*                                                                 | :heavy_check_mark:                                                              | Temporary URL for downloading an image selfie capture.                          | https://example.plaid.com/verifications/idv_52xR9LKo77r1Np/selfie/liveness.jpeg |
| `video_url`                                                                     | *Optional[str]*                                                                 | :heavy_check_mark:                                                              | Temporary URL for downloading a video selfie capture.                           | https://example.plaid.com/verifications/idv_52xR9LKo77r1Np/selfie/liveness.webm |
| `additional_properties`                                                         | Dict[str, *Any*]                                                                | :heavy_minus_sign:                                                              | N/A                                                                             |                                                                                 |