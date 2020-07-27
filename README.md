## To Run
- python3 manage.py runserver
- Use http://localhost:8000 or http://127.0.0.1:8000

## To Run Tests
- python3 manage.py test programs.tests.ActvityTests
- python3 manage.py test programs.tests.ContentItemTests
- python3 manage.py test programs.tests.ContentTests
- python3 manage.py test programs.tests.ProgramTests
- python3 manage.py test programs.tests.SectionTests


The project follows RESTful design was built with Test Driven Development in mind. It uses SQLite for its Database instead of a full fledged MySQL but for the purpose of this project it will work just the same.

There were definitely some questions regarding how to design out the models but I took this as an opportunity to meet requirements without being explicity told how to. 

The assignment mentioned an Activity has either a Q/A or HTML content. Instead of saving a lot of HTML as text into the DB, I implemented the Content and ContentItem class. In the case when Activity is an HTML conent, the Content table represents a header and ContentItem represents a list item. When the front end queries the DB for a specific Activity's Content and receives back a Content and a list of ContentItems, it will ideally construct the page by creating a header tag like "h1" for Content and "li" for ContentItem. 

When Content is Q/A, the front end should treat the data similarly in the way it constructs a question heading based on the Content and the question/answers based on ContentItems.

