requirejs.config({
  baseUrl: "/scripts/celestrium/",
  paths: {
    "jquery": "lib/jquery",
    "jquery.typeahead": "lib/jquery.typeahead",
    "underscore": "lib/underscore",
    "backbone": "lib/backbone",
    "d3": "lib/d3",
  },
  shim: {
    'jquery.typeahead': ['jquery'],
    'd3': {
      exports: "d3",
    },
    'underscore': {
      exports: '_',
    },
    'backbone': {
      deps: ['underscore'],
      exports: 'Backbone',
    },
  }
});

requirejs(["src/celestrium"], function(Celestrium) {

  var dataProvider = new function() {
    this.minThreshold = 0.75;
    this.getLinks = function(node, nodes, callback) {
      var data = {
        node: JSON.stringify(node),
        otherNodes: JSON.stringify(nodes),
      }
      this.ajax('get_edges', data, callback);
    };

    this.getLinkedNodes = function(nodes, callback) {
      var data = {
        nodes: JSON.stringify(nodes),
      };
      this.ajax('get_related_nodes', data, callback);
    };

    this.ajax = function(url, data, callback) {
      $.ajax({
        url: url,
        data: data,
        success: callback,
      });
    }
  };

  var celestrium = new Celestrium({
    el: document.querySelector("#workspace"),
    dataProvider: dataProvider,
    nodePrefetch: "get_nodes",
  }).render();

})