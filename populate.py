# coding=utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITECH_Project.settings')

import django

django.setup()

from product.models import Category, Product
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

def populate():
    iphone_products = [
        {"name": "iPhoneXS",
         "image": "/products/iphoneXS1.jpg",
         "price": 899,
         "description": "Super Retina. In big and bigger",
         "stock": 2000,
         "detail": "The custom OLED displays on iPhone XS deliver the most accurate colour in the industry, HDR and true blacks."},

        {"name": "iPhone XS Max",
         "image": "/products/iPhoneXsMax1.jpg",
         "price": 1000,
         "description": "The new generation of iPhone",
         "stock": 1000,
         "detail": "Super Retina in two sizes,including the largest display ever on an iPhone. Even faster Face ID. The smartest, most powerful chip in a smartPhone."},

        {"name": "iPhone XR",
         "image": "/products/iPhoneXR1.jpg",
         "price": 749,
         "description": "Brilliant. In every way.",
         "stock": 1000,
         "detail": "All-new Liquid Retina display — the most advanced LCD in the industry. A12 Bionic, the smartest, most powerful chip in a smartphone. Advanced Face ID. And a breakthrough camera system with Depth Control."},

        {"name": "iPhone 7",
         "image": "/products/iPhone7 1.jpg",
         "price": 449,
         "description": "This is 7",
         "stock": 500,
         "detail": "Hd retina display and 5.5-inch (diagonal) LCD widescreen multi-touch display with IPS technology. 1920 x 1080 pixel resolution. "},

        {"name": "iPhone 8",
         "image": "/products/iPhone8 1.jpg",
         "price": 599,
         "description": "The biggest thing to happen to iPhone since iPhone 7",
         "stock": 800,
         "detail": "True Tone display and wide color display(P3),3D touch and 625 cd/m2 max brightness(typical)"},

    ]

    watch_products = [
        {"name": "iWatch series 3",
         "image": "/products/watch3 1.jpg",
         "price": 279,
         "description": "Stay active.Stay healthy.Stay connected.",
         "stock": 200,
         "detail": "Monitor your health. Track your workouts. Get the motivation you need to achieve your fitness goals."},

        {"name": "iWatch series 4",
         "image": "/products/watch4 1.jpg",
         "price": 399,
         "description": "All new. For a better you.",
         "stock": 2000,
         "detail": "Fundamentally redesigned and re-engineered to help you stay even more active, healthy and connected."},

        {"name": "iWatch series 4_hermes",
         "image": "/products/hermes1.jpg",
         "price": 1299,
         "description": "A shared vision, seen in a whole new light.",
         "stock": 1200,
         "detail": "A partnership based on parallel thinking, singular vision and mutual regard continues with a fresh new expression. The latest Apple Watch Hermès collection showcases boldly colourful leather straps and a delightful new watch face designed by Apple. "},

        {"name": "iWatch series 4_nike",
         "image": "/products/nike1.jpg",
         "price": 399,
         "description": "Reflective Nike Sport Loop.Be seen in all the right places.",
         "stock": 6000,
         "detail": "To help you stand out, Apple Watch Nike+ Series 4 is now available with a Nike Sport Loop strap that’s woven with special reflective thread designed to shimmer when light strikes it."}]

    pad_products = [
        {
            "name": "iPad Pro 2018",
            "image": "/products/iPad Pro1.jpg",
            "price": 888,
            "description": "New,full screen,all-round powerful",
            "stock": 12,
            "detail": "interactive gesture,intuitive and easy to operate,face ID,scan face to pay",
        },

        {
            "name": "iPad Air",
            "image": "/products/iPad Air1.jpg",
            "price": 479,
            "description": "Power isn't just for the pros",
            "stock": 320,
            "detail": "If the computer were invented today, what would it look like? It would be powerful enough for any task. So mobile you could take it everywhere. And so intuitive you could use it any way you wanted — with touch, a keyboard or even a pencil.1 In other words, it wouldn’t really be a “computer”. It would be iPad.",
        },

        {
            "name": "iPad Mini",
            "image": "/products/iPad mini1.jpg",
            "price": 279,
            "description": "Small stature, more talented.",
            "stock": 580,
            "detail": "The iPad mini is popular because it is small and powerful. Now you have more reasons to love it. The A12, for example, has a neural network engine and a 7.9-inch retina display that USES raw color. Plus, it supports the Apple Pencil, which will help you catch the best ideas as they fly by. It's still the beloved iPad mini, but with more power.",
        },

        {
            "name": "iPad",
            "image": "/products/iPad1.jpg",
            "price": 319,
            "description": "Like a computer. Unlike any computer",
            "stock": 950,
            "detail": "If the computer were invented today, what would it look like? It would be powerful enough for any task. So mobile you could take it everywhere. And so intuitive you could use it any way you wanted — with touch, a keyboard or even a pencil.1 In other words, it wouldn’t really be a “computer”. It would be iPad.",
        },


    ]
    mac_products = [
        {
            "name": "MacBook Air",
            "image": "/products/MacBook Air1.jpg",
            "price": 980,
            "description": "Versatile,many in one",
            "stock": 20,
            "detail": "13.3 inches, 2,560 x 1,600 resolution brings in over 4 million pixels"
        },

        {
            "name": "MacBook",
            "image": "/products/MacBook1.jpg",
            "price": 1249,
            "description": "Thinner takes all.",
            "stock": 200,
            "detail": "The new MacBook delivers up to 20 per cent faster performance with new seventh‑generation Intel Core m3, i5 and i7 processors,1 and up to 50 per cent faster SSD storage"
        },

        {
            "name": "MacBook Pro",
            "image": "/products/MacBook Pro1.jpg",
            "price": 1449,
            "description": "More power.More performance.More Pro",
            "stock": 2130,
            "detail": "New eighth-generation Intel 6-core and quad-core processors.Up to 32GB of memory for running multiple pro apps.Stunning Retina display with True Tone technology.Touch Bar for working more productively."
        },

        {
            "name": "iMac",
            "image": "/products/iMac1.jpg",
            "price": 1449,
            "description": "Pretty.Epic.",
            "stock": 150,
            "detail": "iMac is packed with the latest processors, faster memory and phenomenal graphics. All coming to life on the brightest, most vibrant Retina display ever on a Mac. It’s the total package — powered up."
        },

        {
            "name": "iMac Pro",
            "image": "/products/iMac Pro1.jpg",
            "price": 4899,
            "description": "Power to the Pro.",
            "stock": 2100,
            "detail": "It’s packed with the most powerful graphics and processors ever in a Mac, along with the most advanced storage, memory and I/O — all behind a breathtaking Retina 5K display in a sleek, all-in-one design. "
        },
    ]

    accessories_products = [
        {
            "name": "Cases & Covers",
            "image": "/products/XS case pink.jpg",
            "price": 30,
            "description": "iphone XS case",
            "stock": 5100,
            "detail": "pink"
        },

        {
            "name": "mac bags",
            "image": "/products/MacBook bag1.jpg",
            "price": 79.95,
            "description": "laptop bag",
            "stock": 1001,
            "detail": "Offering functional storage for your devices."
        },

        {
            "name": "keyboard folio",
            "image": "/products/keyboard 1.jpg",
            "price": 179,
            "description": "smart keyboard folio for iPad pro",
            "stock": 550,
            "detail": "The smart keyboard folio for the 11-inch iPad Pro is a full-size keyboard."
        },

        {
            "name": "iPhone XS film",
            "image": "/products/XS film1.jpg",
            "price": 14.95,
            "description": "iphone XS film",
            "stock": 1000,
            "detail": "The Belkin protector not only prevents visual damage to keep your iPhone looking like new, it also preserves the touchscreen’s functionality."
        },

        {
            "name": "iphoneXS armband",
            "image": "/products/XS armband1.jpg",
            "price": 29.95,
            "description": "iphone X armband",
            "stock": 630,
            "detail": "Sport Running Exercise Gym armband for iphone X/XS"
        }
    ]

    other_products = [
        {
            "name": "AirPods",
            "image": "/products/AirPods1.jpg",
            "price": 120,
            "description": "New generation wireless earphone, dissolve numerous and complicated.",
            "stock": 915,
            "detail": "Single click, the AirPods are automatically turned on and always connected."
        },

        {
            "name": "HomePod",
            "image": "/products/homePod1.jpg",
            "price": 319,
            "description": "Major sound, minor scale.",
            "stock": 2566,
            "detail": "HomePod combines custom Apple-engineered audio technology and advanced software to deliver precision sound that fills the room. And at just under 18 centimetres tall, HomePod fits anywhere in your home."
        },

        {
            "name": "Beats Solo3",
            "image": "/products/solo3 2.jpg",
            "price": 249.95,
            "description": "Wireless HeadPhones - New Year Special Edition - Blade Grey. ",
            "stock": 1500,
            "detail": "Celebrate Chinese New Year with special edition Beats Solo3 Wireless headphones. The fierce design features a graphic illustration of a Boar and golden accents, made complete with a matching carrying case. Now you can go wild with award-winning Beats sound and up to 40 hours of battery life on the adventures that come your way."
        },

        {
            "name": "Beats Pill + Speaker",
            "image": "/products/speaker1.jpg",
            "price": 179.95,
            "description": "Undefeated Special Edition",
            "stock": 520,
            "detail": "As two brands that believe in pushing boundaries and taking a stand, Beats and UNDEFEATED have teamed up for a third time with this must-have collaboration. Featuring UNDEFEATED’s unmistakable tiger camouflage, this latest collection includes a Beats Pill+ speaker in camo and the first customized BeatsX color, each with its own unique case."
        },

        {
            "name": "BeatsX Earphones",
            "image": "/products/earphone1.jpg",
            "price": 129.95,
            "description": "Undefeated Special Edition",
            "stock": 630,
            "detail": "Whether playing in your ears or hanging around your neck, BeatsX is incredibly sleek and comfortable for all-day wear. The unique Flex-Form cable provides a flexible fit, a variety of ear-tip options provide personalized comfort and secure-fit wingtips offer added stability. And when you’re not wearing them, magnetic ear buds keep your earphones tangle-free and they easily coil up for compact portability."
        },
    ]
    cats = {
        "iPhone": {"products": iphone_products},
        "iPad": {"products": pad_products},
        "Mac": {"products": mac_products},
        "Watch": {"products": watch_products},
        "Accessories": {"products": accessories_products},
        "Other": {"products": other_products},
    }

    site = {
        "domain": "localhost:8000",
        "name": "iCasa",
    }

    socialapp = {
        "provider": "facebook",
        "name": "iCasa",
        "client_id": "2338256373071830",
        "secret": "e2777dd08b0da339f1f137e7a7891567",
        "site": site,
    }

    s = add_site()
    add_social_app(socialapp['provider'], socialapp['name'], socialapp['client_id'], socialapp['secret'], s)

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["products"]:
            add_product(c, p["name"], p["image"], p["price"], p["description"], p["stock"], p["detail"])
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_product(cat, name, image, price, description, stock, detail):
    p = Product.objects.get_or_create(category=cat, name=name, price=price, stock=stock)[0]
    p.image = image
    # p.price=price
    p.description = description
    # p.stock=stock
    p.detail = detail
    p.save()
    return p


def add_cat(ctitle):
    c = Category.objects.get_or_create(ctitle=ctitle)[0]
    c.save()
    return c


def add_social_app(provider, name, clientid, secret, site):
    sapp = SocialApp.objects.get_or_create(provider=provider, name=name, client_id=clientid, secret=secret)[0]
    sapp.sites.add(site)
    sapp.save()
    print(sapp.provider)
    return sapp


def testprovider():
    t = SocialApp.objects.get_or_create(client_id="2338256373071830")[0]
    print(t.provider)


def add_site():
    s = Site.objects.get_or_create(domain='example.com')[0]
    s.domain = 'localhost:8000'
    s.name = 'iCasa'
    s.save()
    return s


# if __name__ == '_main_':
print("Starting it population script...")
populate()
