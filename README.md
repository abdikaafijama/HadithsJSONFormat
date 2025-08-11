# TheHadithsJSONFormat
A free collection of Hadiths taken from sunnah.com which have been organised book wise ready to use especially for Muslim devs so that they can easily use authentic Hadith data to build whatever they want, feel free to use these in anything, no credits or anything required, May Allah help us all. Includes Arabic texts, English translations, and gradings.

Collections included(For now, planning to expand Inshallah):

Sahih al-Bukhari

Sahih Muslim

Sunan Abu Dawud

Jami at-Tirmidhi

Sunan an-Nasa'i

Sunan Ibn Majah

Muwatta Malik

Riyad as-Salihin

Each json file is structured like this 
{
    "collection": "abudawud",
    "book": "1 Purification (Kitab Al-Taharah) كتاب الطهارة",
    "reference": "Reference : Sunan Abi Dawud 1 In-book reference : Book 1, Hadith 1 English translation : Book 1, Hadith 1",
    "grade": "Grade : Hasan Sahih (Al-Albani) حسن صحيح (الألباني) حكم :",
    "arabic": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مَسْلَمَةَ بْنِ قَعْنَبٍ الْقَعْنَبِيُّ، حَدَّثَنَا عَبْدُ الْعَزِيزِ، - يَعْنِي ابْنَ مُحَمَّدٍ - عَنْ مُحَمَّدٍ، - يَعْنِي ابْنَ عَمْرٍو - عَنْ أَبِي سَلَمَةَ، عَنِ الْمُغِيرَةِ بْنِ شُعْبَةَ، أَنَّ النَّبِيَّ صلى الله عليه وسلم كَانَ إِذَا ذَهَبَ الْمَذْهَبَ أَبْعَدَ .",
    "english": "Narrated Mughirah ibn Shu'bah: When the Prophet (صلى الله عليه وسلم) went (outside) to relieve himself, he went to a far-off place.",
    "id": 1
  },
  {
    "collection": "abudawud",
    "book": "1 Purification (Kitab Al-Taharah) كتاب الطهارة",
    "reference": "Reference : Sunan Abi Dawud 2 In-book reference : Book 1, Hadith 2 English translation : Book 1, Hadith 2",
    "grade": "Grade : Sahih (Al-Albani) صحيح (الألباني) حكم :",
    "arabic": "حَدَّثَنَا مُسَدَّدُ بْنُ مُسَرْهَدٍ، حَدَّثَنَا عِيسَى بْنُ يُونُسَ، أَخْبَرَنَا إِسْمَاعِيلُ بْنُ عَبْدِ الْمَلِكِ، عَنْ أَبِي الزُّبَيْرِ، عَنْ جَابِرِ بْنِ عَبْدِ اللَّهِ، أَنَّ النَّبِيَّ صلى الله عليه وسلم كَانَ إِذَا أَرَادَ الْبَرَازَ انْطَلَقَ حَتَّى لاَ يَرَاهُ أَحَدٌ .",
    "english": "Narrated Jabir ibn Abdullah: When the Prophet (صلى الله عليه وسلم) felt the need of relieving himself, he went far off where no one could see him.",
    "id": 2
  },
  
  Also, the id's reset per sub topic of each book. e.g the ones given above are from abudawud --> Kitab Al Taharah so kitab al taharah has its own id's
  starting from 1 now if u go to abudawud --> kitab as salat it will have its own ids starting from 1
  
  A short test program has also been included called hadith_viewer.py to run it just open the "Sunnah" folder in terminal and type "python hadith_viewer.py" 
  and press enter. U can check out the code to see an example of how to fetch and stuff Inshallah. that program isnt really important, just a 
  demonstration
  Hope this short documentation was enough Inshallah.
  
