# AsknBid Tech | Backend Engineer Internship

[Dstreet Games](https://dstreet.games), a product by [AsknBid](https://asknbid.tech), is India's biggest stock market gaming platform. Dstreet gamifies stock market education through Portfolios & Dshots, 2 major game formats. We believe Dstreet Games is the fastest way to learn stock trading.

Dstreet Games was initially built by 2 LPU alumni [Khushboo Soni](https://www.linkedin.com/in/khushboo-soni) & [Ujjwal Brahmin](https://www.linkedin.com/in/ujjwal-brahmin-2a8321175). They started working on it when they joined us as interns. [Shiv Prakash](https://www.linkedin.com/in/shivp0616), also an LPU alumni, was the mastermind behind the AWS Cloud Infrastrucure for Dstreet Games.

At Dstreet Games, you get to work with the best in class and the most competitive founding team : [Kamaldeep](https://linkedin.com/in/kamaldeep-j), [Khushboo](https://www.linkedin.com/in/khushboo-soni) and [Ujjwal](https://www.linkedin.com/in/ujjwal-brahmin-2a8321175). We are looking for developers who are the builders of the 1st order. The ones who get a rush from creating things from scratch and take pleasure in watching users try to tear it apart through sheer volume and strange, unthinkable use cases. And when it breaks, they cannot sleep without finding that pesky little condition in some forgotten corner.

Founded by [Suresh Bavisetti](https://www.linkedin.com/in/suresh-bavisetti) (CSE '17 Dropout, IIT Madras) & [Paarth Dhar](https://www.linkedin.com/in/paarthdhar) (EE '14, IIT Roorkee) and backed by [ICICI Securities](https://www.icicisecurities.com) & a few other most respected investors, we are on a mission to drive 150 Million+ Indian retail investor participation over in stock markets over the next decade.

## What is the task about?
- This task is designed to help us assess your ability to work on some of the technologies that we use to build products at AsknBid and your ability to craft clean and performant code in the real world.
- For this task we have created a simple API using [Django Rest Framework](https://www.django-rest-framework.org/tutorial/quickstart/). You will need to create a service which periodically hits the API to update the price of all the stocks.

## Getting Started
- Fork the lpu2021-backend repository.
- Once you've successfully forked the repository, clone it to your computer.
- Run ```cd lpu2021-backend/``` command in the terminal.
- You will need docker to run this project. Install docker by following the instructions in this [link](https://docs.docker.com/get-docker/). Skip this step if you have already installed docker on your computer.
- Run ```docker-compose up --build``` command in the terminal to run this project.


## What you'll be doing
- **Task 1** : You have to create a new attribute for ```price``` in ```server/stocks/models.py``` and make changes to ```server/stocks/serializers.py``` accordingly. Make sure to run ```python manage.py migrate``` and ```python manage.py makemigrations``` once the models are updated. After succcessfully creating the ```price``` attribute, you have to create a Docker service which periodically(once in 60 seconds) GETs all the stocks from the ```stocks/``` endpoint and updates the ```price``` attribute for each stock with a random float value. 

## Tips
1. Please follow clean code standards and best practices.
2. Please follow git best practices. We will be going through your commits.
3. You can explore the API by going to http://127.0.0.1:8000/ in your browser. Make sure the docker container is up and running.
4. All the information you will need to solve the above tasks can be found in the links below.

## Useful Links
Here are some resources we think will be useful for you
1. https://www.django-rest-framework.org/tutorial/quickstart/#testing-our-api
2. https://docs.docker.com/compose/gettingstarted/

## Submission Instructions
- Create a pull request.
- Fill [this](https://docs.google.com/forms/d/e/1FAIpQLSfghyGdmHciSWKQ2RjnkemDV9Pdq5a7IT0006E9_1rgylhQCA/viewform?usp=sf_link) Google Form.

## Good Luck!