# RESTful APIs — A Plain-English Guide

---

## What is an API?

Think of an API (**Application Programming Interface**) as a **waiter in a restaurant**. You (the client) sit at the table with a menu of things you can order. The kitchen (the server) is where the food (data) is made. You don't walk into the kitchen yourself — you tell the waiter what you want, the waiter goes to the kitchen, and comes back with your order.

The API is the waiter. It takes your request, delivers it to the right place, and brings back a response.

---

## What makes an API "RESTful"?

**REST** stands for **Representational State Transfer**. It's a set of rules (an architectural style) for designing APIs that are simple, consistent, and work well over the internet.

An API is considered RESTful when it follows these core ideas:

| Principle | What it means in plain English |
|---|---|
| **Client–Server** | The app (client) and the data (server) are separate and talk to each other via requests |
| **Stateless** | Every request must contain all the information needed — the server remembers nothing between requests |
| **Uniform Interface** | All resources are accessed the same predictable way, using standard URLs and HTTP methods |
| **Resources** | Everything is treated as a "resource" — a user, a product, an order — each with its own URL address |
| **Representations** | Resources are sent as data snapshots (usually JSON), not the real object itself |
| **Cacheable** | Responses can be stored temporarily to speed things up |

---

## Resources and URLs

In REST, everything is a **resource** — a thing you can act on. Resources live at **URLs** (web addresses), sometimes called **endpoints**.

```
https://api.example.com/users          ← the collection of all users
https://api.example.com/users/42       ← one specific user (ID: 42)
https://api.example.com/users/42/posts ← all posts belonging to user 42
```

Think of a URL as a postal address. It tells the API exactly *where* the resource lives, and the HTTP verb tells it *what to do* with it.

---

## HTTP Verbs (Methods)

HTTP verbs are the **action words** of a REST API. They tell the server what operation you want to perform on a resource. There are five you'll encounter most often, and a few more used in specific situations.

### The Core Five

| Verb | Action | Real-world analogy |
|---|---|---|
| `GET` | **Read** — fetch data | Looking at a menu |
| `POST` | **Create** — add something new | Placing an order |
| `PUT` | **Replace** — fully update a resource | Rewriting an entire form |
| `PATCH` | **Modify** — partially update a resource | Crossing out one line on a form |
| `DELETE` | **Remove** — delete a resource | Cancelling an order |

### Additional Verbs

| Verb | Action | When it's used |
|---|---|---|
| `HEAD` | Like `GET` but returns **only the headers**, no body | Checking if a resource exists without downloading it |
| `OPTIONS` | Returns the list of **allowed HTTP methods** for a URL | Browser preflight checks (CORS) |
| `CONNECT` | Opens a **tunnel** to the server | Used with HTTPS proxies |
| `TRACE` | **Echoes** the request back — used for diagnostics | Debugging network paths |

### Quick Examples

```
GET    /products           → Fetch the list of all products
GET    /products/7         → Fetch the product with ID 7
POST   /products           → Create a brand new product
PUT    /products/7         → Completely replace product 7
PATCH  /products/7         → Update only one field of product 7
DELETE /products/7         → Delete product 7
```

---

## What Does a Request Look Like?

Every API call has two sides — the **request** (what you send) and the **response** (what you get back).

### Request structure

```
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{
  "name": "Maria Garcia",
  "email": "maria@example.com",
  "role": "admin"
}
```

| Part | What it is |
|---|---|
| `POST /users` | The verb + the resource URL |
| `Host` | The domain of the server |
| `Content-Type` | The format of the data being sent |
| `Authorization` | A token proving who you are |
| `{ ... }` | The **body** — the data you're sending |

