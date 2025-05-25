import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Stock Details")


def scrapper(stock_ticker: str) :
    
        
    stock_ticker = stock_ticker.replace('.NS', '')

    url = f"https://www.screener.in/company/{stock_ticker}/"

    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched the webpage")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    return soup


@mcp.tool()
def profits(stock_ticker: str) -> dict:
    
    soup = scrapper(stock_ticker)

    yearly_values = []
    quarter_values = []

    # Find the section with id "profit-loss"
    section = soup.find('section', id='profit-loss')

    if section:
        # Extract rows from this section
        rows = section.find_all('tr')

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'Net Profit' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                yearly_values = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row



          # Find the section with id "profit-loss"
    section = soup.find('section', id='quarters')

    if section:
        # Extract rows from this section
        rows = section.find_all('tr')

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'Net Profit' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                quarter_values = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row


    return {"Quarter" : quarter_values,
        "Yearly" : yearly_values}



@mcp.tool()
def shareholding(stock_ticker: str) -> dict:
    
    soup = scrapper(stock_ticker)


    Promoters = []
    DII = []
    FII = []
    Public = []

          # Find the section with id "profit-loss"
    section = soup.find('section', id='shareholding')

    if section:
        # Extract rows from this section
        rows = section.find_all('tr')

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'Promoters' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                Promoters = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'DIIs' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                DII = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'FIIs' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                FII = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row

        for row in rows:
            # Check if the row contains the text "Net Profit"
            if 'Public' in row.get_text():
                # Find all <td> elements in the row, skipping the first <td> which contains the button
                columns = row.find_all('td')[1:]
                Public = [col.get_text(strip=True) for col in columns]
                break  # Exit loop once we find the correct row

    return {"Promoters" : Promoters,
        "DII" : DII,
        "FII" : FII,
        "Public" : Public}


@mcp.tool()  
def company_details(stock_ticker: str) -> dict:
    
    soup = scrapper(stock_ticker)
    
    
    company_name = soup.find('h1', class_='margin-0 show-from-tablet-landscape').text.strip()
    current_price = soup.find('div', class_='font-size-18 strong line-height-14').find('span').text.strip()
    market_cap = soup.find('li', {'data-source': 'default'}).find('span', class_='number').text.strip()
    about_section = soup.find('div', class_='company-profile').find('div', class_='sub show-more-box about').text.strip()
    pe_value = soup.find('span', class_='name', string=lambda t: t and "Stock P/E" in t).find_next('span', class_='number').string
    roe = soup.find('span', class_='name', string=lambda t: t and "ROE" in t).find_next('span', class_='number').string
    roce = soup.find('span', class_='name', string=lambda t: t and "ROCE" in t).find_next('span', class_='number').string

    fundainfo = {
        "Company Name": company_name,
        "Current Price": current_price,
        "Market Cap": market_cap,
        "About": about_section,
        "PE" : pe_value,
        "ROE" : roe,
        "ROCE" : roce,}

   
    return fundainfo 


    


if __name__ == "__main__":
    mcp.run(transport='stdio')