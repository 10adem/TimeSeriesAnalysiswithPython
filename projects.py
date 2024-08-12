#!/usr/bin/env python
# coding: utf-8

# # Python ile Zaman Serisi Analizi

# * Bir zaman aralığında kaydedilmiş bir veri kümesini analiz ettiğinizde, Zaman Serisi Analizi yapıyorsunuz demektir. Bir zaman serisi verisinin zaman aralığı haftalık, aylık, günlük ve hatta saatlik zaman aralıkları olabilir, ancak verilerinizi analiz etme süreci çoğu problemde aynı kalacaktır.
# * Zaman serisi analizi, bir zaman serisi veri setindeki örüntüleri analiz etmek ve bulmak anlamına gelir.
# * Hisse senedi fiyat verileri, aylık satış verileri, günlük yağış verileri, saatlik web sitesi trafiği verileri, bir veri bilimcisi olarak iş sorunlarını çözmek için alacağınız zaman serisi verilerinin bazı örnekleridir.
# * Bu projede, Python kullanarak Zaman Serisi Analizi'ni Türkiye Garanti Bankası (GARAN) üzerinden size anlatacağım.
# * Bu projenin sonunda, Python kullanarak Zaman Serisi Analizi yapmayı öğreneceksiniz. Burada Python'daki plotly kütüphanesini kullanacağım çünkü daha az kod ve etkileşimli sonuçlar nedeniyle plotly ile verileri analiz etmek kolaydır. Zaman serisi analizi için bir kod editörü veya VS Code veya PyCharm gibi bir IDE kullanmak yerine bir Jupyter Notebook veya Google Colaboratory kullanmanızı tavsiye ediyorum.

# In[21]:


get_ipython().system('pip install yfinance')


# In[9]:


import pandas as pd
import yfinance as yf
import datetime
import warnings
warnings.filterwarnings("ignore")

from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days = 720)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('GARAN.IS', start = start_date, end = end_date, progress = False)

data.head()


# Yukarıdaki kodda, en son hisse senedi fiyat verilerini çıkarmak için yfinance API'sini kullandım. Şimdi Türkiye Garanti Bankası'nın hisse senedi fiyatlarındaki eğilimleri görmek için bir çizgi grafiği görselleştirelim:

# In[11]:


import plotly.express as px
figure = px.line(data, 
                 x = data.index, 
                 y = "Close",
                 title = "Zaman Serisi Analizi (Çizgi Grafiği - GARAN)")
figure.show()


# * Çizgi grafiği, Zaman serisi analizi üzerinde çalışırken en iyi görselleştirme araçlarından biridir. Yukarıdaki kodda, Türkiye Garanti Bankası'nın kapanış fiyatlarındaki eğilimleri görselleştiriyorum. İmleci çizginin üzerine getirirseniz, imlecinizin üzerinde olduğu veri noktasının tam tarihindeki kapanış fiyatını göreceksiniz.
# 
# * Şimdi Türkiye Garanti Bankası'nın açılış, yüksek, düşük ve kapanış fiyatlarındaki trendleri görmek için bir mum grafiği görselleştirelim:

# In[13]:


import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x = data.index,
                                        open = data["Open"], 
                                        high = data["High"],
                                        low = data["Low"], 
                                        close = data["Close"])])
figure.update_layout(title = "Zaman Serisi Analizi (Mum Grafiği - GARAN)", xaxis_rangeslider_visible = False)
figure.show()


# * Bir mum çubuğu grafiği, bir finansal enstrümanın zaman serisi analizinde her zaman yardımcı olur. İmleci yukarıdaki mum çubuğu grafiğinde herhangi bir noktaya getirirseniz, imlecinizin bulunduğu tarihte Türkiye Garanti Bankası'nın tüm fiyatlarını (açılış, yüksek, düşük ve kapanış) görürsünüz. Bu grafikteki kırmızı çizgiler fiyatlardaki düşüşü, yeşil çizgiler ise fiyatlardaki artışı göstermektedir.
# 
# * Şimdi, dönem boyunca kapanış fiyatlarının eğilimlerini görselleştirmek için bir çubuk grafiği görselleştirelim:

# In[15]:


figure = px.bar(data,
                x = data.index,
                y = "Close",
                title = "Zaman Serisi Analizi (Çubuk Grafik - GARAN)")
figure.show()


# * Yukarıdaki çubuk grafik, uzun vadeli senaryoda hisse senedi fiyatlarındaki artışı göstermektedir. Çizgi grafiği ve mum grafiği size fiyatın artışını ve azalışını gösterir, ancak uzun vadede fiyat artışını ve azalışını görmek istiyorsanız, her zaman bir çubuk grafiği tercih etmelisiniz.
# 
# * Belirli iki tarih arasındaki hisse senedi fiyatlarını analiz etmek istiyorsanız, bunu nasıl yapabileceğinizi aşağıda bulabilirsiniz:

# In[17]:


figure = px.line(data, x = data.index,
                 y = "Close",
                 range_x = ['2023-01-01','2024-08-10'],
                 title = "Zaman Serisi Analizi (Özel Tarih Aralığı - GARAN)")
figure.show()


# Bir zaman serisi verisini analiz etmenin en iyi yollarından biri, çıktı görselleştirmesinin kendisinde zaman aralığını manuel olarak seçebileceğiniz etkileşimli bir görselleştirme oluşturmaktır. Bunu yapmanın bir yolu, görselleştirmenizin altına bir kaydırıcı ve görselleştirmenizin üzerine zaman aralıklarını kontrol etmek için düğmeler eklemektir. Aşağıda, çıktının kendisinde zaman aralıklarını seçebileceğiniz etkileşimli bir mum çubuğu grafiğini nasıl oluşturabileceğinizi göstereceğim:

# In[19]:


figure = go.Figure(data = [go.Candlestick(x = data.index,
                                          open = data["Open"],
                                          high = data["High"],
                                          low = data["Low"],
                                          close = data["Close"])])
figure.update_layout(title = "Zaman Serisi Analizi (Düğmeler ve Kaydırıcı ile Mum Çubuğu Grafiği - GARAN)")

figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()


# İşte Python kullanarak zaman serisi analizini bu şekilde gerçekleştiriyoruz.

# ### Özet

# * Umarım artık Python kullanarak Zaman Serisi Analizinin nasıl yapılacağını ve Zaman Serisi Analizi için kullanabileceğiniz tüm görselleştirmeleri anlamışsınızdır aynı zamanda görselleştirmelerini yaptığımız Türkiye Garanti Bankası (GARAN) hissesini analiz edebilmişsinizdir.
# * Zaman serisi veri kümesi, belirli bir zaman aralığında toplanan bir dizi veridir.
# * Zaman serisi analizi, bir zaman serisi veri setindeki kalıpları analiz etmek ve bulmak anlamına gelir.
# * Bir zaman serisi verisinin zaman aralığı haftalık, aylık, günlük ve hatta saatlik zaman aralıkları olabilir.
# * Umarım Python kullanarak Zaman Serisi Analizi hakkındaki bu projeyi beğenmişsinizdir. 
