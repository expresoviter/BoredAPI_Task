from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import configuration

Base = declarative_base()


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    accessibility = Column(DECIMAL)
    type = Column(String)
    participants = Column(Integer)
    price = Column(DECIMAL)
    link = Column(String)
    key = Column(String)

    def __init__(self, data):
        print(data)
        self.name = data["activity"]
        self.accessibility = data["accessibility"]
        self.type = data["type"]
        self.participants = data["participants"]
        self.price = data["price"]
        self.link = data["link"]
        self.key = data["key"]


class ActivitySaver:
    def __init__(self):
        self.engine = create_engine(configuration.databaseData,
                                    connect_args={'options': '-csearch_path={}'.format(configuration.schemaName)}, echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def saveActivity(self, arg):
        activity = Activity(arg)
        self.session.add(activity)
        self.session.commit()

    @staticmethod
    def getActivity(obj):
        return {"activity": obj.name,
                "accessibility": obj.accessibility,
                "type": obj.type,
                "participants": obj.participants,
                "price": obj.price,
                "link": obj.link,
                "key": obj.key
                }

    def getLatestActivities(self):
        query = self.session.query(Activity).order_by(Activity.id.desc()).limit(5).all()
        for i in query:
            print(self.getActivity(i))
