import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

samsung = "Now with the Galaxy S23 Ultra you will get an epic display, epic performance and epic battery all in the one epic smartphone. An epic camera with the highest resolution sensor in a Galaxy and stunning Nightography so you can take an epic shot in virtually any light and leave everyone asking for more. An epic gaming performance powered by the fastest chipset in a Galaxy so you can share your epic victories. An epic display that allows you to enjoy it all, no matter how bright it gets. And finally, one Mighty S Pen with unlimited ways to create. The Galaxy S23 Ultra easily lives up to its name."
apple = "Forged In Titanium iPhone 15 Pro Max has a strong and light aerospace-grade titanium design with a textured matt glass back. It also features a Ceramic Shield front that’s tougher than any smartphone glass. And it’s splash-, water- and dust-resistant. Advanced Display - The 6.7″ Super Retina XDR display2 with ProMotion ramps up refresh rates to 120Hz when you need exceptional graphics performance. Dynamic Island bubbles up alerts and Live Activities. Plus, with Always-On display, your Lock Screen stays glanceable, so you don’t have to tap it to stay in the know."
motorola = "Introducing motorola edge 30 ultra. Capture your sharpest, most beautifully detailed photos in any light with a 200MP camera system, the industry’s highest resolution. Experience the fastest, most powerful Snapdragon® processor1. Fuel up in minutes2 at unbelievable 125W speeds, the fastest TurboPower™ charging ever. Enjoy the stunning endless edge design and breathtaking views on a totally immersive 6.67 inch 144Hz display3. Find your edge with motorola edge 30 ultra."
asus ="Small is the new big! The fun-loving Zenfone 10 packs mighty performance and plenty of pizzazz into the perfect hand-sized package. It’s everything you need for mobile freedom: a speedy Snapdragon® 8 Gen 2 processor, a camera with the coolest new features, and on-trend colours to show your style. Zenfone 10 — it’s mighty on hand! Swiping the side-mounted ZenTouch key gives you instant shortcuts to your favourite actions, such as unlocking your phone, video playback controls, web browsing and reading notifications."
google = "Meet Pixel 7a, engineered by Google. The Google Tensor G2 chip makes it fast. The Pixel Camera takes amazing photos and video. VPN by Google One helps protect your data.1 Pixel has been recognised as the highest rated smartphone for security by a third-party global research firm.2 And the battery can last all day.3 All at a great price.Engineered by Google, the Tensor G2 chip helps make Pixel 7a faster, more efficient and more secure than the Pixel 6a.4 It's the same chip that's in Pixel 7 and Pixel 7 Pro, powering Google smarts for improved audio on phone calls, great battery life and amazing photo and video quality."
oppo = "Ultra-Clear Portrait Camera System Shoot unbelievable footage backed by flagship imaging hardware and capture ultra-clear master-quality pictures that will have all your friends wanting to get in front of your camera lens.67W SUPERVOOC Flash Charge Go from flat to 31% in just 10 minutes with the 67W SUPERVOOC flash charge6, backed by a large 5000mAh7 battery and a battery health engine that increases battery durability to 4 years"

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Samsung S23 Ultra 5G 1TB (Green)', samsung , 'S23', 2649)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Apple iPhone 15 Pro Max 512GB (Natural Titanium)', apple , 'Iphone15', 2549)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Motorola Edge 30 Ultra 5G 256GB (Interstellar Black)', motorola , 'Motorola', 1399)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Asus Zenfone 10 5G 512GB (Midnight Black)', asus , 'Asus', 1499)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Google Pixel 7a 5G 128GB (Charcoal)', google , 'GooglePixel', 749)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('OPPO Reno10 5G 256GB (Ice Blue)', oppo , 'Oppo', 749)
            )

connection.commit()
connection.close()