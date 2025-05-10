# **Web Services and Applications Repository**

This repository contains code and resources for assignments and the project related to the Web Services and Applications module. 

## **Table of Contents**
- [Assignments](assignments/) 
- [Project](project/)

## **Overview:**
### **Assignments:**

- [Task Two](assignments/assignment02-carddraw.ipynb): Interact with the [Deck of Cards API](https://deckofcardsapi.com/) to simulate drawing five cards from a shuffled deck. The focus is on identifying poker-like patterns such as pairs, triples, straights, and flushes. 
- [Task Three](assignments/assignment03-cso.py): Fetch the **"Exchequer Account (Historical Series)"** dataset from the CSP PxStat API and write it in JSON-stat formaat and save it to `cso.json`. 
- [Task Four](assignments/assignment04-andrew.txt): Authenticates to GitHub using token from `config.py`, lists repository contents to confirm file path, retreives a a text and and replaces pre-set values. Changes are committed and pushed back to the repository. 

### **Project:**

[Cosy Console](project/) - a personal game library management web application designed to give gamers a cosy, intuitive experience for tracking their entire collection in one central place. Built with Flask on the server side and SQLite as the local database, Cosy Console also delivers: 
- A **clean and modern UI**, with a pastel-inspired color scheme and card layouts that feel both playful and profressional. 
- A **responsive dsign** that works seamlessly on desktop, tablet and mobile devices, employing CSS Flexbox and Grid for dynamic layouts. 
- **Interactive features** such as AJAX-powered featured cards on the homepage and dropdown filters that update results without full page reloads. 

**Core Functionality:**
1. **CRUD Operations:** Users can add new games, view details in a dedicated card view, update game metadata(title, platform, genre, play status, descriptions, and ratings), and delete entries when they're no longer relevant. 
2. **Search & Filter:** The catalogue page offers drop-down filters for platform, genre, and play status, allowing quick narrowing of large libraries to find exactly the games you want to play or revisit. 
3. **Star Rating System:** Beyond simple numerical scores, games can be rated via an intutitive 1-5 Star widget, visually reflecting enjoyment levels. 
4. **Quick Access Widgets:** Homepage widgets like "All Games", "By Genre", and "Wishlist" provide one-click access to key views, encouraging exploration and discovery. 
5. **Analytics Dashboard:** Users can take a look at some stats on their games in the catalogue - Doughnut Chart (Games by Status) and Bar Chart (Most Popular Genre). 
6. **Daily Tips & Random Picks:** Rotating gamer tips each visit and a "Surprise Me" button at the bottom of the homepage pulls from the wishlist to spark that next session. 

**by Brianne McGrath**