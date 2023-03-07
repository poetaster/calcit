import QtQuick 2.2
import Sailfish.Silica 1.0
import Sailfish.WebView 1.0
import Sailfish.WebEngine 1.0

Page {
    id: page

    // The effective value will be restricted by ApplicationWindow.allowedOrientations
    allowedOrientations: Orientation.Portrait
    WebView {
        id: webView
        url: "../html/index.html"
        anchors.fill: parent
        Component.onCompleted: {
            WebEngineSettings.setPreference("security.disable_cors_checks", true, WebEngineSettings.BoolPref)
            WebEngineSettings.setPreference("security.fileuri.strict_origin_policy", false, WebEngineSettings.BoolPref)
            WebEngineSettings.setPreference("screenshots.browser.component.enabled", true, WebEngineSettings.BoolPref)
        }

    }

    onStatusChanged: {
        if (status == PageStatus.Active) {
            calcitApp.grabToImage(function(result) {
                console.log(result.url)
                calcitApp.thumbnail = result.url;
            });
        }
    }
}

