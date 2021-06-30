var UIViewController = require("UIViewController");
var UIGameItem = require("UIGameItem");
var UIBoard = require("UIBoard");
var UIView = require("UIView");
var GameBase = require("GameBase");
var GameLevelParse = require("GameLevelParse");

//shu： wx621ff1107207384c
//weixin小程序appid: heng: wx2c5d3abfad26e8b1
//cocos: wx6ac3f5090a6b99c5
//weixin test app：wx844d0aa648111acb
var GameSample = cc.Class({
    extends: GameBase,
    statics: {
      
 

    },

    properties: { 

    },
    //百度tts:  http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=5&text=你要转换的文字 
    onLoad: function () {
        this._super();
        this.node.setContentSize(this.node.parent.getContentSize());
        // var ev = this.node.addComponent(cc.UITouchEvent);
        // ev.callBackTouch = this.OnUITouchEvent.bind(this);

    }, 

    LayOut: function () {
        this._super();

    },
  
});
