var UIViewController = require("UIViewController");
var UIGameBase = require("UIGameBase"); 

var GameLevelParse = cc.Class({
    extends: cc.LevelParseBase,
    statics: { 
    },

    statics: { 
    },

    properties: {
        
    },

    GetGuankaTotal: function () {
        // var count = this.ParseGuanka();
        var count = 0;
     
        return count;
    },
    CleanGuankaList: function () {
       

    },

    ParseGuanka: function (json) {
        // var idx = cc.LevelManager.main().placeLevel;
        // var infoPlace = cc.LevelManager.main().GetPlaceItemInfo(idx);
        // cc.Debug.Log("GameLevelParse ParseGuanka 0");
        // if ((this.listGuanka != null) && (this.listGuanka.length != 0)) {
        //     return;
        // }
        // var strPlace = infoPlace.id;

        // var items = json.items;
        // for (var i = 0; i < items.length; i++) {
        //     var info = new cc.CaiCaiLeItemInfo();
        //     var item = items[i];
        //     info.id = item.id;
        //     info.title = item.title;
        //     info.pronunciation = item.pronunciation;
        //     info.translation = item.translation;
        //     info.album = item.album;

        //     var dirRoot = cc.CloudRes.main().rootPath;
        //     var picdir = dirRoot + "/image/" + strPlace;
        //     info.pic = picdir + "/" + info.id + ".png";

        //     //歇后语
        //     var key = "xiehouyu";
        //     if (item.key != null) {
        //         var xiehouyu = item.key;
        //         for (var j = 0; j < xiehouyu.length; j++) {
        //             var item_xhy = xiehouyu[j];
        //             if (j == 0) {
        //                 info.head = item_xhy.content;
        //             }
        //             if (j == 1) {
        //                 info.end = item_xhy.content;
        //             }
        //         }
        //     }

        //     //谜语
        //     key = "head";
        //     if (item.key != null) {
        //         //Riddle
        //         info.head = item.head;
        //         info.end = item.end;
        //         info.tips = item.tips;
        //         info.type = item.type;
        //     }

        //     info.gameType = infoPlace.gameType;
        //     cc.Debug.Log("UpdateWord ParseGuanka gameType=" + info.gameType);
        //     this.listGuanka.push(info);
        // }

        // cc.Debug.Log("UIGameCaiCaiLe  ParseGuanka gameType=" + info.gameType);
        //  


        // this.ParseGuankaDidFinish();


    },
 


    StartParseGuanka: function (callback) {
        this.callbackGuankaFinish = callback;
        
    },
      

});

GameLevelParse._main = null;
GameLevelParse.main = function () {
    // 
    if (!GameLevelParse._main) {
        GameLevelParse._main = new GameLevelParse();
    }
    return GameLevelParse._main;
}

cc.GameLevelParse = module.export = GameLevelParse; 
