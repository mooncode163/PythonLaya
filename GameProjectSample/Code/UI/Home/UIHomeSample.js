var UIHomeBase = require("UIHomeBase");
var AppRes = require("AppRes"); 
var GameViewController = require("GameViewController"); 
var UIHomeCenterBar = require("UIHomeCenterBar");

cc.Class({
    extends: UIHomeBase,
    properties: { 
 
        uiCenterBar: UIHomeCenterBar,
    },
    onLoad: function () {
        this._super();
        var x, y, w, h;

        //物理系统默认是关闭的，手动开启物理系统 
        //  cc.Common.EnablePhysic(true, false);
  
        this.LayOut();  



    },

    start: function () {
 
    },

    LayOut: function () {
        this._super();
       
    },

      

});

