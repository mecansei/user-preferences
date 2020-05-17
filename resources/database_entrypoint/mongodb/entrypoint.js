db.createCollection("userLikeCollection");
db.userLikeCollection.insertMany([
    {
        "user_id": "abc",
        "product_id": "products_1"
    },
    {
        "user_id": "aaa",
        "product_id": "products_1"
    },
    {
        "user_id": "aaa",
        "product_id": "products_2"
    },
    {
        "user_id": "bbb",
        "product_id": "products_3"
    },
    {
        "user_id": "bbb",
        "product_id": "products_2"
    },
    {
        "user_id": "ccc",
        "product_id": "products_1"
    },
    {
        "user_id": "bca",
        "product_id": "products_1"
    },
]);


db.createCollection("userDislikeCollection");
db.userDislikeCollection.insertMany([
    {
        "user_id": "abc",
        "product_id": "products_2"
    },
    {
        "user_id": "aaa",
        "product_id": "products_3"
    }
]);
