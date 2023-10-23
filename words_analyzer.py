#Lyrics analyzer / words analyzer

#Splitting Words

text = """ 
.. In the past decade, the Internet and social media (SM) have become indispensable components of daily life (Youssef & El-Beltagy, 2018), because they represent a notable source of massive amounts of newly streamed data (Najadat, Al-Abdi & Sayaheen, 2018;Youssef & El-Beltagy, 2018); they allow people, businesses, and organizations to readily share information (Abainia, 2019;Younes, Souissi, Achour & Ferchichi, 2020), thoughts, and views (Alsayat & Elmitwally, 2020). Currently, more than two billion individuals use SM to chat, explore, and share their thoughts online (Youssef & El-Beltagy, 2018). ...
... Arabic has numerous characteristics and contains many different dialects (Abdelli et al., 2019), with more than 22 major dialects being commonly used (Abdelli et al., 2019). MSA is used in formal written communications; however, this is dramatically different from the colloquial DA used in daily speech (Alahmary et al., 2019) in terms of phonology, morphology, vocabulary, grammar, syntax, and all other linguistic features (Abainia, 2019) [even its use in everyday spoken communications ]. DA influences the syntax of MSA (Abdul-Mageed, 2019), with different words expressing the same opinion (Al-Moslmi et al., 2018) or different meanings for the same word (Alahmary et al., 2019); however, certain dialects require multiple words to express similar meanings in MSA and can even feature morphological patterns and function words (usually stop words) that do not exist therein (Alnawas & Arici, 2019). ...
... These regional dialects differ remarkably from one country to another, or even between regions or communities within the same country (Farha & Magdy, 2019). Each group of colloquial DA can be considered a separate language in its own right (Al-Twairesh et al., 2018), with its own grammatical rules and vocabulary (Abainia, 2019). DA is more problematic than MSA because of the absence of standard orthographies (Al-Twairesh et al., 2017). ...
"""


print((text.split()))

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)







