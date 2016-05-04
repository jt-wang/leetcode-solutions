class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return s

        if len(s) == 0:
            return s

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = []
        for i in range(len(s)):
            if s[i] in vowels:
                words.append(s[i])

        st = ""
        for i in range(len(s)):
            if s[i] in vowels:
                st += words.pop()
            else:
                st += s[i]

        return st

s = Solution()
print(s.reverseVowels("""
    Jingtao
Jane Jacobs’ 100th Birthday


trump


AllNewsVideosImagesMapsMoreSearch tools
About 367,000,000 results (0.58 seconds) 
Search Results
In the news
Image for the news result
Primary results: Donald Trump becomes presumptive nominee - CNNPolitics.com
CNN‎ - 7 hours ago
(CNN) Donald Trump is the presumptive Republican presidential nominee following a ...
Cruz unloads with epic takedown of 'pathological liar,' 'narcissist' Donald Trump - CNNPolitics.com
CNN‎ - 11 hours ago
Why Republican Voters Decided On Trump
FiveThirtyEight‎ - 4 hours ago
More news for trump
Make America Great Again! | Donald J Trump for President
https://www.donaldjtrump.com/
Donald J. Trump is the very definition of the American success story, continually setting the standards of excellence in business, real estate and entertainment.
Donald J. Trump (@realDonaldTrump) | Twitter
https://twitter.com/realDonaldTrump
55 mins ago - View on Twitter
I will be interviewed on @foxandfriends at 7:30 A.M. Enjoy!
58 mins ago - View on Twitter
I will be interviewed on @TODAYshow and Good Morning America at 7:00 A.M.
1 hour ago - View on Twitter
I will be interviewed on @Morning_Joe at 6:15 A.M. Enjoy!
1 hour ago - View on Twitter
I would rather run against Crooked Hillary Clinton than Bernie Sanders and that will happen because the books are cooked against Bernie!
2 hours ago - View on Twitter
What a great evening we had. So interesting that Sanders beat Crooked Hillary. The dysfunctional system is totally rigged against him!
Donald Trump - Wikipedia, the free encyclopedia
https://en.wikipedia.org/wiki/Donald_Trump
Wikipedia
Donald John Trump (born June 14, 1946) is an American businessman, politician, television personality, author, and the presumptive nominee of the ...
Donald Trump All but Clinches G.O.P. Race With Indiana Win; Ted ...
www.nytimes.com/2016/05/.../indiana-republican-democratic.htmlThe New York Times
10 hours ago - Donald J. Trump had a decisive win in the Indiana Republican primary, causing Ted Cruz to drop out, while Bernie Sanders won the ...
Trump accuses Cruz's father of helping JFK's assassin - POLITICO
www.politico.com/blogs/2016-gop...live.../trump-ted-cruz-father-222730
Politico
1 day ago - Donald Trump on Tuesday alleged that Ted Cruz's father was with John F. Kennedy's assassin shortly before he murdered the president, ...
Trump 41%, Clinton 39% - Rasmussen Reports™
www.rasmussenreports.com/public.../trump_41_clinton_39
Rasmussen Reports
2 days ago - But Trump edges slightly ahead if the stay-at-home option is removed. Trump also now does twice as well among Democrats as Clinton does ...
Trump: 'I'd have to think about' Cruz for Supreme Court | TheHill
thehill.com/.../278466-trump-id-have-to-think-about-cruz-for-supreme-court
The Hill
1 day ago - "There's a whole question of uniting and there's a whole question as to temperament," Trump continued. "He's certainly a smart guy, but there's ...
Why Donald Trump Will Always Be a “Short-Fingered ... - Vanity Fair
www.vanityfair.com/culture/2015/10/graydon-carter-donald-trump
The myriad vulgarities of Donald Trump—examples of which are retailed daily on Web sites and front pages these days—are not news to those of us who have ...
Why Do People Support Donald Trump? - The Atlantic
www.theatlantic.com/politics/archive/2015/08/donald-trump-voters/401408/
Last week, I asked Donald Trump supporters why they believe that the billionaire real-estate developer will treat them any better than the career ...
Donald Trump 2016: The One Weird Trait That Predicts Whether You ...
www.politico.com/magazine/story/2016/01/donald-trump-2016-authoritarian-213533
In fact, I've found a single statistically significant variable predicts whether a voter supports Trump—and it's not race, income or education ...
Donald J. Trump - Facebook
www.facebook.com › Places › New York, New York
Donald J. Trump, New York, NY. 7305190 likes · 1522720 talking about this. This is the official Facebook page for Donald J. Trump.
Trump
www.trump.com/
The Trump Organization
Trump Luxury Real Estate redefines what is meant by luxury living, built to be the absolute best in the world.
Donald Trump 2016 Presidential Election Candidate - NBC News
www.nbcnews.com/politics/2016-election/candidates/donald-trump
NBCNews.com
Visit Donald Trump's candidate page for the latest news and election polls about his 2016 campaign.
RealClearPolitics - Election 2016 - General Election: Trump vs. Clinton
www.realclearpolitics.com/.../general_election_trump_vs_clinton-54...
RealClearPolitics
RealClearPolitics - Election 2016 - General Election: Trump vs. Clinton.
Donald Trump's file | PolitiFact
www.politifact.com/personalities/donald-trump/
PolitiFact.com
Donald Trump has been a real estate developer, entrepreneur and host of the NBC reality show, "The Apprentice." He is running for the Republican presidential ...
Why Donald Trump Will Always Be a “Short-Fingered ... - Vanity Fair
www.vanityfair.com/culture/2015/10/graydon-carter-donald-trump
Vanity Fair
The myriad vulgarities of Donald Trump—examples of which are retailed daily on Web sites and front pages these days—are not news to those of us who have ...
Donald Trump - Bio, News, Photos - Washington Times
www.washingtontimes.com › Topics
The Washington Times
Latest news and commentary on Donald Trump including photos, videos, quotations, and a biography.
Luxury 5 Star Hotels | Trump Hotel Collection™ | 5 Star Boutique Hotels
https://www.trumphotelcollection.com/
Trump Hotel Collection™ is a hotel management company that manages luxury, 5 star hotel properties in New York City, Chicago, Las Vegas, Hawaii, Toronto ...
Las Vegas Hotels on the Strip | Trump International Hotel Las Vegas ...
https://www.trumphotelcollection.com/las-vegas/
Trump International Hotel Las Vegas is a luxury Las Vegas hotel overlooking the iconic Vegas Strip. This 64-story hotel is equipped with 1232 guest suites and ...
Downtown Chicago Hotels | Trump International Hotel & Tower ...
https://www.trumphotelcollection.com/chicago/
Trump International Hotel & Tower Chicago is a luxury hotel on Michigan Avenue. This Chicago boutique hotel offers river, lake and skyline views, spacious ...
Trump - YouTube
https://www.youtube.com/user/TrumpSC
Trump and Amaz face each other in glorious combat. The first to win 3 games wins the series and the loser has to wear the winners shirt for a whole week!
Searches related to trump
trump news
trump foreign policy speech
trump rally costa mesa
trump speech today
trump delegate
donald trump campaign finance
trump new york
trump campaign
1   
2
3
4
5
6
7
8
9
10
Next

Image result for trump
Donald Trump
American Politician
donaldjtrump.com
Donald John Trump is an American businessman, politician, television personality, author, and the presumptive nominee of the Republican Party for President of the United States in the 2016 election. Wikipedia
On the issues: Economy and jobs
“Raising the prevailing wage paid to H-1Bs will force companies to give these coveted entry-level jobs to the existing domestic pool of unemployed native and immigrant workers in the U.S., instead of flying in cheaper workers from overseas,” wrote Trump.
Donald Trump, zingers and all, emerges as sharp H-1B critic
Computerworld - Aug 16, 2015
More issues
Campaign finance
Jan 2015-Mar 2016
Source: OpenSecrets
$50.6M raised
4%
Super PACs and
other groups
96%
Campaign
donations*
*Includes self-financing
More campaign finance
Profiles

Twitter

Facebook

Instagram

YouTube
More about Donald Trump
Feedback
United States - From your Internet address - Use precise location - Learn more   
Help Send feedback Privacy Terms
"""))