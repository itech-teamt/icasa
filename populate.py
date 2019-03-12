import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ITECH_Project.settings'
import django
django.setup()
from product.models import Category, Product


def populate():
    iPhone_list = [
        {"name": "iPhone XS Max gray",
         "image":"/products/XSMax_gray.jpg",
         "price":100,
         "description":"gray",
         "stock": 20,
         "detail": "The latest model!"},

        {"name": "iPhone XS Max black",
         "image": "/products/XSMax_gray.jpg",
         "price": 300,
         "description":"black",
         "stock": 20,
         "detail": "Cool!"},

        {"name": "iPhone5",
         "image": "/products/XSMax_gray.jpg",
         "price": 300,
         "description": "black",
         "stock": 20,
         "detail": "Cool!"},

        {"name": "iPhone4",
         "image": "/products/XSMax_gray.jpg",
         "price": 300,
         "description": "black",
         "stock": 20,
         "detail": "Cool!"},

        {"name": "iPhone",
         "image": "/products/XSMax_gray.jpg",
         "price": 300,
         "description": "black",
         "stock": 20,
         "detail": "Cool!"}
    ]

    watch_products = [
        {"name":"iWatch 4",
         "image":"/products/XSMax_gray.jpg",
         "price": 200,
         "description":"iWatch 4",
         "stock": 20,
         "detail": "fantastic!"}

    ]
    iPad_products=[


    ]
    Mac_products=[

    ]
    Accessories_products=[

    ]
    other_products=[

    ]

    cats = {"iPhone": {"products": iPhone_list},
            "Watch": {"products": watch_products},
            "iPad": {"products": iPad_products},
            "Mac": {"products": Mac_products},
            "Accessories": {"products": Accessories_products},
            "Other": {"products": other_products}
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["products"]:
            add_product(c, p["name"], p["image"], p["price"], p["description"], p["stock"], p["detail"])
    for c in Category.objects.all():
        for p in Product.objects.filter(category = c):
            print("- {0} - {1}".format(str(c),str(p)))


def add_product(cat, name, image, price, description, stock, detail):
    p = Product.objects.get_or_create(category=cat, name=name, price=price, stock=stock)[0]
    p.image = image
    p.description = description
    p.detail = detail
    p.save()
    return p


def add_cat(ctitle):
    c = Category.objects.get_or_create(ctitle=ctitle)[0]
    c.save()
    return c


# if __name__ == '_main_':
print("Starting it population script...")
populate()
