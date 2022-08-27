import nltk ,re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string 
from nltk.stem import WordNetLemmatizer
import numpy as np

nltk.download('wordnet')
nltk.download('stopwords')

emojis = "🍕🐵😑😢🐶️😜😎👊😁😍💖💵👎😀😂🔥😄🏻💥😋👏😱🚌ᴵ͞🌟😊😳😧🙀😐😕👍😮😃😘💩💯⛽🚄😖🏼🚲😟😈💪🙏🎯🌹😇💔😡👌🙄😠😉😤⛺🙂😏🍾🎉😞🏾😅😭👻😥😔😓🏽🎆🍻🍽🎶🌺🤔😪🐰🐇🐱🙆😨🙃💕💗💚🙈😴🏿🤗🇺🇸⤵🏆🎃😩👮💙🐾🐕😆🌠🐟💫💰💎🖐🙅⛲🍰🤐👆🙌💛🙁👀🙊🙉🚬🤓😵😒͝🆕👅👥👄🔄🔤👉👤👶👲🔛🎓😣⏺😌🤑🌏😯😲💞🚓🔔📚🏀👐💤🍇🏡❔⁉👠》🇹🇼🌸🌞🎲😛💋💀🎄💜🤢َِ🗑💃📣👿༼つ༽😰🤣🐝🎅🍺🎵🌎͟🤡🤥😬🤧🚀🤴😝💨🏈😺🌍⏏ệ🍔🐮🍁🍆🍑🌮🌯🤦🍀😫🤤🎼🕺🍸🥂🗽🎇🎊🆘🤠👩🖒🚪🇫🇷🇩🇪😷🇨🇦🌐📺🐋💘💓💐🌋🌄🌅👺🐷🚶🤘ͦ💸👂👃🎫🚢🚂🏃👽😙🎾👹⎌🏒⛸🏄🐀🚑🤷🤙🐒🐈ﷻ🦄🚗🐳👇⛷👋🦊🐽🎻🎹⛓🏹🍷🦆♾🎸🤕🤒⛑🎁🏝🦁🙋😶🔫👁💲🗯👑🚿💡😦🏐🇰🇵👾🐄🎈🔨🐎🤞🐸💟🎰🌝🛳🍭👣🏉💭🎥🐴👨🤳🦍🍩😗🏂👳🍗🕉🐲🍒🐑⏰💊🌤🍊🔹🤚🍎𝑷🐂💅💢💒🚴🖕🖤🥘📍👈➕🚫🎨🌑🐻🤖🎎😼🕷👼📉🍟🍦🌈🔭《🐊🐍🐦🐡💳ἱ🙇🥜🔼"

def remove_emojis(text):
    for emoji in emojis:
        text = text.replace(emoji, '')
    return text
    def removeUnwantedText(text):
    #remove urls
    if text == np.NaN or type(text) != str:
      text = " "
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+',' ',text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub('r<.*?>',' ', text)
    # html tags
    text = text.lower()
    text = text.split()
    text = " ".join([word for word in text if not word in stopwords])
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    return text
    
wordnet_lemmatizer = WordNetLemmatizer()
stopwords=stopwords.words('english')
stemmer=PorterStemmer()
# clean unwanted text like stopwords, @(Mention), https(url), #(Hashtag), punctuations
def removeUnwantedText(text):
    #remove urls
    if text == np.NaN or type(text) != str:
      text = " "
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+',' ',text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub('r<.*?>',' ', text)
    # html tags
    text = text.lower()
    text = text.split()
    text = " ".join([word for word in text if not word in stopwords])
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    return text
