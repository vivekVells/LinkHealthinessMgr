# LinkHealthinessMgr
input the website url -> extract all possible link -> verify whether those links are not ending up in some sort of error say 404 page not found

# version status
- selenium: pip install seleniuim==3.13.0 | selenium-3.13.0
- webdriver:
  - chrome: 2.4.0 | https://chromedriver.storage.googleapis.com/index.html?path=2.40/
  - Edge: Release 17134 | https://download.microsoft.com/download/F/8/A/F8AF50AB-3C3A-4BC4-8773-DC27B32988DD/MicrosoftWebDriver.exe
  - Firefox: v0.21.0 | make sure you download right version (32 or 64 bit based on your OS version) | https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-win64.zip
  
## Design
### Actual Aim:
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

### Additional capability:
- capability to receive links in .csv or .txt file and verify 404 error of each link