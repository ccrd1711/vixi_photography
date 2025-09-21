# Space Shack on planet Phaedrus-1711 website Testing.md

![The Vixi Website amiresponsive image](/docs/images/features/amiresponsive-vixi.png)

The README.md for this website can be found [here](/README.md).

# Testing Contents Menu 

* [Automated Testing](#automated-testing)
    * [Validators](#validators)
    * [Lighthouse](#lighthouse)

* [Manual Testing](#manual-testing)
    * [User Stories](#user-stories)
    * [New Visitors](#new-visitors-to-the-site)
    * [Returning Visitors](#returning-visitors)

* [Bugs/Issues/Fixes](#bugsissuesfixes)

# Automated Testing

## Validators 

### HTML 

HTML validation was completed using [W3C Validator](https://validator.w3.org). 

### CSS 

CSS validation was completed using [the W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator), no errors were found.

### Javascript 

Javascript validation was completed using [JSHint](https://jshint.com/) and all files came back with no errors found.

### Python

Python PEP8 compliance testing and validation was completed using [the CI Python Linter](https://pep8ci.herokuapp.com). Every single .py file was input on 9/6 after reaching a point in development where likely no more changes were to be made apart from comments. All files were amended and are now compliant with no errors.

Update: Another .py file run for validation was done on 11/6 due to changes made in the code with 500 errors found. These are now rectified and all .py files passed validation. 

## Lighthouse 

Here are the reports I got from running Lighthouse reports on desktop and mobile 

### Desktop

![A screenshot of the results of lighthouse testing on desktop](/docs/images/lighthouse/lighthouse-results-pc.png)

### Mobile 

![A screenshot of the results of Lighthouse testing on mobile devices](/docs/images/lighthouse/lighthouse-results-mobile.png)

# Manual Testing 

## User Stories 

### New visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a new visitor I want to gain a clear understanding of what Vixi Photography offers through a visually striking landing page and simple navigation. | Simplistic design with bold features signalling the sites purpose and ways of navigation | Pass 
|As a new visitor I want to browse the photography gallery so that I can explore the style and quality of work before making a decision.| Two links to the Gallery on the front page with a fading roulette to give a hint of what the gallery has to offer | Pass 
|As a new visitor I want to register for an account so that I can unlock the ability to book sessions and purchase photographs.| Login button on home page which will automatically redirect you to register if you haven't done so already | Pass
|As a new visitor I want to make a booking with the photographer securely so that I can reserve a photoshoot with confidence.| Login required to do this and aptly signalled on the About page- link to which is on the homepage | Pass
|As a new visitor I want to find links to social media or external platforms so that I can follow the photographer and stay updated with new work. | There are social media icons along the bottom of every page to take the user to relevant social channels for updates.| Pass 

### Returning visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a returning user I want to log in and out of my account securely so that my personal details and activity are protected.| Login and logout securely managed and highlighted in top right whether you are logged in or out | Pass 
|As a returning user I want to make, edit, or cancel bookings so that I can manage my upcoming photography sessions easily.| All possible starting with the initial booking on the about page link, followed by all amendments in the My Bookings section | Pass 
|As a returning user I want to purchase or download photos so that I can access images immediately after completing a transaction.| All prints purchases are 'gifted' with immediate access to a digital copy of the same image | Pass 
|As a returning user I want to update my profile details so that my stored information remains accurate and up to date.| Possible to update and amend these in the Profile section, along with the ability to delete your account | Pass
|As a returning user I want to enjoy a consistent and responsive interface across devices so that I can navigate smoothly on both desktop and mobile.| Works responsively on devices and maintains uniformity of design throughout | Pass 

# Bugs/Issues/Fixes

This section contains a range of issues that were solved, including simple ones at project inception to more nuanced/complex ones late in development. What you see here is in chronological order so it gives you an idea of which direction I had my development going in. If any bugs remain at the end of the project that haven't been rectified they will be in their appropriate section. There were likely others through development that haven't been recorded fully due to being so focused on fixing them and forgetting to note them down at the time. 

 Fixed bugs | What happened? | Solution 
-- | -- | -- |
No. 1 | Edit booking view crashed (returned None) | Moved return render(...) outside the if block so GET requests always return a response.
No. 2 | Edit/Cancel buttons not showing as valid links | Fixed missing quote in the <a> tag around {% url 'edit_booking' b.pk %} 
No. 3 | Profile page error: ProfileForm got unexpected keyword arguments: 'instance' | Removed accidental Profile model from forms.py and replaced it with a proper ProfileForm(forms.ModelForm).
No. 4 | Success page error after checkout | Order.objects.obects typo and wrong field name created; corrected to objects and used created_at
No. 5 | My Orders page crashing with invalid literal for int() with base 10: '9000.00' | Template was using divisibleby filter incorrectly on money; replaced with proper total_display method. 
No. 6 | Admin broke after adding download field | Added missing migration for download_path (and later download_path_bw) and updated admin.py to match current model fields.
No. 7 | Download button error (OrderItem not defined) | Added correct import for OrderItem in orders/views.py.
No. 8 | Download path 404 (wrong URL) | Fixed to resolve static file paths properly with static() instead of hardcoded paths. 
No. 9 | Profile edit missing fields | Updated ProfileForm and Profile model to include phone and address fields; added validation.
No.10 | Gradient background not showing | Removed background override in .page {} and locked footer to bottom so gradient covers full viewport.
No.11 | On another page, the gradient repeated behind footer | Fixed CSS with min-height: 100vh; display:flex; flex-direction:column; so footer stays at bottom and gradient doesn’t repeat.
No.12 | Register didn’t log user in | Updated register view to authenticate+login after creating account for better UX.
No.13 | Profile email caused errors | Removed redundant email field from Profile model and used user.email instead. 
No.14 | Adding Colour/B&W option broke gallery | Initially tied gallery display to download paths; refactored to separate image_url (for gallery display) vs download_path/download_path_bw (for purchased downloads).
No.15 | Gallery photos not showing | Admin had .jpeg while static folder used .jpg; fixed by adding correct image_url field and aligning admin entries with actual filenames.
No.16 | Download button crashed (static not defined) | Added from django.templatetags.static import static import in orders/views.py.
No.18 | Double bookings allowed | Added form validation + DB constraint to block duplicate bookings on same date with active status.
No.19 | Booking form date picker missing | Explicitly used DateInput(type="date") widget to restore native date picker.
No.20 | Booking form accepted past dates and numeric-only locations | Added custom clean_event_date and clean_location validators to block past dates and enforce text-based location names.
No.21 | Basket didn't differentiate between colour and black and white items | Updated cart and templates to show CLR or B&W tages
No.22 | Basket 'remove' cleared all items in the basket not just one | Added remove_one view and template link to decrement single item instead of removing all