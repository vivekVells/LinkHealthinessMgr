# LinkHealthinessMgr
- best place to check website url's reliability such that there is no errors such as 404, permission related, etc... for the web development team

## App Working Functionality Previews
### Preview 
![](https://github.com/vivekVells/LinkHealthinessMgr/blob/develop/demo/v1%20Link%20Health%20Verifier.gif)

## Objective
- To validate url's reliability such that there is no errors like 404 page not found, user permission related, etc...

## Project Working Demo
- [Video Link](https://drive.google.com/open?id=125LxihpVWTy23CaovFe-dKGzKHk4yuW1)
- [Working Demo - GIF](https://github.com/vivekVells/LinkHealthinessMgr/blob/develop/demo/v1%20Link%20Health%20Verifier.gif)
- [Working Demo - PDF]() - will be updated
- [Working Demo Files](https://github.com/vivekVells/LinkHealthinessMgr/tree/develop/demo)

## How site works now
### Case 1: verify link reliability by original url/host url/actual url
- say url "http://express-scripts.com/" -> then all links available in that website url's reliability have to be verified 
### Case 2: verify by file upload containing all possible links of the actual/original/host url
- say file containing all available urls of the host url 
  - upload such file to verify its reliability
  
## Technology involved:
- Django
- Python
- HTML | CSS | JavaScript
- Pivotal Cloud Foundry (in process to deploy the app in CF)

# Problem:
- During web development, there is a slight chance where web developer accidently inserts an invalid link to the production code that might end up in server side (5XX) or client side error code (4XX). 

# Aim:
- trying to solve the problem cited above by either
  - url: crawling throught the given url and testing each possible links available
  - file: testing all links available in the testurllinks.txt file 

# What's implemented:
- test by file: implemented
- test by URL: to be implemented in future

# How to test by file:
- Tutorial Link: (will be updated)
- upload a text file containing all possible links of your website. make sure each links are having carriage return (or) refer the format of the link placement below

https://www.express-scripts.com/
https://www.express-scripts.com/login
https://www.express-scripts.com/xyz

# Future plans:
- Will be implementing testing by url

contact: techengineervivek@gmail.com / vivekvellaiyappans@gmail.com

# version status (deprecated - have to recheck whether in need of selenium or not)
- selenium: pip install seleniuim==3.13.0 | selenium-3.13.0
- webdriver:
  - chrome: 2.4.0 | https://chromedriver.storage.googleapis.com/index.html?path=2.40/
  - Edge: Release 17134 | https://download.microsoft.com/download/F/8/A/F8AF50AB-3C3A-4BC4-8773-DC27B32988DD/MicrosoftWebDriver.exe
  - Firefox: v0.21.0 | make sure you download right version (32 or 64 bit based on your OS version) | https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-win64.zip
  
### Actual Aim: (depreceated)
- able to navigate to link
- able to verify whether that page link have 404 error or not
- Phase 1:
  - extract all links available from given webpage address
- Phase 2:
  - able to visit all extracted links and verify 404 error
- Phase 3:
  - loop through extracted links availble in root given webpage link
    - again loop through individual links extracted 
    - redo again until a state reached where all unique links were extracted such that extracted links starts with given root webpage link

  - example:
    - given root link: "www.root.com"
      - extracted links:
        - "www.root.com"
        - "www.root.com/page1"
        - "www.root.com/page2"
        - "www.root.com/page3"
      - looping through to get all unique sub-root links(go deep)
        - "www.root.com"
        - "www.root.com/page1"
        - "www.root.com/page1/page1asroot1"
        - "www.root.com/page1/page1asroot2"
        - "www.root.com/page2/page2asroot"
        - "www.root.com/page2/page2asroot/page1"
        - "www.root.com/page2/page2asroot/page2"
    - verify each unique links received at last to verify 404 error response

### Additional capability: (deprecated)
- capability to receive links in .csv or .txt file and verify 404 error of each link
