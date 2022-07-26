var longitude, latitude;
		
		var url ="/static/planes.geojson"

  		function display_map(longitude=-75.242180, latitude=39.876362) {
  			mapboxgl.accessToken = "{{ mapbox_access_token }}"
  			var map = new mapboxgl.Map({
  			container: 'map',
  			style: 'mapbox://styles/mapbox/streets-v11?optimize',
  			center: [longitude,latitude],
  			// projection: 'globe',
  			zoom: 7,


  			});


			


  			map.on('load', () => {
				// Add a new source from our GeoJSON data and
				// set the 'cluster' option to true. GL-JS will
				// add the point_count property to your source data.

				map.loadImage(
					"static/images/plane-icon.png",
					(error, image) => {
						if (error) throw error;
						
						// Add the image to the map style.
						map.addImage('cat', image);
					
					// Add a data source containing one point feature.
					map.addSource('planes', {
					type: 'geojson',
					// Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
					// from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
					data: "/static/planes.geojson",
					cluster: false,
					// clusterMaxZoom: 14, // Max zoom to cluster points on
					// clusterRadius: 14, // Radius of each cluster when clustering points (defaults to 50)

				});

					map.addLayer({
						id: 'planemarker',
						type: 'symbol',
						source: 'planes',
						'layout': {
							'icon-image': 'cat', // reference the image
							'icon-size': 0.0625
						}
				});

				});


				map.on('click', 'planemarker', (e) => {
					// Copy coordinates array.
					const coordinates = e.features[0].geometry.coordinates.slice();
					const description = e.features[0].properties.title;
					
					// Ensure that if the map is zoomed out such that multiple
					// copies of the feature are visible, the popup appears
					// over the copy being pointed to.
					while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
					coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
					}
					
					new mapboxgl.Popup()
					.setLngLat(coordinates)
					.setHTML(description)
					.addTo(map);
				});

			});
			

			

			







  	  		// Navigation marker at top-left corner
  	  		var nav = new mapboxgl.NavigationControl();
  	  			map.addControl(nav, 'top-left');
  	  		// change false to true, to get your location. Then, enable location in the browser.
  	  		map.addControl(new mapboxgl.GeolocateControl({
  	    			positionOptions: {
  	        			enableHighAccuracy: false
  	    			},
  	    		trackUserLocation: false
  			}));
  		}
  		display_map();