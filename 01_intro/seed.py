from app import app
from models import Coffee, db

with app.app_context():
    Coffee.query.delete()

    # create some coffee

    cappuccino = Coffee(
        name="cappuccino",
        image="https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcTXheDqmR-97MAlV0Q9g6hzLjp_vVKvf4ofu_rGsw0cpI-BUWRc7h-6PbL2Yt_Wofr1",
        price=4.50,
        description="milk and foam on top of a shot expresso",
    )

    expresso = Coffee(
        name="expresso",
        image="https://xanders.pk/wp-content/uploads/2021/06/7C0BADB7-D030-4E4E-BE715FB20458C51E_source.jpg",
        price=3.50,
        description="strong, concentrated coffee",
    )

    db.session.add_all([cappuccino, expresso])
    db.session.commit()

    print("done seeding!!! 😵‍💫")

# SyntaxError: invalid syntax
# (01_intro) igorrakush@irakush 01_intro % flask run
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
# ^C^C
# (01_intro) igorrakush@irakush 01_intro %
# (01_intro) igorrakush@irakush 01_intro % python seed.py
# done seeding!!! 😵‍💫
# (01_intro) igorrakush@irakush 01_intro % flask shell
# Python 3.8.13 (default, Oct 26 2023, 18:31:28)
# [Clang 15.0.0 (clang-1500.0.40.1)] on darwin
# App: app
# Instance: /Users/igorrakush/FlatironSchool/code/phase-4/lecture/SENG-LIVE111323-Phase-4-Flask/01_intro/instance
# >>> Coffee.query
# <flask_sqlalchemy.query.Query object at 0x109204eb0>
# >>> Coffee.query.first()
# <Coffee 1>
# >>> Coffee.query.first().name
# 'cappuccino'
# >>> Coffee.query.first().price
# 4.5
# >>> Coffee.query.first().description
# 'milk and foam on top of a shot expresso'
# >>>
