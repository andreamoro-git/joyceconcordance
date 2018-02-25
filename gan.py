# place your google analytics code here
def addga() :  
    tempstr = "" 
    tempstr +=  "<!-- Global site tag (gtag.js) - Google Analytics --> \n"
    tempstr +=  "<script async src='https://www.googletagmanager.com/gtag/js?id='></script> \n"
    tempstr +=  "<script>\n"
    tempstr +=  "  window.dataLayer = window.dataLayer || []; \n"
    tempstr +=  "  function gtag(){dataLayer.push(arguments);} \n"
    tempstr +=  "  gtag('js', new Date()); \n"
    tempstr +=  "  gtag('config', ''); \n"
    tempstr +=  "  </script> \n"
    return tempstr;

if __name__ == "__main__":
    gastr = addga()
    