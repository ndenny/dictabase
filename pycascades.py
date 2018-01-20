
import logging
import os
import sys
import dictabase as db

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s:%(levelname)s: %(message)s',
    level=os.environ.get('DEBUG_LEVEL') or logging.INFO)

log = logging.getLogger(__name__)  # pylint: disable=C0103

class ExampleModel(db.Model):
    name = db.Property(default="")
    count = db.Property(default=0)
    overall_star_rating = db.Property(default=0)
    rating_count = db.Property(default=0)
    street = db.Property(default="")
    price_range = db.Property(default="")
    fb_id = db.Property(default="")
    description = db.Property(default="")


DATASET = [
        ExampleModel(
            name="Edible Canada at the Market", 
            count=4118, 
            overall_star_rating=2.5, 
            rating_count=4120, 
            street="1596 Johnston Street", 
            price_range="$$", 
            fb_id="267390809951312", 
            description="Edible Canada is a leader in Canadian culinary tourism, with a flagship bistro and retail shop on Granville Island in Vancouver, British Columbia. \n\nWhat is Canadian Cuisine?\n\nDishes that blend our nation\u2019s varied and rich cultural food traditions with the abundant local resources across the country. \n\nDisclaimer: posts which are rude, violent, harassment or hate speech will be removed by this page's moderator. "
        ), 
        ExampleModel(
            name="The Sandbar Seafood Restaurant", 
            count=3214, 
            overall_star_rating=4.4000000000000004, 
            rating_count=547, 
            street="1535 Johnston Street", 
            price_range="$$", 
            fb_id="193094420739517"
        ), 
        ExampleModel(
            description="Great steaks, friendly service and a really comfortable atmosphere are what you find at The Keg Steakhouse + Bar.", 
            count=764, 
            overall_star_rating=4.2000000000000002, 
            rating_count=273, 
            street="1499 Anderson Street - Granville Island", 
            fb_id="224662607545039", 
            price_range="$$", 
            name="The Keg Steakhouse + Bar - Granville Island"
        ), 
        ExampleModel(
            name="Granville Island Brewing", 
            count=30485, 
            overall_star_rating=0, 
            rating_count=0, 
            street="1441 Cartwright Street", 
            price_range="$$", 
            fb_id="68622774001"
        ), 
        ExampleModel(
            name="Burrard Bridge", 
            count=219, 
            overall_star_rating=4.2999999999999998, 
            rating_count=117, 
            street="Burrard St", 
            price_range="$", 
            fb_id="113792051964508", 
            description="The Burrard Bridge is a five-lane, Art Deco style, steel truss bridge constructed in 1930\u20131932 in Vancouver, British Columbia, Canada. The high, five part bridge on four piers spans False Creek, connecting downtown Vancouver with Kitsilano via connections to Burrard Street on both ends. It is one of three bridges crossing False Creek. The other two bridges are the Granville Bridge, three blocks or 0.5km to the southeast, and the Cambie Street Bridge, about 11 blocks or 2km to the east. In addition to the vehicle deck, the Burrard Bridge has sidewalks on both sides, 2.6m wide, the northern one for pedestrians and the southern one now dedicated to cyclists.The architect of the Burrard Bridge was George Lister Thornton Sharp, the engineer John R. Grant. The bridge's two close approach spans are Warren trusses placed below deck level, while its central span is a Pratt truss placed above deck level to allow greater clearance height for ships passing underneath. The central truss is hidden when crossing the bridge in either direction by vertical extensions of the bridge's masonry piers into imposing concrete towers, connected by overhead galleries, which are embellished with architectural and sculptural details that create a torch-like entrance of pylons. Busts of Captain George Vancouver and Sir Harry Burrard-Neale in ship prows jut from the bridge\u2019s superstructure ."
        ), 
        ExampleModel(
            name="Bridges Restaurant", 
            count=2015, 
            overall_star_rating=3.8999999999999999, 
            rating_count=343, 
            street="1696 Duranleau         Granville Island", 
            price_range="$$", 
            fb_id="57065894613"
        ), 
        ExampleModel(
            name="Dockside Restaurant", 
            count=1708, 
            overall_star_rating=4.2000000000000002, 
            rating_count=160, 
            street="1253 Johnston Street", 
            price_range="$$", 
            fb_id="149445668410995", 
            description="The Dockside Restaurant offers superbly prepared classic dishes in a setting like no other. Located on the waterfront where Granville Island faces the city, guests can enjoy panoramic views across False Creek to the world-famous cityscape of Yaletown and beyond to the mountains of the North Shore."
        ), 
        ExampleModel(
            name="The Vancouver Fish Company", 
            count=2049, 
            overall_star_rating=4.2999999999999998, 
            rating_count=108, 
            street="1517 Anderson St", 
            price_range="$$$", 
            fb_id="1456256907954173"
        ), 
        ExampleModel(
            name="Vancouver TheatreSports", 
            count=8730, 
            overall_star_rating=4.7999999999999998, 
            rating_count=276, 
            street="1502 Duranleau St.", 
            price_range="$", 
            fb_id="144748368902495", 
            description="Since its founding in 1980, Vancouver TheatreSports\u2122 League (VTSL) grown to become a well-respected international leader in the improv art form, entertaining more than 60,000 people per year through 11 shows a week, 52 weeks a year at its own theatre, The Improv Centre, located on Granville Island. An intimate space, The Improv Centre is a fully-licensed facility with its own Bar & Lounge over-looking the picturesque False Creek Marina. Unlike most theatres, VTSL patrons are welcome to take their beverages into the theatre to enjoy during the show. In addition, VTSL owns and operates The Improv Comedy Institute \u2013 an improv school offering classes from beginner through professional level, conducts province-wide school tours and operates Improv for Business, a corporate training division with a diverse portfolio of blue-chip clients. In 2016, VTSL was voted the \u2018#1 Improv Comedy Company\u2019 at the  prestigious \u2018Best of Vancouver Awards.\u2019\n\nVancouver TheatreSports\u2122 League brand of improvisation is a highly theatrical fusion of the dramatic elements of comedy and tragedy coupled with the enthusiasm and edge-of-your-seat excitement of professional sport."
        ), 
        ExampleModel(
            name="Urban Fitness Vancouver", 
            count=17042, 
            overall_star_rating=5, 
            rating_count=3, 
            street="1348 Granville Street", 
            price_range="$$", 
            fb_id="188939921642896", 
            description="Award-winning group fitness and professional personal training studio specializing in functional bodyweight high intensity interval training. Featuring TRX, Kickboxing Bootcamps and Yoga."
        ), 
        ExampleModel(
            name="Morar no Canada", 
            count=13311, 
            overall_star_rating=4.9000000000000004, 
            rating_count=36, 
            fb_id="331547983644880"
        )
    ]



def main():

    with db.DictaBase(
            DATASET, 
            indexes=('rating_count', 'overall_star_rating', 'price_range')) \
                as view:

        query = view.query()
    
        query = query.filter(
            ExampleModel.overall_star_rating > 2)
    
        query = query.filter(
            ExampleModel.price_range > '$')

        results = query.fetch()
        
        for result in results:
            log.info('%s: %s', result.name, result.street)

if __name__ == '__main__':
    main()

