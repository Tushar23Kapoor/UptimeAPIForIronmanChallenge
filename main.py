from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
import dateutil.parser
from datetime import datetime, timezone

app = Flask(__name__)
api = Api(app)

class TimeFetcher(Resource):

    def get(self):

        marathon_start_date = dateutil.parser.parse("2022-07-14T17:02:46Z") 
        current_date_time = datetime.now(timezone.utc)
        try:
            timediff = current_date_time - marathon_start_date
        except Exception:
            result = make_response('API unavailable, contact @Potterapple')
        
        days = str(timediff).split('days, ')
        hrs = days[1].split(":")
        mins = hrs[1].split(":")
        seconds = hrs[2].split(".")
        

        result = make_response('Time since start of challenge - ' + str(days[0]) + " days " + hrs[0] + " hrs " + mins[0] + " minutes and " + seconds[0] + " seconds!")       
        return result

api.add_resource(TimeFetcher, '/')

if __name__ == "__main__":
    app.run(debug=True)