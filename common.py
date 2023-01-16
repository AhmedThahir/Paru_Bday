import streamlit as st
# from streamlit_extras.no_default_selectbox import selectbox

options = [
		"Aachal",
		"Aparna",
		"Atul",
		"Bharat",
		"Garima",
		"Sahil",
		"Swastik",
		"Thahir",
		"Ziya"
]

def common_select():
	if "my_input" not in st.session_state:
		st.session_state["my_input"] = []

	my_input = st.multiselect(
		"Displaying results for",
		options,
		label_visibility = "hidden"
	)

	if my_input:
		st.session_state["my_input"] = my_input
		selected_msg = ", ".join(my_input)
	else:
		st.session_state["my_input"] = options
		selected_msg = "All"

	st.write(f"Displaying results for **{selected_msg}**")

def common_styles():
	common_styles = """
	<style>
	#MainMenu,
	#footer,
	a[href="https://streamlit.io/cloud"]
	{display: none;}
	</style>
	"""

	st.markdown(common_styles, unsafe_allow_html=True)