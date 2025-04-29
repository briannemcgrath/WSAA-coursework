# Web Services & Applications Project - Cosy Console 

This repository contains code and resources related to a project carried out for the Web Services & Applications module. 

## Project Overview: 

**Cosy Console** is a personal game library management web application designed to give gamers a cosy, intuitive experience for tracking their entire collection in one central place. Built with Flask on the server side and SQLite as the local database, Cosy Console also delivers: 

- A **clean and modern UI**, with a pastel-inspired color scheme and card layouts that feel both playful and profressional. 
- A **responsive dsign** that works seamlessly on desktop, tablet and mobile devices, employing CSS Flexbox and Grid for dynamic layouts. 
- **Interactive features** such as AJAX-powered featured cards on the homepage and dropdown filters that update results without full page reloads. 

## Core Functionality:
1. **CRUD Operations:** Users can add new games, view details in a dedicated card view, update game metadata(title, platform, genre, play status, descriptions, and ratings), and delete entries when they're no longer relevant. 
2. **Search & Filter:** The catalogue page offers drop-down filters for platform, genre, and play status, allowing quick narrowing of large libraries to find exactly the games you want to play or revisit. 
3. **Star Rating System:** Beyond simple numerical scores, games can be rated via an intutitive 1-5 Star widget, visually reflecting enjoyment levels. 
4. **Quick Access Wdigets:** Homepage widgets like "All Games", "By Genre", and "Wishlist" provide one-click access to key views, encouraging exploration and discovery. 

## Vision & Roadmap: 
- **Personalised Profiles** Future support for user authentication will enable multiple gamers on one instance to maintain private libraries. 
- **Community Features** Plans for game reviews, comments, and social sharing so players can recommend titles to friends. 
- **Data Integration** Potential integration with external APIs (e.g., IGDB, RAWG) to automatically fetch cover art, release dates, and genre tags. 
- **Analytics Dashboard** Visual charts and progress trackers to monitor play time, completion rates, and wish-list growth over time. 

Cosy Console aims to be more than just a database: it's a cosy corner of the internet where gamers can unwind, organise, and celebrate their passion for games - all in one place. 

# Key Features: 
1. **RESTful API**
- `GET /games` & `GET /games/<id>` - retrieve game list or details. 
- `POST /games`, `PUT /game/<id>`, `DELETE /games/<id>` - manage game entries via JSON or form. 

2. **Interactive Front-End**
- Server-rendered templates with dynamic Jinja2 logic. 
- AJAX integration for featured game cards. 
- Responsive card layouts, dropdown filters, and star-rating widgets. 

3 **Database Integration**
- SQLAlchemy ORM with a single `Game` model (id, title, platform, genre, status, description, rating)

4. **Deployment Ready**
- Configured for local development and easily deployed on PythonAnywhere or similar hosts. 


## Prerequisities/How to Run: 
1. Clone the repository.
2. Create and activate a virtual environment. 
3. Install dependencies 
4. Run the app. 
5. Open http://127.0.0.1:5000 in your browser.

## Next Steps: 

## Known Issues: 

## References: 

**Framework & ORM**
- Flask Documentation - The foundation for routing, request handling, and templating. (https://flask.palletsprojects.com/en/stable/)
- Flask/SQLAlchemy Documentation - Integrates SQLAlchemy ORM with Flask for the `Game` model and database sessions (https://flask-sqlalchemy.palletsprojects.com/en/stable/)
- Incoming Request Data Flask - How to access form data and query strings via `request.form` and `request.args` (https://flask.palletsprojects.com/en/stable/api/#incoming-request-data )

**Template & Rendering**
- Jinja2 "for" loops - powering all `{% for ... %}` blocks. (https://jinja.palletsprojects.com/en/latest/templates/#for)

**Front-End Layout & Styling**
- CSS Flexboxes - Used for game grid, quick-link widgets, and form layouts. (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)
- CSS Grid Layout - Reference for more complex layouts if extended. (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
- CSS Card Layout - Building the card UI for basic templates and color schemes. (https://www.w3schools.com/howto/howto_css_cards.asp, https://blog.pixelfreestudio.com/creating-complex-layouts-with-css-flexbox/)
- W3 CSS Templates - Inspiration for basic templates and color schemes. (https://www.w3schools.com/w3css/w3css_templates.asp )
- CSS Transitions - Smooth hover and focus effects on cards, buttons, and dropdowns. (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions/Using_CSS_transitions)
- Box Shadow - Applied soft shadows to cards and footer. (https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow )
- CSS Pills & Badges - Styling `.stat.pill` with `display_inline-block`, `border-radius`, `padding` and `background` - (https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius)
- CSS Variables - Used `var(--xx)` for colours and typography in `styles.css`. (https://www.w3schools.com/css/css3_variables.asp)

**Typography & Elements**
- HTML Tables - Layout for the full catalogue page table. (https://www.w3schools.com/html/html_tables.asp, https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table )
- HTML Forms & Inputs -Base for add/edit forms. (https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms )
- HTML <select> & <option> - Dropdowns for platform, genre, and status filter. (https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select ,https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#attr-selected, https://www.w3schools.com/TAgs/tag_select.asp  )
- HTML <input type="radio"> - Star rating inputs on the game form. (https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
- CSS ::before Pseudo-Element - Injected star characters for rating display. (https://www.w3schools.com/TAgs/tag_select.asp, https://developer.mozilla.org/en-US/docs/Web/CSS/::before )

**JavaScript & AJAX**
- Fetch API - AJAX calls to load featured games and delete entries without full page reload (https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch,https://www.freecodecamp.org/news/,https://www.youtube.com/watch?v=Oive66jrwBs   )
- Dynamically Deleting Rows - Removing table rows client-side after a successful DELETE. (https://www.youtube.com/watch?v=vkqZC_rEkVA)
- URLSearchParams - Parsing and preserving query parameters for filters. (https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams )
- Query String in Flask Routes - Handling `request.args` for server-side filtering. (https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes) 
- Array.prototype.slice() - Used to grab a sub-array of fixed length for 'Catalogue Overview' section - (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
- Array.prototype.sort() - Quick shuffle of games array for 'Catalogue Overview' section - (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

**Navigation & Usability**
- Active Page Highlight - Conditionally adding an `active` class to `<nav>` links based on `request.path`. (https://stackoverflow.com/questions/66427694/how-do-i-isolate-the-root-path-to-turn-on-and-off-its-active-class-on-the-navb )
- Breadcrumb Navigation - Design patterns for breadcrumbs to show context. (https://www.w3schools.com/howto/howto_css_breadcrumbs.asp)

## Acknowledgements: 
This repository was developed as part of coursework for the Higher Diploma in Science in Computing in Data Analytics with Atlantic Technological University. Special thanks to lecturer Andrew Beatty for guidance and support. 

**by Brianne McGrath**