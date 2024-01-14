 ## Flask Application Design for Curating Memories Website

### HTML Files

**1. index.html**
- Serves as the main page of the website.
- Contains a form for users to input their memories.
- Includes a section to display the curated memories.

**2. memories.html**
- Displays the curated memories in a visually appealing manner.
- Provides options for users to edit or delete their memories.

**3. edit_memory.html**
- Allows users to edit their existing memories.
- Contains a form for users to make changes to their memories.

### Routes

**1. @app.route('/')**
- Handles the main page of the website.
- Renders the index.html file.

**2. @app.route('/memories')**
- Handles the display of curated memories.
- Queries the database for all memories and passes them to the memories.html file for rendering.

**3. @app.route('/add_memory', methods=['POST'])**
- Handles the addition of new memories.
- Receives the user input from the form on index.html and saves it to the database.
- Redirects to the memories page after successful addition.

**4. @app.route('/edit_memory/<int:memory_id>', methods=['GET', 'POST'])**
- Handles the editing of existing memories.
- Retrieves the memory with the specified ID from the database and passes it to the edit_memory.html file for rendering.
- Updates the memory in the database if the user makes changes and submits the form.
- Redirects to the memories page after successful update.

**5. @app.route('/delete_memory/<int:memory_id>')**
- Handles the deletion of memories.
- Deletes the memory with the specified ID from the database.
- Redirects to the memories page after successful deletion.