# README

## Ruby version
- 3.0.2

## Rails version
- 7.0.4

## API endpoints
#### __1. POST products__
### Request
```bash
POST /api/v1/products/?search_key=dell g15
```
### Response body
```json
[
    {
        "price": 84999.0,
        "rate": 0.0,
        "score": -0.8925874606601575,
        "imageUrl": "https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/21/549493/1.jpg?5324",
        "reviewsCount": 0,
        "link": "https://www.jumia.com.eg/asus-rog-strix-scar-15-g533zw-ln086w-core-i9-12900h-15.6-16gb-ddr5-2-1tb-ssd-rtxtm-3070-ti-8gb-gddr6-win11home-39494512.html",
        "source": "jumia",
        "header": "Asus ROG Strix SCAR 15 G533ZW-LN086W-core I9 12900H-15.6-16GB DDR5 *2-1TB SSD-RTX™ 3070 Ti 8GB GDDR6-Win11Home"
    }
]
```
 
- - - -

#### __2. GET products (search)__
### Request
```bash
GET /api/v1/products
```
### Response body
```json
[
    {
        "id": 47,
        "name": "ASUS ROG Strix 750 Fully Modular 80 Plus Gold 750W ATX Power Supply with 0dB Axial Tech Fan and 10 Year Warranty",
        "price": 6208.0,
        "link": "https://www.amazon.eg/-/en/ASUS-Strix-Modular-Supply-Warranty/dp/B07YXKMGX7/ref=sr_1_12?keywords=asus+rog+strix&qid=1683328240&sr=8-12",
        "rating": 4.8,
        "reviews_count": 1025,
        "img_url": "https://m.media-amazon.com/images/I/81GgwLqahaL._AC_UL400_.jpg",
        "source": "amazon",
        "created_at": "2023-05-05T23:11:47.481Z",
        "updated_at": "2023-05-05T23:11:47.481Z",
        "score": 0.9537266780523959
    },
    {
        "id": 30,
        "name": "Dell G15 15-5510 Gaming laptop - Intel Core i5-10500H 6Cores, 8GB RAM, 512GB SSD, Nvidia Geforce GTX1650 4GB GDDR6 Graphics, 15.6 FHD IPS 120Hz, Backlit Keyboard, UBUNTU - Shadow Grey",
        "price": 26225.9,
        "link": "https://www.amazon.eg/-/en/Dell-G15-15-5510-Gaming-laptop/dp/B09QP2GBNR/ref=sr_1_9?keywords=dell+g15&qid=1683158036&sr=8-9",
        "rating": 3.9,
        "reviews_count": 42,
        "img_url": "https://m.media-amazon.com/images/I/51A8t1QkjRL._AC_UL400_.jpg",
        "source": "amazon",
        "created_at": "2023-05-03T23:55:09.239Z",
        "updated_at": "2023-05-03T23:55:09.239Z",
        "score": 0.6774193548387096
    }
]
```
- - - -

#### __3. Get search keywords__
### Request
```bash
GET /api/v1/searches
```
### Response body
```json
[
    {
        "id": 1,
        "search_key": "dell g15",
        "website_name": "all",
        "created_at": "2023-05-03T23:52:54.680Z",
        "updated_at": "2023-05-03T23:52:54.680Z"
    },
    {
        "id": 3,
        "search_key": "asus rog strix",
        "website_name": "all",
        "created_at": "2023-05-05T23:10:22.896Z",
        "updated_at": "2023-05-05T23:10:22.896Z"
    }
]
```
#### Note: Add this in Headers section of every request:
Key  | Value
------------- | -------------
Authorization  | eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7xGXdq5PJHMYyvqCCV0hwA2lCCde9LrUZkyFTX2Bc0s
##### where the value must be replaced with the token value obtained after login.
