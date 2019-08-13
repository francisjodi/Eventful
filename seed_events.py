from event_models import Event, Category
import datetime;

def seed_data():
    event_1 = Event(event_name="Basketball game",
              location="gym",
              organization_name="Basketball Team",
              category="Athletics",
              college_name="Loyola Marymount University",
              date_and_time=datetime.date(2019, 9, 26),
              time=datetime.time(3,30,0,0))
    event_1.put()
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
