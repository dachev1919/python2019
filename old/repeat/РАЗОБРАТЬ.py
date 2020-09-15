cache = {} 
def get_page(url): 
	if cache.get(url): 
		return cache [url] #Возвращаются кэwированные данные 
	else: 
		data = get_data_from_server(url) 
		cache[url] = data #Данные сначала сохраняются в кэwе 
		return data