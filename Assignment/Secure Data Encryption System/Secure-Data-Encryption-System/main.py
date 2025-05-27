import streamlit as st
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64
import json
from datetime import datetime, timedelta

# Authored by Kashan Malik

# --- Application Configuration ---
# File paths for storing user data and encrypted messages
USERS_DB_FILE = "users.json"
ENCRYPTED_DATA_FILE = "encrypted_data.json"

# Security parameters for password hashing (PBKDF2)
SALT_BYTES_LENGTH = 16
PBKDF2_ITERATIONS = 100000 # More iterations mean stronger hashing, but slightly slower login

# Account lockout settings to deter brute-force attacks
MAX_FAILED_ATTEMPTS = 3
LOCKOUT_DURATION_MINUTES = 5

# A fixed, application-wide salt for deriving Fernet keys from user passwords.
# This is crucial for consistent key derivation across sessions.
# In a production app, this would be loaded from a truly secure, external source.
APP_FERNET_KEY_DERIVATION_SALT = b'a_unique_and_secret_app_salt_for_key_derivation_please_dont_change_me!' 

# --- Utility Functions for File Handling ---

def load_json_data(filepath):
    """Loads data from a JSON file. Initializes an empty dict if file doesn't exist."""
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({}, f) # Start fresh with an empty JSON object
        return {}
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            st.error(f"Error reading {filepath}. It might be corrupted. Starting with empty data.")
            # Consider backing up the corrupted file here in a real scenario
            return {}

def save_json_data(filepath, data):
    """Saves data to a JSON file with pretty indentation."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# --- User Authentication and Security Logic ---

def get_all_users():
    """Retrieves all user records from the user database file."""
    return load_json_data(USERS_DB_FILE)

def update_user_records(users_data):
    """Saves the current state of user records back to the database file."""
    save_json_data(USERS_DB_FILE, users_data)

def hash_user_password(password):
    """Hashes a user's password using PBKDF2 with a unique salt."""
    salt = os.urandom(SALT_BYTES_LENGTH)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, # Output length for the derived key (suitable for hashing)
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    hashed_key = kdf.derive(password.encode('utf-8'))
    return base64.b64encode(hashed_key).decode('utf-8'), base64.b64encode(salt).decode('utf-8')

