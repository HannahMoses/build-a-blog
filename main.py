
#FEb20 ,2017 1:19 pm
import webapp2
header="<h2 style='color:white;background-color:rgb(145,0,0);text-align:center'>WELCOME </h2>"
form="""<form method="post"  style='color:rgb(145,0,0);background-color:pink'>
    <div style='color:green'><h2>%(error)s</h2></div>
    <body style='color:rgb(145,0,0);background-color:pink' ><p>Please enter your birthday</p>
        <label>Month <input type="text" name="month" value=%(month)s ></label> <br><br>
    	<label>Day <input type="text" name="day" value=%(day)s></label><br><br>
        <label>Year <input type="text" name="year" value=%(year)s></label><br><br>
        <br><br>
        <input type="submit" value="Submit Bday"style='color:white;background-color:rgb(145,0,0)'>
    </body>
</form>"""
outform="""<form method='post'>
                 <body style='color:white;background-color:rgb(200,134,125)' >
                  <p> ****************************************** </p>
                 </body>
           </form>"""
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
    def write_form(self,error="",month="",day="",year=""):
        self.response.out.write(form % {"error": error,"month":month,"day":day,"year":year})
    def get(self):
        self.response.out.write(header)
        self.write_form()
    def post(self):
        user_month=(self.request.get("month"))
        user_day = (self.request.get("day"))
        user_year =(self.request.get("year"))

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            outmessage="That is not a valid birthday !"
            self.write_form(outmessage,user_month,user_day,user_year)
        else:
            outhead =" <h2 style='background-color:rgb(200,134,125)'> Thanks for entering good data !</h2>"
            self.response.write(outhead + outform)
app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)
