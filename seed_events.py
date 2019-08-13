from event_models import Event, Category
import datetime;

def seed_data():
    event_1 = Event(event_name="Basketball Game",
              location="gym",
              organization_name="Women's Basketball Team",
              category="Athletics",
              college_name="Loyola Marymount University",
              date_and_time=datetime.date(2019, 9, 26),
              time=datetime.time(18,0,0,0))
    event_1.put()
    event_2 = Event(event_name="Dance Performance",
              location="Performing Arts Center",
              organization_name="Dance Team",
              category="Arts",
              college_name="Pepperdine University",
              date_and_time=datetime.date(2019, 8, 23),
              time=datetime.time(5,30,0,0))
    event_2.put()
    event_3 = Event(event_name="Club Meeting",
              location="Room 253",
              organization_name="Red Cross Club",
              category="Service",
              college_name="University of California Los Angeles",
              date_and_time=datetime.date(2019, 8, 30),
              time=datetime.time(12,15,0,0))
    event_3.put()
    event_4 = Event(event_name="Mixer",
              location="House",
              organization_name="Gamma Delta",
              category="Greek Life",
              college_name="University of Southern California",
              date_and_time=datetime.date(2019, 9, 26),
              time=datetime.time(20,0,0,0))
    event_4.put()
    event_5 = Event(event_name="Art Showing",
              location="Quad",
              organization_name="Art Club",
              category="Arts",
              college_name="Loyola Marymount University",
              date_and_time=datetime.date(2019, 9, 3),
              time=datetime.time(13,30,0,0))
    event_5.put()
    event_6 = Event(event_name="Volleyball Game",
              location="Gym",
              organization_name="Men's Volleyball Team",
              category="Athletics",
              college_name="University of California Los Angeles",
              date_and_time=datetime.date(2019, 9, 7),
              time=datetime.time(18,30,0,0))
    event_6.put()
    category_athletics = Category(category_name="Athletics")
    category_athletics.put()
    category_arts = Category(category_name="Arts")
    category_arts.put()
    category_academics = Category(category_name="Academics")
    category_academics.put()
    category_service = Category(category_name="Service")
    category_service.put()
    category_religion = Category(category_name="Religion")
    category_religion.put()
    category_culture = Category(category_name="Culture")
    category_culture.put()
    category_greeklife = Category(category_name="Greek Life")
    category_greeklife.put()
    category_volunteer = Category(category_name="Volunteer")
    category_volunteer.put()
    category_housing = Category(category_name="Housing")
    category_housing.put()
    category_other = Category(category_name="Other")
    category_other.put()
