import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

import streamlit as st

# import plotly.graph_objs as go

pio.templates.default = "ggplot2"

st.set_page_config(
	page_title = "App",
	page_icon = "💖"
)

from common import *

common_styles()

with st.sidebar:
	page = st.radio(
		"Aspects",
		[
			"Categories",
			"Locations",
			"Progression"
		]
	)

if page == "Categories":
	st.title("Categories of Friends 🤼")

	common_select()

	names = [
		["Thahir", "Morning Gang"],
		["Sahil", "Morning Gang"],
		["Swastik", "waaaow"],
		["Aparna", "waaaow"],
		["Garima", "waaaow"],
		["Bharat", "waaaow"],
		["Atul", "waaaow"],
		["Ziya", "School"],
		["Aachal", "School"],
	]

	others = [
		["School", ""],
		["Uni", ""],
		["Morning Gang", "Uni"],
		["waaaow", "Uni"]
	]

	filtered_list = others + [name for name in names if name[0] in st.session_state["my_input"]]
	filtered_names = [name[0] for name in filtered_list]
	filtered_parents = [name[1] for name in filtered_list]

	treemap = px.treemap(
		names = filtered_names,
		parents = filtered_parents,
		color = np.random.rand(len(filtered_names)) * 10,
		color_continuous_scale = "Plasma"
	).update(layout_coloraxis_showscale=False)

	treemap.update_layout(
		margin = dict(t=20, l=0, r=0, b=0)
	)

	st.plotly_chart(
		treemap,
		True
	)

if page == "Locations":
	st.title("Locations of Friends 🌍")

	common_select()

	df = pd.DataFrame(
			columns = ["Name", "Lat", "Lon"],
			data = [
				["Thahir", 25.3, 55.40],
				["Sahil", 25.3, 55.45],
				["Aparna", 25.3, 55.35],
				["Bharat", 24.9, 55.25],
				["Garima", 24.9, 55.35],
				["Swastik", 25.1, 55.2],
				["Atul", 25.1, 55.3],
				["Aachal", 24.9, 54.9],
				["Ziya", 9.9, 76.2]
			]
	)

	fig = px.scatter_geo(
			df.loc[
				df["Name"].isin(st.session_state["my_input"])
			],
			lat = "Lat",
			lon = "Lon",
			color = "Name"
	).update_traces(
			marker = dict(size = 10),
	).update_layout(
			margin = dict(t=0, l=0, r=0, b=0)
	).update_geos(
			projection_type="orthographic",
			center=dict(lat=17, lon=65.5),
			projection_rotation=dict(lon=65, lat=10),
			showcountries=True,
			countrycolor="rgba(0,0,0, 0.1)"
	)

	st.plotly_chart(
		fig,
		True
	)

if page == "Progression":
	st.title("Progression of Friends ⌚")
	
	common_select()

	df = pd.DataFrame(
		columns = ["Year", "Name", "Age", "Height", "Love for Paru"],
		data = [
				[2020, "Thahir", 17, 177, 0],
				[2021, "Thahir", 18, 178, 30],
				[2022, "Thahir", 19, 179, 60],
				[2023, "Thahir", 20, 180, 100],
				
				[2020, "Sahil", 17, 173, 0],
				[2021, "Sahil", 18, 174, 30],
				[2022, "Sahil", 19, 175, 60],
				[2023, "Sahil", 20, 176, 100],
				
				[2020, "Aparna", 17, 167, 0],
				[2021, "Aparna", 18, 168, 30],
				[2022, "Aparna", 19, 169, 60],
				[2023, "Aparna", 20, 170, 100],
				
				[2020, "Swastik", 18, 176, 0],
				[2021, "Swastik", 19, 177, 30],
				[2022, "Swastik", 20, 178, 60],
				[2023, "Swastik", 21, 179, 100],
				
				[2020, "Bharat", 18, 172, 0],
				[2021, "Bharat", 19, 173, 30],
				[2022, "Bharat", 20, 174, 60],
				[2023, "Bharat", 21, 175, 100],
				
				[2020, "Atul", 18, 174, 0],
				[2021, "Atul", 19, 175, 30],
				[2022, "Atul", 20, 176, 60],
				[2023, "Atul", 21, 177, 100],
				
				[2020, "Garima", 18, 158, 0],
				[2021, "Garima", 19, 159, 30],
				[2022, "Garima", 20, 160, 60],
				[2023, "Garima", 21, 161, 100],

				[2020, "Ziya", 18, 146, 0],
				[2021, "Ziya", 19, 147, 30],
				[2022, "Ziya", 20, 148, 60],
				[2023, "Ziya", 21, 149, 100],

				[2020, "Aachal", 18, 154, 0],
				[2021, "Aachal", 19, 155, 30],
				[2022, "Aachal", 20, 156, 60],
				[2023, "Aachal", 21, 157, 100],
		]
	)


	fig = px.scatter_3d(
			df.loc[
				df["Name"].isin(st.session_state["my_input"])
			],
			x = "Age",
			y = 'Height',
			z = 'Love for Paru',
			color = "Name",
			animation_frame = 'Year',
			animation_group = 'Name'
	)
	fig.update_layout(
			scene = dict(
					xaxis = dict(nticks=4, range=[1.1 * df["Age"].to_numpy().max(), 0.9*df["Age"].to_numpy().min()]),
					yaxis = dict(nticks=4, range=[0.9*df["Height"].to_numpy().min(), 1.1 * df["Height"].to_numpy().max()]),
					zaxis = dict(nticks=4, range=[0, df["Love for Paru"].to_numpy().max()])
			),
			margin = dict(t=0, l=0, r=0, b=0),
			scene_camera = dict(
					eye=dict(x=1, y=2, z=0)
			)
	)

	st.plotly_chart(
		fig,
		True
	)