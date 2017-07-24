# -*- coding: utf-8 -*-

'''
    Poseidon Add-on
    Copyright (C) 2016 Poseidon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt


sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.jpg', 'DefaultTVShows.jpg')
        self.addDirectoryItem('Top Movies', 'playlistNavigator', 'top.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem('Playlists', 'customNavigator', 'playlist.jpg', 'DefaultMovies.jpg')

        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.jpg', 'DefaultVideoPlaylists.jpg')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.jpg', 'DefaultVideoPlaylists.jpg')

        self.addDirectoryItem(32008, 'toolNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.jpg', 'DefaultFolder.jpg')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.jpg', 'DefaultFolder.jpg')

        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'genres.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem(32012, 'movieYears', 'years.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem('Actor', 'moviePersons', 'actor.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.jpg', 'DefaultRecentlyAddedMovies.jpg')
        self.addDirectoryItem('Great Directors', 'spikeNavigator', 'director.jpg', 'DefaultMovies.jpg')
		
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.jpg', 'DefaultVideoPlaylists.jpg')

            self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'DefaultMovies.jpg')
            self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'DefaultMovies.jpg')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.jpg', 'DefaultMovies.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.jpg', 'DefaultMovies.jpg', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.jpg', 'DefaultMovies.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.jpg', 'DefaultMovies.jpg', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.jpg', 'DefaultMovies.jpg', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.jpg', 'DefaultMovies.jpg', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.jpg', 'DefaultMovies.jpg', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.jpg', 'DefaultMovies.jpg', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'mymovies.jpg', 'DefaultMovies.jpg')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.jpg', 'DefaultMovies.jpg')
            self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'DefaultMovies.jpg')
            self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'DefaultMovies.jpg')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'genres.jpg', 'DefaultTVShows.jpg')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.jpg', 'DefaultTVShows.jpg')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.jpg', 'DefaultTVShows.jpg')
        self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.jpg', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.jpg', 'DefaultVideoPlaylists.jpg')

            self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'DefaultTVShows.jpg')
            self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'DefaultTVShows.jpg')

        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.jpg', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.jpg', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.jpg', 'DefaultTVShows.jpg')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.jpg', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.jpg', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.jpg', 'DefaultTVShows.jpg')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.jpg', 'DefaultTVShows.jpg')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.jpg', 'DefaultTVShows.jpg')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'imdb.jpg', 'DefaultMovies.jpg', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.jpg', 'DefaultTVShows.jpg', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.jpg', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.jpg', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'mytvshows.jpg', 'DefaultTVShows.jpg')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'mytvshows.jpg', 'DefaultTVShows.jpg')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.jpg', 'DefaultTVShows.jpg')
            self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'DefaultTVShows.jpg')
            self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'DefaultTVShows.jpg')

        self.endDirectory()

		
    def custom(self, lite=False):		
	
        self.addDirectoryItem('Anime', 'movies&url=anime', 'anime.jpg', 'playlist.jpg')
        self.addDirectoryItem('Avant Garde', 'movies&url=avant', 'avant.jpg', 'playlist.jpg')
        self.addDirectoryItem('Based On A True Story', 'movies&url=true', 'true.jpg', 'playlist.jpg')
        self.addDirectoryItem('Biker', 'movies&url=biker', 'biker.jpg', 'playlist.jpg')
        self.addDirectoryItem('B Movies', 'movies&url=bmovie', 'bmovie.jpg', 'playlist.jpg')
        self.addDirectoryItem('Breaking The Fourth Wall', 'movies&url=breaking', 'breaking.jpg', 'playlist.jpg')
        self.addDirectoryItem('Business', 'movies&url=business', 'business.jpg', 'playlist.jpg')
        self.addDirectoryItem('Capers', 'movies&url=caper', 'caper.jpg', 'playlist.jpg')
        self.addDirectoryItem('Car Chases', 'movies&url=car', 'chase.jpg', 'playlist.jpg')
        self.addDirectoryItem('Character Study', 'movies&url=char', 'character.jpg', 'playlist.jpg')
        self.addDirectoryItem('Chick Flix', 'movies&url=chick', 'chick.jpg', 'playlist.jpg')
        self.addDirectoryItem('Coming to Age', 'movies&url=coming', 'coming.jpg', 'playlist.jpg')
        self.addDirectoryItem('Competition', 'movies&url=competition', 'comps.jpg', 'playlist.jpg')
        self.addDirectoryItem('Cult', 'movies&url=cult', 'cult.jpg', 'playlist.jpg')
        self.addDirectoryItem('Cyberpunk', 'movies&url=cyber', 'cyber.jpg', 'playlist.jpg')
        self.addDirectoryItem('Drug Addiction', 'movies&url=drugs', 'drug.jpg', 'playlist.jpg')
        self.addDirectoryItem('Dystopia', 'movies&url=dystopia', 'dystopia.jpg', 'playlist.jpg')
        self.addDirectoryItem('Epic', 'movies&url=epic', 'epic.jpg', 'playlist.jpg')
        self.addDirectoryItem('Espionage', 'movies&url=espionage', 'espionage.jpg', 'playlist.jpg')
        self.addDirectoryItem('Experimental', 'movies&url=expiremental', 'experimental.jpg', 'playlist.jpg')
        self.addDirectoryItem('Existential', 'movies&url=Existential', 'exis.jpg', 'playlist.jpg')
        self.addDirectoryItem('Fairy Tale', 'movies&url=fairytale', 'fairytale.jpg', 'playlist.jpg')
        self.addDirectoryItem('Farce', 'movies&url=farce', 'farce.jpg', 'playlist.jpg')
        self.addDirectoryItem('Femme Fatale', 'movies&url=femme', 'femme.jpg', 'playlist.jpg')
        self.addDirectoryItem('Futuristic', 'movies&url=futuristic', 'futuristic.jpg', 'playlist.jpg')
        self.addDirectoryItem('Heist', 'movies&url=heist', 'heist.jpg', 'playlist.jpg')
        self.addDirectoryItem('High School', 'movies&url=highschool', 'highschool.jpg', 'playlist.jpg')
        self.addDirectoryItem('Horror Movie Remakes', 'movies&url=remakes', 'horror.jpg', 'playlist.jpg')
        self.addDirectoryItem('James Bond', 'movies&url=bond', 'bond.jpg', 'playlist.jpg')
        self.addDirectoryItem('Kidnapping', 'movies&url=kidnapped', 'kidnapped.jpg', 'playlist.jpg')
        self.addDirectoryItem('Kung Fu', 'movies&url=kungfu', 'kungfu.jpg', 'playlist.jpg')
        self.addDirectoryItem('Monster', 'movies&url=monster', 'monster.jpg', 'playlist.jpg')
        self.addDirectoryItem('Movie Box Sets', 'movies&url=box', 'boxsets.jpg', 'playlist.jpg')
        self.addDirectoryItem('Movie Loners', 'movies&url=loners', 'loner.jpg', 'playlist.jpg')
        self.addDirectoryItem('Movies & Racism', 'movies&url=racist', 'race.jpg', 'playlist.jpg')
        self.addDirectoryItem('Neo Noir', 'movies&url=neo', 'neo.jpg', 'playlist.jpg')
        self.addDirectoryItem('Parenthood', 'movies&url=parenthood', 'parenthood.jpg', 'playlist.jpg')
        self.addDirectoryItem('Parody', 'movies&url=parody', 'parody.jpg', 'playlist.jpg')
        self.addDirectoryItem('Post Apocalypse', 'movies&url=apocalypse', 'apocalypse.jpg', 'playlist.jpg')
        self.addDirectoryItem('Private Eye', 'movies&url=private', 'dick.jpg', 'playlist.jpg')
        self.addDirectoryItem('Remakes', 'movies&url=remake', 'remake.jpg', 'playlist.jpg')
        self.addDirectoryItem('Road Movies', 'movies&url=road', 'road.jpg', 'playlist.jpg')
        self.addDirectoryItem('Robots', 'movies&url=robot', 'robot.jpg', 'playlist.jpg')
        self.addDirectoryItem('Satire', 'movies&url=satire', 'satire.jpg', 'playlist.jpg')
        self.addDirectoryItem('Schizophrenia', 'movies&url=schiz', 'schiz.jpg', 'playlist.jpg')
        self.addDirectoryItem('Serial Killers', 'movies&url=serial', 'serial.jpg', 'playlist.jpg')
        self.addDirectoryItem('Slasher', 'movies&url=slasher', 'slasher.jpg', 'playlist.jpg')
        self.addDirectoryItem('Sleeper Hits', 'movies&url=sleeper', 'sleeper.jpg', 'playlist.jpg')
        self.addDirectoryItem('Spiritual', 'movies&url=spiritual', 'spiritual.jpg', 'playlist.jpg')
        self.addDirectoryItem('Spoofs', 'movies&url=spoof', 'spoof.jpg', 'playlist.jpg')
        self.addDirectoryItem('Star Wars', 'movies&url=star', 'starwars.jpg', 'playlist.jpg')
        self.addDirectoryItem('Steampunk', 'movies&url=steampunk', 'steampunk.jpg', 'playlist.jpg')
        self.addDirectoryItem('Superheros', 'movies&url=superhero', 'superhero.jpg', 'playlist.jpg')
        self.addDirectoryItem('Supernatural', 'movies&url=supernatural', 'supernatural.jpg', 'playlist.jpg')
        self.addDirectoryItem('Tech Noir', 'movies&url=tech', 'tech.jpg', 'playlist.jpg')
        self.addDirectoryItem('Time Travel', 'movies&url=time', 'time.jpg', 'playlist.jpg')
        self.addDirectoryItem('Vampires', 'movies&url=vampire', 'vampire.jpg', 'playlist.jpg')
        self.addDirectoryItem('Virtual Reality', 'movies&url=vr', 'vr.jpg', 'playlist.jpg')
        self.addDirectoryItem('Wilhelm Scream', 'movies&url=wilhelm', 'wilhelm.jpg', 'playlist.jpg')
        self.addDirectoryItem('Zombies', 'movies&url=zombie', 'zombie.jpg', 'playlist.jpg')

        self.endDirectory()		


    def playlist(self, lite=False):		
	
        self.addDirectoryItem('IMDB Top 1000', 'movies&url=thousand', 'imdb.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Documentaries 00-17', 'movies&url=docs', 'docs.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Action Movies 00-17', 'movies&url=action', 'action.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Animated 00-17', 'movies&url=animated', 'animated.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Gangster Movies', 'movies&url=gangster', 'gangster.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Horror Movies 00-17', 'movies&url=horror', 'horror.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Action Movies 60-99', 'movies&url=action2', 'action.jpg', 'playlist.jpg')
        self.addDirectoryItem('Greatest Horror Films of All Time', 'movies&url=horror2', 'horror.jpg', 'playlist.jpg')
        self.addDirectoryItem('Greatest Sci-Fi Films of All Time', 'movies&url=scifi', 'scifi.jpg', 'playlist.jpg')
        self.addDirectoryItem('Greatest Westerns of All Time', 'movies&url=western', 'western.jpg', 'playlist.jpg')
        self.addDirectoryItem('Top Cop Movies', 'movies&url=cop', 'cop.jpg', 'playlist.jpg')
        self.addDirectoryItem('Greatest War Movies', 'movies&url=war', 'war.jpg', 'playlist.jpg')
        self.addDirectoryItem('Great Movies Directed By Women', 'movies&url=women', 'women.jpg', 'playlist.jpg')
        self.addDirectoryItem('Greatest Political Movies', 'movies&url=political', 'political.jpg', 'playlist.jpg')
        self.addDirectoryItem('The Most Romantic Movies', 'movies&url=romance', 'romance.jpg', 'playlist.jpg')

        self.endDirectory()		
    def spike(self, lite=False):		
	
        self.addDirectoryItem('Spike Lee', 'movies&url=spike', 'spike.jpg', 'playlist.jpg')
        self.addDirectoryItem('Alfred Hitchcock', 'movies&url=alfred', 'alfred.jpg', 'playlist.jpg')
        self.addDirectoryItem('Clint Eastwood', 'movies&url=clint', 'clint.jpg', 'playlist.jpg')
        self.addDirectoryItem('Steven Spielberg', 'movies&url=steven', 'steven.jpg', 'playlist.jpg')
        self.addDirectoryItem('James Cameron', 'movies&url=james', 'james.jpg', 'playlist.jpg')
        self.addDirectoryItem('Quentin Tarantino', 'movies&url=quentin', 'quentin.jpg', 'playlist.jpg')
        self.addDirectoryItem('Mel Gibson', 'movies&url=mel', 'mel.jpg', 'playlist.jpg')
        self.addDirectoryItem('Ben Affleck', 'movies&url=ben', 'ben.jpg', 'playlist.jpg')
        self.addDirectoryItem('Martin Scorsese', 'movies&url=martin', 'martin.jpg', 'playlist.jpg')	

		
        self.endDirectory()		
		
    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32050, 'clearSources', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32052, 'clearCache', 'tools.jpg', 'DefaultAddonProgram.jpg')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.jpg')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.jpg', 'DefaultMovies.jpg', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.jpg', 'DefaultTVShows.jpg', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.jpg', 'DefaultMovies.jpg')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.jpg')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.jpg')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.jpg')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.jpg', 'DefaultMovies.jpg', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.jpg', 'DefaultTVShows.jpg', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem(32002, 'tvSearch', 'search.jpg', 'DefaultTVShows.jpg')
        self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'DefaultMovies.jpg')
        self.addDirectoryItem('TV Actor Search', 'tvPerson', 'actorsearch.jpg', 'DefaultTVShows.jpg')

        self.endDirectory()


    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()




    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


