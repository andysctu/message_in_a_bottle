{GoogleMapLoader, GoogleMap, Marker} =  require "react-google-maps"


class Map extends react.Component

  render: ->
    section {style: height: '100%'},
      GoogleMapLoader {
        containerElement: {
          div style: height: '100%'
        }
        #     {...props.containerElementProps}
        #     style={{
        #       height: "100%",
        #     }}
        #   />
        # }
        googleMapElement:
          GoogleMap {
            ref:{(map) => console.log(map)}
            defaultZoom:{3}
            defaultCenter:{{ lat: -25.363882, lng: 131.044922 }}
            onClick:{@props.onMapClick}
          }
        }

module.exports = Map
