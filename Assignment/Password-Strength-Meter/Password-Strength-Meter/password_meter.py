import streamlit as st
import re

# --- Password Strength Logic ---

def calculate_strength(password: str) -> tuple[int, list[str]]:
    """
    Calculates the strength of a password and provides feedback.

    Args:
        password: The password string to evaluate.

    Returns:
        A tuple containing the strength score (0-5) and a list of feedback messages.
    """
    score = 0
    feedback = []

    if not password:
        return 0, ["Password cannot be empty."]

    # 1. Length
    if len(password) >= 12:
        score += 1
        feedback.append("✅ Excellent length (12+ characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("✔️ Good length (8-11 characters).")
    else:
        feedback.append("❌ Too short! Aim for at least 8 characters, 12+ is better.")

    # 2. Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✔️ Contains uppercase letters.")
    else:
        feedback.append("⚠️ Add uppercase letters (A-Z).")

    # 3. Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✔️ Contains lowercase letters.")
    else:
        feedback.append("⚠️ Add lowercase letters (a-z).")

    # 4. Numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✔️ Contains numbers.")
    else:
        feedback.append("⚠️ Add numbers (0-9).")

    # 5. Special Characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~`]", password):
        score += 1
        feedback.append("✔️ Contains special characters.")
    else:
        feedback.append("⚠️ Add special characters (e.g., !@#$%).")

    # Ensure score doesn't exceed a max (e.g., if we add more criteria later)
    # Current max score based on criteria: 2(length) + 1(upper) + 1(lower) + 1(num) + 1(special) = 6
    # Let's normalize to a 0-5 scale for simplicity in strength levels
    if score > 5: # Cap score for level mapping
        score = 5
    if len(password) > 0 and len(password) < 8 and score > 1: # Penalize short passwords even if they have variety
        score = 1 # Cap at 'Weak' if too short but has other criteria

    return score, feedback

def get_strength_level(score: int) -> str:
    """Converts a numerical score to a strength level string."""
    if score <= 1:
        return "🚨 Very Weak"
    elif score == 2:
        return "😡 Weak"
    elif score == 3:
        return "😟 Medium"
    elif score == 4:
        return "🙂 Strong"
    else: # score == 5 or 6 (capped at 5 for this mapping)
        return "🎉 Very Strong!"

# --- Streamlit UI ---

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")
st.caption("Enter a password below to check its strength and get suggestions.")

password_input = st.text_input("Password", type="password", key="password_field", placeholder="Type your password here...")

if password_input:
    score, feedback_messages = calculate_strength(password_input)
    strength_level = get_strength_level(score)

    # Display strength level with color
    if strength_level == "🚨 Very Weak":
        st.error(f"**Strength: {strength_level}**")
    elif strength_level == "😡 Weak":
        st.warning(f"**Strength: {strength_level}**")
    elif strength_level == "😟 Medium":
        st.info(f"**Strength: {strength_level}**")
    else: # Strong or Very Strong
        st.success(f"**Strength: {strength_level}**")

    # Progress bar for visual feedback
    # Max score is 6 (length 2 + 4 criteria * 1)
    # We map this to a 0-100 scale for the progress bar
    progress_value = int((score / 6) * 100) # Max possible score is 6
    st.progress(progress_value)

    st.subheader("📝 Feedback & Suggestions:")
    for msg in feedback_messages:
        if "✅" in msg or "✔️" in msg :
            st.markdown(f"<p style='color:green;font-size:1.05em;'>{msg}</p>", unsafe_allow_html=True)
        elif "❌" in msg or "😡" in msg or "🚨" in msg:
            st.markdown(f"<p style='color:red;font-size:1.05em;'>{msg}</p>", unsafe_allow_html=True)
        elif "⚠️" in msg or "😟" in msg:
             st.markdown(f"<p style='color:orange;font-size:1.05em;'>{msg}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='font-size:1.05em;'>{msg}</p>", unsafe_allow_html=True)

else:
    st.info("Awaiting password input...")

st.markdown("---")
st.markdown("Built with ❤️  by Kashan Malik using [Python](https://python.org) & [Streamlit](https://streamlit.io)")
st.markdown("Project based on [Panaverse Assignment](https://github.com/panaversity/learn-modern-ai-python/blob/main/CLASS_PROJECTS/02_password_strength_meter/password_strength_meter_assignment.md)")