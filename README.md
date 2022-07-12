# **Disclaimer**
Unfortunately I couldn't find a fitting ml algorithm for this project. I tried implementing a normal generator script, but it works very badly and would require **a lot** of fine tuning. Unless I can find a good ML algorithm, this project is gonna stay archived. If you think you know a fitting ML algorithm, dm me after reading the [concept](https://github.com/Fornball/username-ai-helper/blob/main/README.md#concept).  

If you wish to try the app anyways, download the whole repo and run [main.py](https://github.com/Fornball/username-ai-helper/blob/main/cli/main.py) in the cli folder.
# username-ai-helper
Generates a username based on your preferences. Can optionally check availability of usernames online.
## TODO:
- [ ] Write non-ai personalization
- [ ] Add machine-learning
- [ ] CLI version
- [ ] Android port
- [ ] F-droid release
- [ ] Linux port
- [ ] Windows port
## Concept:
This project is supposed to generate a username based on userinput. 4 usernames would be displayed to the user, from which the user may choose one. That data is then fed to the ai, the selected username being treated as "desired" and the unselected once as "undesired". The ai then generates 20 new usernames based on the fed data. The first 20 usernames are randomly generated using the websites mentioned below.
## Credit:
Icons: https://materialdesignicons.com/  
Random usernames: https://boredhumans.com/superhero.php  
Username availability:(for reddit, twitch, steam, minecraft, fortnite, pinterest, vimeo): https://nordpass.com/username-generator/  
