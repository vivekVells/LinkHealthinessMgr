# LinkHealthinessMgr
input the website url -> extract all possible link -> verify whether those links are not ending up in some sort of error say 404 page not found

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