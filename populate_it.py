# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ITECH_Project.settings')

import django
django.setup()

from product.models import Category, Product

def populate():
        iphone_products = [
                {"name":"iPhoneXS",
                "image":"/images/products/iphoneXS.jpg",
                "price":"899",
                "description":"Super Retina. In big and bigger",
                 "stock":"2000",
                 "detail":"The custom OLED displays on iPhone XS deliver the most accurate colour in the industry, HDR and true blacks."},

                {"name": "iPhone XS Max",
                 "image": "/images/products/XSMax_gray.jpg",
                 "price": "1000",
                 "description": "The new generation of iPhone",
                 "stock": "1000",
                 "detail": "Super Retina in two sizes,including the largest display ever on an iPhone. Even faster Face ID. The smartest, most powerful chip in a smartPhone."},

                {"name": "iPhone XR",
                 "image": "/products/iPhone-XR.jpg",
                 "price": "749",
                 "description": "Brilliant. In every way.",
                 "stock": "1000",
                 "detail": "All-new Liquid Retina display — the most advanced LCD in the industry. A12 Bionic, the smartest, most powerful chip in a smartphone. Advanced Face ID. And a breakthrough camera system with Depth Control."},

        ]
        
        watch_products = [
                {"name":"iWatch series 3",
                "image":"/products/watch series3.jpg",
                "price":"279",
                "description":"Stay active.Stay healthy.Stay connected.",
                 "stock":"200",
                 "detail":"Monitor your health. Track your workouts. Get the motivation you need to achieve your fitness goals."},

                {"name": "iWatch series 4",
                 "image": "/products/iwatch-series-4.jpg",
                 "price": "399",
                 "description": "All new. For a better you.",
                 "stock": "20",
                 "detail": "Fundamentally redesigned and re-engineered to help you stay even more active, healthy and connected."},

                {"name": "iWatch series 4_hermes",
                 "image": "/products/watch4_hermes.gif",
                 "price": "1299",
                 "description": "A shared vision, seen in a whole new light.",
                 "stock": "200",
                 "detail": "A partnership based on parallel thinking, singular vision and mutual regard continues with a fresh new expression. The latest Apple Watch Hermès collection showcases boldly colourful leather straps and a delightful new watch face designed by Apple. "},

                {"name": "iWatch series 4_nike",
                 "image": "/products/watch-Nike-Series-4.jpg",
                 "price": "399",
                 "description": "Reflective Nike Sport Loop.Be seen in all the right places.",
                 "stock": "600",
                 "detail": "To help you stand out, Apple Watch Nike+ Series 4 is now available with a Nike Sport Loop strap that’s woven with special reflective thread designed to shimmer when light strikes it."}]


        pad_products=[
            {
                "name": "iPad Pro 2018",
                "image": "/products/iPad Pro2018.jpg",
                "price": "888",
                "description": "New,full screen,all-round powerful",
                "stock": "12",
                "detail": "interactive gesture,intuitive and easy to operate,face ID,scan face to pay",
            }

        ]
        mac_products=[
            {
                "name": "MacBook Air",
                "image": "/products/bookAir 4color.jpg",
                "price": "980",
                "description": "Versatile,many in one",
                "stock": "20",
                "detail": "13.3 inches, 2,560 x 1,600 resolution brings in over 4 million pixels"
            }
        ]

        accessories_products=[
            {
                "name": "Cases & Covers",
                "image": "/products/iphone case pink.jpg",
                "price": "30",
                "description": "iphone 8 case",
                "stock": "100",
                "detail": "pink"
            },

            {
                "name": "mac bags",
                "image": "/products/bag.jpg",
                "price": "79.95",
                "description": "laptop bag",
                "stock": "100",
                "detail": "Offering functional storage for your devices."
            },

            {
                "name": "keyboard folio",
                "image": "/products/keyboard.jpg",
                "price": "179",
                "description": "smart keyboard folio for iPad pro",
                "stock": "50",
                "detail": "The smart keyboard folio for the 11-inch iPad Pro is a full-size keyboard."
            },

            {
                "name": "iPhone XS film",
                "image": "/products/iphoneXS film.jpg",
                "price": "14.95",
                "description": "iphone XS film",
                "stock": "1000",
                "detail": "The Belkin protector not only prevents visual damage to keep your iPhone looking like new, it also preserves the touchscreen’s functionality."
            },

            {
                "name": "iphoneXS armband",
                "image": "/products/iphone XS armband.jpg",
                "price": "29.95",
                "description": "iphone X armband",
                "stock": "30",
                "detail": "Sport Running Exercise Gym armband for iphone X/XS"
            }
        ]

        other_products=[
            {
                "name": "AirPods",
                "image": "/products/AirPods.jpg",
                "price": "120",
                "description": "New generation wireless earphone, dissolve numerous and complicated.",
                "stock": "15",
                "detail": "Single click, the AirPods are automatically turned on and always connected."
            }
        ]
        cats = {
                "iphone":{"products":iphone_products},
                "iPad": {"products": pad_products},
                "mac": {"products": mac_products},
                "watch":{"products":watch_products},
                "accessories":{"products":accessories_products},
                "other":{"products":other_products},
                }
                

        for cat, cat_data in cats.items():
                c = add_cat(cat)
                for p in cat_data["products"]:
                        add_product(c,p["name"],p["image"],p["price"],p["description"],p["stock"],p["detail"])
        for c in Category.objects.all():
                for p in Product.objects.filter(category = c):
                        print("- {0} - {1}".format(str(c),str(p)))

def add_product(cat,name,image,price,description,stock,detail):
    p = Product.objects.get_or_create(category=cat, name=name,price=price,stock=stock)[0]
    p.image=image
    #p.price=price
    p.description=description
    #p.stock=stock
    p.detail=detail
    p.save()
    return p

def add_cat(ctitle):
    c = Category.objects.get_or_create(ctitle=ctitle)[0]
    c.save()
    return c

#if __name__ == '_main_':
print("Starting it population script...")
populate()