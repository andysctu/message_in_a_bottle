require './index.styl'
react = require 'react'
{div} = react.DOM
Map = require '../map'


module.exports = (props) ->
  div className: 'c-layout',
    div className: 'layout-content',
      Map {}
