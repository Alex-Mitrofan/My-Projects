# Manners Matter
made by: Mitrofan Alexandru, Ciocan Alexandru <br/>
<br/>
Mitrofan Alexandru: <br/>
-Articles 1,2,5 from index.html;<br/>
-Login and Register;<br/>
-Profile;<br/>
-Advices;<br/>
-Contact;<br/>
<br/>
Ciocan Alexandru: <br/>
-Articles 3,4 from index.html;
-Challange;<br/>
-quizzes;<br/>
-Rank;<br/>
-Administrative module;<br/>
-About;<br/>
<br/>

Table of Contents
=================
  * [Introduction](#1-introduction)
    * 1.1 [Purpose](#11-purpose)
    * 1.2 [Intended Audience and Reading Suggestions](#12-intended-audience-and-reading-suggestions)
    * 1.3 [Product Scope](#13-product-scope)
    * 1.4 [References](#14-references)
  * [Overall Description](#overall-description)
    * 2.1 [Product Perspective](#21-product-perspective)
    * 2.2 [Product Functions](#22-product-functions)
    * 2.3 [User Classes and Characteristics](#23-user-classes-and-characteristics)
  * [External Interface Requirements](#external-interface-requirements)
    * 3.1 [User Interfaces](#31-user-interfaces)
    * 3.2 [Software Interfaces](#32-software-interfaces)
    * 3.3 [Communications Interfaces](#33-communications-interfaces)
  * [System Features](#system-features)
    * 4.1 [Register, login and logout](#41-register-login-and-logout)
    * 4.2 [View Profile](#42-view-profile)
    * 4.3 [Get Advices](#43-get-advices)
    * 4.4 [Challange](#44-challange)
    * 4.5 [About and Contact](#45-about-and-contact)
    * 4.6 [Articles](#46-articles)
    * 4.7 [Administrative Module](#47-administrative-module)
    




## 1. Introduction
### 1.1 Purpose 
This document describes the website named Manners Matter. The purpose of the documentation is to present the way the application runs, the architecture of the application and its characteristics.

### 1.2 Intended Audience and Reading Suggestions
The audience is anyone who wants to use the application. Next, the documentation presents the way the application works, software specifications and its architecture. 
Section 2 covers aspects related to the mode of operation and is suitable for regular users. The other sections cover advanced aspects and are intended for developers.

### 1.3 Product Scope
The role of this web application is to provide users with information about manners in the online environment, to offer them personalized advice based on their needs and to test their knowledge gained from reading the informative materials provided.
The application has a section with the ranking of the best users, its purpose being to motivate them to put into practice the information learned through the tests in the related section.

### 1.4 References
Here is a diagram in figma with the functionalities of the Manners Matter website and the administrative module.<br/>
https://www.figma.com/file/2cJVIJ6ku0oD69fC9lEOOG/Manner-Matter-Teh-Web?node-id=0%3A1&t=wRPjlI6jsy2qQtMC-1.<br/>
Here is a C4 diagram https://drive.google.com/file/d/1cERVsXgzrXQRfqmNIwXbIRhsZTBM5MBC/view?usp=sharing

## Overall Description
### 2.1 Product Perspective

The application is self-contained. It has two components: the administrative one and the component intended for users.


### 2.2 Product Functions

Functions of the user component that a user can perform: <br />
-register and login; <br />
-edit profile; <br />
-acces articles; <br />
-get personalized advices; <br />
-sustain tests; <br />
-see a scoreboard; <br />
-give feedback to admins. <br />
 <br />
Functions that an admin can perform on administrative module: <br />
-add new articles; <br />
-receive feedback/questions from users; <br />
-add new advices; <br />
-add new questions for tests. <br />


### 2.3 User Classes and Characteristics
Types of users:<br />
-users without an account can acces informations, get personalized advices, sustain test. They can't have a profile and can't get points for their tests.<br />
-users with an account can additionaly view their profile, keep track of their score and rank and appear on the leaderboard;<br />
-admins can add new articles, new advices, new questions for tests and receive feedback from users.<br />
<br />

Usual users are those who want to find more about manners on the internet. They can use this app as long as admins add new articles to read, new advices and new questions for tests in order to keep users engaged.<br />
The most important users are those who create an account.

 
## External Interface Requirements
### 3.1 User Interfaces

The home page (index.html) is the page that contains previews of all articles.<br />
The menu lights up depending on the page the user is on to facilitate page navigation.<br />
In the header, if the user hovers over the profile picture, a menu with 2 links opens, one that leads to his profile and the other that is a logout button.<br />
On the Home page, each article title is a link that leads to a separate html page with the entire article.<br />
The Profile.html page presents an "Edit" button that allows the user to edit his data, when pressed, text input fields will appear and a "Save" button will appear to save the changes.<br />
On the Advice.html page there is a form with radio buttons and a submit button. When the user chooses his preferred features from the form the list of tips will be filtered according to his choices.<br />
The Challenge.html page has a form where you select the difficulty of the test, and the submit button opens a new page with a question. The user ticks the correct answer and then clicks next question to display the next question until the test is ready and is redirected to the Home page.<br />
The Rank.html page shows a podium with the first 3 users and a table with more users.<br />
The About.html page presents information about the website.<br />
The Contact.html page contains a text input to allow users to provide input and an input field for email. The message is sent after pressing the submit button.

 

### 3.2 Software Interfaces


This website is connected to a database that stores user data, but also data present on the site such as articles, advices, questions, etc.

### 3.3 Communications Interfaces

Communication occurs only between users and administrators. The user communicates with the administrator through the Contact.html page. The administrator sees the message in the administration module on a page specific to viewing messages. The user receives a reply by email.

## System Features
In this section each feature has specific priority component ratings, such as benefit, penalty, cost, and risk (each rated on a relative scale from a low of 1 to a high of 9).
### 4.1 Register, login and logout

### 4.1.1   Description and Priority

This is an account management feature and has a medium priority because the website can be used without having an account. The benefit is that users can keep track of the accumulated score and appear in the ranking. The cost is the need for a database to store user data.<br />
<br />
priority -> medium<br />
benefit  -> 8<br />
cost     -> 4<br />
risk     -> 3<br />

  
### 4.1.2   Stimulus/Response Sequences
-User presses on login link.<br />
-If he does not have an account, he will press the register button.<br />
-Here you will enter your username, name, password, password x2.<br />
-After submitting, he will be redirected to Home.<br />
<br />

-The login page has the username and password fields.<br />
-The submit button will redirect user to Home if the data is correct, or a message will be displayed if the data is wrong.<br />
<br />
-The logout button present in the dropdown menu in the profile picture in the header will disconnect the user and redirect him to Home.

 
### 4.1.3   Functional Requirements
1. Pages Login.html and Register.html can be accessed only if the user is loged in.<br />
2. The user will be loged in only if the username and password are correct.<br />
3. The button "Logout" will logout the user only if the user is logged in, otherwise it will do nothing. <br />
4. If the user tries to acces pages Login.html and Register.hmtl via URL while logged in, he will be redirected to Home.html.<br />
 


### 4.2 View Profile
### 4.2.1   Description and Priority

This feature allows user to visualise his profile that contains following information: a profile picture, username, name, location, score, rank, age, ocupation. The user can edit his profile. This feature has a low priority because the user can have an account even if he doesn't add details to his profile. The benefit of this feature is that it keeps the user engaged. The cost is that requires a database. The risk is that the user won't use the feature to much. <br />
<br />
priority -> low<br />
benefit  -> 5<br />
cost     -> 4<br />
risk     -> 5<br />

### 4.2.2   Stimulus/Response Sequences
-User press "Profile" buttons from nav menu or user press "My Profile" button from dropdown menu hovered from profile picture from header;<br />
-User is redirected to Profile.html;<br />
-User presses "Edit" button to add a profile picture or update his information;<br />
-User presses "Save" button to save changes;

### 4.1.3   Functional Requirements
The Profile.html page can be acces only if the user is logged in. Otherwise he will be redirected to Login.html.


### 4.3 Get Advices
### 4.3.1   Description and Priority
This feature allows user to visualise all advices available on the website or to filter the advices according to his preferences. This feature has a high priority because it gives to the user useful information. The benefit is that user will be more intersted in this website. The cost is that it requires a database with advices. <br />
<br />
priority -> high<br />
benefit  -> 10<br />
cost     -> 4<br />
risk     -> 2<br />

### 4.3.2   Stimulus/Response Sequences
-User press "Advices" button from menu;<br />
-He is redirected to Advices.html;<br />
-User completes his prefferences from the form;<br />
-User presses "Submit" button;<br />
-Advices are filtered by the website.



### 4.4 Challenge
### 4.4.1   Description and Priority
This feature allows user to take a test with different level of difficulties and to gain points. The priority is high because it engages the user. The cost is that it requires a database for questions. The risk is low because the user may not use this feature.<br />
<br />
priority -> high<br />
benefit  -> 8<br />
cost     -> 5<br />
risk     -> 4<br />

### 4.4.2   Stimulus/Response Sequences
-User presses "Challenge" button from menu;<br />
-He is redirected to Challenge.html;<br />
-User selects test's difficulty from the form;<br />
-User presses "Start" button;<br />
-The website redirects user to Quiz page;<br />
-User selects the correct answer;<br />
-User presses "next question" button;<br />
-The website shows the next questions;<br />
-The website shows the score user obtained;<br />
-User is redirected to Home.html;


### 4.5 About and Contact

### 4.5.1   Description and Priority
This feature allows user to se information about website on "About.html" and to ask a question or give feedback in "Contact.html". The priority is low. The benefit is that user can be helped if he needs something and asks on contact form. The cost is that this type of communication requires a special page on administrative module. The risk is that the user won't use this feature.<br />
<br />
priority -> low<br />
benefit  -> 2<br />
cost     -> 6<br />
risk     -> 8<br />

 
### 4.5.2   Stimulus/Response Sequences
-User presses "About" button from menu;<br />
-User reads information about the website;<br />
-User presses "Contact" button from menu;<br />
-User types his message on form;<br />
-User types his email address on form;<br />
-The website redirects message and email to administrative module;<br />
-Admin responds user using email;<br />
  
### 4.5.3   Functional Requirements
Contact feature can be used only if the user completes the form with his email address.



### 4.6 Articles
### 4.6.1   Description and Priority
This features is composed by pages index.html and articles. On index.html there are previews for every article. Every preview contains a href title that redirects to article's page. The benefit and priority are high. The cost is that the feature requires a database with articles and it requires active admins that add new articles to keep users engaged.<br />
<br />
priority -> high<br />
benefit  -> 10<br />
cost     -> 7<br />
risk     -> 1<br />

### 4.6.2   Stimulus/Response Sequences

-User presses "Home" button from menu or the logo from header;<br />
-User reads the previews of articles;<br />
-User presses on article's title;<br />
-The website redirects user to article's specific page;<br />
-User reads entire article;<br />


### 4.7 Administrative Module
### 4.7.1   Description and Priority
This feature allows admins to add previews for articles, articles, questions, advices, read feedback. The priority is high. The benefit is that is keeps users engaged because they will have more content. The cost is high because this feature suppose active admins that add new content. The risk is high becasue it requires active admins.<br />
<br />
priority -> high<br />
benefit  -> 10<br />
cost     -> 8<br />
risk     -> 8<br />

### 4.7.2   Stimulus/Response Sequences
-Admin selects page where he wants to add content (Add article, Add advice, Add Question) or read feedback



