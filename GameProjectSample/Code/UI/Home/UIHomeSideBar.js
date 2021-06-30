var UIView = require("UIView");
var AppRes = require("AppRes");
var HomeViewController = require("HomeViewController");
var SettingViewController = require("SettingViewController");


cc.Class({
    extends: UIView,
    properties: {
        indexAction: 0,
        timeAction: 0.3,
        isActionFinish: false,
        btnSetting: cc.UIButton,
        btnMore: cc.UIButton,
        btnShare: cc.UIButton,
        btnNoAd: cc.UIButton,

        btnRestoreIAP: cc.UIButton,
        btnMusic: cc.UIButton,
        btnSound: cc.UIButton,
    },
    onLoad: function () {
        this._super();
        var x, y, w, h;
        
        this.btnShare.node.active = false;
        if (cc.Common.main().isWeiXin) {
            this.btnMore.node.active = false;
            this.btnNoAd.node.active = false;
        }

        this.LayOut();

    },

    start: function () {
        this.UpdateBtnMusic();
        this.UpdateBtnSound();
    },
    LayOut: function () {
        this._super();
        var size = this.node.getContentSize();
        var x, y, w, h;
        var ly = this.node.getComponent(cc.LayOutGrid);
        var rctran = this.node.getComponent(cc.RectTransform);
        // rctran.LayOut();
        cc.Debug.Log("UIHomeSideBar  w=  " + rctran.width + " h=" + rctran.height);
        if (ly != null) {
            ly.row = cc.LayoutUtil.main().GetChildCount(this.node, false);
            cc.Debug.Log("GetChildCount ly.row=" + ly.row);
            //有些按钮隐藏后重新布局
            ly.LayOut();
        }

    },

    UpdateBtnMusic: function () {
        var ret = cc.Common.GetBoolOfKey(cc.CommonRes.KEY_BACKGROUND_MUSIC, false);

        this.btnMusic.UpdateSwitch(ret);

    },


    UpdateBtnSound: function () {
        var ret = cc.Common.GetBoolOfKey(cc.CommonRes.KEY_BTN_SOUND, false);
        cc.Debug.Log("UpdateBtnSound ret=" + ret);
        this.btnSound.UpdateSwitch(ret);
    },

    OnClickBtnMusic: function (event, customEventData) {
        var ret = cc.Common.GetBoolOfKey(cc.CommonRes.KEY_BACKGROUND_MUSIC, false);//(AppString.STR_KEY_BACKGROUND_MUSIC);
        var v = !ret;
        cc.Debug.Log("UpdateBtnSwitch value=" + v);
        cc.Common.SetBoolOfKey(cc.CommonRes.KEY_BACKGROUND_MUSIC, v);
        this.UpdateBtnMusic();
        if (v) {
            cc.AudioPlay.main().PlayBgMusic();
        }
        else {
            cc.AudioPlay.main().PlayStopBgMusic();
        }
    },

    OnClickBtnSound: function (event, customEventData) {
        var ret = cc.Common.GetBoolOfKey(cc.CommonRes.KEY_BTN_SOUND, false);//(AppString.STR_KEY_BACKGROUND_MUSIC);
        var v = !ret;
        cc.Debug.Log("OnClickBtnSound UpdateBtnSwitch value=" + v);
        cc.Common.SetBoolOfKey(cc.CommonRes.KEY_BTN_SOUND, v);
        this.UpdateBtnSound();
    },

    OnClickBtnNoAd: function (event, customEventData) {
    },
    OnClickBtnMore: function (event, customEventData) {
    },
    OnClickBtnShare: function (event, customEventData) {
        cc.Share.main().ShareImageText("", cc.AppRes.SHARE_TITLE, cc.AppRes.SHARE_IMAGE_URL, "");
    },
    OnClickBtnSetting: function (event, customEventData) {
        cc.Debug.Log("UIHomeSideBar OnClickBtnSetting 1");
        var controller = HomeViewController.main();
        if (controller != null) {
            var navi = controller.naviController;
            cc.Debug.Log("UIHomeSideBar OnClickBtnSetting 2");
            navi.Push(SettingViewController.main());

        }
    },
    OnClickBtnAdVideo: function (event, customEventData) {
    },

    OnClickBtnFrendBoard: function (event, customEventData) {
        cc.FrendBoard.main().Show();
    },

});