def check_password_match(stored_hash, stored_salt, entered_password):
    """Verifies if the entered password matches the stored hash and salt."""
    salt_bytes = base64.b64decode(stored_salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_bytes,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    try:
        kdf.verify(entered_password.encode('utf-8'), base64.b64decode(stored_hash))
        return True
    except Exception: # Catches InvalidKey or other verification errors
        return False

def register_new_user(username, password):
    """Registers a new user account."""
    users = get_all_users()
    if username in users:
        return False, "This username is already taken. Please choose another."
    if not username or not password:
        return False, "Username and password cannot be empty."

    hashed_pw, pw_salt = hash_user_password(password)
    users[username] = {
        "password_hash": hashed_pw,
        "salt": pw_salt,
        "failed_attempts": 0,
        "last_failed_attempt_iso": None # Stored as ISO format string for easy datetime conversion
    }
    update_user_records(users)
    return True, "Registration successful! You can now log in."

def perform_user_login(username, password):
    """Authenticates a user, handling lockout logic."""
    users = get_all_users()
    user_record = users.get(username)

    if not user_record:
        # Generic message to avoid leaking user existence
        return False, "Invalid username or password."

    # Check if account is currently locked out
    if user_record["failed_attempts"] >= MAX_FAILED_ATTEMPTS and user_record["last_failed_attempt_iso"]:
        last_attempt_time = datetime.fromisoformat(user_record["last_failed_attempt_iso"])
        time_since_last_attempt = datetime.now() - last_attempt_time
        
        if time_since_last_attempt < timedelta(minutes=LOCKOUT_DURATION_MINUTES):
            remaining_time = timedelta(minutes=LOCKOUT_DURATION_MINUTES) - time_since_last_attempt
            mins, secs = divmod(int(remaining_time.total_seconds()), 60)
            return False, f"Account locked. Please wait {mins}m {secs}s before trying again."

    # Verify password
    if check_password_match(user_record["password_hash"], user_record["salt"], password):
        # Reset failed attempts on successful login
        user_record["failed_attempts"] = 0
        user_record["last_failed_attempt_iso"] = None
        update_user_records(users) # Corrected: Use update_user_records
        return True, "Login successful!"
    else:
        # Increment failed attempts and record timestamp
        user_record["failed_attempts"] += 1
        user_record["last_failed_attempt_iso"] = datetime.now().isoformat()
        update_user_records(users) # Corrected: Use update_user_records
        return False, "Invalid username or password."

# --- Encryption/Decryption with Password-Derived Keys ---

def derive_encryption_key_from_password(password):
    """Derives a Fernet encryption key from the user's password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, # Fernet keys are 32 bytes
        salt=APP_FERNET_KEY_DERIVATION_SALT, # Use the fixed app salt
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    # Fernet requires a URL-safe base64 encoded key
    derived_key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    return derived_key

def encrypt_user_message(message_text, user_password):
    """Encrypts a plaintext message using a key derived from the user's password."""
    encryption_key = derive_encryption_key_from_password(user_password)
    f = Fernet(encryption_key)
    encrypted_bytes = f.encrypt(message_text.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8') # Store as base64 string for JSON

def decrypt_user_message(encrypted_b64_string, user_password):
    """Decrypts a base64-encoded encrypted message using a key derived from the password."""
    encryption_key = derive_encryption_key_from_password(user_password)
    f = Fernet(encryption_key)
    try:
        decrypted_bytes = f.decrypt(base64.b64decode(encrypted_b64_string))
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        # Catch common decryption errors (e.g., InvalidToken if password is wrong)
        st.error(f"Decryption failed! Check your password or if the data is corrupted. Error: {e}")
        return None

# --- User-Specific Encrypted Data Management ---

def load_user_encrypted_data(username): # Renamed function for clarity
    """Loads all encrypted messages for a given user."""
    all_app_data = load_json_data(ENCRYPTED_DATA_FILE)
    return all_app_data.get(username, [])

def save_user_encrypted_data(username, messages_list): # Renamed function for clarity
    """Saves the list of encrypted messages for a given user."""
    all_app_data = load_json_data(ENCRYPTED_DATA_FILE)
    all_app_data[username] = messages_list
    save_json_data(ENCRYPTED_DATA_FILE, all_app_data)

# --- Streamlit Application Layout and Logic ---

st.set_page_config(layout="centered", page_title="Kashan's Secure App", page_icon="🔒")

# Initialize session state variables if they don't exist
# These persist across reruns of the Streamlit script
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_username' not in st.session_state:
    st.session_state.current_username = None
if 'login_feedback_message' not in st.session_state:
    st.session_state.login_feedback_message = ""
if 'register_feedback_message' not in st.session_state:
    st.session_state.register_feedback_message = ""
if 'user_session_password' not in st.session_state: # Stores the password for encryption/decryption
    st.session_state.user_session_password = None
# This is used to clear the password input field after submission
if 'login_password_input_value' not in st.session_state:
    st.session_state.login_password_input_value = ""


st.title("🔒 Kashan's Secure Multi-User Encryption App")
st.markdown("""
    Welcome to a secure vault for your messages! This application provides:
    - **Robust User Authentication**: Register and log in with your unique credentials.
    - **Advanced Password Security**: Passwords are never stored directly; they are securely hashed using PBKDF2.
    - **Brute-Force Protection**: A time-based lockout mechanism activates after too many failed login attempts.
    - **Persistent Data Storage**: Your encrypted messages are safely stored in a dedicated file, accessible only by you.
    - **Password-Derived Encryption Keys**: Your encryption key is dynamically generated from your password, ensuring it's never explicitly saved.
""")

# --- Login / Registration Section (displayed if not logged in) ---
if not st.session_state.logged_in:
    st.header("Access Your Vault")

    # Login Form
    with st.form("login_form_kashan"):
        st.subheader("Login")
        login_username_input = st.text_input("Username", key="login_user_input")
        login_password_input = st.text_input(
            "Password", 
            type="password", 
            key="login_password_widget", 
            value=st.session_state.login_password_input_value # Controls the input's displayed value
        ) 
        login_submit_button = st.form_submit_button("Login to Vault")

        if login_submit_button:
            if login_username_input and login_password_input:
                success, message = perform_user_login(login_username_input, login_password_input)
                st.session_state.login_feedback_message = message # Always set the message immediately
                
                if success:
                    st.session_state.logged_in = True
                    st.session_state.current_username = login_username_input
                    st.session_state.user_session_password = login_password_input 
                    st.session_state.login_password_input_value = "" # Clear password field on successful login
                    st.success(message) # Display success message
                    st.rerun() # Rerun to switch to main app view
                else:
                    # If not successful, the appropriate warning/error message will be displayed below the form
                    st.session_state.login_password_input_value = "" # Clear password field on failed login
            else:
                st.session_state.login_feedback_message = "Both username and password are required."
                st.session_state.login_password_input_value = "" # Clear password field if empty submission

        # Display the message AFTER the form submission logic has run
        if st.session_state.login_feedback_message:
            # Check if the message indicates an account lockout
            if "Account locked" in st.session_state.login_feedback_message:
                st.error(st.session_state.login_feedback_message) # Use st.error for critical lockout messages
            else:
                st.warning(st.session_state.login_feedback_message)
                # Display wrong input counter only for non-lockout failed attempts
                users_data = get_all_users()
                user_data = users_data.get(login_username_input)
                # Ensure user_data exists and they are not logged in (implying a failed attempt)
                if user_data and not st.session_state.logged_in:
                    st.info(f"Wrong attempts: {user_data['failed_attempts']} / {MAX_FAILED_ATTEMPTS}")

    st.markdown("---")

    # Registration Form
    with st.form("register_form_kashan"):
        st.subheader("New User Registration")
        new_username = st.text_input("Choose a Username", key="register_user_input")
        new_password = st.text_input("Set a Password", type="password", key="register_password_input")
        register_submit_button = st.form_submit_button("Register Account")

        if register_submit_button:
            if new_username and new_password:
                success, message = register_new_user(new_username, new_password)
                if success:
                    st.session_state.register_feedback_message = message
                    st.success(message)
                else:
                    st.session_state.register_feedback_message = message
                    st.error(message)
            else:
                st.session_state.register_feedback_message = "Please provide both a username and a password."
        if st.session_state.register_feedback_message:
            st.info(st.session_state.register_feedback_message)

# --- Main Application Section (displayed after successful login) ---
else:
    st.sidebar.header(f"Welcome, {st.session_state.current_username}!")
    if st.sidebar.button("Logout"):
        # Clear all relevant session state on logout
        st.session_state.logged_in = False
        st.session_state.current_username = None
        st.session_state.user_session_password = None 
        st.session_state.login_feedback_message = ""
        st.session_state.register_feedback_message = ""
        st.session_state.login_password_input_value = "" # Ensure login password field is clear for next login
        st.success("You have been securely logged out.")
        st.rerun() # Force rerun to show login page

    st.header("Encrypt Your Confidential Messages")
    message_to_encrypt = st.text_area("Type your secret message here:", height=150, key="message_encrypt_area")

    if st.button("Encrypt and Save Message"):
        if message_to_encrypt:
            with st.spinner("Encrypting and securely saving your message..."):
                try:
                    # Use the password stored in session state for encryption
                    encrypted_message_content = encrypt_user_message(message_to_encrypt, st.session_state.user_session_password) 
                    user_messages_list = load_user_encrypted_data(st.session_state.current_username)
                    user_messages_list.append({
                        "message_content": encrypted_message_content,
                        "timestamp": datetime.now().isoformat()
                    })
                    save_user_encrypted_data(st.session_state.current_username, user_messages_list)
                    st.success("Message encrypted and saved successfully!")
                    st.rerun() # Refresh display to show new message
                except Exception as e:
                    st.error(f"Failed to encrypt or save message: {e}")
        else:
            st.warning("Please enter some text before encrypting.")

    st.markdown("---")
    st.header("Your Encrypted Message History")

    # Button to clear all encrypted messages for the current user
    if st.button("Clear All Encrypted Messages (Irreversible!)"):
        # A simple confirmation. For critical actions, a stronger confirmation dialog is recommended.
        # In Streamlit, this often involves a two-step button or a separate input for confirmation.
        # For this example, we'll proceed if the user clicks the button.
        with st.spinner("Erasing your message history..."):
            save_user_encrypted_data(st.session_state.current_username, []) # Overwrite with empty list
            st.success("Encrypted message history cleared!")
            st.rerun() # Refresh the display

    user_stored_messages = load_user_encrypted_data(st.session_state.current_username)
    if user_stored_messages:
        # Display messages in reverse chronological order (newest first)
        for i, item in enumerate(reversed(user_stored_messages)): 
            display_time = datetime.fromisoformat(item['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            st.subheader(f"Message ({display_time})")
            st.code(item['message_content'], language='text') # Show the encrypted blob

            # Decrypt button for each message
            # Unique key for each button is important
            if st.button(f"Decrypt This Message", key=f"decrypt_btn_{i}_{item['timestamp']}"): # More robust key
                with st.spinner("Attempting decryption..."):
                    # Use the password stored in session state for decryption
                    decrypted_text = decrypt_user_message(item['message_content'], st.session_state.user_session_password) 
                    if decrypted_text is not None:
                        st.success("Decrypted Message:")
                        st.info(decrypted_text)
    else:
        st.info("Your encrypted message history is empty. Start encrypting above!")

    st.markdown("---")
    st.write("Crafted with dedication by Kashan Malik ❤️ using Streamlit")
