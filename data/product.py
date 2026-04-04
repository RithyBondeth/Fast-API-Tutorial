from typing import List
from schemas.product import ProductSchema

products: List[ProductSchema] = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 100,
        "description": "Description 1",
        "stock": 10,
        "reviews": [
            {
                "user": "User 1",
                "rating": 5,
                "comment": "Comment 1",
            },
            {
                "user": "User 2",
                "rating": 4,
                "comment": "Comment 2",
            },
        ],
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 200,
        "description": "Description 2",
        "stock": 20,
        "reviews": [
            {
                "user": "User 3",
                "rating": 3,
                "comment": "Comment 3",
            },
            {
                "user": "User 4",
                "rating": 2,
                "comment": "Comment 4",
            },
        ],
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 300,
        "description": "Description 3",
        "stock": 30,
        "reviews": [
            {
                "user": "User 5",
                "rating": 1,
                "comment": "Comment 5",
            },
            {
                "user": "User 6",
                "rating": 5,
                "comment": "Comment 6",
            },
        ],
    },
    {
        "id": 4,
        "name": "Product 4",
        "price": 400,
        "description": "Description 4",
        "stock": 40,
        "reviews": [
            {
                "user": "User 7",
                "rating": 4,
                "comment": "Comment 7",
            },
            {
                "user": "User 8",
                "rating": 3,
                "comment": "Comment 8",
            },
        ],
    },
]