var UIViewController = require("UIViewController");
var UIGameBase = require("UIGameBase");
var GameSample = require("GameSample"); 

var UIGameSample = cc.Class({
    extends: UIGameBase,
    statics: {
        
    },

    properties: {
        game: {
            default: null,
            type: GameSample
        },
        isShowGame: false,
    },
    onLoad: function () {
        this._super();
        this.LoadLanguageGame(); 
        this.textTitle.node.active = false;
    },
    start: function () {
        this._super();
    },
    

    CreateGame: function () {
        var node = cc.instantiate(this.gamePrefab);
        this.game = node.getComponent(GameShapeColor);
        this.game.node.parent = this.node;
        this.game.languageColor = this.languageColor;
        this.game.cbGameDidError = this.OnGameShapeColorDidError.bind(this);
        //zorder 让imageBg 显示在最底层，game显示在UI下面
        this.imageBg.node.zIndex = -20;
        this.game.node.zIndex = -10;
        this.isShowGame = true;
        this.callbackGuankaFinish = null;
        this.UpdateGuankaLevel(cc.LevelManager.main().gameLevel);

    },

    

    UpdateGuankaLevel: function (level) {
        cc.Debug.Log("UIGameShapeColor::UpdateGuankaLevel");
        this._super();
        this.game.listShape = cc.GameLevelParse.main().listShape;
        this.game.listColor = cc.GameLevelParse.main().listColor;
        this.game.textTitle = this.textTitle;
        this.textTitle.node.active = false;

        this.game.objGameFinish = {
            onWin: function (ui) {
                this.OnGameWinFinish(ui, false);
            }.bind(this),
            onFail: function (ui) {
                this.OnGameWinFinish(ui, true);
            }.bind(this),
        };

        this.game.LoadGame(cc.GameManager.gameMode);
      

    },
     
    

    //interface
    OnGameWinFinish(ui, isFail) {
        var info = cc.GameLevelParse.main().GetItemInfo();
        var strPrefab = ""; 

        // cc.PopUpManager.main().Show({
        //     prefab: strPrefab,
        //     open: function (ui) {
        //         ui.UpdateItem(info);
        //     }.bind(this),
        //     close: function (ui) {
        //     }.bind(this),
        // });

    },



});
