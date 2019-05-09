# Random quote machine

This started as a project for a freecodecamp certification. The task was to build a website that would show random quotes.

I chose to learn enough Django to scrape quotes from quotes.net. When the page loads, ten quotes (shorter than 300 characters) are scraped, and stored in the html that's served. Each click on the New Quote button uses jQuery to change the quote displayed on the page. After all quotes stored in the page have been shown, the next button click refreshes the page, which scrapes ten more quotes.

Clicking the Twitter icon loads the current quote into a form to be tweeted.

Setting up the static assets in Django (the images and css files used) was tricky. There's room for more learning on my part around that.

A redirect from incblots.com/randomquote points to where the live project is hosted on Heroku.


