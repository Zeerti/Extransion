https://www.youtube.com/watch?v=4T5Gnrmzjak

# Register Registry Service

## Usage

All responses will have the form
```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "RX",
        "name": "Register X",
        "device_type": "Register",
        "ip": "192.168.0.1",
        "login_code": "1234567890",
        "order_iterations": "1000",
        "action_delay": "0.25",
        "clocked_in_status": "True",
    },
    {
        "identifier": "K2",
        "name": "Kitchen 2",
        "device_type": "KDS",
        "ip": "192.168.0.1"
    }
]
```

`POST /devices`


### Update register order iteration

**Definition**

`POST /status`

**Response**
```json