import streamlit as st
import json
import uuid
import pandas as pd
from datetime import datetime

# --- Configuration ---
DATA_FILE = "books_library.json"

# --- Data Handling Functions ---
def load_books():
    """Loads books from the JSON data file."""
    try:
        with open(DATA_FILE, 'r') as f:
            books_data = json.load(f)
            # Ensure year_published is int, handle potential string from older data
            for book in books_data:
                if 'year_published' in book and isinstance(book['year_published'], str):
                    try:
                        book['year_published'] = int(book['year_published'])
                    except ValueError:
                        book['year_published'] = 0 # Default or handle error
            return books_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books_data):
    """Saves the list of books to the JSON data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(books_data, f, indent=4)

def generate_id():
    """Generates a unique ID for a book."""
    return str(uuid.uuid4())

# --- Core Library Functions ---
def add_book(title, author, genre, year_published, isbn=""):
    """Adds a new book to the library."""
    if not title or not author:
        st.error("Title and Author are required fields.")
        return False

    try:
        year_published = int(year_published)
        if year_published > datetime.now().year or year_published < 0:
            st.error(f"Please enter a valid year (e.g., up to {datetime.now().year}).")
            return False
    except ValueError:
        st.error("Year Published must be a number.")
        return False

    books = load_books()
    new_book = {
        "id": generate_id(),
        "title": title.strip(),
        "author": author.strip(),
        "genre": genre.strip(),
        "year_published": year_published,
        "isbn": isbn.strip(),
        "added_date": datetime.now().isoformat()
    }
    books.append(new_book)
    save_books(books)
    st.success(f"Book '{title}' added successfully!")
    return True

def update_book(book_id, title, author, genre, year_published, isbn=""):
    """Updates an existing book's details."""
    if not title or not author:
        st.error("Title and Author are required fields.")
        return False
    try:
        year_published = int(year_published)
        if year_published > datetime.now().year or year_published < 0:
            st.error(f"Please enter a valid year (e.g., up to {datetime.now().year}).")
            return False
    except ValueError:
        st.error("Year Published must be a number.")
        return False

    books = load_books()
    book_found = False
    for book in books:
        if book["id"] == book_id:
            book["title"] = title.strip()
            book["author"] = author.strip()
            book["genre"] = genre.strip()
            book["year_published"] = year_published
            book["isbn"] = isbn.strip()
            book_found = True
            break
    if book_found:
        save_books(books)
        st.success(f"Book '{title}' updated successfully!")
        return True
    else:
        st.error("Book not found for updating.")
        return False

def delete_book(book_id):
    """Deletes a book from the library."""
    books = load_books()
    initial_len = len(books)
    books = [book for book in books if book["id"] != book_id]
    if len(books) < initial_len:
        save_books(books)
        st.success("Book deleted successfully!")
        return True
    else:
        st.error("Book not found for deletion.")
        return False

# --- Streamlit UI ---
st.set_page_config(page_title="Personal Library Manager", layout="wide", page_icon="📚")

st.title("📚 Personal Library Manager")
st.markdown("Manage your personal book collection with ease.")

# --- Load books initially ---
if 'books_data' not in st.session_state:
    st.session_state.books_data = load_books()
if 'editing_book_id' not in st.session_state:
    st.session_state.editing_book_id = None


# --- Sidebar for Actions (Add/Edit) ---
st.sidebar.header("Actions")
action = st.sidebar.radio("Choose an action:", ["View Books", "Add New Book"], key="action_radio")

if st.session_state.editing_book_id:
    action = "Edit Book" # Force action to Edit if an edit is in progress

