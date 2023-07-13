# Joboskop
## **Description**
Joboskop is a student job portal, a website designed to cater to the needs of students seeking employment opportunities. Created using Django, JavaScript, Python, HTML, and CSS, this platform offers a seamless experience to users.

Upon landing on the website, visitors are greeted by a comprehensive main page that serves as the central hub for job-related information. Here, they can access a diverse range of job listings, peruse the latest blogs, and establish contact with the administrator. Conveniently located in the footer section are essential links and information.

A standout feature of the website is its user-friendly search and filtering capabilities, accessible directly from the homepage. By leveraging intuitive search functionality, students can narrow down their preferences and discover job listings that align with their interests and qualifications. After entering their search criteria, a tailored list of jobs matching their preferences is presented.

In addition to the main page, the website offers distinct sections dedicated to blogs, contact information, and an "About Us" page. The blog section is a valuable resource for students, providing insightful articles on various career development topics such as interview techniques, resume writing, and industry trends. This ensures students remain informed and up-to-date.

The contact page serves as a convenient means for users to connect with the administrator. The "About Us" page offers an in-depth look into the platform's purpose, mission, and the team driving its success, providing users with a better understanding of its values.
To maintain an organized approach, all job and blog postings are centrally managed through the /admin page. By leveraging Django models, the administrator retains full control over content uploads, ensuring an accurate representation of job listings and blog articles while keeping the platform updated with the latest opportunities.

The student job portal is committed to delivering a user-friendly and informative experience to students embarking on their job search journey. With powerful search functionality, valuable blog resources, and seamless contact options, this platform empowers students to find their ideal job and kickstart their professional careers with confidence.


## **Distinctiveness and Complexity**

The web page created using Django, JavaScript, Python, HTML, and CSS offers a student-oriented job portal, providing a unique and tailored experience for users. Its distinctive features include: 
1. Seamless Job Search: The platform allows students to filter and search for jobs directly from the homepage. This feature enhances user experience by enabling targeted job exploration based on preferences, making it stand out from generic job websites. 
2. Latest Blogs: In addition to job listings, the website offers a dedicated section for blogs. Students can access valuable career advice and industry insights, keeping them informed and engaged throughout their job search journey. 
3. Contact Administrator: The website provides a convenient contact page where students can reach out to the administrator for inquiries, feedback, or assistance. This direct communication channel distinguishes the platform by fostering personalized interaction with users. 
4. Admin Control: The implementation of Django models allows the administrator to have complete control over job and blog postings through the /admin page. This feature provides a secure and centralized system for managing and updating content, ensuring accuracy and relevance.


Complexity: The code provided showcases the complexity of the web application and its underlying functionality. Some notable aspects include: 
1. Database Interaction: The code utilizes Django's models and performs various database queries to fetch job listings, blogs, and their associated information. It employs filtering, ordering, and pagination techniques to present data in a structured and organized manner.
2. Dynamic Content Rendering: The code dynamically renders job listings, blogs, and their details based on user actions and input. It handles pagination to display limited results per page and adjusts content based on search queries, category selections, and blog searches.
3. User Input Handling: The code incorporates form submissions to handle user input for search queries, category selections, and blog searches. It applies validation and filtering techniques to ensure data integrity and improve user experience.
4. Template Rendering: The code employs Django's templating engine to render HTML templates dynamically. It passes data from the views to the templates, allowing for the seamless integration of backend logic and frontend presentation.


Overall, the code demonstrates the complexity involved in creating a student job portal using Django, JavaScript, Python, HTML, and CSS. It incorporates database interactions, dynamic content rendering, user input handling, and template rendering to provide an interactive and feature-rich web application.

## **Files**

1. The **views.py** file plays a crucial role in handling all requests and rendering the necessary views for the web page. It contains various functions that correspond to different URLs and endpoints of the website. Here's a brief description of the views implemented in the provided code:
- index(request): This view handles the request for the main page of the website. It retrieves job listings, latest blogs, and featured jobs from the database and renders the "index.html" template. It also incorporates pagination to display a limited number of jobs per page.
- about(request): This view handles the request for the "About Us" page. It renders the "about.html" template, which provides information about the platform.
- blogs(request): This view handles the request for the blogs page. It retrieves the blog posts from the database, incorporates pagination, and renders the "blog-posts.html" template to display the blogs.
- job(request, job_id): This view handles the request for a specific job's details. It retrieves the job with the given job_id from the database and renders the "single_job.html" template, displaying the job details.
- job_category(request, job_category): This view handles the request for jobs belonging to a specific category. It filters the jobs based on the given job_category and retrieves related blogs. It renders the "category.html" template, displaying the jobs and associated blogs.
- location(request, job_location): This view handles the request for jobs based on a specific location. It filters the jobs based on the given job_location and renders the "category.html" template, displaying the filtered jobs.
- search(request): This view handles the search functionality for jobs. It retrieves the search query from the request, filters the jobs based on the query, retrieves related blogs, and renders the "category.html" template, displaying the search results.
- blog(request, blog_id): This view handles the request for a specific blog post. It retrieves the blog with the given blog_id from the database, retrieves related blogs, and renders the "blog_single.html" template, displaying the blog post and associated blogs.
- blog_search(request): This view handles the search functionality for blogs. It retrieves the search query from the request, filters the blogs based on the query, incorporates pagination, and renders the "blog-posts.html" template, displaying the search results.
- type_search(request, type_job): This view handles the request for jobs based on a specific job type. It filters the jobs based on the given type_job, retrieves related blogs, and renders the "category.html" template, displaying the filtered jobs.

