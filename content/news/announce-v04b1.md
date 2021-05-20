Title: Announcing the first beta of Bookworm version 0.4
Slug: v0.4b1
Lang: en
Date: 2021-05-18 03:20
Category: news
Author: Musharraf
Tags: release, announcement
Keywords: Bookworm, accessible, document, reader, blind, screen reader, a11y, NVDA, JAWS, TTS, speech
Summary: Announcing The First Beta of Bookworm Version 0.4
cover: static/uploads/Carlosruizzafon.jpeg
cover_caption: The late Spanish Novelist Carlos Ruiz Zafon.  Source: Wikipedia
--------------------------------------

The Blind Pandas Team is pleased to announce the immediate availability of the first beta of Bookworm version 0.4.

This release of Bookworm has been in the making for over an year. It includes many new features beside performance and stability improvements. Following are some of the new features in this version:

* Support for additional document formats. This brings the total number of supported document formats to 15
* Support for extracting text from scanned documents using Optical Character Recognition (OCR)
* Support for navigating content using single-letter navigation commands to jump between structural elements
* Support for opening URLs within Bookworm with the ability of extracting the main text of the article
* Support for defining terms from Wikipedia with the ability of opening the Wikipedia page in Bookworm

You can download this release from the [download page](https://getbookworm.com/download/). Read on to learn more about what's new in this release.

## A New Sponsor, A New Website

This release of Bookworm is supported by [Capeds](https://capeds.org), A Japan based non-profit organization, founded by blind Sudanese professionals to support the education of persons with disabilities in Sudan. In February 2021 Capeds funded the project's infrastructure for the next three years, and sponsored the integration of Tesseract OCR engine into Bookworm.

Thanks to [Capeds](https://capeds.org), we're able to ensure the sustainability of Bookworm's development during this year. We also created this beautiful, highly accessible website to be the permanent home of Bookworm.

If you or your organization would like to sponsor the project or a specific feature, please [get in touch](https://getbookworm.com/contact-us/).

### Support for new document formats

In this version of Bookworm we added support for the following document formats, bringing the total number of document types that you can open in Bookworm to 15:

* Kindle eBooks of the extensions .mobi, .kf8, and .azw3
* Microsoft Word 2007 Documents (.docx)
* PowerPoint presentations (.pptx)
* Open document text (.otf) and open document presentation (.opf)
* XPS documents
* Fiction eBooks (.fb2)
* Commic book archive (.cbz)
* Markdown files (.md)

### Optical Character Recognition (OCR)

Bookworm enables you to extract text from any scanned document or image using Optical Character Recognition (OCR) technology. While in an opened document, just press F4 to start configuring OCR for the current document. Bookworm comes with builtin support for Windows 10 OCR and the free and open-source Tesseract OCR Engine.

By default Bookworm uses Windows 10 OCR, but if you want better performance, we recommend using the Tesseract OCR Engine, which supports more than 100 languages. Tesseract OCR Engine is downloadable from within Bookworm itself; just go to the application preferences, and then navigate to the OCR tab.

Additionally, Bookworm allows you to use computer vision (CV) technologies to improve text extraction. You can apply some processing to the scanned page image in order to improve OCR accuracy and performance through a comprehensive set of image filters.

### Single Letter Navigation

You can quickly jump back and forth between certain structural elements using single letter keys in supported document types. Bookworm allows you to jump between headings, tables, lists, and quotes by pressing a letter or number key. For instance, you can press "H" to jump between headings, numbers from 1 to 6 to jump to a specific heading level, "T" to jump between tables, and so on. This feature is available only in document types that provide structural information about their content.

### Opening web Pages

You can now open web links directly in Bookworm. Just go to the new "Web Services" menu and select "Open URL" or press Ctrl + Shift + U. By default Bookworm will open the web page in a clean  view; this means that Bookworm will try to remove secondary content from the page keeping only the main content. You can view the full web page by choosing the "Full text"  reading mode from the tools menu.

### Wikipedia Integration

You can quickly define terms and get information about events, places, and people from Wikipedia. While a document is opened in Bookworm, you can get a summary about the selected text, just click "Wikipedia quick search" from the "Web Services" menu, or press Ctrl + Shift + W. You can also enter the term you want to look for directly if you wish whether there is an opened book or not. Initially, Bookworm shows a short summary, if you want to get the full page, Bookworm enables you to open the page in the browser or in the app itself.

### Reading Modes

For some document formats, such as PDF, text could be extracted in multiple ways. For PDF you can extract text based on the physical flow of the document, or based on the reading order of the text. Selecting the right reading mode is crucial for enhancing your reading experience in Bookworm.

For instance  if you're reading a novel, you want the text tidy, without many blank lines and spaces. Whereas if you're reading a programming book, you want the spaces and empty lines intact.

To configure the reading mode, go to the "Tools"  menu and click on the "Change Reading Mode" menu item, or just press Ctrl + Shift + M, and a list of supported reading modes for the currently opened document will be shown.

### Additional features and bug fixes

The above features are the main highlights of this release. There are many improvements and bug fixes in this release, including:

* The ability to pin documents to the app, this enable you to have those documents always available in Bookworm
* Support for customizing the text styling, including font size and typeface 
* Support for using the open-dyslectic font in Bookworm
 * Support for page labels in PDFs. Page labels are page numbers based on the printed book
 * Added Support for Japanese language

## Credits

This release of Bookworm would not be available without the invaluable help of the following people:

* [Mohammed Bashir](http://bashir.taibat.com/) a blind programmer from Sudan. Mr. Bashir offered us his technical expertise, patience, and a sizable portion  of his time to properly implement the OCR features in Bookworm. Mr. Bashir also translated Bookworm to Japanese. 
* Dr. Mohammed Abdin: the director of [Capeds](https://capeds.org). Dr. Abdin lent us his confidence, his endless desire to make a difference, and his repertoire of insightful knowledge on what blind people really need.

## Dedication

This release of Bookworm is dedicated to the memory of the late Spanish author [Carlos Ruiz Zafon](https://en.wikipedia.org/wiki/Carlos_Ruiz_Zaf%C3%B3n) who passed away last June. In his masterpiece [The Shadow of the Wind](https://en.wikipedia.org/wiki/The_Shadow_of_the_Wind), Zafon showed us how reading, loving, and cherishing books can make the world a much, much better place. I'll leave you with one of Zafon's quotes:

> "Every book, every volume you see here, has a soul. The soul of the person who wrote it and of those who read it and lived and dreamed with it. Every time a book changes hands, every time someone runs his eyes down its pages, its spirit grows and strengthens.”  &mdash; Carlos Ruiz Zafón, The Shadow of the Wind