# --- Add New Book / Edit Book Form ---
if action == "Add New Book" or action == "Edit Book":
    form_header = "✏️ Edit Book Details" if action == "Edit Book" else "➕ Add a New Book"
    st.sidebar.subheader(form_header)

    book_to_edit = None
    if action == "Edit Book" and st.session_state.editing_book_id:
        book_to_edit = next((book for book in st.session_state.books_data if book["id"] == st.session_state.editing_book_id), None)
        if not book_to_edit:
            st.sidebar.error("Error: Could not find the book to edit.")
            st.session_state.editing_book_id = None # Reset
            st.experimental_rerun()


    default_title = book_to_edit['title'] if book_to_edit else ""
    default_author = book_to_edit['author'] if book_to_edit else ""
    default_genre = book_to_edit['genre'] if book_to_edit else ""
    default_year = book_to_edit['year_published'] if book_to_edit else datetime.now().year
    default_isbn = book_to_edit['isbn'] if book_to_edit else ""

    with st.sidebar.form(key="book_form", clear_on_submit=True if action == "Add New Book" else False):
        title = st.text_input("Title*", value=default_title)
        author = st.text_input("Author*", value=default_author)
        genre = st.text_input("Genre", value=default_genre)
        year = st.number_input("Year Published*", min_value=0, max_value=datetime.now().year + 5, value=default_year, step=1)
        isbn = st.text_input("ISBN (Optional)", value=default_isbn)

        submit_button_label = "Update Book" if action == "Edit Book" else "Add Book"
        submitted = st.form_submit_button(submit_button_label)

        if submitted:
            if action == "Add New Book":
                if add_book(title, author, genre, year, isbn):
                    st.session_state.books_data = load_books() # Refresh data
                    st.rerun() # Rerun to clear form and update view
            elif action == "Edit Book" and book_to_edit:
                if update_book(book_to_edit["id"], title, author, genre, year, isbn):
                    st.session_state.books_data = load_books() # Refresh data
                    st.session_state.editing_book_id = None # Clear editing state
                    st.experimental_rerun() # Rerun to reflect changes and clear form

    if action == "Edit Book":
        if st.sidebar.button("Cancel Edit"):
            st.session_state.editing_book_id = None
            st.experimental_rerun()

# --- View Books Section ---
if action == "View Books":
    st.header("My Book Collection")

    if not st.session_state.books_data:
        st.info("Your library is empty. Add some books to get started!")
    else:
        # --- Search and Filter ---
        search_col1, search_col2 = st.columns([3,1])
        with search_col1:
            search_term = st.text_input("Search by Title, Author, or Genre:", placeholder="Enter keyword...").lower()
        with search_col2:
            # Create a list of unique genres for filtering
            all_genres = sorted(list(set(book.get('genre', 'N/A') for book in st.session_state.books_data if book.get('genre'))))
            if not all_genres: # Handle case with no genres yet
                selected_genre_filter = st.selectbox("Filter by Genre:", ["All"], disabled=True)
            else:
                selected_genre_filter = st.selectbox("Filter by Genre:", ["All"] + all_genres)


        filtered_books = st.session_state.books_data
        if search_term:
            filtered_books = [
                book for book in filtered_books
                if search_term in book.get('title', '').lower() or \
                   search_term in book.get('author', '').lower() or \
                   search_term in book.get('genre', '').lower()
            ]
        if selected_genre_filter != "All":
            filtered_books = [book for book in filtered_books if book.get('genre', '') == selected_genre_filter]

        if not filtered_books and (search_term or selected_genre_filter != "All"):
            st.warning("No books match your search/filter criteria.")
        elif not filtered_books:
             st.info("Your library is empty or no books match the current filter.")
        else:
            # Display books using Pandas DataFrame for better table formatting
            # Select and reorder columns for display
            display_data = []
            for book in filtered_books:
                display_data.append({
                    "Title": book.get("title"),
                    "Author": book.get("author"),
                    "Genre": book.get("genre"),
                    "Year": book.get("year_published"),
                    "ISBN": book.get("isbn", "N/A")
                })
            
            df = pd.DataFrame(display_data)
            st.dataframe(df, use_container_width=True)

            st.subheader("Manage Books")
            for i, book in enumerate(filtered_books): # Iterate over filtered books to get correct indices
                cols = st.columns([4, 1, 1]) # Title | Edit | Delete
                full_title_author = f"{book.get('title', 'N/A')} by {book.get('author', 'N/A')}"
                
                # Shorten displayed title if too long
                display_title = (full_title_author[:50] + '...') if len(full_title_author) > 50 else full_title_author
                cols[0].markdown(f"**{display_title}** ({book.get('genre', 'N/A')}, {book.get('year_published', 'N/A')})")

                edit_button_key = f"edit_{book['id']}"
                if cols[1].button("✏️ Edit", key=edit_button_key, help=f"Edit '{book.get('title')}'"):
                    st.session_state.editing_book_id = book['id']
                    st.experimental_rerun() # Rerun to switch to edit mode

                delete_button_key = f"delete_{book['id']}"
                if cols[2].button("🗑️ Delete", key=delete_button_key, help=f"Delete '{book.get('title')}'"):
                    if delete_book(book['id']):
                        st.session_state.books_data = load_books() # Refresh
                        st.experimental_rerun() # Rerun to update view
                if i < len(filtered_books) -1: # Add a divider for all but the last book
                    st.divider()


st.sidebar.markdown("---")
st.sidebar.info(f"Data stored in: `{DATA_FILE}`")
st.sidebar.markdown("Made with Python & Streamlit")