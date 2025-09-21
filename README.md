# VIXI Photography website README.md

![The Vixi Website amiresponsive image](/docs/images/amiresponsive-shack.png)

The live Vixi Photography site can be viewed [here](https://vixi-photography-98e8a4e90f4d.herokuapp.com/)

# Contents 

* [Introduction](#introduction)
* [Site objectives](#site-objectives)
* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
* [Design Development](#design-development)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Wireframes](#wireframes)
    * [Images](#images)
    * [Database Tables](#database-tables)
    * [Flow Diagrams](#flow-diagrams)
* [Features](#features)
* [Ideas going forward](#ideas-going-forward)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [External programs and libraries](#external-programs-or-libraries-used)
* [Testing File](#testing-file)
* [Deployment](#deployment-and-accessing-code-workspace)
* [Credits](#credits)
    * [Content & Media](#content&media)
* [Acknowledgements](#acknowledgements)

# Introduction 

## A Brief Summary 

Welcome to the VIXI photography website ReadMe. The idea for this website was firstly born out of the submission requirements - knowing that I had to have 'products' or something that had to be transacted. I knew then that I wanted to have access to as much content as I could get without having to worry about creating - like I did in the last project (Space Shack). I contacted a friend of mine, Tom, to ask if I could use his images. The VIXI - again, you may have seen elements of this in my last project (Phaedrus 1711) - is historically significant for the number 17, a lucky or favoured number for me. In Rome, 17 was considered unlucky and even today some buildings in Italy do not have a 17th floor or room number. The anagram of XVII - the traditional way of writing 17 in Roman numberals - VIXI, translates to 'I havelived'. There is no link between this and Tom's work - I just wanted a clean and interesting name for the website. 

# Site objectives 

## Deliver a clean, immersive user experience

The site is intentionally minimal in design, with bold highlights to guide navigation. Photography remains the central focus on all pages where images appear, ensuring they are not overshadowed by heavy styling or unnecessary clutter.

## Enable dynamic user interaction through full-stack functionality

Powered by Django, the site supports authenticated user interaction across multiple features. Users can purchase photographs, make and manage bookings with the photographer, download digital copies of prints, and update their profile details. All of these interactions are backed by a secure relational database, ensuring reliability and persistence.

## Use a cloud-hosted relational database

The project uses Neon.tech to host a PostgreSQL database, managing all persistent data including user profiles, bookings, and purchases. This cloud-based approach provides a secure, scalable solution that integrates seamlessly with the deployed Heroku application while following best practices for environment separation and data security. 

# User Experience 

## Target Audience 

The website is designed for sports enthusiasts, athletes, and event organisers who are looking for high-quality photography services. It also caters to potential clients who want to book professional photoshoots (e.g., sports teams, individual players, fitness professionals) and casual visitors who want to browse and potentially purchase sports photography prints.

More specifically, the target audience includes:

* Athletes and Teams – wanting to book a photographer for matches, training sessions, or promotional material.

* Sports Clubs and Event Organisers – needing reliable coverage of fixtures, tournaments, or local competitions.

* Fans and Collectors – interested in purchasing unique sports images as prints or digital downloads.

* General Public – casual visitors who enjoy browsing photography and may be inspired to book a session.

The platform is tailored to be simple, clean, and professional, so that both tech-savvy and less experienced users can easily browse galleries, make bookings, and manage their profiles.

## User Stories 

The manual testing for these can be found in the [Testing document](/TESTING.md)

### New Visitor Goals 

- As a new visitor I want to gain a clear understanding of what Vixi Photography offers through a visually striking landing page and simple navigation.

- As a new visitor I want to browse the photography gallery so that I can explore the style and quality of work before making a decision. 

- As a new visitor I want to register for an account so that I can unlock the ability to book sessions and purchase photographs.

- As a new visitor I want to make a booking with the photographer securely so that I can reserve a photoshoot with confidence.

- As a new visitor I want to find links to social media or external platforms so that I can follow the photographer and stay updated with new work. 

### Existing Visitor Goals 

- As a returning user I want to log in and out of my account securely so that my personal details and activity are protected.

- As a returning user I want to make, edit, or cancel bookings so that I can manage my upcoming photography sessions easily.

- As a returning user I want to purchase or download photos so that I can access images immediately after completing a transaction.

- As a returning user I want to update my profile details so that my stored information remains accurate and up to date.

- As a returning user I want to enjoy a consistent and responsive interface across devices so that I can navigate smoothly on both desktop and mobile.

# Design Development

Overall, I wanted this website to have a clean, modern, and minimal design so that the photography always takes centre stage. The use of whitespace and simple layouts ensures that images are never overshadowed by heavy styling or distractions. This approach helps create a professional yet immersive experience that encourages visitors to focus on the photographs and explore the services on offer.

Before committing to this design, I explored alternative ideas, such as creating a more feature-rich site with multiple content-heavy sections. However, I realised this would distract from the primary goal — showcasing the photography. By focusing on a stripped-back, image-led interface, I ensured that the photos remain the highlight and that users can easily navigate to bookings, purchases, or profile management.

## Typography 

The site uses the Marcellus font throughout to create a refined and professional aesthetic that complements the photography. Marcellus strikes a balance between elegance and readability, giving the site a timeless look suitable for sports photography. For accents and highlights, I opted for bold but subtle colour choices, avoiding anything too harsh that could detract from the imagery. This helps maintain visual clarity while reinforcing the clean and minimal design principles that guided the overall build.

## Colour Scheme

Every page of the site features a dark gradient background that shifts from grey to black, creating a consistent and professional backdrop for the photography. This design choice ensures that the images remain the focal point while adding depth and subtle visual interest to the layout.

To provide contrast and highlight key interactive elements, the site uses #f88604 (a vibrant orange) for all buttons, icons, and accent details. This bold pop of colour not only draws the user’s attention to important actions (such as making a booking or completing a purchase) but also reflects a recurring design motif across my projects.

The combination of a dark, neutral background with bright orange accents creates a minimal yet dynamic aesthetic — keeping the photography front and centre while ensuring usability and clear navigation.

## Wireframes 

Here are the wireframes created for this project. There is no difference between desktop and mobile layout. 

Landing/Home page

The plan was always to be quite minimal in the design of the homepage. I wanted it to be simple yet striking, with one focal point, that being the 'product' of the site. It does not show ALL the images you see in the Gallery as I wanted that to be the main display area. 

![A wireframe for the homepage of the website](/docs/images/features/landing-wireframe-desktop.png)

I wanted to go for the classic look here on the Gallery page. The thought did come through my head of doing another fading carousel type display and changing the landing entirely but I believe this design is better overall for UX.

![A wireframe for the gallery page](/docs/images/features/gallery-wireframe-desktop.png)

On the orders/confirmation list I wanted it to be laid out simply, something like you see in the wireframe below. I wanted it to be clear and highlighted well for navigation and accessibility. 

![A wireframe for the order or booking confirmations part of the profile](/docs/images/features/orders-bookings-desktop.png)

## Images 

All the images in this project are real photographs which have been provided by my good friend Tom who is endeavouring on a new career as a professional photographer in Kidderminster. He travelled to Belgium for the F1 earlier this year around the time where I was planning this project. He is also mentioned below in Acknowledgments. 

## Database Tables 

This project uses four main database tables alongside Django’s built-in User model. These handle core functionality for bookings, photo orders, and user profiles.

### Booking Table 

Stores confirmed bookings with the photographer, including client details, booking date, location, and cost. Each booking is linked to a user.

| key | name             | type              |
|-----|------------------|-------------------|
| PK  | id               | integer           |
|     | name             | string            |
|     | email            | string            |
|     | phone            | string            |
|     | event_date       | datetime          |
|     | location         | string            |
|     | notes            | text              |
|     | total_cost       | decimal           |
|     | created_on       | datetime          |
| FK  | user             | foreignkey(user)  |

### Order table

Tracks photo orders made by users, storing the purchased photo, payment status, and delivery method (digital download or print).

| key | name        | type                  |
|-----|-------------|-----------------------|
| PK  | id          | integer               |
| FK  | user        | foreignkey(user)      |
| FK  | photo       | foreignkey(photo)     |
|     | quantity    | integer               |
|     | total_price | decimal               |
|     | status      | string                |
|     | created_on  | datetime              |


### Photo Table

Stores metadata about each uploaded photograph in the gallery.

| key | name       | type                     |
|-----|------------|--------------------------|
| PK  | id         | integer                  |
|     | title      | string                   |
|     | image      | image field              |
|     | description| text                     |
|     | price      | decimal                  |
|     | created_on | datetime                 |

### Profile Table

Extends Django’s built-in User model with additional user information.

| key | name         | type             |
|-----|--------------|------------------|
| PK  | id           | integer          |
| FK  | user         | one-to-one(user) |
|     | display_name | string           |
|     | address      | string           |
|     | phone        | string           |
|     | created_on   | datetime         |

## Flow Diagrams 

Here is a Flow Diagram for the User of the site

![User Flow Diagram](/docs/images/tests/user-flow.drawio.png)


Here is a Flow Diagram for the Admin/Superuser(s) of the site

![Admin Flow Diagram](/docs/images/tests/admin-flow.drawio.png)

# Features 


# Ideas going forward 

While the current version of the site meets the core requirements, there is definite scope for growth...??? 

# Technologies Used 

## Languages Used 
- HTML5
- CSS3
- JavaScript
- Python 
- Django
- SQL

## External Programs or Libraries used (STRIPE?) 
- VSCode for local development
- PostgreSQL
- [GoogleFonts](https://fonts.google.com/)
- [GitPod](https://www.gitpod.io/)
- [GitHub](https://github.com/)
- [Heroku](https://heroku.com)
- [NeonTech](https://neon.com/)
- [PEP8 Validator](https://pep8ci.herokuapp.com/)
- [Draw.io](https://app.diagrams.net/)
- [ChatGPT](https://chatgpt.com)
- [Imageresizer.com](https://imageresizer.com/)
- [Imagecolorpicker.com](https://imagecolorpicker.com/)

# Testing File
The testing.md file for this website can be viewed [here](/TESTING.md) 

# Deployment and accessing code workspace

## GitHub Deployment
This project used GitHub for version control and code storage throughout development.

After each addition, change, or removal of code, I committed updates using the following commands in the terminal (VS Code with Git Bash was used for this project):

git add .
git commit -m "Meaningful and descriptive commit message"
git push

This ensured the latest version of the codebase was stored and backed up in my [GitHub repository](https://github.com/ccrd1711/space_shack)

## Forking or Cloning the Repository

To make your own copy of this repository:

Fork:
Click the Fork button in the top-right corner of the GitHub page to add it to your own account.

Clone:
Click the green Code button.

Copy the repository URL using the clipboard icon.

Open your terminal (Git Bash recommended) and run:
git clone https://github.com/your-username/space_shack.git

Change into the project directory:
cd space_shack

You now have a local copy ready to work on.

## Heroku Deployment 

The live version of this site is hosted on Heroku, using a PostgreSQL database hosted by Neon.tech. The site is fully integrated with Django and configured for deployment using standard production settings.

Create a New App
Log in to your Heroku dashboard.

Click New → Create new app.

Name your app (e.g. space-shack-live) and choose your region.

Click Create app.

et Config Vars
In the Settings tab, click Reveal Config Vars, and add the following environment variables:

Key	Value
DATABASE_URL	From Neon.tech
SECRET_KEY	Your Django secret key
ALLOWED_HOSTS	Your Heroku app domain
PORT	(Optional, usually not needed)

These variables are used by your Django settings to keep sensitive information out of version control.

## Deploying from GitHub

Go to the Deploy tab.

Choose GitHub as the deployment method.

Connect your GitHub account if you haven’t already.

Search for your repository name (space_shack) and click Connect.

Under Manual deploy, choose the branch (e.g. main) and click Deploy Branch.

Once the build process finishes, click Open App to launch the live site.

You can also enable Automatic Deploys so that every push to GitHub triggers a redeployment.

# Credits 

## Content & Media 
 
All the content in this project, in terms of the photography, are owned and shared by my friend Tom. He currently does not have a working website so shares his work exclusively on his Instagram @shotsbytombow.
The website in its entirety was created by me. 

## Acknowledgements 

I would like to thank my family and friends for encouraging me to continue working on this project during the start of the summer and continuing through to this final weekend through what has been an intensely challenging and saddening time for us all, which has coincided with a lot of change. Also I would like to thank all the members of Code Institute who have offered any sort of guidance along the way in this past year. 