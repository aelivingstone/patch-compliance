/*
 * Copyright 2017 SideeX committers
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 */

// handle dialogs (alert, prompt etc.) commands

var originalPrompt = originalPrompt ? originalPrompt : window.prompt;
//var topPrompt = topPrompt ? topPrompt : window.top.prompt;
var nextPromptResult = false;
var recordedPrompt = null;

var originalConfirmation = originalConfirmation ? originalConfirmation : window.confirm;
var nextConfirmationResult = false;
var recordedConfirmation = null;

var originalAlert = originalAlert ? originalAlert : window.alert;
var nextAlertResult = false;
var recordedAlert = null;

function getFrameLocation() {
    let frameLocation = "";
    let currentWindow = window;
    let currentParentWindow;
    while (currentWindow !== window.top) {
        currentParentWindow = currentWindow.parent;
        for (let idx = 0; idx < currentParentWindow.frames.length; idx++)
            if (currentParentWindow.frames[idx] === currentWindow) {
                frameLocation = ":" + idx + frameLocation;
                currentWindow = currentParentWindow;
                break;
            }
    }
    frameLocation = "root" + frameLocation;
    return frameLocation;
}


//before record prompt

// Not a top window
if (window !== window.top) {

    window.prompt = function(text, defaultText) {
        if (document.body.hasAttribute("SideeXPlayingFlag")) {
            return window.top.prompt(text, defaultText);
        } else {
            let result = originalPrompt(text, defaultText);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction: "from-page-script",
                recordedType: "prompt",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };

    window.confirm = function(text) {
        if (document.body.hasAttribute("SideeXPlayingFlag")) {
            return window.top.confirm(text);
        } else {
            let result = originalConfirmation(text);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction: "from-page-script",
                recordedType: "confirm",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };

    window.alert = function(text) {
        if(document.body.hasAttribute("SideeXPlayingFlag")){
            recordedAlert = text;
            // Response directly
            window.top.postMessage({
                direction: "from-page-script",
                response: "alert",
                value: recordedAlert
            }, "*");
            return;
        } else {
            let result = originalAlert(text);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction:"from-page-script",
                recordedType: "alert",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };

} else { // top window

    window.prompt = function(text, defaultText) {
        if (document.body.hasAttribute("setPrompt")) {
            recordedPrompt = text;
            document.body.removeAttribute("setPrompt");
            return nextPromptResult;
        } else {
            let result = originalPrompt(text, defaultText);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction: "from-page-script",
                recordedType: "prompt",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };
    window.confirm = function(text) {
        if (document.body.hasAttribute("setConfirm")) {
            recordedConfirmation = text;
            document.body.removeAttribute("setConfirm");
            return nextConfirmationResult;
        } else {
            let result = originalConfirmation(text);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction: "from-page-script",
                recordedType: "confirm",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };
    window.alert = function(text) {
        if(document.body.hasAttribute("SideeXPlayingFlag")){
            recordedAlert = text;
            // Response directly
            window.top.postMessage({
                direction: "from-page-script",
                response: "alert",
                value: recordedAlert
            }, "*");
            return;
        } else {
            let result = originalAlert(text);
            let frameLocation = getFrameLocation();
            window.top.postMessage({
                direction:"from-page-script",
                recordedType: "alert",
                recordedMessage: text,
                recordedResult: result,
                frameLocation: frameLocation
            }, "*");
            return result;
        }
    };
}

//before record confirm
/*
window.confirm = function(text) {
    if (document.body.hasAttribute("SideeXPlayingFlag")) {
        recordedConfirmation = text;
        return nextConfirmationResult;
    } else {
        let result = originalConfirmation(text);
        window.postMessage({
            direction: "from-page-script",
            recordedType: "confirm",
            recordedMessage: text,
            recordedResult: result,
        }, "*");
        return result;
    }
};
*/
//before record alert
/*
window.alert=function(text){
    if(document.body.hasAttribute("SideeXPlayingFlag")){
        recordedAlert=text;
        return nextAlertResult;
    }else{
        let result=originalAlert(text);
        window.postMessage({
            direction:"from-page-script",
            recordedType: "alert",
            recordedMessage: text,
            recordedResult:result,
        },"*");
        return result;
    }
};
*/

//play window methods
if (window == window.top) {
    window.addEventListener("message", function(event) {
        if (event.source == window && event.data &&
            event.data.direction == "from-content-script") {
            let result = undefined;
            switch (event.data.command) {
                case "setNextPromptResult":
                    nextPromptResult = event.data.target;
                    document.body.setAttribute("setPrompt", true);
                    window.postMessage({
                        direction: "from-page-script",
                        response: "prompt"
                    }, "*");
                    break;
                case "getPromptMessage":
                    result = recordedPrompt;
                    recordedPrompt = null;
                    window.postMessage({
                        direction: "from-page-script",
                        response: "prompt",
                        value: result
                    }, "*");
                    break;
                case "setNextConfirmationResult":
                    nextConfirmationResult = event.data.target;
                    document.body.setAttribute("setConfirm", true);
                    window.postMessage({
                        direction: "from-page-script",
                        response: "confirm"
                    }, "*");
                    break;
                case "getConfirmationMessage":
                    result = recordedConfirmation;
                    recordedConfirmation = null;
                    try{
                        console.error("no");
                        window.postMessage({
                            direction: "from-page-script",
                            response: "confirm",
                            value: result
                        }, "*");
                    } catch (e) {
                        console.error(e);
                    }
                    break;

                case "setNextAlertResult":
                    nextAlertResult = event.data.target;
                    document.body.setAttribute("setAlert", true);
                    window.postMessage({
                        direction: "from-page-script",
                        response: "alert"
                    }, "*");
                    break;
                // Has been send to content scripts, do not need to require value again
                //case "getAlertMessage":
                    //let result1 = recordedAlert;
                    //recordedAlert = null;
                    //window.postMessage({
                        //direction: "from-page-script",
                        //response: "alert",
                        //value: result1
                    //}, "*");
                    //break;
            }
        }
    });
}