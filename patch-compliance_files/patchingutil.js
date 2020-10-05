/**
* @file Page script that runs on pages that qualify /sso/login requests.
* Checks if the page has an overriden XHR, if so, we refuse to apply our XHR patch.
* The page script also provides configurations for OpenId script and the hook method(s).
* @author Sabarish Raghu <sbrg@amazon.com>
*/

var event = new CustomEvent("FromPageScript", {detail:{shouldPatch: shouldPatch()}});
window.dispatchEvent(event);

/**
* Function that check if XMLHttpRequest monkey patched already.
* @return true if already patched. false if not already patched.
*/
function shouldPatch()
{
	var shouldPatch = false;
	try
	{
		if(window.Amazon.IDP.config == null)
		{
			shouldPatch = true;
		}
	}
	catch(e)
	{
		shouldPatch = true;
	}
	return shouldPatch;
}

// If the OpenId script patched is compatible with this config,
// it picks up this function in place of default implementation
// of openEnterpriseAccessAuthWindowHandler
window.Amazon = window.Amazon || {};
window.Amazon.IDP = window.Amazon.IDP || {};
window.Amazon.IDP.config = window.Amazon.IDP.config || {};
window.Amazon.IDP.config.openEnterpriseAccessAuthWindowHandler = openEnterpriseAccessAuthWindowHandler;


/**
* Function that hook's plugin's implementation of auth window.
* Relays the token fetching error response to background script.
* @param midwayAuthResponse : Responsetext from midway for IDP token fetch.
*/
function openEnterpriseAccessAuthWindowHandler(midwayAuthResponse)
{
	midwayAuthResponse.action="create";
	var event = new CustomEvent("FromPageScript", {detail: midwayAuthResponse});
	window.dispatchEvent(event);
}
