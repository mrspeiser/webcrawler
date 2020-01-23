const EventEmitter = require('events')
const util = require('util');

function Webcrawler(url=""){
  this.type = "webcrawler";
  this.initUrl = url
}

util.inherits(Webcrawler, EventEmitter)

module.exports = Webcrawler
