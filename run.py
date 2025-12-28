from app import create_app, db # app folder mese create_app function and database(db) ko call kiya
from app.models import Task #app folder mese models file ki Task class ko import kiya

app=create_app() #app variable mee create_app function ko save kiya

with app.app_context(): #jo bhi app folder mee hee vo run karo
    db.create_all() # DB ko table mee banavo

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)