2. The **urls.py** file is responsible for mapping URLs to the corresponding views in the web application. It defines the URL patterns and associates them with the appropriate views. Here's a description of the URL patterns defined in the provided code:
- "" (empty string): This pattern corresponds to the root URL of the website. It maps to the index view, which renders the main page.
- "about-us": This pattern maps to the about view, which renders the "about.html" template and displays the "About Us" page.
- "blog-posts": This pattern maps to the blogs view, which renders the "blog-posts.html" template and displays the blog posts page.
- "job/int:job_id": This pattern maps to the job view, which takes an integer parameter (job_id) corresponding to the ID of a specific job. It renders the "single_job.html" template and displays the details of the selected job.
- "category/str:job_category": This pattern maps to the job_category view, which takes a string parameter (job_category) representing a specific job category. It renders the "category.html" template and displays the jobs belonging to the specified category.
- "location/str:job_location": This pattern maps to the location view, which takes a string parameter (job_location) representing a specific job location. It renders the "category.html" template and displays the jobs located at the specified location.
- "search": This pattern maps to the search view, which handles the search functionality for jobs. It renders the "category.html" template and displays the search results based on the provided search query.
- "blog/int:blog_id": This pattern maps to the blog view, which takes an integer parameter (blog_id) representing the ID of a specific blog post. It renders the "blog_single.html" template and displays the details of the selected blog post.
- "blog-search": This pattern maps to the blog_search view, which handles the search functionality for blogs. It renders the "blog-posts.html" template and displays the search results based on the provided search query.
- "type/str:type_job": This pattern maps to the type_search view, which takes a string parameter (type_job) representing a specific job type. It renders the "category.html" template and displays the jobs associated with the specified job type.

3. The **models.py** file defines the structure and fields for the database tables used in the web application. Here's a concise description of the models and their fields:
 - User (inherits from AbstractUser): This model represents the user entity and inherits from Django's AbstractUser model, providing standard user authentication fields.
 - Job: This model represents a job listing and includes the following fields:
1. title: CharField for the job title (max length: 200)
2. description: RichTextField for the job description (default: "description")
3. requirements: RichTextField for the job requirements (default: "requirements")
4. contact: CharField for contact information (max length: 2000)
5. description_of_the_potential_candidate: RichTextField for describing potential candidates (default: "potential")
6. image: CharField for the image URL (max length: 3000)
7. timestamp: DateTimeField for the job posting timestamp (auto-generated)
8. category: CharField for job category (max length: 100)
9. type: CharField for job type (max length: 100)
10. location: CharField for job location (max length: 100, default: "Bosna i Hercegovina")
11. short: RichTextField for a short description (default: "short")

- Blog: This model represents a blog post and includes the following fields:
1. author: CharField for the blog author (max length: 200, default: "author")
2. author_education: CharField for author's education (max length: 1000, default: "zanimanje")
3. tag: CharField for blog tags (max length: 100)
4. title: CharField for the blog title (max length: 200)
5. intro: RichTextField for a short introduction (default: "short intro")
6. description: RichTextField for the blog content (default: "blog content")
7. timestamp: DateTimeField for the blog posting timestamp (auto-generated)
8. image: CharField for the image URL (max length: 5000, default: “pic")

4. The **admin.py** file is responsible for registering the models in the Django admin interface, enabling administrators to manage and interact with the data stored in the database. The provided code registers the User, Job, and Blog models. By utilizing the admin.site.register() method, the models are associated with their respective admin views.

5. The **templates and static** folders was a crucial role in organizing and serving HTML templates, JavaScript and CSS files, as well as images, and fonts. Here's a short description of each folder:
- Templates Folder:
1. The templates folder is where I stored HTML templates that define the structure and presentation of web pages.
- Static Folder:
1. The static folder I used to store static files such as JavaScript, CSS, fonts,  and images. These files are served directly to the client without any processing by the server.

## **How To Run Application**
To run the Joboskop web application locally, follow these steps:

1. Clone the repository to your local machine.
2. Ensure that Python and Django are installed on your system.
3. Create a virtual environment for the project.
4. Activate the virtual environment.
5. Install the project dependencies by running pip install -r requirements.txt.
6. Apply the database migrations using python3 manage.py makemigrations/python3 manage.py migrate.
7. Create a superuser account to access the admin interface.
8. Start the development server with python3 manage.py runserver.
9. Access the application in your web browser at http://localhost:8000.

## Contact

Any information, bugs, or questions can be sent to the e-mail address: adzamija@icloud.com

