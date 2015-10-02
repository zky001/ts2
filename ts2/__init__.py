#
#   Copyright (C) 2008-2015 by Nicolas Piganeau
#   npi@m4x.org                                                           
#                                                                         
#   This program is free software; you can redistribute it and/or modify  
#   it under the terms of the GNU General Public License as published by  
#   the Free Software Foundation; either version 2 of the License, or     
#   (at your option) any later version.                                   
#                                                                         
#   This program is distributed in the hope that it will be useful,       
#   but WITHOUT ANY WARRANTY; without even the implied warranty of        
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#   GNU General Public License for more details.                          
#                                                                         
#   You should have received a copy of the GNU General Public License     
#   along with this program; if not, write to the                         
#   Free Software Foundation, Inc.,                                       
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             
#

###############################################################
### Please try and not include any imports here
### As this file may be laodes in any enviroment
### such as a packager, docs compile etc
###############################################################


__VERSION__ = "0.6.0"
__FILE_FORMAT__ = 0.6
__APP_SHORT__ = "TS2"
__APP_LONG__ = "Train Signalling Simulation"
__APP_DESCRIPTION__ = "A railway simulation game where you have to dispatch trains across an area and keep them on schedule"

__ORG_NAME__ = "TS2 team"
__ORG_CONTACT__ = "npiganeau"

__PROJECT_DOMAIN__ = "ts2.github.io"
__PROJECT_WWW__ = "http://ts2.github.io/"
__PROJECT_HOME__ = "https://github.com/ts2"


def get_info():
	"""ts2 info
	
	 :rtype: `dict`
	"""
	return dict(
		version = __VERSION__,
		app_short = __APP_SHORT__,
		app_long = __APP_LONG__,
		app_description = __APP_DESCRIPTION__,
		project_domain = __PROJECT_DOMAIN__,
		project_www = __PROJECT_WWW__,
		project_home = __PROJECT_HOME__
	)
