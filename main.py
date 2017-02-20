
#FEb20 ,2017 10:47 am
import webapp2
header="<h2 style='color:white;background-color:rgb(145,0,0);text-align:center'>WELCOME </h2>"
form="""
<form method="post"  style='color:rgb(145,0,0);background-color:pink'>
    <body style='color:rgb(145,0,0);background-color:pink' ><p>Please enter your Bday</p>
    	<label>Month <input type="text" name="month" ></label> <br><br>
    	<label>Day <input type="text" name="day"></label><br><br>
        <label>Year <input type="text" name="year"></label><br><br>
      	<br><br>
        <input type="submit" value="Submit Bday"style='color:white;background-color:rgb(145,0,0)'>
    </body>
</form>
"""
months = ['January','February','March','April','May','June','July',
        'August','September','October','November','December']
month_abbvs=dict((m[:3].lower(),m)for m in months)
def valid_month(month):
    if month :
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if (0<day<=31):
            return day
def valid_year(year):
    if year and year.isdigit():
        year=int(year)
        if (1900<year<2020):
            return year
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(header + form)

    def post(self):
        user_month=valid_month(self.request.get("month"))
        user_day = valid_day(self.request.get("day"))
        user_year = valid_year(self.request.get("year"))
        if not(user_month and user_day and user_year):
            self.response.write("Error")
        else:
            gooddata = "Thanks for entering valid data !"
            outmessage = gooddata
            outhead = "<h2 style='background-color:rgb(200,134,125)'>"+outmessage+" </h2>"
            outbody ="<body style='color:white;background-color:rgb(200,134,125)' ><p> *************** </p></body>"
            self.response.out.write(outhead+outbody)

app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)
