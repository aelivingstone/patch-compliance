(function(){var a="";document&&(document.body&&document.body.getAttribute)&&(a=document.body.getAttribute("data-aws-proxy-region"));window.AWSConsoleProxyRegion=window.__amznUtmPagePostfix=a;window.__amznUtmhnOverride="console.aws.amazon.com"})();(function(){window.goog=window.goog||{provide:function(){},require:function(){}};window.amzn=window.amzn||{};window.amzn.sm=window.amzn.sm||{}})();(function(){amzn.sm.components={};window.amzn.sm.components=angular.module("smComponents",[])})();(function(){amzn.sm.components.awsAlert={};amzn.sm.components.directive("awsAlert",["Alerts","$log",function(a,c){return{restrict:"E",scope:{alert:"="},templateUrl:"partials/components/alert.html",replace:!0,link:function(b){b.alert||c.error("Expected there to be an alert for alerts section: "+b.alert);b.closeAlert=function(b){a.removeAlert(b)}}}}])})();(function(){amzn.sm.components.blurToClass={};amzn.sm.components.directive("blurToClass",[function(){return function(a,c,b){var d=b.blurToClass||"blurred";c.find(":input").blur(function(){c.addClass(d)})}}])})();(function(){amzn.sm.components.checkAllBox={};amzn.sm.components.directive("checkAllBox",[function(){return function(a,c,b){function d(){var b=a.$eval(f),d=a.$eval(g),h=!1,m=!1;_.each(b,function(a){d[a[e]]?h=!0:m=!0});h&&m?c[0].indeterminate=!0:(c[0].indeterminate=!1,c.prop("checked",h))}var f=b.checkAllAll,g=b.checkAllSelected,e=b.checkAllKey;c.bind("change",function(){a.$apply(function(){var b=c.prop("checked"),d=a.$eval(f),h=a.$eval(g);_.each(d,function(a){h[a[e]]=b})})});a.$watch(f,d,!0);a.$watch(g,
d,!0)}}])})();(function(){amzn.sm.components.clickEater={};amzn.sm.components.directive("clickEater",function(){return{restrict:"A",link:function(a,c,b){c.bind("click",function(a){(!b.clickEater||"default"===b.clickEater||"both"===b.clickEater)&&a.preventDefault();("both"===b.clickEater||"propagation"===b.clickEater)&&a.stopPropagation()})}}})})();(function(){amzn.sm.components.clickOutside={};amzn.sm.components.directive("clickOutside",["DocumentClickedService",function(a){return{restrict:"A",link:function(c,b,d){var f=function(a){if(!d.clickOutsideEnabler||c.$apply(d.clickOutsideEnabler)){a:{for(a=a.target;a;){if(a===b[0]){a=!0;break a}a=a.parentNode}a=!1}a||c.$apply(d.clickOutside)}};a.addHandler(f);c.$on("$destroy",function(){a.removeHandler(f)})}}}])})();(function(){amzn.sm.components.conditionalFocus={};amzn.sm.components.directive("conditionalFocus",function(){return{restrict:"A",link:function(a,c,b){a.$eval(b.conditionalFocus)&&c.focus()}}})})();(function(){amzn.sm.components.intToDateTimeString={};amzn.sm.components.filter("intToDateTimeString",["LocalizationService",function(a){return function(c,b,d){if(!c)return"";d=d||1;b=b?a.localize(b):a.localize("time_format");return moment(c*d).format(b)}}])})();(function(){amzn.sm.components.localize={};amzn.sm.components.localizeSafe={};amzn.sm.components.filter("localize",["LocalizationService",function(a){return function(c,b,d){return a.localize(c,b,d)}}]);amzn.sm.components.filter("localizeSafe",["LocalizationService",function(a){return function(c,b,d){return a.localizeSafe(c,b,d)}}])})();(function(){amzn.sm.components.repeatDefinitionList={};amzn.sm.components.DefinitionTerm={};amzn.sm.components.directive("repeatDefinitionList",[function(){return{restrict:"A",scope:{values:"="},templateUrl:"partials/directives/repeat-definition-list.html"}}]);amzn.sm.components.DefinitionTerm=function(a,c){this.term=a;this.definition=c}})();(function(){amzn.sm.components.ReportingController={};amzn.sm.components.controller("amzn.sm.ReportingController",["$window","$rootScope","$timeout","HOME_CONTROLLER","OLD_FINISHED_METRIC_NAME",function(a,c,b,d,f){var g=function(b){return function(){var c=(new Date).getTime(),h=b.controller,e={reportingStart:a.clientReporting.reportingStart,routeFinished:c};a.performance&&a.performance.timing&&(e.timing=a.performance.timing,a.clientReporting.time("load:fetchToRoute:"+h,c-e.timing.fetchStart),a.clientReporting.time("load:requestRoute:"+
h,c-e.timing.requestStart),a.clientReporting.time("load:firstByte:"+h,e.timing.responseStart-e.timing.requestStart));a.clientReporting.time("load:loadFinished:"+h,c-a.clientReporting.reportingStart);h===d&&a.clientReporting.time(f,c-a.clientReporting.reportingStart);a.clientReporting.event("pageLoad",{url:a.location.href,referrer:a.document.referrer,timing:e,screen:{availWidth:a.screen.availWidth,availHeight:a.screen.availHeight},window:{width:a.innerWidth||a.document.clientWidth,height:a.innerHeight||
a.document.clientHeight},userAgent:a.navigator.userAgent,vendor:a.navigator.vendor,opera:a.opera});a.clientReporting.report()}},e=c.$on("$routeChangeSuccess",function(a,c){c.controller&&(b(g(c),10),e())});c.$on("$routeUpdate",function(){a.clientReporting.event("routeUpdate",{location:a.location.href})});c.$on("$routeChangeStart",function(){a.clientReporting.event("routeChangeStart",{location:a.location.href})})}])})();(function(){amzn.sm.components.resettable={};amzn.sm.components.directive("resettable",["$timeout",function(a){return{require:"form",link:function(c,b,d,f){f.resetValidation=function(){a(function(){f.$setPristine();b.find("[focus-on-reset]").focus();_.has(d,"submitToClass")&&b.removeClass(d.submitToClass||"submitted");b.find("[blur-to-class]").removeClass(function(){return $(this).attr("blur-to-class")||"blurred"})},1)}}}}])})();(function(){amzn.sm.components.simplePopover={};amzn.sm.components.directive("simplePopover",[function(){return{restrict:"A",templateUrl:"partials/components/simple-popover.html",scope:{popoverDirection:"@",popoverText:"@",popoverTitle:"@",showPopover:"="},link:function(a,c,b){a.$watch("showPopover",function(b){c.find(".popover").css("display",b&&(a.popoverText||a.popoverTitle)?"block":"none")});var d=a.$watch("popoverText",function(){var a=parseInt(b.popoverLeftOffset,10)||0,g=c.find(".popover"),
e=c.find(".popover-content");g.show();a=Math.floor(e.width()/2)+a;g.css("left","-"+a+"px");g.hide();d()})}}}])})();(function(){amzn.sm.components.stringPrefixFilter={};amzn.sm.components.filter("stringPrefix",[function(){return function(a,c){return c+a}}])})();(function(){amzn.sm.components.submitToClass={};amzn.sm.components.directive("submitToClass",[function(){return function(a,c,b){var d=b.submitToClass||"submitted";c.find("button:first").on("click",function(){c.addClass(d)});c.on("submit",function(){c.addClass(d)})}}])})();(function(){amzn.sm.components.TitleController={};amzn.sm.components.controller("TitleController",["$scope","$rootScope","LocalizationService","$injector","TITLE_DATA_PROVIDER",function(a,c,b,d,f){c.$on("$routeChangeSuccess",function(c,e){if(e&&e.$$route){var k=d.invoke(f);a.pagetitle=b.localize(e.$$route.title,k)}else a.pagetitle=b.localize("default_page_title")})}])})();(function(){amzn.sm.components.SelectToggle={};amzn.sm.components.SelectButton={};amzn.sm.components.ActionButton={};var a=function(a){return{restrict:"E",scope:{values:"=",selection:"=",disableMenu:"=",valueFilterExpr:"@"},templateUrl:a,replace:!0,link:function(a){a.filter=function(c){return a.$eval("value"+(a.valueFilterExpr||""),{value:c})};a.opened=!1;a.selectValue=function(c){a.selection=c;a.opened=!1};a.toggleOpen=function(){a.disableMenu||(a.opened=!a.opened)}}}};amzn.sm.components.directive("awsSelectToggle",
function(){return a("partials/components/select-toggle.html")});amzn.sm.components.directive("awsSelectButton",function(){return a("partials/components/select-button.html")});amzn.sm.components.directive("awsActionButton",["LocalizationService",function(a){return{restrict:"E",replace:!0,scope:{actions:"=",category:"@","class":"@",disableMenu:"=",onAction:"&"},templateUrl:"partials/components/action-button.html",link:function(b,d,f){d.addClass(b["class"]);b.label=_.isUndefined(f.label)?a.localize("aws_action_button_label"):
f.label;b.opened=!1;b.actionSelected=function(a){b.opened=!1;b.onAction({action:a,category:b.category})};b.toggleOpen=function(){b.disableMenu||(b.opened=!b.opened)}}}}])})();(function(){amzn.sm.constants={};window.amzn.sm.constants={ENTER_KEY:13}})();(function(){amzn.sm.components.onEnter={};amzn.sm.components.directive("onEnter",[function(){return function(a,c,b){c.bind("keyup",function(c){c.which===amzn.sm.constants.ENTER_KEY&&a.$apply(b.onEnter)})}}])})();(function(){amzn.sm.models={};window.amzn.sm.models=angular.module("smModels",[])})();(function(){amzn.sm.models.Alerts={};amzn.sm.models.factory("Alerts",["$log","$timeout","LocalizationService","$window","$rootScope",function(a,c,b,d,f){function g(a,b){return angular.isNumber(b)?c(function(){e.removeAlert(a)},b):void 0}var e={alerts:[]},k=[];f.$on("$routeChangeStart",function(){var a=_.chain(e.alerts).pluck("id").difference(k).value();_.each(a,e.removeAlert)});e.alert=function(a,h,f,n,p,l){f=f||"alert-error";h=h||{};p=p||"error_title";l&&k.push(a);l=_.find(e.alerts,function(b){return b.id===
a});_.isUndefined(l)?(d.scrollTo(0,0),e.alerts.push({id:a,text:b.localize(a,h),title:b.localize(p,h),data:h,level:f,delay:n,delayPromise:g(a,n)})):(l.delayPromise&&c.cancel(l.delayPromise),l.text=b.localize(a,h),l.data=h,l.level=f,l.delay=n,l.delayPromise&&(l.delayPromise=g(a,n)))};e.error=function(a,b,c,d){e.alert(a,b,"alert-error",c,"error_title",d)};e.info=function(a,b,c){e.alert(a,b,"alert-info",c,"info_title")};e.success=function(a,b,c){e.alert(a,b,"alert-success",c,"success_title")};e.removeAlert=
function(a){e.alerts=_.filter(e.alerts,function(b){return b.id!==a});k=_.without(k,a)};return e}])})();(function(){amzn.sm.components.AlertsController={};amzn.sm.components.controller("AlertsController",["$scope","Alerts",function(a,c){a.AlertsModel=c}])})();(function(){amzn.sm.services={};window.amzn.sm.services=angular.module("smServices",["ngSanitize"])})();(function(){amzn.sm.services.AutoRefresher={};amzn.sm.services.factory("AutoRefresher",["$timeout","$rootScope","Alerts",function(a,c,b){var d=1,f={},g=[],e=[],k=[];c.$on("$routeChangeStart",function(){_.each(g,function(b){a.cancel(b)});g=[];k=_.difference(k,e);e=[]});f.autoRefresh=function(c,f,m){function n(){var b=a(l,f);m||g.push(b)}var p=d;d+=1;m||e.push(p);var l;l=function(){var a=_.indexOf(k,p,!0);-1===a?window.credExpired||(!0===navigator.onLine?(b.removeAlert("no_internet_error"),c()):b.error("no_internet_error"),
n()):k.splice(a,1)};n();return p};f.cancel=function(a){_.isNumber(a)&&k.splice(_.sortedIndex(k,a),0,a)};return f}])})();(function(){amzn.sm.services.DocumentClickedService={};amzn.sm.services.provider("DocumentClickedService",function(){var a=[],c=!1,b={addHandler:function(b,c){a.push({fn:b,scope:c})},removeHandler:function(b){a=_.reject(a,function(a){return a.fn===b})}},d=function(b){c=!0;b.bind("click",function(b){_.each(a,function(a){a.fn.call(a.scope,b)})})};return{$get:["$document",function(a){c||d(a);return b}]}})})();(function(){amzn.sm.services.HttpHelper={};var a={message:"Internal Failure",code:"InternalFailure",type:"Receiver"};amzn.sm.services.factory("HttpHelper",["$window","$log","$http","$q","LocalizationService","PageUtil","RegionUtil","XsrfProtection","$timeout","REQUEST_ID_HEADER",function(c,b,d,f,g,e,k,q,h,m){var n={},p={message:g.localize("credential_warning_message"),code:"InternalFailure",type:"Receiver"},l=n.failureCallbackFactory=function(d,e,g,l){return function(k,m,s,r){l+=1;_.isFunction(s)&&
(s=s());s={data:k,status:m,responseHeaders:s,config:e,evaledConfig:r,tries:l};if(401===m)d.reject(p),window.credExpired=!0;else{if(3>l){if(k&&"InvalidXsrf"===k.code){d.resolve(q.refreshToken().then(function(){return n.httpFactory(e,g,l)},f.reject));c.clientReporting.info("xhrError:"+m,s);return}r="POST"!==e.method||e.idempost;if((!m||500<=m)&&r){d.resolve(h(function(){return n.httpFactory(e,g,l)},1E3*Math.random()*(Math.pow(2,l)-1)));c.clientReporting.info("xhrError:"+m,s);return}}0===m?c.clientReporting.info("xhrError:0",
s):c.clientReporting.error("xhrError:"+m,s);if(k)try{k=angular.fromJson(k)}catch(t){b.error("Couldn't parse error as JSON: "+k)}_.isObject(k)?d.reject(k):d.reject(a)}}},r=n.successCallbackFactory=function(a,b){return function(c){c?c.Error?a.reject(c.Error):b?a.resolve(c[b]):a.resolve(c):a.resolve()}};n.httpFactory=function(a,b,c){var e=f.defer(),h=Math.random().toString(36).substring(2)+"-"+Math.random().toString(36).substring(2);a.params=_.extend(a.params||{},{region:k.getCurrentRegion()});var g=
{};g[m]=h;a.headers=_.extend(a.headers||{},q.getHeaders(),g);d(a).success(r(e,b)).error(l(e,a,b,c||0));return e.promise};return n}])})();(function(){amzn.sm.services.LocalizationService={};amzn.sm.services.factory("LocalizationService",["$interpolate","$window","ReportingService","LOCALIZATION_SOURCE",function(a,c,b,d){function f(a,c,d){if(!a)return d||"";var f=e[a];if(_.isFunction(f))return f(c);if(!_.isUndefined(d))return d;b.assert("localization:invalidMessageId",{messageId:a})}function g(a){a&&(a=a.toLowerCase().replace(/[^a-z0-9]/ig,"_"));return a}var e={},k=c.amzn.sm.localized,q=c;if(!d)throw b.assert("localization:missingSource"),
Error("No localization source specified");_.each(d.split("."),function(a){if(!q[a])throw b.assert("localization:badSource",{source:d,failedStep:a}),Error("Unable to find localization source.");q=q[a]});_.each(k,function(b,c){e[c]=a(b)});_.each(q,function(b,c){e[c]=a(b)});return{localize:f,localizeSafe:function(a,b,c){return f(g(a),b,c)},cleanMessageId:g}}])})();(function(){amzn.sm.services.PageUtil={};amzn.sm.services.factory("PageUtil",["$window",function(a){return{refresh:function(){var c=a.location.search,b="#"+(a.location.href.split("#")[1]||""),c=c?c+"&":"?",b="state=hashArgs"+encodeURIComponent(b);a.location.replace(a.location.pathname+c+b)}}}])})();(function(){amzn.sm.services.RegionUtil={};amzn.sm.services.factory("RegionUtil",["$window",function(a){return{getCurrentRegion:function(){var c=a.location.search;if(!c)throw"No query parameters found.";c=/region=([a-zA-Z0-9\-]+)/.exec(c);if(!c)throw"No region found";return c[1]}}}])})();(function(){amzn.sm.services.ReportingService={};amzn.sm.services.service("ReportingService",["$window","$log",function(a,c){return{event:function(b,c){a.clientReporting.event(b,c)},time:function(b,c){a.clientReporting.time(b,c)},assert:function(b,d){a.clientReporting.error(b,d);c.error("Assertion failed:",b,d)},fault:function(b,c){a.clientReporting.error(b,c)},error:function(b,c){a.clientReporting.error(b,c)},info:function(b,c){a.clientReporting.error(b,c)}}}])})();(function(){amzn.sm.services.SettingsService={};amzn.sm.services.factory("SettingsService",["$q","$window",function(a,c){return{getSettings:function(b){_.isArray(b)&&(b=b.join("/"));var d=a.defer();try{d.resolve(angular.fromJson(c.localStorage.getItem(b)))}catch(f){d.reject({Error:{message:f.message}})}return d.promise},putSettings:function(b,d){if(!_.has(d,"settings"))throw"Data object must have settings key.";if(!_.has(d,"versionTag"))throw"Data object must have versionTag key.";_.isArray(b)&&(b=
b.join("/"));var f=a.defer();try{var g=c.localStorage.getItem(b);g&&(g=angular.fromJson(g));!g||g.versionTag===d.versionTag?(c.localStorage.setItem(b,angular.toJson({settings:d.settings,versionTag:d.versionTag+1})),f.resolve(d.versionTag+1)):f.reject({Error:{message:"Version mismatch",code:"VersionMismatch",type:"Sender"}})}catch(e){f.reject({Error:{message:e.message}})}return f.promise}}}])})();(function(){amzn.sm.services.XsrfProtection={};amzn.sm.services.service("XsrfProtection",["preload","$http","$timeout","$log","$window","$q","PageUtil","XSRF_ENDPOINT","XSRF_TOKEN_HEADER",function(a,c,b,d,f,g,e,k,q){function h(){function a(c){if(c&&401===c.status)deferred.reject(p),e.refresh();else{n+=1;f.clientReporting.error("xsrfError:refresh",c);var d=8<n?298E3:1E3*(Math.pow(2,n)-1);l=b(h,2E3+Math.random()*d);return g.reject(c)}}b.cancel(l);return c({method:"GET",url:k}).then(function(c){_.has(c.data,
"Error")?a(c.data):(n=0,r=c.data,l=b(h,m));return!0},a)}var m=432E5,n=0,p={message:"Internal Failure",code:"InternalFailure",type:"Receiver"};d={};var l,r;d.refreshToken=h;(a=a["xsrf-token"])?(a=angular.fromJson(a),a.Error?(f.clientReporting.fault("xsrfError:preload",a),h()):(r=a.token,moment.utc().isAfter(moment.utc(a.created).add(m,"milliseconds"))?(f.clientReporting.fault("expiredXsrf:preload",a),h()):l=b(h,m))):(f.clientReporting.fault("expiredXsrf:preload:empty"),h());d.getHeaders=function(){var a=
{};a[q]=r;return a};return d}])})();(function(){amzn.sm.localized={};amzn.sm.localized={default_page_title:"AWS Management Console",error_title:"Error",credential_warning_message:"Your credentials have expired. Refresh the page to sign in; however, unsaved changes will be lost.",no_internet_error:"Failed to receive response from server. Check your network connection and try again.",time_format:"YYYY-MM-DD HH:mm:ss UTCZZ",success_title:"Success",info_title:"Info",aws_action_button_label:"Actions",warn_title:"Warning"}})();(function(){amzn.sm.templates={};angular.module("smTemplates",[]).run(["$templateCache",function(a){a.put("partials/alerts-display.html",'<ul class="alert-display"> <li ng-repeat="alert in AlertsModel.alerts" ng-animate="\'alert\'"> <div><aws-alert alert="alert"></aws-alert></div> </li></ul>');a.put("partials/components/action-button.html",'<div class="dropdown inline-block" ng-class="{open: opened}" click-outside="toggleOpen()" click-outside-enabler="opened"> <button class="btn dropdown-toggle" ng-click="toggleOpen()" ng-disabled="disableMenu" data-actions>{{label}}</button> <ul class="dropdown-menu" data-actions-menu> <li ng-repeat="action in actions" ng-click="actionSelected(action.name)" data-action="{{action.display}}"><a href="">{{action.display | localize}}</a></li> </ul></div>');
a.put("partials/components/alert.html",'<div class="alert {{alert.level}} alert-icon"> <a class="close" ng-click=\'closeAlert(alert.id)\' href="#" click-eater>&times;</a> <h3>{{alert.title}}</h3> <p ng-bind="alert.text"></p></div>');a.put("partials/components/select-button.html",'<div class="dropdown inline-block" ng-class="{open: opened}" click-outside="toggleOpen()" click-outside-enabler="opened"> <button class="btn dropdown-toggle" ng-click="toggleOpen()" ng-disabled="disableMenu">{{filter(selection)}}</button> <ul class="dropdown-menu"> <li ng-repeat="value in values" ng-click="selectValue(value)"><a href="">{{filter(value)}}</a></li> </ul></div>');
a.put("partials/components/select-toggle.html",'<div class="dropdown inline-block" ng-class="{open: opened}" click-outside="toggleOpen()" click-outside-enabler="opened"> <button class="btn-link dropdown-toggle" ng-click="toggleOpen()">{{selection | localize:{}:value}}</button> <ul class="dropdown-menu"> <li ng-repeat="value in values" ng-click="selectValue(value)"><a href="">{{value | localize:{}:value}}</a></li> </ul></div>');a.put("partials/components/simple-popover.html",'<div ng-show="showPopover" class="popover {{popoverDirection || \'bottom\'}}"> <div class="arrow"></div> <h3 class="popover-title" ng-show="popoverTitle">{{popoverTitle}}</h3> <div class="popover-content">{{popoverText}}</div></div>');
a.put("partials/directives/repeat-definition-list.html",'<dt ng-repeat-start="value in values"><p ng-bind="value.term"></p></dt><dd ng-repeat-end><p ng-bind="value.definition"></p></dd>')}])})();