# Space Shack on planet Phaedrus-1711 website Testing.md

![The Space Shack Website amiresponsive image](/docs/images/amiresponsive-shack.png)

The README.md for this website can be found [here](/README.md).

# Testing Contents Menu 

* [Automated Testing](#automated-testing)
    * [Validators](#validators)
    * [Lighthouse](#lighthouse)

* [Manual Testing](#manual-testing)
    * [User Stories](#user-stories)
    * [New Visitors](#new-visitors-to-the-site)
    * [Returning Visitors](#returning-visitors)
    * [Fault Testing](#fault-finding)

* [Bugs/Issues/Fixes](#bugsissuesfixes)

# Automated Testing

## Validators 

### HTML 

HTML validation was completed using [W3C Validator](https://validator.w3.org). In past projects I have copied and pasted my HTML directly from the files in VS Code in to the validator to test. This time, due to having base.html and most html pages in my project extending from base.html, I went to every single page on the deployed website and viewed the source code. I copied and pasted this html in to the validator. Every single page passed with no errors. When putting base.html into the HTML validator itself by direct input it fails however this is due to the {% ...} tag at the start, a Django-specific command invisible to the browser. 

### CSS 

CSS validation was completed using [the W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator), no errors were found. This one was completed as normal, by copying my CSS file input into the direct input box. 

### Javascript 

Javascript validation was completed using [JSHint](https://jshint.com/) and both files came back with no errors found.

### Python

Python PEP8 compliance testing and validation was completed using [the CI Python Linter](https://pep8ci.herokuapp.com). Every single .py file was input on 9/6 after reaching a point in development where likely no more changes were to be made apart from comments. All files were amended and are now compliant with no errors. 

Update: Another .py file run for validation was done on 11/6 due to changes made in the code with 500 errors found. These are now rectified and all .py files passed validation. 

## Lighthouse 

Here are the reports I got from running Lighthouse reports on desktop and mobile 

### Desktop

![A screenshot of the results of lighthouse testing on desktop](/docs/images/lighthouse/desktop%20index%20lighthouse.png)

### Mobile 

![A screenshot of the results of Lighthouse testing on mobile devices](/docs/images/lighthouse/mobile-lighthouse-report.png)

# Manual Testing 

## User Stories 

### New visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a new visitor I want to gain an understanding of what Phaedrus-1711 and the Space Shack experience offers, through an immersive landing page and rich descriptions. | The user is welcomed by a vibrant and cosy-feeling landing page and the About page provides more immersive information on their potential stay at the Shack.| Pass 
|As a new visitor I want to successfully navigate the site to explore reviews and comments from previous “guests.” | All users are able to *view* the reviews, and can see who it was written by, the content and star rating.| Pass 
|As a new visitor I want to register for an account to become part of the interplanetary travel community.| Continuing on from the previous story, users can go one further and register which allows them full interactivity and can leave comments and like reviews.| Pass
|As a new visitor I want to make a (rather expensive) booking securely and then be able to leave my own reviews.| You are not able to leave a review or book the Shack on the site without being logged in. The form is fully interactive so that it will snuff out typo errors on email fields, and avoids double bookings.| Pass
|As a new visitor I want to make sure I can follow this accommodation in other ways so that I can get updates from elsewhere.| There are social media icons along the bottom of every page to take the user to relevant social channels for updates.| Pass 

### Returning visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a returning user I want to log in and out of their account securely.| Users have a login button brightly signposted in the nav bar, and a log out option in the dropdown under their username.| Pass 
|As a returning user I want to submit, view, edit, or delete their own reviews and comments.| As mentioned above, this is a continuation. All submissions, views, edits and deletes have their own dedicated screens.| Pass 
|As a returning user I want to enjoy a consistent and responsive user interface across devices, reinforcing a seamless and immersive space tourism experience.| The site is fully functional and responsive on all screen sizes and is designed for ease of navigation| Pass 
|As a returning user I want to enjoy navigating through the site on mobile as well as desktop.| There is an accessible and well highlighted dropdown to take you to all elements of the site plus an icon in the top left to take you to the index page quicker.| Pass
|As a returning user I want to view and manage my upcoming bookings, so I can keep track of my interplanetary travel plans with ease.| In the dropdown under the user name is a section for My Bookings where any booked trips can be removed or amended as necessary| Pass 

## Fault Testing 

This section is dedicated to showing visually how some of the Error 500's have been rectified and what they show instead of breaking the site and showing an error. Most of these were found through the Booking form as that's arguably the heaviest section of user interaction. 

The screenshot below shows what happens when a user attempts to submit a comment containing only whitespace (in this case, under a particularly harsh review!).
Previously, these inputs were incorrectly accepted but not displayed — and no error message was shown to the user, which led to poor user experience.
Now, both review and comment submissions strip whitespace and validate properly. If the input is empty after trimming, a user-friendly warning is shown instead of triggering a server error. This also extends to the edit comment page. 

![Screenshot of whitespace in comments section](/docs/images/tests/whitespace-comments.jpg)

Below are 5 screenshots all relating to errors I had found within the booking form and were subsequently fixed (please see [bugs](#bugsissuesfixes)). 

Despite setting initial parameters, my code did not sufficiently prevent all booking-related faults. During testing, I discovered that unvalidated users could submit bookings with:

- Incorrectly formatted email addresses
- Stay durations longer than intended
- Guest numbers exceeding the 2-person limit
- Stays that begun in the past, or when the check-in date was after the check-out date

Each of these issues caused the site to break or behave unexpectedly. Validation checks were added to address these problems and ensure user input meets all booking requirements.These screenshots provide additional contextual proof that these issues are now dealt with and hopefully should no longer be an issue on the site. 

![Screenshot of booking error number 1](/docs/images/tests/forms-validation-1.jpg)

![Screenshot of booking error number 2](/docs/images/tests/forms-validation-2.jpg)

![Screenshot of booking error number 3](/docs/images/tests/forms-validation-3.jpg)

![Screenshot of booking error number 4](/docs/images/tests/forms-validation-4.jpg)

![Screenshot of booking error number 5](/docs/images/tests/forms-validation-5.png)

# Bugs/Issues/Fixes

This section contains a range of issues that were solved, including simple ones at project inception to more nuanced/complex ones late in development. What you see here is in chronological order so it gives you an idea of which direction I had my development going in. If any bugs remain at the end of the project that haven't been rectified they will be in their appropriate section. There were likely others through development that haven't been recorded fully due to being so focused on fixing them and forgetting to note them down at the time. 

 Fixed bugs | What happened? | Solution 
-- | -- | -- |
No. 1 | XX | XX
No. 2 | XX | XX 
No. 3 | XX | XX
No. 4 | XX | XX
No. 5 | XX | XX 
No. 6 | XX | XX 
No. 7 | XX | XX
No. 8 | XX | XX 
No. 9 | XX | XX 
No.10 | XX | XX 
No.11 | XX | XX
No.12 | XX | XX
No.13 | XX | XX 
No.14 | XX | XX
No.15 | XX | XX 
No.16 | XX | XX
No.18 | XX | XX
No.19 | XX | XX 
No.20 | XX | XX