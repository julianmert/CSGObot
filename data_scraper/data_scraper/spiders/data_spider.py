import scrapy
from scrapy.http import Request
import my_functions as mf

class DataSpiderSpider(scrapy.Spider):
    name = 'data_spider'
    allowed_domains = ['https://www.hltv.org/results']
    start_urls = ['http://www.hltv.org/results/']

    def parse(self, response):
        # empty dictionary to store games.
        # game_i = {"team_1":score_1, "team_2":score_2, "winner":"team_name", "loser": team_name}
        matches_played = {}

        # obtaining the teams and result
        winning_teams = response.xpath('//*[@class = "team team-won"]/text()').extract()
        losing_teams = response.xpath('//*[@class = "team "]/text()').extract()

        winner_scores = response.xpath('//*[@class = "score-won"]/text()').extract()
        loser_scores = response.xpath('//*[@class = "score-lost"]/text()').extract()

        # obtain match types
        match_type = response.xpath('//*[@class = "map-text"]/text()').extract()
        # starred games are special games (finals etc.)
        match_type_star = response.xpath('//*[@class = "map map-text"]/text()').extract()

        # populating matches_played with matches.
        for i in range(len(winning_teams)):
            match = "match_" + str(i)
            match_type = mf.calc_match_type(int(winner_scores[i]), int(loser_scores[i]))
            matches_played[match] = {"match_ID": match,
                                     "team_1": winning_teams[i],
                                     "team_2": losing_teams[i],
                                     "team_1_score": winner_scores[i],
                                     "team_2_score": loser_scores[i],
                                     "match_type":match_type}

            yield matches_played[match]

# obtaining match_links

# match link preprocessing. (can be done in a seperate helper function)
        #match_links_info = response.xpath('//div/a/@href').extract()
        #match_links = []
        #for match in match_links_info:
        #    if 'vs' in match:
        #        match_links.append(match)

        # game links seem to repeat. Ensure each link is unique.
