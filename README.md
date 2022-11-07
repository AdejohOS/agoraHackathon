# agoraHackathon
Dennis Ivy October Hackathon

Build an API that outputs a list of developer advocates with their details such as where they work, social links, bio, etc. Example API response bellow.

Project Requirements

Your API should at a minumum have these 2 endpoints

    /advocates
    /advocates/:username

Your API should be searchable (By user name), paginated.

Ex:

/advocates/?query=dennis

Your endpoints should provide links to user profile pictures and company logos.

User Data Ex:

// advocates/:id
{
 "advocates": [
     {
         "profile_pic": "https://pbs.twimg.com/profile_images/1489066537407365126/iViPGBVE_400x400.jpg",
         "username": "dennisivy11",
         "name": "Dennis Ivy",
         "bio": "YouTuber, contributor at @traversymedia , developer advocate @agoraio and online instructor.",
         "twitter": "https://twitter.com/dennisivy11",
     },
 ]
}

Submission Requirements

    Github link
    Live URL - API must be hosted
    Tag Agora on Twitter OR Linkedin



