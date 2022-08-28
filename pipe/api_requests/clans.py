class Clan:
    clans = []
    
    def __init__(self, clantag: str):
        """Initialize new instance of a Clan.
        
        Args:
            clantag (str): Clan tag assigned by Supercell; required input for
                clan api requests
        
        """
        self.clantag = clantag
        self.members = []
        self.clans.append(self)

    def convert_to_url(cls):
        """Convert clan tag to the url format used to make api requests.
        
        Returns:
            url (str): Url to make api requests for class instance.
            
        """
        clantag = cls.clantag
        first_char = clantag[0]
        if first_char == '#':
            clantag = '%23' + clantag[1:]
        url = f'https://api.clashofclans.com/v1/clans/{clantag}/members'
        return url