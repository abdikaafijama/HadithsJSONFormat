# TheHadithsJSONFormat
Free Organized Hadith Collection especially for Devs

A free, ready-to-use collection of authentic Hadiths taken from sunnah.com, organized book-wise and topic-wise to make it easy for Muslim devs to use Hadith data in their projects.

Free to use in any project, no credits required.
Includes:
- Arabic texts
- English translations
- Hadith gradings
- References

May Allah accept and make this beneficial for all.

------------------------------------------------------------
Collections Included (so far, more planned InshaAllah):
------------------------------------------------------------
- Sahih al-Bukhari
- Sahih Muslim
- Sunan Abu Dawud
- Jami` at-Tirmidhi
- Sunan an-Nasa'i
- Sunan Ibn Majah
- Muwatta Malik
- Riyad as-Salihin
- Adab
- Ahmad(NOT COMPLETE)
- Bulugh
- Darimi
- Forty
- HisnAlMuslim
- Mishkat
- Shamail
(Planned expansion to Musnad Ahmad and more in future, InshaAllah.)

------------------------------------------------------------
Data Structure
------------------------------------------------------------
Each hadith is stored in a .json file per topic 
(e.g. 001_purification_kitab_al-taharah.json).

IDs reset per sub topic — so “Book of Purification” starts at ID 1,
and “Book of Prayer” starts again at ID 1.

Example:

{
  "collection": "abudawud",
  "book": "1 Purification (Kitab Al-Taharah) كتاب الطهارة",
  "reference": "Reference : Sunan Abi Dawud 1 In-book reference : Book 1, Hadith 1 English translation : Book 1, Hadith 1",
  "grade": "Grade : Hasan Sahih (Al-Albani) حسن صحيح (الألباني) حكم :",
  "arabic": "حَدَّثَنَا ...",
  "english": "Narrated Mughirah ibn Shu'bah: When the Prophet (صلى الله عليه وسلم) went (outside) to relieve himself, he went to a far-off place.",
  "id": 1
}

------------------------------------------------------------
Included Example Program
------------------------------------------------------------
A simple demonstration program `hadith_viewer.py` is included to show how to:
- Automatically list available books and topics.
- Fetch and display a hadith by its ID.

To run it:
1. Open the "Sunnah" folder in a terminal.
2. Run:
   python hadith_viewer.py
3. Follow the prompts.
This program is just for demonstration purposes to help u guys out InshaAllah

  