### Response structure

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 105,
  "name": "Maria Garcia",
  "email": "maria@example.com",
  "role": "admin",
  "created_at": "2026-03-12T09:00:00Z"
}
```

| Part | What it is |
|---|---|
| `201 Created` | The **status code** — tells you if it worked |
| `Content-Type` | The format of the response data |
| `{ ... }` | The **body** — the data the server sends back |

---

## HTTP Status Codes — The Full List

Status codes are **three-digit numbers** the server sends back to tell you what happened with your request. They are grouped into five families, each with a clear meaning.

---

### 1xx — Informational
*"Hold on, something is in progress."*

| Code | Name | What it means |
|---|---|---|
| `100` | Continue | The server received the first part of the request and the client should continue sending the rest |
| `101` | Switching Protocols | The server agrees to switch protocols (e.g. upgrading from HTTP to WebSockets) |
| `102` | Processing | The server has received and is processing the request, but no response is ready yet *(WebDAV)* |
| `103` | Early Hints | Lets the browser start loading resources while the main response is still being prepared |

---

### 2xx — Success
*"Everything worked perfectly."*

| Code | Name | What it means |
|---|---|---|
| `200` | OK | The most common success. The request worked and here is your data |
| `201` | Created | A new resource was successfully created (e.g. after a POST) |
| `202` | Accepted | The request was accepted but hasn't been fully processed yet (async task queued) |
| `203` | Non-Authoritative Information | Success, but the data comes from a third-party cache, not the original server |
| `204` | No Content | Success, but there is nothing to return (common after DELETE or PATCH) |
| `205` | Reset Content | Success — the client should reset its form or view |
| `206` | Partial Content | The server is returning only part of the resource (used for large file downloads / streaming) |
| `207` | Multi-Status | Multiple operations were performed; status for each is in the response body *(WebDAV)* |
| `208` | Already Reported | The resource was already reported in an earlier part of the same response *(WebDAV)* |
| `226` | IM Used | The server fulfilled a `GET` request using delta encoding (only changes were sent) |

---

### 3xx — Redirection
*"The thing you want is somewhere else."*

| Code | Name | What it means |
|---|---|---|
| `300` | Multiple Choices | There are several possible responses — the client should pick one |
| `301` | Moved Permanently | The resource has moved to a new URL forever. Update your bookmark |
| `302` | Found | The resource is temporarily at a different URL. Keep using the original |
| `303` | See Other | The response to the request can be found at a different URL (use GET to retrieve it) |
| `304` | Not Modified | The cached version the client has is still fresh — no new data to send |
| `305` | Use Proxy | Must access the resource through a specific proxy *(deprecated)* |
| `307` | Temporary Redirect | Temporarily at a different URL — repeat the original request method (don't change POST to GET) |
| `308` | Permanent Redirect | Permanently moved — like 301, but the method must not change |

---

### 4xx — Client Errors
*"You did something wrong in the request."*

| Code | Name | What it means |
|---|---|---|
| `400` | Bad Request | The request is malformed — missing fields, bad JSON, invalid syntax |
| `401` | Unauthorized | You need to log in. No valid credentials were provided |
| `402` | Payment Required | Reserved for payment-related barriers (used by some billing APIs) |
| `403` | Forbidden | You're logged in but not allowed to access this resource |
| `404` | Not Found | The resource doesn't exist at this URL |
| `405` | Method Not Allowed | You used the wrong verb (e.g. sent a DELETE to a read-only endpoint) |
| `406` | Not Acceptable | The server can't return data in the format the client requested (Accept header mismatch) |
| `407` | Proxy Authentication Required | You need to authenticate with a proxy server first |
| `408` | Request Timeout | The client took too long to send the request and the server gave up waiting |
| `409` | Conflict | The request conflicts with the current state of the resource (e.g. duplicate entry) |
| `410` | Gone | The resource existed before but has been permanently deleted — it's not coming back |
| `411` | Length Required | The request must include a `Content-Length` header |
| `412` | Precondition Failed | A condition in the request headers was not met by the server |
| `413` | Content Too Large | The request body is bigger than the server is willing to accept |
| `414` | URI Too Long | The URL is too long for the server to process |
| `415` | Unsupported Media Type | The server doesn't support the format of the data you sent (e.g. sent XML, expected JSON) |
| `416` | Range Not Satisfiable | The byte range requested doesn't exist in the resource |
| `417` | Expectation Failed | The `Expect` request header couldn't be met by the server |
| `418` | I'm a Teapot | An April Fools' joke from 1998 — a teapot refuses to brew coffee. Some APIs use it humorously |
| `421` | Misdirected Request | The request was sent to a server that can't produce a response for it |
| `422` | Unprocessable Content | The request is well-formed but contains semantic errors (e.g. invalid field values) |
| `423` | Locked | The resource is locked and cannot be modified *(WebDAV)* |
| `424` | Failed Dependency | The request failed because a previous dependent request failed *(WebDAV)* |
| `425` | Too Early | The server refuses to process a request that might be replayed |
| `426` | Upgrade Required | The client must upgrade to a different protocol (e.g. TLS) |
| `428` | Precondition Required | The request must be conditional to prevent accidental overwrites |
| `429` | Too Many Requests | You've sent too many requests in a short time — slow down (rate limiting) |
| `431` | Request Header Fields Too Large | The HTTP headers in the request are too large |
| `451` | Unavailable For Legal Reasons | The content has been blocked for legal reasons (censorship, court order, etc.) |

---

### 5xx — Server Errors
*"We received your request, but something went wrong on our end."*

| Code | Name | What it means |
|---|---|---|
| `500` | Internal Server Error | A generic catch-all. Something broke on the server and it doesn't know what |
| `501` | Not Implemented | The server doesn't support the HTTP method that was used |
| `502` | Bad Gateway | The server was acting as a gateway and got a bad response from the upstream server |
| `503` | Service Unavailable | The server is down — overloaded or under maintenance. Try again later |
| `504` | Gateway Timeout | The gateway didn't get a response from the upstream server in time |
| `505` | HTTP Version Not Supported | The server doesn't support the HTTP version used in the request |
| `506` | Variant Also Negotiates | A configuration error in content negotiation on the server |
| `507` | Insufficient Storage | The server can't store the data needed to complete the request *(WebDAV)* |
| `508` | Loop Detected | The server detected an infinite loop while processing the request *(WebDAV)* |
| `510` | Not Extended | Further extensions to the request are required for the server to fulfill it |
| `511` | Network Authentication Required | The client must authenticate to gain network access (e.g. a captive Wi-Fi portal) |

---

## The Most Important Codes to Know

If you only memorise a handful, make it these:

| Code | Meaning | Remember it as |
|---|---|---|
| `200` | OK | ✅ All good |
| `201` | Created | ✅ New thing made |
| `204` | No Content | ✅ Done, nothing to return |
| `400` | Bad Request | ❌ You sent garbage |
| `401` | Unauthorized | 🔒 Who are you? |
| `403` | Forbidden | 🚫 I know who you are — still no |
| `404` | Not Found | 🔍 Doesn't exist |
| `409` | Conflict | ⚠️ Already exists |
| `422` | Unprocessable Content | ⚠️ Makes sense but values are wrong |
| `429` | Too Many Requests | 🐢 Slow down |
| `500` | Internal Server Error | 💥 Server broke |
| `503` | Service Unavailable | 🛑 Server is down |

---

## Putting It All Together — A Real Example

Here's a mini story of CRUD operations (Create, Read, Update, Delete) on a `books` resource:

```
# 1. Get all books
GET /books
→ 200 OK  [ { "id": 1, "title": "Dune" }, { "id": 2, "title": "1984" } ]

# 2. Get one book
GET /books/1
→ 200 OK  { "id": 1, "title": "Dune", "author": "Frank Herbert" }

# 3. Create a new book
POST /books  { "title": "Neuromancer", "author": "William Gibson" }
→ 201 Created  { "id": 3, "title": "Neuromancer", "author": "William Gibson" }

# 4. Try to create the same book again
POST /books  { "title": "Neuromancer", "author": "William Gibson" }
→ 409 Conflict  { "error": "A book with this title already exists" }

# 5. Update just the author field
PATCH /books/3  { "author": "W. Gibson" }
→ 200 OK  { "id": 3, "title": "Neuromancer", "author": "W. Gibson" }

# 6. Delete the book
DELETE /books/3
→ 204 No Content

# 7. Try to fetch the deleted book
GET /books/3
→ 404 Not Found  { "error": "Book not found" }
```

---

## Quick Reference Summary

```
REST  =  Resources + HTTP Verbs + Status Codes + JSON

URL   →  WHERE the resource lives
Verb  →  WHAT you want to do with it
Code  →  HOW the operation went
Body  →  THE DATA going in or coming out
```

---

*REST is the common language of the modern web. Once you understand resources, verbs, and status codes, you can read and work with virtually any public API out there.* 🌐
