::: head
[![W3C](https://www.w3.org/StyleSheets/TR/2016/logos/W3C){height="48" width="72"}](https://www.w3.org/){.logo}

# WebVTT: The Web Video Text Tracks Format {#title .p-name .no-ref}

## [W3C Candidate Recommendation 4 April 2019]{.content} {#subtitle .no-num .no-toc .no-ref .heading .settled}

::: {fill-with="spec-metadata"}

This version:
:   [https://www.w3.org/TR/2019/CR-webvtt1-20190404/](https://www.w3.org/TR/2019/CR-webvtt1-20190404/){.u-url}

Latest published version:
:   <https://www.w3.org/TR/webvtt1/>

Editor\'s Draft:
:   <https://w3c.github.io/webvtt/>

Previous Versions:
:   [https://www.w3.org/TR/2018/CR-webvtt1-20180510/](https://www.w3.org/TR/2018/CR-webvtt1-20180510/){rel="prev"}

Test Suite:
:   <https://github.com/web-platform-tests/wpt/tree/master/webvtt>

Editor:
:   [Silvia Pfeiffer](mailto:silvia.pfeiffer@data61.csiro.au){.p-name .fn .u-email .email} ([CSIRO](https://www.csiro.au/){.p-org .org})

Former Editors:
:   [Simon Pieters](mailto:simonp@opera.com){.p-name .fn .u-email .email} ([Opera Software AS](http://www.opera.com/){.p-org .org})
:   [Silvia Pfeiffer](mailto:silviapfeiffer1@gmail.com){.p-name .fn .u-email .email} ([NICTA](http://nicta.com.au/){.p-org .org})
:   [Philip Jägenstedt](mailto:philipj@opera.com){.p-name .fn .u-email .email} ([Opera Software ASA](http://www.opera.com/){.p-org .org})
:   [Ian Hickson](mailto:ian@hixie.ch){.p-name .fn .u-email .email} ([Google](https://www.google.com/){.p-org .org})

Participate:
:   [GitHub w3c/webvtt](https://github.com/w3c/webvtt) ([new issue](https://github.com/w3c/webvtt/issues/new), [open issues](https://github.com/w3c/webvtt/issues), [legacy open bugs](https://www.w3.org/Bugs/Public/buglist.cgi?product=TextTracks%20CG&component=WebVTT&resolution=---))

Commits:
:   [GitHub w3c/webvtt/commits](https://github.com/w3c/webvtt/commits)
:   [\@webvtt](https://twitter.com/webvtt)
:::

::: {fill-with="warning"}
:::

[Copyright](https://www.w3.org/Consortium/Legal/ipr-notice#Copyright) © 2019 [W3C](https://www.w3.org/)^®^ ([MIT](https://www.csail.mit.edu/), [ERCIM](https://www.ercim.eu/), [Keio](https://www.keio.ac.jp/), [Beihang](https://ev.buaa.edu.cn/)). W3C [liability](https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer), [trademark](https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks) and [document use](https://www.w3.org/Consortium/Legal/copyright-documents) rules apply.

------------------------------------------------------------------------
:::

::: {.p-summary fill-with="abstract"}
## [Abstract]{.content} {#abstract .no-num .no-toc .no-ref .heading .settled}

This specification defines WebVTT, the Web Video Text Tracks format. Its main use is for marking up external text track resources in connection with the HTML \<track\> element. WebVTT files provide captions or subtitles for video content, and also text video descriptions [\[MAUR\]](#biblio-maur){link-type="biblio"}, chapters for content navigation, and more generally any form of metadata that is time-aligned with audio or video content.

This specification is based on the [Draft Community Group Report](https://w3c.github.io/webvtt/) of the [Web Media Text Tracks Community Group](https://www.w3.org/community/texttracks/).
:::

## [Status of this document]{.content} {#status .no-num .no-toc .no-ref .heading .settled}

::: {fill-with="status"}
*This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index at https://www.w3.org/TR/.](https://www.w3.org/TR/)*

This document was produced by the [W3C Timed Text Working Group](https://www.w3.org/AudioVideo/TT/) as a Candidate Recommendation. This document is intended to become a W3C Recommendation. If you wish to make comments regarding this document, please send them to [public-tt@w3.org](mailto:public-tt@w3.org?subject=%5Bwebvtt%5D) ([subscribe](mailto:public-tt-request@w3.org?subject=subscribe), [archives](http://lists.w3.org/Archives/Public/public-tt/)) with `[webvtt]` at the start of your email's subject. All comments are welcome. W3C publishes a Candidate Recommendation to indicate that the document is believed to be stable and to encourage implementation by the developer community. This document will remain a Candidate Recommendation at least until 2 May 2019 in order to ensure the opportunity for wide review.

Please see the Working Group\'s [Implementation Report](https://www.w3.org/wiki/TimedText/WebVTT_Implementation_Report).

For this specification to exit the CR stage, at least 2 independent implementations of every feature defined in this specification need to be documented in the implementation report. The implementation report is based on implementer-provided test results for the [test suite](https://github.com/web-platform-tests/wpt/tree/master/webvtt). The Working Group does not require that implementations are publicly available but encourages them to be so.

::: {fill-with="at-risk"}
The following features are at-risk, and may be dropped during the CR period:

-   [collision avoidance with snap-to-lines false](#collision-avoidance)
-   [::cue-region pseudo-element](#the-cue-region-pseudo-element)
-   [:past and :future pseudo-classes](#the-past-and-future-pseudo-classes)
:::

A cumulative summary of all changes applied to this version since the [WebVTT First Public Working Draft](https://www.w3.org/TR/2014/WD-webvtt1-20141113/) was published is available at [Changes from FPWD WebVTT](changes.html).

For convenience, a complete diff between this version and the WebVTT previous Working Draft was published is found at [Diff from previous Working Draft WebVTT](diff.html).

Publication as a Candidate Recommendation does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/2004/01/pp-impl/34314/status#disclosures){rel="disclosure"} made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/Consortium/Patent-Policy/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy/#sec-Disclosure).

This document is governed by the [1 March 2019 W3C Process Document](https://www.w3.org/2019/Process-20190301/){#w3c_process_revision}.
:::

## Table of Contents {#contents .no-num .no-toc .no-ref}

1.  [[1]{.secno} [Introduction]{.content}](#introduction)
    1.  [[1.1]{.secno} [A simple caption file]{.content}](#introduction-caption)
    2.  [[1.2]{.secno} [Caption cues with multiple lines]{.content}](#introduction-multiple-lines)
    3.  [[1.3]{.secno} [Styling captions]{.content}](#styling)
    4.  [[1.4]{.secno} [Other caption and subtitling features]{.content}](#introduction-other-features)
    5.  [[1.5]{.secno} [Comments in WebVTT]{.content}](#introduction-comments)
    6.  [[1.6]{.secno} [Chapters example]{.content}](#introduction-chapters)
    7.  [[1.7]{.secno} [Metadata example]{.content}](#introduction-metadata)
2.  [[2]{.secno} [Conformance]{.content}](#conformance)
    1.  [[2.1]{.secno} [Conformance classes]{.content}](#conformance-classes)
    2.  [[2.2]{.secno} [Unicode normalization]{.content}](#unicode-normalization)
3.  [[3]{.secno} [Data model]{.content}](#data-model)
    1.  [[3.1]{.secno} [Overview]{.content}](#model-overview)
    2.  [[3.2]{.secno} [WebVTT cues]{.content}](#model-cues)
    3.  [[3.3]{.secno} [WebVTT caption or subtitle cues]{.content}](#cues)
    4.  [[3.4]{.secno} [WebVTT caption or subtitle regions]{.content}](#regions)
    5.  [[3.5]{.secno} [WebVTT chapter cues]{.content}](#chapter-cues)
    6.  [[3.6]{.secno} [WebVTT metadata cues]{.content}](#metadata-cues)
4.  [[4]{.secno} [Syntax]{.content}](#syntax)
    1.  [[4.1]{.secno} [WebVTT file structure]{.content}](#file-structure)
    2.  [[4.2]{.secno} [Types of WebVTT cue payload]{.content}](#types-of-webvtt-cue-payload)
        1.  [[4.2.1]{.secno} [WebVTT metadata text]{.content}](#metadata-text)
        2.  [[4.2.2]{.secno} [WebVTT caption or subtitle cue text]{.content}](#caption-text)
        3.  [[4.2.3]{.secno} [WebVTT chapter title text]{.content}](#chapter-title-text)
    3.  [[4.3]{.secno} [WebVTT region settings]{.content}](#region-settings)
    4.  [[4.4]{.secno} [WebVTT cue settings]{.content}](#cue-settings)
    5.  [[4.5]{.secno} [Properties of cue sequences]{.content}](#properties-of-cue-sequences)
        1.  [[4.5.1]{.secno} [WebVTT file using only nested cues]{.content}](#file-using-only-nested-cues)
    6.  [[4.6]{.secno} [Types of WebVTT files]{.content}](#types-of-webvtt-files)
        1.  [[4.6.1]{.secno} [WebVTT file using metadata content]{.content}](#file-using-metadata-content)
        2.  [[4.6.2]{.secno} [WebVTT file using chapter title text]{.content}](#file-using-chapter-title-text)
        3.  [[4.6.3]{.secno} [WebVTT file using caption or subtitle cue text]{.content}](#file-using-cue-text)
5.  [[5]{.secno} [Default classes for WebVTT Caption or Subtitle Cue Components]{.content}](#default-classes)
    1.  [[5.1]{.secno} [Default text colors]{.content}](#default-text-color)
    2.  [[5.2]{.secno} [Default text background colors]{.content}](#default-text-background)
6.  [[6]{.secno} [Parsing]{.content}](#parsing)
    1.  [[6.1]{.secno} [WebVTT file parsing]{.content}](#file-parsing)
    2.  [[6.2]{.secno} [WebVTT region settings parsing]{.content}](#region-settings-parsing)
    3.  [[6.3]{.secno} [WebVTT cue timings and settings parsing]{.content}](#cue-timings-and-settings-parsing)
    4.  [[6.4]{.secno} [WebVTT cue text parsing rules]{.content}](#cue-text-parsing-rules)
    5.  [[6.5]{.secno} [WebVTT cue text DOM construction rules]{.content}](#dom-construction-rules)
    6.  [[6.6]{.secno} [WebVTT rules for extracting the chapter title]{.content}](#rules-for-extracting-the-chapter-title)
7.  [[7]{.secno} [Rendering]{.content}](#rendering)
    1.  [[7.1]{.secno} [Processing model]{.content}](#processing-model)
    2.  [[7.2]{.secno} [Processing cue settings]{.content}](#processing-cue-settings)
    3.  [[7.3]{.secno} [Obtaining CSS boxes]{.content}](#obtaining-css-boxes)
    4.  [[7.4]{.secno} [Applying CSS properties to WebVTT Node Objects]{.content}](#applying-css-properties)
8.  [[8]{.secno} [CSS extensions]{.content}](#css-extensions)
    1.  [[8.1]{.secno} [Introduction]{.content}](#css-extensions-introduction)
    2.  [[8.2]{.secno} [Processing model]{.content}](#css-extensions-processing-model)
        1.  [[8.2.1]{.secno} [The [::cue]{.css} pseudo-element]{.content}](#the-cue-pseudo-element)
        2.  [[8.2.2]{.secno} [The [:past]{.css} and [:future]{.css} pseudo-classes]{.content}](#the-past-and-future-pseudo-classes)
        3.  [[8.2.3]{.secno} [The [::cue-region]{.css} pseudo-element]{.content}](#the-cue-region-pseudo-element)
9.  [[9]{.secno} [API]{.content}](#api)
    1.  [[9.1]{.secno} [The `VTTCue`{.idl} interface]{.content}](#the-vttcue-interface)
    2.  [[9.2]{.secno} [The `VTTRegion`{.idl} interface]{.content}](#the-vttregion-interface)
10. [[10]{.secno} [IANA considerations]{.content}](#iana)
    1.  [[10.1]{.secno} [`text/vtt`]{.content}](#iana-text-vtt)
11. [[]{.secno} [Privacy and Security Considerations]{.content}](#privacy-and-security-considerations)
    1.  [[]{.secno} [Text-based format security]{.content}](#fromat-security)
    2.  [[]{.secno} [Styling-related privacy and security]{.content}](#styling-security)
    3.  [[]{.secno} [Scripting-related security]{.content}](#scripting-security)
    4.  [[]{.secno} [Privacy of preference]{.content}](#privacy-of-preference)
12. [[]{.secno} [Acknowledgements]{.content}](#acknowledgements)
13. [[]{.secno} [Index]{.content}](#index)
    1.  [[]{.secno} [Terms defined by this specification]{.content}](#index-defined-here)
    2.  [[]{.secno} [Terms defined by reference]{.content}](#index-defined-elsewhere)
14. [[]{.secno} [References]{.content}](#references)
    1.  [[]{.secno} [Normative References]{.content}](#normative)
    2.  [[]{.secno} [Informative References]{.content}](#informative)
15. [[]{.secno} [IDL Index]{.content}](#idl-index)

::: {role="main"}
## [1. ]{.secno}[Introduction]{.content}[](#introduction){.self-link} {#introduction .heading .settled level="1"}

*This section is non-normative.*

The [WebVTT]{#webvtt .dfn .dfn-paneled dfn-type="dfn" noexport=""} (Web Video Text Tracks) format is intended for marking up external text track resources in connection with the HTML \<track\> element.

WebVTT files provide captions or subtitles for video content, and also text video descriptions [\[MAUR\]](#biblio-maur){link-type="biblio"}, chapters for content navigation, and more generally any form of metadata that is time-aligned with audio or video content.

The majority of the current version of this specification is dedicated to describing how to use WebVTT files for captioning or subtitling. There is minimal information about chapters and time-aligned metadata and nothing about video descriptions at this stage.

In this section we provide some example WebVTT files as an introduction.

### [1.1. ]{.secno}[A simple caption file]{.content}[](#introduction-caption){.self-link} {#introduction-caption .heading .settled level="1.1"}

*This section is non-normative.*

The main use for WebVTT files is captioning or subtitling video content. Here is a sample file that captions an interview:

    WEBVTT

    00:11.000 --> 00:13.000
    <v Roger Bingham>We are in New York City

    00:13.000 --> 00:16.000
    <v Roger Bingham>We’re actually at the Lucern Hotel, just down the street

    00:16.000 --> 00:18.000
    <v Roger Bingham>from the American Museum of Natural History

    00:18.000 --> 00:20.000
    <v Roger Bingham>And with me is Neil deGrasse Tyson

    00:20.000 --> 00:22.000
    <v Roger Bingham>Astrophysicist, Director of the Hayden Planetarium

    00:22.000 --> 00:24.000
    <v Roger Bingham>at the AMNH.

    00:24.000 --> 00:26.000
    <v Roger Bingham>Thank you for walking down here.

    00:27.000 --> 00:30.000
    <v Roger Bingham>And I want to do a follow-up on the last conversation we did.

    00:30.000 --> 00:31.500 align:right size:50%
    <v Roger Bingham>When we e-mailed—

    00:30.500 --> 00:32.500 align:left size:50%
    <v Neil deGrasse Tyson>Didn’t we talk about enough in that conversation?

    00:32.000 --> 00:35.500 align:right size:50%
    <v Roger Bingham>No! No no no no; 'cos 'cos obviously 'cos

    00:32.500 --> 00:33.500 align:left size:50%
    <v Neil deGrasse Tyson><i>Laughs</i>

    00:35.500 --> 00:38.000
    <v Roger Bingham>You know I’m so excited my glasses are falling off here.

You can see that a WebVTT file in general consists of a sequence of text segments associated with a time-interval, called a cue ([definition](#webvtt-cue){#ref-for-webvtt-cue-1 link-type="dfn"}). Beyond captioning and subtitling, WebVTT can be used for time-aligned metadata, typically in use for delivering name-value pairs in cues. WebVTT can also be used for delivering chapters, which helps with contextual navigation around an audio/video file. Finally, WebVTT can be used for the delivery of text video descriptions, which is text that describes the visual content of time-intervals and can be synthesized to speech to help vision-impaired users understand context.

This version of WebVTT focuses on solving the captioning and subtitling use cases. More specification work is possible for the other use cases. A decision on what type of use case a WebVTT file is being used for is made by the software that is using the file. For example, if in use with a HTML file through a \<track\> element, the [kind](https://www.w3.org/TR/html51/semantics-embedded-content.html#kind-of-track){link-type="dfn"} attribute defines how the WebVTT file is to be interpreted.

The following subsections provide an overview of some of the key features of the WebVTT file format, particularly when in use for captioning and subtitling.

### [1.2. ]{.secno}[Caption cues with multiple lines]{.content}[](#introduction-multiple-lines){.self-link} {#introduction-multiple-lines .heading .settled level="1.2"}

*This section is non-normative.*

Line breaks in cues are honored. User agents will also insert extra line breaks if necessary to fit the cue in the cue's width. In general, therefore, authors are encouraged to write cues all on one line except when a line break is definitely necessary.

::: {#example-c6fa39cb .example}
[](#example-c6fa39cb){.self-link}

These captions on a public service announcement video demonstrate line breaking:

    WEBVTT

    00:01.000 --> 00:04.000
    Never drink liquid nitrogen.

    00:05.000 --> 00:09.000
    — It will perforate your stomach.
    — You could die.

    00:10.000 --> 00:14.000
    The Organisation for Sample Public Service Announcements accepts no liability for the content of this advertisement, or for the consequences of any actions taken on the basis of the information provided.

The first cue is simple, it will probably just display on one line. The second will take two lines, one for each speaker. The third will wrap to fit the width of the video, possibly taking multiple lines. For example, the three cues could look like this:

               Never drink liquid nitrogen.

            — It will perforate your stomach.
                    — You could die.

        The Organisation for Sample Public Service
        Announcements accepts no liability for the
        content of this advertisement, or for the
         consequences of any actions taken on the
            basis of the information provided.

If the width of the cues is smaller, the first two cues could wrap as well, as in the following example. Note how the second cue's explicit line break is still honored, however:

          Never drink
        liquid nitrogen.

      — It will perforate
          your stomach.
        — You could die.

      The Organisation for
      Sample Public Service
      Announcements accepts
      no liability for the
         content of this
      advertisement, or for
       the consequences of
      any actions taken on
        the basis of the
      information provided.

Also notice how the wrapping is done so as to keep the line lengths balanced.
:::

### [1.3. ]{.secno}[Styling captions]{.content}[](#styling){.self-link} {#styling .heading .settled level="1.3"}

*This section is non-normative.*

CSS style sheets that apply to an HTML page that contains a [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element can target WebVTT cues and regions in the video using the [::cue]{.css}, [::cue()]{.css}, [::cue-region]{.css} and [::cue-region()]{.css} pseudo-elements.

::: {#example-6a17c0df .example}
[](#example-6a17c0df){.self-link}

In this example, an HTML page has a CSS style sheet in a [style](https://www.w3.org/TR/html51/document-metadata.html#the-style-element){link-type="element"} element that styles all cues in the video with a gradient background and a text color, as well as changing the text color for all [WebVTT Bold Objects](#webvtt-bold-object){#ref-for-webvtt-bold-object-1 link-type="dfn"} in cues in the video.

    <!doctype html>
    <html>
     <head>
      <title>Styling WebVTT cues</title>
      <style>
       video::cue {
         background-image: linear-gradient(to bottom, dimgray, lightgray);
         color: papayawhip;
       }
       video::cue(b) {
         color: peachpuff;
       }
      </style>
     </head>
     <body>
      <video controls autoplay src="video.webm">
       <track default src="track.vtt">
      </video>
     </body>
    </html>
:::

CSS style sheets can also be embedded in WebVTT files themselves.

Style blocks are placed after any headers but before the first cue, and start with the line \"STYLE\". Comment blocks can be interleaved with style blocks.

Blank lines cannot appear in the style sheet. They can be removed or be filled with a space or a CSS comment (e.g. `/**/`).

The string \"`-->`\" cannot be used in the style sheet. If the style sheet is wrapped in \"`<!--`\" and \"`-->`\", then those strings can just be removed. If \"`-->`\" appears inside a CSS string, then it can use CSS escaping e.g. \"`--\>`\".

::: {#example-3f42c0aa .example}
[](#example-3f42c0aa){.self-link}

This example shows how cues can be styled with style blocks in WebVTT.

    WEBVTT

    STYLE
    ::cue {
      background-image: linear-gradient(to bottom, dimgray, lightgray);
      color: papayawhip;
    }
    /* Style blocks cannot use blank lines nor "dash dash greater than" */

    NOTE comment blocks can be used between style blocks.

    STYLE
    ::cue(b) {
      color: peachpuff;
    }

    hello
    00:00:00.000 --> 00:00:10.000
    Hello <b>world</b>.

    NOTE style blocks cannot appear after the first cue.
:::

### [1.4. ]{.secno}[Other caption and subtitling features]{.content}[](#introduction-other-features){.self-link} {#introduction-other-features .heading .settled level="1.4"}

*This section is non-normative.*

WebVTT also supports some less-often used features.

::: {#example-59f83607 .example}
[](#example-59f83607){.self-link}

In this example, the cues have an identifier:

    WEBVTT

    test
    00:00.000 --> 00:02.000
    This is a test.

    123
    00:00.000 --> 00:02.000
    That’s an, an, that’s an L!

    crédit de transcription
    00:04.000 --> 00:05.000
    Transcrit par Célestes™

This allows a style sheet to specifically target the cues.

    /* style for cue: test */
    ::cue(#test) { color: lime; }

Due to the syntax rules of CSS, some characters need to be escaped with CSS character escape sequences. For example, an ID that starts with a number 0-9 needs to be escaped. The ID `123` can be represented as \"\\31 23\" (31 refers to the Unicode code point for \"1\"). See [Using character escapes in markup and CSS](https://www.w3.org/International/questions/qa-escapes) for more information on CSS escapes.

    /* style for cue: 123 */
    ::cue(#\31 23) { color: lime; }
    /* style for cue: crédit de transcription */
    ::cue(#crédit\ de\ transcription) { color: red; }
:::

::: {#example-3fb8f9dd .example}
[](#example-3fb8f9dd){.self-link}

This example shows how classes can be used on elements, which can be helpful for localization or maintainability of styling, and also how to indicate a language change in the cue text.

    WEBVTT

    04:02.500 --> 04:05.000
    J’ai commencé le basket à l'âge de 13, 14 ans

    04:05.001 --> 04:07.800
    Sur les <i.foreignphrase><lang en>playground</lang></i>, ici à Montpellier
:::

::: {#example-954e004d .example}
[](#example-954e004d){.self-link}

In this example, each cue says who is talking using voice spans. In the first cue, the span specifying the speaker is also annotated with two classes, \"first\" and \"loud\". In the third cue, there is also some italics text (not associated with a specific speaker). The last cue is annotated with just the class \"loud\".

    WEBVTT

    00:00.000 --> 00:02.000
    <v.first.loud Esme>It’s a blue apple tree!

    00:02.000 --> 00:04.000
    <v Mary>No way!

    00:04.000 --> 00:06.000
    <v Esme>Hee!</v> <i>laughter</i>

    00:06.000 --> 00:08.000
    <v.loud Mary>That’s awesome!

Notice that as a special exception, the voice spans don't have to be closed if they cover the entire cue text.

Style sheets can style these spans:

    ::cue(v[voice="Esme"]) { color: cyan }
    ::cue(v[voice="Mary"]) { color: lime }
    ::cue(i) { font-style: italic }
    ::cue(.loud) { font-size: 2em }
:::

::: {#example-b30cb609 .example}
[](#example-b30cb609){.self-link}

This example shows how to position cues at explicit positions in the video viewport.

    WEBVTT

    00:00:00.000 --> 00:00:04.000 position:10%,line-left align:left size:35%
    Where did he go?

    00:00:03.000 --> 00:00:06.500 position:90% align:right size:35%
    I think he went down this lane.

    00:00:04.000 --> 00:00:06.500 position:45%,line-right align:center size:35%
    What are you waiting for?

Since the cues in these examples are horizontal, the \"position\" setting refers to a percentage of the width of the video viewpoint. If the text were vertical, the \"position\" setting would refer to the height of the video viewport.

The \"line-left\" or \"line-right\" only refers to the physical side of the box to which the \"position\" setting applies, in a way which is agnostic regarding the horizontal or vertical direction of the cue. It does not affect or relate to the direction or position of the text itself within the box.

The cues cover only 35% of the video viewport's width - that's the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-1 link-type="dfn"}'s \"size\" for all three cues.

The first cue has its [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-2 link-type="dfn"} positioned at the 10% mark. The \"line-left\" and \"line-right\" within the \"position\" setting indicates which side of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-3 link-type="dfn"} the position refers to. Since in this case the text is horizontal, \"line-left\" refers to the left side of the box, and the cue box is thus positioned between the 10% and the 45% mark of the video viewport's width, probably underneath a speaker on the left of the video image. If the cue was vertical, \"line-left\" positioning would be from the top of the video viewport's height and the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-4 link-type="dfn"} would cover 35% of the video viewport's height.

The text within the first cue's cue box is aligned using the \"align\" cue setting. For left-to-right rendered text, \"start\" alignment is the left of that box, for right-to-left rendered text the right of the box. So, independent of the directionality of the text, it will stay underneath that speaker. Note that \"center\" position alignment of the cue box is the default for start aligned text, in order to avoid having the box move when the base direction of the text changes (from left-to-right to right-to-left or vice versa) as a result of translation.

The second cue has its [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-5 link-type="dfn"} right aligned at the 90% mark of the video viewport width (\"right\" aligned text right aligns the box). The same effect can be achieved with \"position:55%,line-left\", which explicitly positions the cue box. The third cue has center aligned text within the same positioned cue box as the first cue.
:::

::: {#example-cd0199a2 .example}
[](#example-cd0199a2){.self-link}

This example shows two regions containing rollup captions for two different speakers. Fred's cues scroll up in a region in the left half of the video, Bill's cues scroll up in a region on the right half of the video. Fred's first cue disappears at 12.5sec even though it is defined until 20sec because its region is limited to 3 lines and at 12.5sec a fourth cue appears:

    WEBVTT

    REGION
    id:fred
    width:40%
    lines:3
    regionanchor:0%,100%
    viewportanchor:10%,90%
    scroll:up

    REGION
    id:bill
    width:40%
    lines:3
    regionanchor:100%,100%
    viewportanchor:90%,90%
    scroll:up

    00:00:00.000 --> 00:00:20.000 region:fred align:left
    <v Fred>Hi, my name is Fred

    00:00:02.500 --> 00:00:22.500 region:bill align:right
    <v Bill>Hi, I’m Bill

    00:00:05.000 --> 00:00:25.000 region:fred align:left
    <v Fred>Would you like to get a coffee?

    00:00:07.500 --> 00:00:27.500 region:bill align:right
    <v Bill>Sure! I’ve only had one today.

    00:00:10.000 --> 00:00:30.000 region:fred align:left
    <v Fred>This is my fourth!

    00:00:12.500 --> 00:00:32.500 region:fred align:left
    <v Fred>OK, let’s go.

Note that regions are only defined for horizontal cues.
:::

### [1.5. ]{.secno}[Comments in WebVTT]{.content}[](#introduction-comments){.self-link} {#introduction-comments .heading .settled level="1.5"}

*This section is non-normative.*

Comments can be included in WebVTT files.

Comments are just blocks that are preceded by a blank line, start with the word \"`NOTE`\" (followed by a space or newline), and end at the first blank line.

::: {#example-44941b0b .example}
[](#example-44941b0b){.self-link}

Here, a one-line comment is used to note a possible problem with a cue.

    WEBVTT

    00:01.000 --> 00:04.000
    Never drink liquid nitrogen.

    NOTE I’m not sure the timing is right on the following cue.

    00:05.000 --> 00:09.000
    — It will perforate your stomach.
    — You could die.
:::

::: {#example-03a9f3ad .example}
[](#example-03a9f3ad){.self-link}

In this example, the author has written many comments.

    WEBVTT

    NOTE
    This file was written by Jill. I hope
    you enjoy reading it. Some things to
    bear in mind:
    - I was lip-reading, so the cues may
    not be 100% accurate
    - I didn’t pay too close attention to
    when the cues should start or end.

    00:01.000 --> 00:04.000
    Never drink liquid nitrogen.

    NOTE check next cue

    00:05.000 --> 00:09.000
    — It will perforate your stomach.
    — You could die.

    NOTE end of file
:::

### [1.6. ]{.secno}[Chapters example]{.content}[](#introduction-chapters){.self-link} {#introduction-chapters .heading .settled level="1.6"}

*This section is non-normative.*

A WebVTT file can consist of chapters, which are navigation markers for the video.

Chapters are plain text, typically just a single line.

::: {#example-5b78f944 .example}
[](#example-5b78f944){.self-link}

In this example, a talk is split into each slide being a chapter.

    WEBVTT

    NOTE
    This is from a talk Silvia gave about WebVTT.

    Slide 1
    00:00:00.000 --> 00:00:10.700
    Title Slide

    Slide 2
    00:00:10.700 --> 00:00:47.600
    Introduction by Naomi Black

    Slide 3
    00:00:47.600 --> 00:01:50.100
    Impact of Captions on the Web

    Slide 4
    00:01:50.100 --> 00:03:33.000
    Requirements of a Video text format
:::

### [1.7. ]{.secno}[Metadata example]{.content}[](#introduction-metadata){.self-link} {#introduction-metadata .heading .settled level="1.7"}

*This section is non-normative.*

A WebVTT file can consist of time-aligned metadata.

Metadata can be any string and is often provided as a JSON construct.

Note that you cannot provide blank lines inside a metadata block, because the blank line signifies the end of the WebVTT cue.

::: {#example-7e3f730b .example}
[](#example-7e3f730b){.self-link}

In this example, a talk is split into each slide being a chapter.

    WEBVTT

    NOTE
    Thanks to http://output.jsbin.com/mugibo

    1
    00:00:00.100 --> 00:00:07.342
    {
     "type": "WikipediaPage",
     "url": "https://en.wikipedia.org/wiki/Samurai_Pizza_Cats"
    }

    2
    00:07.810 --> 00:09.221
    {
     "type": "WikipediaPage",
     "url" :"http://samuraipizzacats.wikia.com/wiki/Samurai_Pizza_Cats_Wiki"
    }

    3
    00:11.441 --> 00:14.441
    {
     "type": "LongLat",
     "lat" : "36.198269",
     "long": "137.2315355"
    }
:::

## [2. ]{.secno}[Conformance]{.content}[](#conformance){.self-link} {#conformance .heading .settled level="2"}

All diagrams, examples, and notes in this specification are non-normative, as are all sections explicitly marked non-normative. Everything else in this specification is normative.

The key words \"MUST\", \"MUST NOT\", \"SHOULD\", \"SHOULD NOT\", \"MAY\", and \"OPTIONAL\" in the normative parts of this document are to be interpreted as described in RFC2119. The key word \"OPTIONALLY\" in the normative parts of this document is to be interpreted with the same normative meaning as \"MAY\" and \"OPTIONAL\". For readability, these words do not appear in all uppercase letters in this specification. [\[RFC2119\]](#biblio-rfc2119){link-type="biblio"}

Requirements phrased in the imperative as part of algorithms (such as \"strip any leading space characters\" or \"return false and abort these steps\") are to be interpreted with the meaning of the key word (\"must\", \"should\", \"may\", etc) used in introducing the algorithm.

Conformance requirements phrased as algorithms or specific steps may be implemented in any manner, so long as the end result is equivalent. (In particular, the algorithms defined in this specification are intended to be easy to follow, and not intended to be performant.)

### [2.1. ]{.secno}[Conformance classes]{.content}[](#conformance-classes){.self-link} {#conformance-classes .heading .settled level="2.1"}

This specification describes the conformance criteria for user agents (relevant to implementors) and [WebVTT files](#webvtt-file){#ref-for-webvtt-file-1 link-type="dfn"} (relevant to authors and authoring tool implementors).

[§4 Syntax](#syntax) defines what consists of a valid [WebVTT file](#webvtt-file){#ref-for-webvtt-file-2 link-type="dfn"}. Authors need to follow the requirements therein, and are encouraged to use a conformance checker. [§6 Parsing](#parsing) defines how user agents are to interpret a file labelled as [text/vtt](#text-vtt){#ref-for-text-vtt-1 link-type="dfn"}, for both valid and invalid [WebVTT files](#webvtt-file){#ref-for-webvtt-file-3 link-type="dfn"}. The parsing rules are more tolerant to author errors than the syntax allows, in order to provide for extensibility and to still render cues that have some syntax errors.

[](#example-a403a5ba){.self-link}For example, the parser will create two cues even if the blank line between them is skipped. This is clearly a mistake, so a conformance checker will flag it as an error, but it is still useful to render the cues to the user.

User agents fall into several (possibly overlapping) categories with different conformance requirements.

User agents that support scripting

:   All processing requirements in this specification apply. The user agent must also be conforming implementations of the IDL fragments in this specification, as described in the Web IDL specification. [\[WEBIDL-1\]](#biblio-webidl-1){link-type="biblio"}

User agents with no scripting support

:   All processing requirements in this specification apply, except those in [§6.5 WebVTT cue text DOM construction rules](#dom-construction-rules) and [§9 API](#api).

[User agents that do not support CSS]{#user-agents-that-do-not-support-css .dfn .dfn-paneled dfn-type="dfn" noexport=""}

:   All processing requirements in this specification apply, except parts of [§6 Parsing](#parsing) that relate to stylesheets and CSS, and all of [§7 Rendering](#rendering) and [§8 CSS extensions](#css-extensions). The user agent must instead only render the text inside [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-1 link-type="dfn"} in an appropriate manner and specifically support the color classes defined in [§5 Default classes for WebVTT Caption or Subtitle Cue Components](#default-classes). Any other styling instructions are optional.

[User agents that do not support a full HTML CSS engine]{#user-agents-that-do-not-support-a-full-html-css-engine .dfn .dfn-paneled dfn-type="dfn" noexport=""}

:   All processing requirements in this specification apply, including the color classes defined in [§5 Default classes for WebVTT Caption or Subtitle Cue Components](#default-classes). However, the user agent will need to apply the CSS related features in [§6 Parsing](#parsing), [§7 Rendering](#rendering) and [§8 CSS extensions](#css-extensions) in such a way that the rendered results are equivalent to what a full CSS supporting renderer produces.

[User agents that support a full HTML CSS engine[](#user-agents-that-support-a-full-html-css-engine){.self-link}]{#user-agents-that-support-a-full-html-css-engine .dfn dfn-type="dfn" noexport=""}

:   All processing requirements in this specification apply. However, only a limited set of CSS styles is allowed because [user agents that do not support a full HTML CSS engine](#user-agents-that-do-not-support-a-full-html-css-engine){#ref-for-user-agents-that-do-not-support-a-full-html-css-engine-1 link-type="dfn"} will need to implement CSS functionality equivalents. User agents that support a full CSS engine must therefore limit the CSS styles they apply for WebVTT so as to enable identical rendering without bleeding in extra CSS styles that are beyond the WebVTT specification.

Conformance checkers

:   Conformance checkers must verify that a [WebVTT file](#webvtt-file){#ref-for-webvtt-file-4 link-type="dfn"} conforms to the applicable conformance criteria described in this specification. The term \"validator\" is equivalent to conformance checker for the purpose of this specification.

Authoring tools

:   Authoring tools must generate conforming [WebVTT files](#webvtt-file){#ref-for-webvtt-file-5 link-type="dfn"}. Tools that convert other formats to [WebVTT](#webvtt){#ref-for-webvtt-1 link-type="dfn"} are also considered to be authoring tools.

    When an authoring tool is used to edit a non-conforming [WebVTT file](#webvtt-file){#ref-for-webvtt-file-6 link-type="dfn"}, it may preserve the conformance errors in sections of the file that were not edited during the editing session (i.e. an editing tool is allowed to round-trip erroneous content). However, an authoring tool must not claim that the output is conformant if errors have been so preserved.

### [2.2. ]{.secno}[Unicode normalization]{.content}[](#unicode-normalization){.self-link} {#unicode-normalization .heading .settled level="2.2"}

Implementations of this specification must not normalize Unicode text during processing.

[](#example-aaaec267){.self-link}For example, a cue with an identifier consisting of the characters U+0041 LATIN CAPITAL LETTER A followed by U+030A COMBINING RING ABOVE (a decomposed character sequence), or the character U+212B ANGSTROM SIGN (a compatibility character), will not match a selector targeting a cue with an ID consisting of the character U+00C5 LATIN CAPITAL LETTER A WITH RING ABOVE (a precomposed character).

## [3. ]{.secno}[Data model]{.content}[](#data-model){.self-link} {#data-model .heading .settled level="3"}

The box model of WebVTT consists of three key elements: the video viewport, cues, and regions. The video viewport is the rendering area into which cues and regions are rendered. Cues are boxes consisting of a set of cue lines. Regions are subareas of the video viewport that are used to group cues together. Cues are positioned either inside the video viewport directly or inside a region, which is positioned inside the video viewport.

The position of a cue inside the video viewport is defined by a set of cue settings. The position of a region inside the video viewport is defined by a set of region settings. Cues that are inside regions can only use a limited set of their cue settings. Specifically, if the cue has a \"vertical\", \"line\" or \"size\" setting, the cue drops out of the region. Otherwise, the cue's width is calculated to be relative to the region width rather than the viewport.

### [3.1. ]{.secno}[Overview]{.content}[](#model-overview){.self-link} {#model-overview .heading .settled level="3.1"}

*This section is non-normative.*

The WebVTT file is a container file for chunks of data that are time-aligned with a video or audio resource. It can therefore be regarded as a serialisation format for time-aligned data.

A WebVTT file starts with a header and then contains a series of data blocks. If a data block has a start and end time, it is called a WebVTT cue. A comment is another kind of data block.

Different kinds of data can be carried in WebVTT files. The HTML specification identifies captions, subtitles, chapters, audio descriptions and metadata as data kinds and specifies which one is being used in the [text track kind](https://www.w3.org/TR/html51/semantics-embedded-content.html#kind-of-track){link-type="dfn"} attribute of the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} element [\[HTML51\]](#biblio-html51){link-type="biblio"}.

A WebVTT file must only contain data of one kind, never a mix of different kinds of data. The data kind of a WebVTT file is externally specified, such as in a HTML file's [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} element. The environment is responsible for interpreting the data correctly.

WebVTT caption or subtitle cues are rendered as overlays on top of a video viewport or into a region, which is a subarea of the video viewport.

### [3.2. ]{.secno}[WebVTT cues]{.content}[](#model-cues){.self-link} {#model-cues .heading .settled level="3.2"}

A [WebVTT cue]{#webvtt-cue .dfn .dfn-paneled dfn-type="dfn" noexport=""} is a [text track cue](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"} [\[HTML51\]](#biblio-html51){link-type="biblio"} that additionally consist of the following:

[A cue text]{#cue-text .dfn .dfn-paneled dfn-type="dfn" lt="cue text" noexport=""}

:   The raw text of the cue, and rules for its interpretation.

### [3.3. ]{.secno}[WebVTT caption or subtitle cues]{.content}[](#cues){.self-link} {#cues .heading .settled level="3.3"}

A [WebVTT caption or subtitle cue]{#webvtt-caption-or-subtitle-cue .dfn .dfn-paneled dfn-type="dfn" noexport=""} is a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-2 link-type="dfn"} that has the following additional properties allowing the [cue text](#cue-text){#ref-for-cue-text-1 link-type="dfn"} to be rendered and converted to a DOM fragment:

[A cue box]{#webvtt-cue-box .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue box" noexport=""}

:   The cue box of a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-3 link-type="dfn"} is a box within which the text of all lines of the cue is to be rendered. It is either rendered into the video's viewport or a region inside the viewport if the cue is part of a region.

    The position of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-6 link-type="dfn"} within the video viewport's or region's dimensions depends on the value of the [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-1 link-type="dfn"} and the [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-1 link-type="dfn"}.

    Lines are wrapped within the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-7 link-type="dfn"}'s [size](#webvtt-cue-size){#ref-for-webvtt-cue-size-1 link-type="dfn"} if lines\' lengths make this necessary.

[A writing direction]{#webvtt-cue-writing-direction .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue writing direction" noexport=""}

:   A writing direction, either

    -   [horizontal]{#webvtt-cue-horizontal-writing-direction .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue horizontal writing direction" noexport=""} (a line extends horizontally and is offset vertically from the video viewport's top edge, with consecutive lines displayed below each other),
    -   [vertical growing left]{#webvtt-cue-vertical-growing-left-writing-direction .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue vertical growing left writing direction" noexport=""} (a line extends vertically and is offset horizontally from the video viewport's right edge, with consecutive lines displayed to the left of each other), or
    -   [vertical growing right]{#webvtt-cue-vertical-growing-right-writing-direction .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue vertical growing right writing direction" noexport=""} (a line extends vertically and is offset horizontally from the video viewport's left edge, with consecutive lines displayed to the right of each other).

    The [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-1 link-type="dfn"} affects the interpretation of the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-2 link-type="dfn"}, [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-2 link-type="dfn"}, and [size](#webvtt-cue-size){#ref-for-webvtt-cue-size-2 link-type="dfn"} cue settings to be interpreted with respect to either the width or height of the video.

    By default, the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-2 link-type="dfn"} is set to to [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-1 link-type="dfn"}.

    The [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-1 link-type="dfn"} writing direction could be used for vertical Chinese, Japanese, and Korean, and the [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-1 link-type="dfn"} writing direction could be used for vertical Mongolian.

[A snap-to-lines flag]{#webvtt-cue-snap-to-lines-flag .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue snap-to-lines flag" noexport=""}

:   A boolean indicating whether the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-3 link-type="dfn"} is an integer number of lines (using the line dimensions of the first line of the cue), or whether it is a percentage of the dimension of the video. The flag is set to true when lines are counted, and false otherwise.

    Cues where the flag is false will be offset as requested modulo overlap avoidance if multiple cues are in the same place.

    By default, the [snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-1 link-type="dfn"} is set to true.

[A line]{#webvtt-cue-line .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line" noexport=""}

:   The [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-4 link-type="dfn"} defines positioning of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-8 link-type="dfn"}.

    The [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-5 link-type="dfn"} offsets the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-9 link-type="dfn"} from the top, the right or left of the video viewport as defined by the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-3 link-type="dfn"}, the [snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-2 link-type="dfn"}, or the lines occupied by any other showing tracks.

    The [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-6 link-type="dfn"} is set either as a number of lines, a percentage of the video viewport height or width, or as the special value [auto]{#webvtt-cue-line-automatic .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line
      automatic" noexport=""}, which means the offset is to depend on the other showing tracks.

    By default, the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-7 link-type="dfn"} is set to [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-1 link-type="dfn"}.

    If the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-4 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-2 link-type="dfn"}, then the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-8 link-type="dfn"} percentages are relative to the height of the video, otherwise to the width of the video.

    A [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-4 link-type="dfn"} has a [computed line]{#cue-computed-line .dfn .dfn-paneled dfn-type="dfn" lt="cue computed line" noexport=""} whose value is that returned by the following algorithm, which is defined in terms of the other aspects of the cue:

    1.  If the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-9 link-type="dfn"} is numeric, the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-3 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-5 link-type="dfn"} is false, and the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-10 link-type="dfn"} is negative or greater than 100, then return 100 and abort these steps.

        Although the [WebVTT parser](#webvtt-parser){#ref-for-webvtt-parser-1 link-type="dfn"} will not set the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-11 link-type="dfn"} to a number outside the range 0..100 and also set the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-4 link-type="dfn"} to false, this can happen when using the DOM API's [`snapToLines`{.idl}](#dom-vttcue-snaptolines){#ref-for-dom-vttcue-snaptolines-1 link-type="idl"} and [`line`{.idl}](#dom-vttcue-line){#ref-for-dom-vttcue-line-1 link-type="idl"} attributes.

    2.  If the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-12 link-type="dfn"} is numeric, return the value of the [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-13 link-type="dfn"} and abort these steps. (Either the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-5 link-type="dfn"} is true, so any value, not just those in the range 0..100, is valid, or the value is in the range 0..100 and is thus valid regardless of the value of that flag.)

    3.  If the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-6 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-6 link-type="dfn"} is false, return the value 100 and abort these steps. (The [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-14 link-type="dfn"} is the special value [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-2 link-type="dfn"}.)

    4.  Let `cue`{.variable} be the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-7 link-type="dfn"}.

    5.  If `cue`{.variable} is not in a [list of cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-cues){link-type="dfn"} of a [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}, or if that [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} is not in the [list of text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-text-tracks){link-type="dfn"} of a [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"}, return −1 and abort these steps.

    6.  Let `track`{.variable} be the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} whose [list of cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-cues){link-type="dfn"} the `cue`{.variable} is in.

    7.  Let `n`{.variable} be the number of [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} whose [text track mode](https://www.w3.org/TR/html51/semantics-embedded-content.html#a-mode){link-type="dfn"} is [showing](https://www.w3.org/TR/html51/semantics-embedded-content.html#modedef-track-showing){link-type="dfn"} and that are in the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"}'s [list of text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-text-tracks){link-type="dfn"} before `track`{.variable}.

    8.  Increment `n`{.variable} by one.

    9.  Negate `n`{.variable}.

    10. Return `n`{.variable}.

    [](#example-d1c46c31){.self-link}For example, if two [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} are [showing](https://www.w3.org/TR/html51/semantics-embedded-content.html#modedef-track-showing){link-type="dfn"} at the same time in one [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"}, and each [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} currently has an active [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-8 link-type="dfn"} whose [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-15 link-type="dfn"} are both [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-3 link-type="dfn"}, then the first [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}'s cue's [computed line](#cue-computed-line){#ref-for-cue-computed-line-1 link-type="dfn"} will be −1 and the second will be −2.

[A line alignment]{#webvtt-cue-line-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line alignment" noexport=""}

:   An alignment for the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-10 link-type="dfn"}'s [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-16 link-type="dfn"}, one of:

    [Start alignment]{#webvtt-cue-line-start-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line start alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-11 link-type="dfn"}'s top side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-3 link-type="dfn"} cues), left side (for [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-2 link-type="dfn"}), or right side (for [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-2 link-type="dfn"}) is aligned at the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-17 link-type="dfn"}.

    [Center alignment]{#webvtt-cue-line-center-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line center alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-12 link-type="dfn"} is centered at the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-18 link-type="dfn"}.

    [End alignment]{#webvtt-cue-line-end-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue line end alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-13 link-type="dfn"}'s bottom side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-4 link-type="dfn"} cues), right side (for [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-3 link-type="dfn"}), or left side (for [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-3 link-type="dfn"}) is aligned at the [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-19 link-type="dfn"}.

    By default, the [line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-1 link-type="dfn"} is set to [start](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-1 link-type="dfn"}.

    The [line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-2 link-type="dfn"} is separate from the [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-1 link-type="dfn"} --- right-to-left vs. left-to-right cue text does not affect the [line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-3 link-type="dfn"}.

[A position]{#webvtt-cue-position .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position" noexport=""}

:   The [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-3 link-type="dfn"} defines the indent of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-14 link-type="dfn"} in the direction defined by the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-5 link-type="dfn"}.

    The [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-4 link-type="dfn"} is either a number giving the position of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-15 link-type="dfn"} as a percentage value or the special value [auto]{#webvtt-cue-automatic-position .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue
      automatic position" noexport=""}, which means the position is to depend on the [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-2 link-type="dfn"} of the cue.

    If the cue is not within a [region](#webvtt-region){#ref-for-webvtt-region-1 link-type="dfn"}, the percentage value is to be interpreted as a percentage of the video dimensions, otherwise as a percentage of the region dimensions.

    By default, the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-5 link-type="dfn"} is set to [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-1 link-type="dfn"}.

    If the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-6 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-5 link-type="dfn"}, then the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-6 link-type="dfn"} percentages are relative to the width of the video, otherwise to the height of the video.

    A [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-9 link-type="dfn"} has a [computed position]{#cue-computed-position .dfn .dfn-paneled dfn-type="dfn" lt="cue computed position" noexport=""} whose value is that returned by the following algorithm, which is defined in terms of the other aspects of the cue:

    1.  If the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-7 link-type="dfn"} is numeric between 0 and 100, then return the value of the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-8 link-type="dfn"} and abort these steps. (Otherwise, the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-9 link-type="dfn"} is the special value [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-2 link-type="dfn"}.)

    2.  If the [cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-3 link-type="dfn"} is [left](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-1 link-type="dfn"}, return 0 and abort these steps.

    3.  If the [cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-4 link-type="dfn"} is [right](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-1 link-type="dfn"}, return 100 and abort these steps.

    4.  Otherwise, return 50 and abort these steps.

    Since the default value of the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-1 link-type="dfn"} is [center](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-1 link-type="dfn"}, if there is no [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-5 link-type="dfn"} setting for a cue, the [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-10 link-type="dfn"} defaults to 50%.

    Even for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-6 link-type="dfn"} cues with right-to-left cue text, the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-16 link-type="dfn"} is positioned from the left edge of the video viewport. This allows defining a rendering space template which can be filled with either left-to-right or right-to-left cue text, or both.

    For [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-10 link-type="dfn"} that have a [size](#webvtt-cue-size){#ref-for-webvtt-cue-size-3 link-type="dfn"} other than 100%, and a [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-6 link-type="dfn"} of [start](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-1 link-type="dfn"} or [end](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-1 link-type="dfn"}, authors must not use the default [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-3 link-type="dfn"} [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-11 link-type="dfn"}.

    When the [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-7 link-type="dfn"} is [start](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-2 link-type="dfn"} or [end](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-2 link-type="dfn"}, the [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-4 link-type="dfn"} [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-12 link-type="dfn"} is 50%. This is different from [left](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-2 link-type="dfn"} and [right](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-2 link-type="dfn"} aligned text, where the [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-5 link-type="dfn"} [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-13 link-type="dfn"} is 0% and 100%, respectively. The above requirement is present because it can be surprising that automatic positioning doesn't work for [start](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-3 link-type="dfn"} or [end](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-3 link-type="dfn"} aligned text. Since [cue text](#cue-text){#ref-for-cue-text-2 link-type="dfn"} can consist of text with left-to-right base direction, or right-to-left base direction, or both (on different lines), such automatic positioning would have unexpected results.

[A position alignment]{#webvtt-cue-position-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position alignment" noexport=""}

:   An alignment for the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-17 link-type="dfn"} in the dimension of the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-7 link-type="dfn"}, describing what the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-14 link-type="dfn"} is anchored to, one of:

    [Line-left alignment]{#webvtt-cue-position-line-left-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position line-left alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-18 link-type="dfn"}'s left side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-7 link-type="dfn"} cues) or top side (otherwise) is aligned at the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-15 link-type="dfn"}.

    [Center alignment]{#webvtt-cue-position-center-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position center alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-19 link-type="dfn"} is centered at the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-16 link-type="dfn"}.

    [Line-right alignment]{#webvtt-cue-position-line-right-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position line-right alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-20 link-type="dfn"}'s right side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-8 link-type="dfn"} cues) or bottom side (otherwise) is aligned at the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-17 link-type="dfn"}.

    [Auto alignment]{#webvtt-cue-position-automatic-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue position automatic alignment" noexport=""}
    :   The [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-21 link-type="dfn"}'s alignment depends on the value of the [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-8 link-type="dfn"} of the cue.

    By default, the [position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-2 link-type="dfn"} is set to [auto](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-1 link-type="dfn"}.

    A [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-11 link-type="dfn"} has a [computed position alignment]{#cue-computed-position-alignment .dfn .dfn-paneled dfn-type="dfn" lt="cue computed position alignment" noexport=""} whose value is that returned by the following algorithm, which is defined in terms of other aspects of the cue:

    1.  If the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-3 link-type="dfn"} is not [auto](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-2 link-type="dfn"}, then return the value of the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-4 link-type="dfn"} and abort these steps.

    2.  If the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-9 link-type="dfn"} is [left](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-3 link-type="dfn"}, return [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-1 link-type="dfn"} and abort these steps.

    3.  If the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-10 link-type="dfn"} is [right](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-3 link-type="dfn"}, return [line-right](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-1 link-type="dfn"} and abort these steps.

    4.  If the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-11 link-type="dfn"} is [start](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-4 link-type="dfn"}, return [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-2 link-type="dfn"} if the base direction of the cue text is left-to-right, [line-right](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-2 link-type="dfn"} otherwise.

    5.  If the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-12 link-type="dfn"} is [end](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-4 link-type="dfn"}, return [line-right](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-3 link-type="dfn"} if the base direction of the cue text is left-to-right, [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-3 link-type="dfn"} otherwise.

    6.  Otherwise, return [center](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-2 link-type="dfn"}.

    Since the [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-18 link-type="dfn"} always measures from the left of the video (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-9 link-type="dfn"} cues) or the top (otherwise), the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-5 link-type="dfn"} [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-4 link-type="dfn"} value varies between left and top for horizontal and vertical cues.

[A size]{#webvtt-cue-size .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue size" noexport=""}

:   A number giving the size of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-22 link-type="dfn"}, to be interpreted as a percentage of the video, as defined by the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-8 link-type="dfn"}.

    By default, the [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-4 link-type="dfn"} is set to 100%.

    If the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-9 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-10 link-type="dfn"}, then the [size](#webvtt-cue-size){#ref-for-webvtt-cue-size-5 link-type="dfn"} percentages are relative to the width of the video, otherwise to the height of the video.

[A text alignment]{#webvtt-cue-text-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue text alignment" noexport=""}

:   An alignment for all lines of text within the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-23 link-type="dfn"}, in the dimension of the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-10 link-type="dfn"}, one of:

    [Start alignment]{#webvtt-cue-start-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue start alignment" noexport=""}
    :   The text of each line is individually aligned towards the start side of the box, where the start side for that line is determined by using the CSS rules for [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext){.css link-type="maybe"} value of the [unicode-bidi](https://www.w3.org/TR/css-writing-modes-3/#propdef-unicode-bidi){.property link-type="propdesc"} property. [\[CSS-WRITING-MODES-3\]](#biblio-css-writing-modes-3){link-type="biblio"}

    [Center alignment]{#webvtt-cue-center-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue center alignment" noexport=""}
    :   The text is aligned centered between the box's start and end sides.

    [End alignment]{#webvtt-cue-end-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue end alignment" noexport=""}
    :   The text of each line is individually aligned towards the end side of the box, where the end side for that line is determined by using the CSS rules for [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext){.css link-type="maybe"} value of the [unicode-bidi](https://www.w3.org/TR/css-writing-modes-3/#propdef-unicode-bidi){.property link-type="propdesc"} property. [\[CSS-WRITING-MODES-3\]](#biblio-css-writing-modes-3){link-type="biblio"}

    [Left alignment]{#webvtt-cue-left-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue left alignment" noexport=""}
    :   The text is aligned to the box's left side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-11 link-type="dfn"} cues) or top side (otherwise).

    [Right alignment]{#webvtt-cue-right-alignment .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue right alignment" noexport=""}
    :   The text is aligned to the box's right side (for [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-12 link-type="dfn"} cues) or bottom side (otherwise).

    By default, the [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-13 link-type="dfn"} is set to [center](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-3 link-type="dfn"}.

    The base direction of each line in a cue (which is used by the Unicode Bidirectional Algorithm to determine the order in which to display the characters in the line) is determined by looking up the first strong directional character in each line, using the CSS [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext){.css link-type="maybe"} algorithm. In the occasional cases where the first strong character on a line would produce the wrong base direction for that line, the author can use an U+200E LEFT-TO-RIGHT MARK or U+200F RIGHT-TO-LEFT MARK character at the start of the line to correct it. [\[BIDI\]](#biblio-bidi){link-type="biblio"}

    ::: {#example-4a66a3ef .example}
    [](#example-4a66a3ef){.self-link}
    In this example, the second cue will have a right-to-left base direction, rendering as \"[`.I think ,يلاع`{.sample}]{dir="ltr"}\". (Note that the text below shows all characters left-to-right; a text editor would not necessarily have the same rendering.)

        WEBVTT

        00:00:07.000 --> 00:00:09.000
        What was his name again?

        00:00:09.000 --> 00:00:11.000
        عالي, I think.

    To change that line to left-to-right base direction, start the line with an U+200E LEFT-TO-RIGHT MARK character (it can be escaped as \"`&lrm;`\").
    :::

    Where the base direction of some embedded text within a line needs to be different from the surrounding text on that line, this can be achieved by using the paired Unicode bidi formatting code characters.

    ::: {#example-89bafe37 .example}
    [](#example-89bafe37){.self-link}
    In this example, assuming no bidi formatting code characters are used, the cue text is rendered as \"[`I’ve read the book 3 דנליונ times!`{.sample}]{dir="ltr"}\" (i.e. the \"3\" is on the wrong side of the book title) because of the effect of the Unicode Bidirection Algorithm. (Again, the text below shows all characters left-to-right.)

        WEBVTT

        00:00:04.000 --> 00:00:08.000
        I’ve read the book נוילנד 3 times!

    If a U+2068 FIRST STRONG ISOLATE (FSI) character was placed before the book title and a U+2069 POP DIRECTIONAL ISOLATE (PDI) character after it, the rendering would be the intended \"[`I’ve read the book דנליונ 3 times!`{.sample}]{dir="ltr"}\". (Those characters can be escaped as \"`&#x2068;`\" and \"`&#x2069;`\", respectively.)
    :::

    The default text alignment is [center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-4 link-type="dfn"} regardless of the base direction of the cue text. To make the text alignment of each line match the base direction of the line (e.g. left for English, right for Hebrew), use [start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-5 link-type="dfn"}, or [end alignment](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-5 link-type="dfn"} for the opposite alignment.

    ::: {#example-73203b99 .example}
    [](#example-73203b99){.self-link}
    In this example, [start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-6 link-type="dfn"} is used. The first line is left-aligned because the base direction is left-to-right, and the second line is right-aligned because the base direction is right-to-left.

        WEBVTT

        00:00:00.000 --> 00:00:05.000 align:start
        Hello!
        שלום!

    This would render as follows:

        Hello!
                                                    !םולש
    :::

    The [left alignment](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-4 link-type="dfn"} and [right alignment](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-4 link-type="dfn"} can be used to left-align or right-align the cue text regardless of its lines\' base direction.

[A region]{#webvtt-cue-region .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue region" noexport=""}

:   An optional [WebVTT region](#webvtt-region){#ref-for-webvtt-region-2 link-type="dfn"} to which a cue belongs.

    By default, the [region](#webvtt-region){#ref-for-webvtt-region-3 link-type="dfn"} is set to null.

The associated [rules for updating the text track rendering](https://www.w3.org/TR/html51/semantics-embedded-content.html#rules-for-updating-the-text-track-rendering){link-type="dfn"} of [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-12 link-type="dfn"} are the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-1 link-type="dfn"}.

::: impl
When a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-13 link-type="dfn"} whose [active flag](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-active-flag){link-type="dfn"} is set has its [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-11 link-type="dfn"}, [snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-7 link-type="dfn"}, [line](#webvtt-cue-line){#ref-for-webvtt-cue-line-20 link-type="dfn"}, [line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-4 link-type="dfn"}, [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-19 link-type="dfn"}, [position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-6 link-type="dfn"}, [size](#webvtt-cue-size){#ref-for-webvtt-cue-size-6 link-type="dfn"}, [text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-14 link-type="dfn"}, [region](#webvtt-cue-region){#ref-for-webvtt-cue-region-1 link-type="dfn"}, or [text](#cue-text){#ref-for-cue-text-3 link-type="dfn"} change value, then the user agent must empty the [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"}, and then immediately run the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}'s [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-2 link-type="dfn"}.
:::

### [3.4. ]{.secno}[WebVTT caption or subtitle regions]{.content}[](#regions){.self-link} {#regions .heading .settled level="3.4"}

A [WebVTT region]{#webvtt-region .dfn .dfn-paneled dfn-type="dfn" noexport=""} represents a subpart of the video viewport and provides a limited rendering area for [WebVTT caption or subtitle cues](#webvtt-caption-or-subtitle-cue){#ref-for-webvtt-caption-or-subtitle-cue-1 link-type="dfn"}.

Regions provide a means to group caption or subtitle cues so the cues can be rendered together, which is particularly important when scrolling up.

Each [WebVTT region](#webvtt-region){#ref-for-webvtt-region-4 link-type="dfn"} consists of:

[An identifier]{#webvtt-region-identifier .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region identifier" noexport=""}

:   An arbitrary string of zero or more characters other than U+0020 SPACE or U+0009 CHARACTER TABULATION character. The string must not contain the substring \"\--\>\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN). Defaults to the empty string.

[A width]{#webvtt-region-width .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region width" noexport=""}

:   A number giving the width of the box within which the text of each line of the containing cues is to be rendered, to be interpreted as a percentage of the video width. Defaults to 100.

[A lines value]{#webvtt-region-lines .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region lines" noexport=""}

:   A number giving the number of lines of the box within which the text of each line of the containing cues is to be rendered. Defaults to 3.

    Since a WebVTT region defines a fixed rendering area, a cue that has more lines than the region allows will be clipped. For scrolling regions, the clipping happens at the top, for non-scrolling regions it happens at the bottom.

[A region anchor point]{#webvtt-region-anchor .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region anchor" noexport=""}

:   Two numbers giving the x and y coordinates within the region which is anchored to the video viewport and does not change location even when the region does, e.g. because of font size changes. Defaults to (0,100), i.e. the bottom left corner of the region.

[A region viewport anchor point]{#webvtt-region-viewport-anchor .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region viewport anchor" noexport=""}

:   Two numbers giving the x and y coordinates within the video viewport to which the region anchor point is anchored. Defaults to (0,100), i.e. the bottom left corner of the video viewport.

[A scroll value]{#webvtt-region-scroll .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region scroll" noexport=""}

:   One of the following:

    [None]{#webvtt-region-scroll-none .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region scroll none" noexport=""}
    :   Indicates that the cues in the region are not to scroll and instead stay fixed at the location they were first painted in.

    [Up]{#webvtt-region-scroll-up .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT region scroll up" noexport=""}
    :   Indicates that the cues in the region will be added at the bottom of the region and push any already displayed cues in the region up until all lines of the new cue are visible in the region.

::: {.note role="note"}
The following diagram illustrates how anchoring of a region to a video viewport works. The black cross is the anchor, orange explains the anchor's offset within the region and green the anchor's offset within the video viewport. Think of it as sticking a pin through a note onto a board:

<figure>
<img src="webvtt-region-diagram.png" alt="visual explanation of WebVTT regions" />
<figcaption>Image description: Within the video viewport, there is a WebVTT region. Inside the region, there is an anchor point marked with a black cross. The vertical and horizontal distance from the video viewport’s edges to the anchor is marked with green arrows, representing the region viewport anchor X and Y offsets. The vertical and horizontal distance from the region’s edges to the anchor is marked with orange arrows, representing the region anchor X and Y offsets. The size of the region is represented by the region width for the horizontal axis, and region lines for the vertical axis.</figcaption>
</figure>
:::

For parsing, we also need the following:

[A text track list of regions]{#text-track-list-of-regions .dfn .dfn-paneled dfn-type="dfn" lt="text track list of regions" noexport=""}

:   A list of zero or more [WebVTT regions](#webvtt-region){#ref-for-webvtt-region-5 link-type="dfn"}.

### [3.5. ]{.secno}[WebVTT chapter cues]{.content}[](#chapter-cues){.self-link} {#chapter-cues .heading .settled level="3.5"}

A [WebVTT chapter cue[](#webvtt-chapter-cue){.self-link}]{#webvtt-chapter-cue .dfn dfn-type="dfn" noexport=""} is a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-14 link-type="dfn"} whose [cue text](#cue-text){#ref-for-cue-text-4 link-type="dfn"} is interpreted as a chapter title that describes the chapter as a navigation target.

Chapter cues mark up the timeline of a audio or video file in consecutive, non-overlapping intervals. It is further possible to subdivide these intervals into sub-chapters building a navigation tree.

### [3.6. ]{.secno}[WebVTT metadata cues]{.content}[](#metadata-cues){.self-link} {#metadata-cues .heading .settled level="3.6"}

A [WebVTT metadata cue[](#webvtt-metadata-cue){.self-link}]{#webvtt-metadata-cue .dfn dfn-type="dfn" noexport=""} is a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-15 link-type="dfn"} whose [cue text](#cue-text){#ref-for-cue-text-5 link-type="dfn"} is interpreted as time-aligned metadata.

## [4. ]{.secno}[Syntax]{.content}[](#syntax){.self-link} {#syntax .heading .settled level="4"}

### [4.1. ]{.secno}[WebVTT file structure]{.content}[](#file-structure){.self-link} {#file-structure .heading .settled level="4.1"}

A [WebVTT file]{#webvtt-file .dfn .dfn-paneled dfn-type="dfn" noexport=""} must consist of a [WebVTT file body](#webvtt-file-body){#ref-for-webvtt-file-body-1 link-type="dfn"} encoded as UTF-8 and labeled with the [MIME type](https://www.w3.org/TR/html51/infrastructure.html#mime-type){link-type="dfn"} `text/vtt`. [\[RFC3629\]](#biblio-rfc3629){link-type="biblio"}

A [WebVTT file body]{#webvtt-file-body .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the following order:

1.  An optional U+FEFF BYTE ORDER MARK (BOM) character.
2.  The string \"`WEBVTT`\".
3.  Optionally, either a U+0020 SPACE character or a U+0009 CHARACTER TABULATION (tab) character followed by any number of characters that are not U+000A LINE FEED (LF) or U+000D CARRIAGE RETURN (CR) characters.
4.  Two or more [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-1 link-type="dfn"} to terminate the line with the file magic and separate it from the rest of the body.
5.  Zero or more [WebVTT region definition blocks](#webvtt-region-definition-block){#ref-for-webvtt-region-definition-block-1 link-type="dfn"}, [WebVTT style blocks](#webvtt-style-block){#ref-for-webvtt-style-block-1 link-type="dfn"} and [WebVTT comment blocks](#webvtt-comment-block){#ref-for-webvtt-comment-block-1 link-type="dfn"} separated from each other by one or more [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-2 link-type="dfn"}.
6.  Zero or more [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-3 link-type="dfn"}.
7.  Zero or more [WebVTT cue blocks](#webvtt-cue-block){#ref-for-webvtt-cue-block-1 link-type="dfn"} and [WebVTT comment blocks](#webvtt-comment-block){#ref-for-webvtt-comment-block-2 link-type="dfn"} separated from each other by one or more [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-4 link-type="dfn"}.
8.  Zero or more [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-5 link-type="dfn"}.

A [WebVTT line terminator]{#webvtt-line-terminator .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of one of the following:

-   A U+000D CARRIAGE RETURN U+000A LINE FEED (CRLF) character pair.
-   A single U+000A LINE FEED (LF) character.
-   A single U+000D CARRIAGE RETURN (CR) character.

A [WebVTT region definition block]{#webvtt-region-definition-block .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the given order:

1.  The string \"`REGION`\" (U+0052 LATIN CAPITAL LETTER R, U+0045 LATIN CAPITAL LETTER E, U+0047 LATIN CAPITAL LETTER G, U+0049 LATIN CAPITAL LETTER I, U+004F LATIN CAPITAL LETTER O, U+004E LATIN CAPITAL LETTER N).
2.  Zero or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters.
3.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-6 link-type="dfn"}.
4.  A [WebVTT region settings list](#webvtt-region-settings-list){#ref-for-webvtt-region-settings-list-1 link-type="dfn"}.
5.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-7 link-type="dfn"}.

A [WebVTT style block]{#webvtt-style-block .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the given order:

1.  The string \"`STYLE`\" (U+0053 LATIN CAPITAL LETTER S, U+0054 LATIN CAPITAL LETTER T, U+0059 LATIN CAPITAL LETTER Y, U+004C LATIN CAPITAL LETTER L, U+0045 LATIN CAPITAL LETTER E).
2.  Zero or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters.
3.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-8 link-type="dfn"}.
4.  Any sequence of zero or more characters other than U+000A LINE FEED (LF) characters and U+000D CARRIAGE RETURN (CR) characters, each optionally separated from the next by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-9 link-type="dfn"}, except that the entire resulting string must not contain the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN). The string represents a CSS style sheet; the requirements given in the relevant CSS specifications apply. [\[CSS22\]](#biblio-css22){link-type="biblio"}
5.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-10 link-type="dfn"}.

A [WebVTT cue block]{#webvtt-cue-block .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the given order:

1.  Optionally, a [WebVTT cue identifier](#webvtt-cue-identifier){#ref-for-webvtt-cue-identifier-1 link-type="dfn"} followed by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-11 link-type="dfn"}.
2.  [WebVTT cue timings](#webvtt-cue-timings){#ref-for-webvtt-cue-timings-1 link-type="dfn"}.
3.  Optionally, one or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters followed by a [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-1 link-type="dfn"}.
4.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-12 link-type="dfn"}.
5.  The [cue payload]{#cue-payload .dfn .dfn-paneled dfn-type="dfn" noexport=""}: either [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-2 link-type="dfn"}, [WebVTT chapter title text](#webvtt-chapter-title-text){#ref-for-webvtt-chapter-title-text-1 link-type="dfn"}, or [WebVTT metadata text](#webvtt-metadata-text){#ref-for-webvtt-metadata-text-1 link-type="dfn"}, but it must not contain the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN).
6.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-13 link-type="dfn"}.

A [WebVTT cue block](#webvtt-cue-block){#ref-for-webvtt-cue-block-2 link-type="dfn"} corresponds to one piece of time-aligned text or data in the [WebVTT file](#webvtt-file){#ref-for-webvtt-file-7 link-type="dfn"}, for example one subtitle. The [cue payload](#cue-payload){#ref-for-cue-payload-1 link-type="dfn"} is the text or data associated with the cue.

A [WebVTT cue identifier]{#webvtt-cue-identifier .dfn .dfn-paneled dfn-type="dfn" noexport=""} is any sequence of one or more characters not containing the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN), nor containing any U+000A LINE FEED (LF) characters or U+000D CARRIAGE RETURN (CR) characters.

A [WebVTT cue identifier](#webvtt-cue-identifier){#ref-for-webvtt-cue-identifier-2 link-type="dfn"} must be unique amongst all the [WebVTT cue identifiers](#webvtt-cue-identifier){#ref-for-webvtt-cue-identifier-3 link-type="dfn"} of all [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-16 link-type="dfn"} of a [WebVTT file](#webvtt-file){#ref-for-webvtt-file-8 link-type="dfn"}.

A [WebVTT cue identifier](#webvtt-cue-identifier){#ref-for-webvtt-cue-identifier-4 link-type="dfn"} can be used to reference a specific cue, for example from script or CSS.

The [WebVTT cue timings]{#webvtt-cue-timings .dfn .dfn-paneled dfn-type="dfn" noexport=""} part of a [WebVTT cue block](#webvtt-cue-block){#ref-for-webvtt-cue-block-3 link-type="dfn"} consists of the following components, in the given order:

1.  A [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-1 link-type="dfn"} representing the start time offset of the cue. The time represented by this [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-2 link-type="dfn"} must be greater than or equal to the start time offsets of all previous cues in the file.
2.  One or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters.
3.  The string \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN).
4.  One or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters.
5.  A [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-3 link-type="dfn"} representing the end time offset of the cue. The time represented by this [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-4 link-type="dfn"} must be greater than the start time offset of the cue.

The [WebVTT cue timings](#webvtt-cue-timings){#ref-for-webvtt-cue-timings-2 link-type="dfn"} give the start and end offsets of the [WebVTT cue block](#webvtt-cue-block){#ref-for-webvtt-cue-block-4 link-type="dfn"}. Different cues can overlap. Cues are always listed ordered by their start time.

A [WebVTT timestamp]{#webvtt-timestamp .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the given order:

1.  Optionally (required if `hours`{.variable} is non-zero):
    1.  Two or more [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, representing the `hours`{.variable} as a base ten integer.
    2.  A U+003A COLON character (:)
2.  Two [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, representing the `minutes`{.variable} as a base ten integer in the range 0 ≤ `minutes`{.variable} ≤ 59.
3.  A U+003A COLON character (:)
4.  Two [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, representing the `seconds`{.variable} as a base ten integer in the range 0 ≤ `seconds`{.variable} ≤ 59.
5.  A U+002E FULL STOP character (.).
6.  Three [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, representing the thousandths of a second `seconds-frac`{.variable} as a base ten integer.

A [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-5 link-type="dfn"} is always interpreted relative to the [current playback position](https://www.w3.org/TR/html51/semantics-embedded-content.html#current-position){link-type="dfn"} of the media data that the WebVTT file is to be synchronized with.

A [WebVTT cue settings list]{#webvtt-cue-settings-list .dfn .dfn-paneled dfn-type="dfn" noexport=""} consist of a sequence of zero or more [WebVTT cue settings]{#webvtt-cue-setting .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT cue
setting" noexport=""} in any order, separated from each other by one or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters. Each setting consists of the following components, in the order given:

1.  A [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-1 link-type="dfn"}.
2.  An optional U+003A COLON (colon) character.
3.  An optional [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-1 link-type="dfn"}.

A [WebVTT cue setting name]{#webvtt-cue-setting-name .dfn .dfn-paneled dfn-type="dfn" noexport=""} and a [WebVTT cue setting value]{#webvtt-cue-setting-value .dfn .dfn-paneled dfn-type="dfn" noexport=""} each consist of any sequence of one or more characters other than U+000A LINE FEED (LF) characters and - U+000D CARRIAGE RETURN (CR) characters except that the entire resulting string must not contain the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN).

A [WebVTT percentage]{#webvtt-percentage .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components:

1.  One or more [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}.
2.  Optionally:
    1.  A U+002E DOT character (.).
    2.  One or more [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}.
3.  A U+0025 PERCENT SIGN character (%).

When interpreted as a number, a [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-1 link-type="dfn"} must be in the range 0..100.

A [WebVTT comment block]{#webvtt-comment-block .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the given order:

1.  The string \"`NOTE`\".
2.  Optionally, the following components, in the given order:
    1.  Either:
        -   A U+0020 SPACE character or U+0009 CHARACTER TABULATION (tab) character.
        -   A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-14 link-type="dfn"}.
    2.  Any sequence of zero or more characters other than U+000A LINE FEED (LF) characters and U+000D CARRIAGE RETURN (CR) characters, each optionally separated from the next by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-15 link-type="dfn"}, except that the entire resulting string must not contain the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN).
3.  A [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-16 link-type="dfn"}.

A [WebVTT comment block](#webvtt-comment-block){#ref-for-webvtt-comment-block-3 link-type="dfn"} is ignored by the parser.

### [4.2. ]{.secno}[Types of WebVTT cue payload]{.content}[](#types-of-webvtt-cue-payload){.self-link} {#types-of-webvtt-cue-payload .heading .settled level="4.2"}

#### [4.2.1. ]{.secno}[WebVTT metadata text]{.content}[](#metadata-text){.self-link} {#metadata-text .heading .settled level="4.2.1"}

[WebVTT metadata text]{#webvtt-metadata-text .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of any sequence of zero or more characters other than U+000A LINE FEED (LF) characters and U+000D CARRIAGE RETURN (CR) characters, each optionally separated from the next by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-17 link-type="dfn"}. (In other words, any text that does not have two consecutive [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-18 link-type="dfn"} and does not start or end with a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-19 link-type="dfn"}.)

[WebVTT metadata text](#webvtt-metadata-text){#ref-for-webvtt-metadata-text-2 link-type="dfn"} cues are only useful for scripted applications (e.g. using the `metadata` [text track kind](https://www.w3.org/TR/html51/semantics-embedded-content.html#kind-of-track){link-type="dfn"} in a HTML [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}).

#### [4.2.2. ]{.secno}[WebVTT caption or subtitle cue text]{.content}[](#caption-text){.self-link} {#caption-text .heading .settled level="4.2.2"}

[WebVTT caption or subtitle cue text]{#webvtt-caption-or-subtitle-cue-text .dfn .dfn-paneled dfn-type="dfn" noexport=""} is [cue payload](#cue-payload){#ref-for-cue-payload-2 link-type="dfn"} that consists of zero or more [WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-1 link-type="dfn"}, in any order, each optionally separated from the next by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-20 link-type="dfn"}.

The [WebVTT caption or subtitle cue components]{#webvtt-caption-or-subtitle-cue-components .dfn .dfn-paneled dfn-type="dfn" noexport=""} are:

-   A [WebVTT cue class span](#webvtt-cue-class-span){#ref-for-webvtt-cue-class-span-1 link-type="dfn"}.
-   A [WebVTT cue italics span](#webvtt-cue-italics-span){#ref-for-webvtt-cue-italics-span-1 link-type="dfn"}.
-   A [WebVTT cue bold span](#webvtt-cue-bold-span){#ref-for-webvtt-cue-bold-span-1 link-type="dfn"}.
-   A [WebVTT cue underline span](#webvtt-cue-underline-span){#ref-for-webvtt-cue-underline-span-1 link-type="dfn"}.
-   A [WebVTT cue ruby span](#webvtt-cue-ruby-span){#ref-for-webvtt-cue-ruby-span-1 link-type="dfn"}.
-   A [WebVTT cue voice span](#webvtt-cue-voice-span){#ref-for-webvtt-cue-voice-span-1 link-type="dfn"}.
-   A [WebVTT cue language span](#webvtt-cue-language-span){#ref-for-webvtt-cue-language-span-1 link-type="dfn"}.
-   A [WebVTT cue timestamp](#webvtt-cue-timestamp){#ref-for-webvtt-cue-timestamp-1 link-type="dfn"}.
-   A [WebVTT cue text span](#webvtt-cue-text-span){#ref-for-webvtt-cue-text-span-1 link-type="dfn"}, representing the text of the cue.
-   An [HTML character reference](https://www.w3.org/TR/html51/syntax.html#character-references){link-type="dfn"}, representing one or two Unicode code points, as defined in HTML, in the text of the cue. [\[HTML51\]](#biblio-html51){link-type="biblio"}

All [WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-2 link-type="dfn"} bar the HTML character reference may have one or more [cue component class names]{#cue-component-class-names .dfn .dfn-paneled dfn-type="dfn" noexport=""} attached to it by separating the cue component class name from the cue component start tag using the period (\'.\') notation. The class name must immediately follow the \"period\" (.).

[WebVTT cue internal text]{#webvtt-cue-internal-text .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of an optional [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-21 link-type="dfn"}, followed by zero or more [WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-3 link-type="dfn"}, in any order, each optionally followed by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-22 link-type="dfn"}.

A [WebVTT cue class span]{#webvtt-cue-class-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of a [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-1 link-type="dfn"} \"`c`\" that disallows an annotation, [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-1 link-type="dfn"} representing cue text, and a [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-1 link-type="dfn"} \"`c`\".

A [WebVTT cue italics span]{#webvtt-cue-italics-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of a [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-2 link-type="dfn"} \"`i`\" that disallows an annotation, [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-2 link-type="dfn"} representing the italicized text, and a [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-2 link-type="dfn"} \"`i`\".

A [WebVTT cue bold span]{#webvtt-cue-bold-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of a [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-3 link-type="dfn"} \"`b`\" that disallows an annotation, [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-3 link-type="dfn"} representing the boldened text, and a [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-3 link-type="dfn"} \"`b`\".

A [WebVTT cue underline span]{#webvtt-cue-underline-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of a [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-4 link-type="dfn"} \"`u`\" that disallows an annotation, [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-4 link-type="dfn"} representing the underlined text, and a [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-4 link-type="dfn"} \"`u`\".

A [WebVTT cue ruby span]{#webvtt-cue-ruby-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  A [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-5 link-type="dfn"} \"`ruby`\" that disallows an annotation.
2.  One or more occurrences of the following group of components, in the order given:
    1.  [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-5 link-type="dfn"}, representing the ruby base.
    2.  A [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-6 link-type="dfn"} \"`rt`\" that disallows an annotation.
    3.  A [WebVTT cue ruby text span]{#webvtt-cue-ruby-text-span .dfn .dfn-paneled dfn-type="dfn" noexport=""}: [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-6 link-type="dfn"}, representing the ruby text component of the ruby annotation.
    4.  A [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-5 link-type="dfn"} \"`rt`\". If this is the last occurrence of this group of components in the [WebVTT cue ruby span](#webvtt-cue-ruby-span){#ref-for-webvtt-cue-ruby-span-2 link-type="dfn"}, then this last end tag string may be omitted.
3.  If the last end tag string was not omitted: Optionally, a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-23 link-type="dfn"}.
4.  If the last end tag string was not omitted: Zero or more U+0020 SPACE characters or U+0009 CHARACTER TABULATION (tab) characters, each optionally followed by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-24 link-type="dfn"}.
5.  A [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-6 link-type="dfn"} \"`ruby`\".

Cue positioning controls the positioning of the baseline text, not the ruby text.

Ruby in WebVTT is a subset of the ruby features in HTML. This might be extended in the future to also support an object for ruby base text as well as complex ruby, when these features are more mature in HTML and CSS. [\[HTML51\]](#biblio-html51){link-type="biblio"} [\[CSS3-RUBY\]](#biblio-css3-ruby){link-type="biblio"}

A [WebVTT cue voice span]{#webvtt-cue-voice-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  A [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-7 link-type="dfn"} \"`v`\" that requires an annotation; the annotation represents the name of the voice.
2.  [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-7 link-type="dfn"}.
3.  A [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-7 link-type="dfn"} \"`v`\". If this [WebVTT cue voice span](#webvtt-cue-voice-span){#ref-for-webvtt-cue-voice-span-2 link-type="dfn"} is the only [component](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-4 link-type="dfn"} of its [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-3 link-type="dfn"} sequence, then the end tag may be omitted for brevity.

A [WebVTT cue language span]{#webvtt-cue-language-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  A [WebVTT cue span start tag](#webvtt-cue-span-start-tag){#ref-for-webvtt-cue-span-start-tag-8 link-type="dfn"} \"`lang`\" that requires an annotation; the annotation represents the language of the following component, and must be a valid BCP 47 language tag. [\[BCP47\]](#biblio-bcp47){link-type="biblio"}
2.  [WebVTT cue internal text](#webvtt-cue-internal-text){#ref-for-webvtt-cue-internal-text-8 link-type="dfn"}.
3.  A [WebVTT cue span end tag](#webvtt-cue-span-end-tag){#ref-for-webvtt-cue-span-end-tag-8 link-type="dfn"} \"`lang`\".

The requirement above regarding valid BCP 47 language tag is an authoring requirement, so a conformance checker will do validity checking of the language tag, but other user agents will not.

A [WebVTT cue span start tag]{#webvtt-cue-span-start-tag .dfn .dfn-paneled dfn-type="dfn" noexport=""} has a `tag name`{.variable} and either requires or disallows an annotation, and consists of the following components, in the order given:

1.  A U+003C LESS-THAN SIGN character (\<).

2.  The `tag name`{.variable}.

3.  Zero or more occurrences of the following sequence:
    1.  U+002E FULL STOP character (.)
    2.  One or more characters other than U+0009 CHARACTER TABULATION (tab) characters, U+000A LINE FEED (LF) characters, U+000D CARRIAGE RETURN (CR) characters, U+0020 SPACE characters, U+0026 AMPERSAND characters (&), U+003C LESS-THAN SIGN characters (\<), U+003E GREATER-THAN SIGN characters (\>), and U+002E FULL STOP characters (.), representing a class that describes the cue span's significance.

4.  If the start tag requires an annotation: a U+0020 SPACE character or a U+0009 CHARACTER TABULATION (tab) character, followed by one or more of the following components, the concatenation of their representations having a value that contains at least one character other than U+0020 SPACE and U+0009 CHARACTER TABULATION (tab) characters:

    -   [WebVTT cue span start tag annotation text](#webvtt-cue-span-start-tag-annotation-text){#ref-for-webvtt-cue-span-start-tag-annotation-text-1 link-type="dfn"}, representing the text of the annotation.
    -   An [HTML character reference](https://www.w3.org/TR/html51/syntax.html#character-references){link-type="dfn"}, representing one or two Unicode code points, as defined in HTML, in the text of the annotation. [\[HTML51\]](#biblio-html51){link-type="biblio"}

5.  A U+003E GREATER-THAN SIGN character (\>).

A [WebVTT cue span end tag]{#webvtt-cue-span-end-tag .dfn .dfn-paneled dfn-type="dfn" noexport=""} has a `tag name`{.variable} and consists of the following components, in the order given:

1.  A U+003C LESS-THAN SIGN character (\<).
2.  U+002F SOLIDUS character (/).
3.  The `tag name`{.variable}.
4.  A U+003E GREATER-THAN SIGN character (\>).

A [WebVTT cue timestamp]{#webvtt-cue-timestamp .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of a U+003C LESS-THAN SIGN character (\<), followed by a [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-6 link-type="dfn"} representing the time that the given point in the cue becomes active, followed by a U+003E GREATER-THAN SIGN character (\>). The time represented by the [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-7 link-type="dfn"} must be greater than the times represented by any previous [WebVTT cue timestamps](#webvtt-cue-timestamp){#ref-for-webvtt-cue-timestamp-2 link-type="dfn"} in the cue, as well as greater than the cue's start time offset, and less than the cue's end time offset.

A [WebVTT cue text span]{#webvtt-cue-text-span .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of one or more characters other than U+000A LINE FEED (LF) characters, U+000D CARRIAGE RETURN (CR) characters, U+0026 AMPERSAND characters (&), and U+003C LESS-THAN SIGN characters (\<).

[WebVTT cue span start tag annotation text]{#webvtt-cue-span-start-tag-annotation-text .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of one or more characters other than U+000A LINE FEED (LF) characters, U+000D CARRIAGE RETURN (CR) characters, U+0026 AMPERSAND characters (&), and U+003E GREATER-THAN SIGN characters (\>).

#### [4.2.3. ]{.secno}[WebVTT chapter title text]{.content}[](#chapter-title-text){.self-link} {#chapter-title-text .heading .settled level="4.2.3"}

[WebVTT chapter title text]{#webvtt-chapter-title-text .dfn .dfn-paneled dfn-type="dfn" noexport=""} is [cue text](#cue-text){#ref-for-cue-text-6 link-type="dfn"} that makes use of zero or more of the following components, each optionally separated from the next by a [WebVTT line terminator](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-25 link-type="dfn"}:

-   [WebVTT cue text span](#webvtt-cue-text-span){#ref-for-webvtt-cue-text-span-2 link-type="dfn"}
-   [HTML character reference](https://www.w3.org/TR/html51/syntax.html#character-references){link-type="dfn"} [\[HTML51\]](#biblio-html51){link-type="biblio"}

### [4.3. ]{.secno}[WebVTT region settings]{.content}[](#region-settings){.self-link} {#region-settings .heading .settled level="4.3"}

A [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-2 link-type="dfn"} can contain a reference to a [WebVTT region](#webvtt-region){#ref-for-webvtt-region-6 link-type="dfn"}. To define a region, a [WebVTT region definition block](#webvtt-region-definition-block){#ref-for-webvtt-region-definition-block-2 link-type="dfn"} is specified.

The [WebVTT region settings list]{#webvtt-region-settings-list .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of zero or more of the following components, in any order, separated from each other by one or more U+0020 SPACE characters, U+0009 CHARACTER TABULATION (tab) characters, or [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-26 link-type="dfn"}, except that the string must not contain two consecutive [WebVTT line terminators](#webvtt-line-terminator){#ref-for-webvtt-line-terminator-27 link-type="dfn"}. Each component must not be included more than once per [WebVTT region settings list](#webvtt-region-settings-list){#ref-for-webvtt-region-settings-list-2 link-type="dfn"} string.

-   A [WebVTT region identifier setting](#webvtt-region-identifier-setting){#ref-for-webvtt-region-identifier-setting-1 link-type="dfn"}.
-   A [WebVTT region width setting](#webvtt-region-width-setting){#ref-for-webvtt-region-width-setting-1 link-type="dfn"}.
-   A [WebVTT region lines setting](#webvtt-region-lines-setting){#ref-for-webvtt-region-lines-setting-1 link-type="dfn"}.
-   A [WebVTT region anchor setting](#webvtt-region-anchor-setting){#ref-for-webvtt-region-anchor-setting-1 link-type="dfn"}.
-   A [WebVTT region viewport anchor setting](#webvtt-region-viewport-anchor-setting){#ref-for-webvtt-region-viewport-anchor-setting-1 link-type="dfn"}.
-   A [WebVTT region scroll setting](#webvtt-region-scroll-setting){#ref-for-webvtt-region-scroll-setting-1 link-type="dfn"}.

The [WebVTT region settings list](#webvtt-region-settings-list){#ref-for-webvtt-region-settings-list-3 link-type="dfn"} gives configuration options regarding the dimensions, positioning and anchoring of the region. For example, it allows a group of cues within a region to be anchored in the center of the region and the center of the video viewport. In this example, when the font size grows, the region grows uniformly in all directions from the center.

A [WebVTT region identifier setting]{#webvtt-region-identifier-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`id`\".

2.  A U+003A COLON character (:).

3.  An arbitrary string of one or more characters other than [ASCII whitespace](https://www.w3.org/TR/html51/infrastructure.html#space-characters){link-type="dfn"}. The string must not contain the substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN).

A [WebVTT region identifier setting](#webvtt-region-identifier-setting){#ref-for-webvtt-region-identifier-setting-2 link-type="dfn"} must be unique amongst all the [WebVTT region identifier settings](#webvtt-region-identifier-setting){#ref-for-webvtt-region-identifier-setting-3 link-type="dfn"} of all [WebVTT regions](#webvtt-region){#ref-for-webvtt-region-7 link-type="dfn"} of a [WebVTT file](#webvtt-file){#ref-for-webvtt-file-9 link-type="dfn"}.

A [WebVTT region identifier setting](#webvtt-region-identifier-setting){#ref-for-webvtt-region-identifier-setting-4 link-type="dfn"} must be present in each [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-3 link-type="dfn"}. Without an identifier, it is not possible to associate a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-17 link-type="dfn"} with a [WebVTT region](#webvtt-region){#ref-for-webvtt-region-8 link-type="dfn"} in the syntax.

The [WebVTT region identifier setting](#webvtt-region-identifier-setting){#ref-for-webvtt-region-identifier-setting-5 link-type="dfn"} gives a name to the region so it can be referenced by the cues that belong to the region.

A [WebVTT region width setting]{#webvtt-region-width-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`width`\".

2.  A U+003A COLON character (:).

3.  A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-2 link-type="dfn"}.

The [WebVTT region width setting](#webvtt-region-width-setting){#ref-for-webvtt-region-width-setting-2 link-type="dfn"} provides a fixed width as a percentage of the video width for the region into which cues are rendered and based on which alignment is calculated.

A [WebVTT region lines setting]{#webvtt-region-lines-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`lines`\".

2.  A U+003A COLON character (:).

3.  One or more [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}.

The [WebVTT region lines setting](#webvtt-region-lines-setting){#ref-for-webvtt-region-lines-setting-2 link-type="dfn"} provides a fixed height as a number of lines for the region into which cues are rendered. As such, it defines the height of the roll-up region if it is a scroll region.

A [WebVTT region anchor setting]{#webvtt-region-anchor-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`regionanchor`\".

2.  A U+003A COLON character (:).

3.  A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-3 link-type="dfn"}.

4.  A U+002C COMMA character (,).

5.  A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-4 link-type="dfn"}.

The [WebVTT region anchor setting](#webvtt-region-anchor-setting){#ref-for-webvtt-region-anchor-setting-2 link-type="dfn"} provides a tuple of two percentages that specify the point within the region box that is fixed in location. The first percentage measures the x-dimension and the second percentage y-dimension from the top left corner of the region box. If no [WebVTT region anchor setting](#webvtt-region-anchor-setting){#ref-for-webvtt-region-anchor-setting-3 link-type="dfn"} is given, the anchor defaults to 0%, 100% (i.e. the bottom left corner).

A [WebVTT region viewport anchor setting]{#webvtt-region-viewport-anchor-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`viewportanchor`\".

2.  A U+003A COLON character (:).

3.  A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-5 link-type="dfn"}.

4.  A U+002C COMMA character (,).

5.  A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-6 link-type="dfn"}.

The [WebVTT region viewport anchor setting](#webvtt-region-viewport-anchor-setting){#ref-for-webvtt-region-viewport-anchor-setting-2 link-type="dfn"} provides a tuple of two percentages that specify the point within the video viewport that the region anchor point is anchored to. The first percentage measures the x-dimension and the second percentage measures the y-dimension from the top left corner of the video viewport box. If no region viewport anchor is given, it defaults to 0%, 100% (i.e. the bottom left corner).

For browsers, the region maps to an absolute positioned CSS box relative to the video viewport, i.e. there is a relative positioned box that represents the video viewport relative to which the regions are absolutely positioned. Overflow is hidden.

A [WebVTT region scroll setting]{#webvtt-region-scroll-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`scroll`\".

2.  A U+003A COLON character (:).

3.  The string \"`up`\".

The [WebVTT region scroll setting](#webvtt-region-scroll-setting){#ref-for-webvtt-region-scroll-setting-2 link-type="dfn"} specifies whether cues rendered into the region are allowed to move out of their initial rendering place and roll up, i.e. move towards the top of the video viewport. If the scroll setting is omitted, cues do not move from their rendered position.

Cues are added to a region one line at a time below existing cue lines. When an existing rendered cue line is removed, and it was above another already rendered cue line, that cue line moves into its space, thus scrolling in the given direction. If there is not enough space for a new cue line to be added to a region, the top-most cue line is pushed off the visible region (thus slowly becoming invisible as it moves into overflow:hidden). This eventually makes space for the new cue line and allows it to be added.

When there is no scroll direction, cue lines are added in the empty line closest to the line in the bottom of the region. If no empty line is available, the oldest line is replaced.

### [4.4. ]{.secno}[WebVTT cue settings]{.content}[](#cue-settings){.self-link} {#cue-settings .heading .settled level="4.4"}

A [WebVTT cue setting](#webvtt-cue-setting){#ref-for-webvtt-cue-setting-1 link-type="dfn"} is part of a [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-4 link-type="dfn"} and provides configuration options regarding the position and alignment of the cue box and the cue text within.

For example, a set of WebVTT cue settings may allow a cue box to be aligned to the left or positioned at the top right with the cue text within center aligned.

The current available [WebVTT cue settings](#webvtt-cue-setting){#ref-for-webvtt-cue-setting-2 link-type="dfn"} that may appear in a [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-5 link-type="dfn"} are:

-   A [WebVTT vertical text cue setting](#webvtt-vertical-text-cue-setting){#ref-for-webvtt-vertical-text-cue-setting-1 link-type="dfn"}.
-   A [WebVTT line cue setting](#webvtt-line-cue-setting){#ref-for-webvtt-line-cue-setting-1 link-type="dfn"}.
-   A [WebVTT position cue setting](#webvtt-position-cue-setting){#ref-for-webvtt-position-cue-setting-1 link-type="dfn"}.
-   A [WebVTT size cue setting](#webvtt-size-cue-setting){#ref-for-webvtt-size-cue-setting-1 link-type="dfn"}.
-   A [WebVTT alignment cue setting](#webvtt-alignment-cue-setting){#ref-for-webvtt-alignment-cue-setting-1 link-type="dfn"}.
-   A [WebVTT region cue setting](#webvtt-region-cue-setting){#ref-for-webvtt-region-cue-setting-1 link-type="dfn"}.

Each of these setting must not be included more than once per [WebVTT cue settings list](#webvtt-cue-settings-list){#ref-for-webvtt-cue-settings-list-6 link-type="dfn"}.

A [WebVTT vertical text cue setting]{#webvtt-vertical-text-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} is a [WebVTT cue setting](#webvtt-cue-setting){#ref-for-webvtt-cue-setting-3 link-type="dfn"} that consists of the following components, in the order given:

1.  The string \"`vertical`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-2 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  One of the following strings as the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-2 link-type="dfn"}: \"`rl`\", \"`lr`\".

A [WebVTT vertical text cue setting](#webvtt-vertical-text-cue-setting){#ref-for-webvtt-vertical-text-cue-setting-2 link-type="dfn"} configures the cue to use vertical text layout rather than horizontal text layout. Vertical text layout is sometimes used in Japanese, for example. The default is horizontal layout.

A [WebVTT line cue setting]{#webvtt-line-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`line`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-3 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  As the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-3 link-type="dfn"}:
    1.  an offset value, either:

        To represent a specific offset relative to the video viewport

        :   A [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-7 link-type="dfn"}.

        Or to represent a line number

        :   1.  Optionally a U+002D HYPHEN-MINUS character (-).
            2.  One or more [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}.
    2.  An optional alignment value consisting of the following components:
        1.  A U+002C COMMA character (,).
        2.  One of the following strings: \"`start`\", \"`center`\", \"`end`\"

A [WebVTT line cue setting](#webvtt-line-cue-setting){#ref-for-webvtt-line-cue-setting-2 link-type="dfn"} configures the offset of the cue box from the video viewport's edge in the direction orthogonal to the [writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-12 link-type="dfn"}. For horizontal cues, this is the vertical offset from the top of the video viewport, for vertical cues, it's the horizontal offset. The offset is for the [start](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-2 link-type="dfn"}, [center](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-1 link-type="dfn"}, or [end](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-1 link-type="dfn"} of the cue box, depending on the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-5 link-type="dfn"} value - [start](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-3 link-type="dfn"} by default. The offset can be given either as a percentage of the relevant writing-mode dependent video viewport dimension or as a line number. Line numbers are based on the size of the first line of the cue. Positive line numbers count from the start of the video viewport (the first line is numbered 0), negative line numbers from the end of the video viewport (the last line is numbered −1).

A [WebVTT position cue setting]{#webvtt-position-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`position`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-4 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  As the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-4 link-type="dfn"}:
    1.  a position value consisting of: a [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-8 link-type="dfn"}.
    2.  an optional alignment value consisting of:
        1.  A U+002C COMMA character (,).
        2.  One of the following strings: \"`line-left`\", \"`center`\", \"`line-right`\"

A [WebVTT position cue setting](#webvtt-position-cue-setting){#ref-for-webvtt-position-cue-setting-2 link-type="dfn"} configures the indent position of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-24 link-type="dfn"} in the direction orthogonal to the [WebVTT line cue setting](#webvtt-line-cue-setting){#ref-for-webvtt-line-cue-setting-3 link-type="dfn"}. For horizontal cues, this is the horizontal position. The cue position is given as a percentage of the video viewport. The positioning is for the [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-5 link-type="dfn"}, [center](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-1 link-type="dfn"}, or [line-right](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-4 link-type="dfn"} of the cue box, depending on the cue's [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-1 link-type="dfn"}, which is overridden by the [WebVTT position cue setting](#webvtt-position-cue-setting){#ref-for-webvtt-position-cue-setting-3 link-type="dfn"}.

A [WebVTT size cue setting]{#webvtt-size-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`size`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-5 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  As the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-5 link-type="dfn"}: a [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-9 link-type="dfn"}.

A [WebVTT size cue setting](#webvtt-size-cue-setting){#ref-for-webvtt-size-cue-setting-2 link-type="dfn"} configures the size of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-25 link-type="dfn"} in the same direction as the [WebVTT position cue setting](#webvtt-position-cue-setting){#ref-for-webvtt-position-cue-setting-4 link-type="dfn"}. For horizontal cues, this is the width of the [cue box](#webvtt-cue-box){#ref-for-webvtt-cue-box-26 link-type="dfn"}. It is given as a percentage of the width of the video viewport.

A [WebVTT alignment cue setting]{#webvtt-alignment-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`align`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-6 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  One of the following strings as the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-6 link-type="dfn"}: \"`start`\", \"`center`\", \"`end`\", \"`left`\", \"`right`\"

A [WebVTT alignment cue setting](#webvtt-alignment-cue-setting){#ref-for-webvtt-alignment-cue-setting-2 link-type="dfn"} configures the alignment of the text within the cue. The \"`start`\" and \"`end`\" keywords are relative to the cue text's lines\' base direction; for left-to-right English text, \"`start`\" means left-aligned.

A [WebVTT region cue setting]{#webvtt-region-cue-setting .dfn .dfn-paneled dfn-type="dfn" noexport=""} consists of the following components, in the order given:

1.  The string \"`region`\" as the [WebVTT cue setting name](#webvtt-cue-setting-name){#ref-for-webvtt-cue-setting-name-7 link-type="dfn"}.

2.  A U+003A COLON character (:).

3.  As the [WebVTT cue setting value](#webvtt-cue-setting-value){#ref-for-webvtt-cue-setting-value-7 link-type="dfn"}: a [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-1 link-type="dfn"}.

A [WebVTT region cue setting](#webvtt-region-cue-setting){#ref-for-webvtt-region-cue-setting-2 link-type="dfn"} configures a cue to become part of a region by referencing the region's identifier unless the cue has a [\"vertical\"](#webvtt-vertical-text-cue-setting){#ref-for-webvtt-vertical-text-cue-setting-3 link-type="dfn"}, [\"line\"](#webvtt-line-cue-setting){#ref-for-webvtt-line-cue-setting-4 link-type="dfn"} or [\"size\"](#webvtt-size-cue-setting){#ref-for-webvtt-size-cue-setting-3 link-type="dfn"} cue setting. If a cue is part of a region, its cue settings for [\"position\"](#webvtt-position-cue-setting){#ref-for-webvtt-position-cue-setting-5 link-type="dfn"} and [\"align\"](#webvtt-alignment-cue-setting){#ref-for-webvtt-alignment-cue-setting-3 link-type="dfn"} are applied to the line boxes in the cue relative to the region box and the cue box width and height are calculated relative to the region dimensions rather than the viewport dimensions.

### [4.5. ]{.secno}[Properties of cue sequences]{.content}[](#properties-of-cue-sequences){.self-link} {#properties-of-cue-sequences .heading .settled level="4.5"}

#### [4.5.1. ]{.secno}[WebVTT file using only nested cues]{.content}[](#file-using-only-nested-cues){.self-link} {#file-using-only-nested-cues .heading .settled level="4.5.1"}

A [WebVTT file](#webvtt-file){#ref-for-webvtt-file-10 link-type="dfn"} whose cues all follow the following rules is said to be a [WebVTT file using only nested cues]{#webvtt-file-using-only-nested-cues .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT file using only nested cues" noexport=""}:

given any two cues `cue1`{.variable} and `cue2`{.variable} with start and end time offsets (`x1`{.variable}, `y1`{.variable}) and (`x2`{.variable}, `y2`{.variable}) respectively,

-   either `cue1`{.variable} lies fully within `cue2`{.variable}, i.e. `x1`{.variable} \>= `x2`{.variable} and `y1`{.variable} \<= `y2`{.variable}
-   or `cue1`{.variable} fully contains `cue2`{.variable}, i.e. `x1`{.variable} \<= `x2`{.variable} and `y1`{.variable} \>= `y2`{.variable}.

::: {#example-0689f1d2 .example}
[](#example-0689f1d2){.self-link}

The following example matches this definition:

    WEBVTT

    00:00.000 --> 01:24.000
    Introduction

    00:00.000 --> 00:44.000
    Topics

    00:44.000 --> 01:19.000
    Presenters

    01:24.000 --> 05:00.000
    Scrolling Effects

    01:35.000 --> 03:00.000
    Achim’s Demo

    03:00.000 --> 05:00.000
    Timeline Panel

Notice how you can express the cues in this WebVTT file as a tree structure:

-   WebVTT file
    -   Introduction
        -   Topics
        -   Presenters
    -   Scrolling Effects
        -   Achim's Demo
        -   Timeline Panel

If the file has cues that can't be expressed in this fashion, then they don't match the definition of a [WebVTT file using only nested cues](#webvtt-file-using-only-nested-cues){#ref-for-webvtt-file-using-only-nested-cues-1 link-type="dfn"}. For example:

    WEBVTT

    00:00.000 --> 01:00.000
    The First Minute

    00:30.000 --> 01:30.000
    The Final Minute

In this ninety-second example, the two cues partly overlap, with the first ending before the second ends and the second starting before the first ends. This therefore is not a [WebVTT file using only nested cues](#webvtt-file-using-only-nested-cues){#ref-for-webvtt-file-using-only-nested-cues-2 link-type="dfn"}.
:::

### [4.6. ]{.secno}[Types of WebVTT files]{.content}[](#types-of-webvtt-files){.self-link} {#types-of-webvtt-files .heading .settled level="4.6"}

The syntax definition of WebVTT files allows authoring of a wide variety of WebVTT files with a mix of cues. However, only a small subset of WebVTT file types are typically authored.

Conformance checkers, when validating [WebVTT files](#webvtt-file){#ref-for-webvtt-file-11 link-type="dfn"}, may offer to restrict syntax checking for validating these types.

#### [4.6.1. ]{.secno}[WebVTT file using metadata content]{.content}[](#file-using-metadata-content){.self-link} {#file-using-metadata-content .heading .settled level="4.6.1"}

A [WebVTT file](#webvtt-file){#ref-for-webvtt-file-12 link-type="dfn"} whose cues all have a [cue payload](#cue-payload){#ref-for-cue-payload-3 link-type="dfn"} that is [WebVTT metadata text](#webvtt-metadata-text){#ref-for-webvtt-metadata-text-3 link-type="dfn"} is said to be a [WebVTT file using metadata content[](#webvtt-file-using-metadata-content){.self-link}]{#webvtt-file-using-metadata-content .dfn dfn-type="dfn" noexport=""}.

#### [4.6.2. ]{.secno}[WebVTT file using chapter title text]{.content}[](#file-using-chapter-title-text){.self-link} {#file-using-chapter-title-text .heading .settled level="4.6.2"}

A [WebVTT file using chapter title text[](#webvtt-file-using-chapter-title-text){.self-link}]{#webvtt-file-using-chapter-title-text .dfn dfn-type="dfn" noexport=""} is a [WebVTT file using only nested cues](#webvtt-file-using-only-nested-cues){#ref-for-webvtt-file-using-only-nested-cues-3 link-type="dfn"} whose cues all have a [cue payload](#cue-payload){#ref-for-cue-payload-4 link-type="dfn"} that is [WebVTT chapter title text](#webvtt-chapter-title-text){#ref-for-webvtt-chapter-title-text-2 link-type="dfn"}.

#### [4.6.3. ]{.secno}[WebVTT file using caption or subtitle cue text]{.content}[](#file-using-cue-text){.self-link} {#file-using-cue-text .heading .settled level="4.6.3"}

A [WebVTT file](#webvtt-file){#ref-for-webvtt-file-13 link-type="dfn"} whose cues all have a [cue payload](#cue-payload){#ref-for-cue-payload-5 link-type="dfn"} that is [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-4 link-type="dfn"} is said to be a [WebVTT file using caption or subtitle cue text[](#webvtt-file-using-caption-or-subtitle-cue-text){.self-link}]{#webvtt-file-using-caption-or-subtitle-cue-text .dfn dfn-type="dfn" noexport=""}.

## [5. ]{.secno}[Default classes for WebVTT Caption or Subtitle Cue Components]{.content}[](#default-classes){.self-link} {#default-classes .heading .settled level="5"}

Many captioning formats have simple ways of specifying a limited subset of text colors and background colors for text. Therefore, the WebVTT spec makes available a set of default [cue component class names](#cue-component-class-names){#ref-for-cue-component-class-names-1 link-type="dfn"} for [WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-5 link-type="dfn"} that authors can use in a standard way to mark up colored text and text background.

User agents that support CSS style sheets may implement this section through adding User Agent stylesheets.

### [5.1. ]{.secno}[Default text colors]{.content}[](#default-text-color){.self-link} {#default-text-color .heading .settled level="5.1"}

[WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-6 link-type="dfn"} that have one or more [class names](#cue-component-class-names){#ref-for-cue-component-class-names-2 link-type="dfn"} matching those in the first cell of a row in the table below must set their [color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"} property as [presentational hints](https://html.spec.whatwg.org/multipage/rendering.html#presentational-hints){link-type="dfn"} to the value in the second cell of the row:

[class names](#cue-component-class-names){#ref-for-cue-component-class-names-3 link-type="dfn"}

[color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"} value

`white`

[rgba(255,255,255,1)]{.css}

`lime`

[rgba(0,255,0,1)]{.css}

`cyan`

[rgba(0,255,255,1)]{.css}

`red`

[rgba(255,0,0,1)]{.css}

`yellow`

[rgba(255,255,0,1)]{.css}

`magenta`

[rgba(255,0,255,1)]{.css}

`blue`

[rgba(0,0,255,1)]{.css}

`black`

[rgba(0,0,0,1)]{.css}

If your background is captioning, don't get confused: The color for the class `lime` is what has traditionally been used in captioning under the name [green](https://www.w3.org/TR/css-color-4/#valdef-color-green){.css link-type="maybe"} (e.g. 608/708).

Do not use the classes `blue` and `black` on the default dark background, since they result in unreadable text. In general, please refer to WCAG for guidance on color contrast [\[WCAG20\]](#biblio-wcag20){link-type="biblio"} and make sure to take into account the text color, background color and also the video's color.

### [5.2. ]{.secno}[Default text background colors]{.content}[](#default-text-background){.self-link} {#default-text-background .heading .settled level="5.2"}

[WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components){#ref-for-webvtt-caption-or-subtitle-cue-components-7 link-type="dfn"} that have one or more [class names](#cue-component-class-names){#ref-for-cue-component-class-names-4 link-type="dfn"} matching those in the first cell of a row in the table below must set their [background-color](https://www.w3.org/TR/css3-background/#propdef-background-color){.property link-type="propdesc"} property as [presentational hints](https://html.spec.whatwg.org/multipage/rendering.html#presentational-hints){link-type="dfn"} to the value in the second cell of the row:

[class names](#cue-component-class-names){#ref-for-cue-component-class-names-5 link-type="dfn"}

[background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} value

`bg_white`

[rgba(255,255,255,1)]{.css}

`bg_lime`

[rgba(0,255,0,1)]{.css}

`bg_cyan`

[rgba(0,255,255,1)]{.css}

`bg_red`

[rgba(255,0,0,1)]{.css}

`bg_yellow`

[rgba(255,255,0,1)]{.css}

`bg_magenta`

[rgba(255,0,255,1)]{.css}

`bg_blue`

[rgba(0,0,255,1)]{.css}

`bg_black`

[rgba(0,0,0,1)]{.css}

The color for the class `bg_lime` is what has traditionally been used in captioning under the name [green](https://www.w3.org/TR/css-color-4/#valdef-color-green){.css link-type="maybe"} (e.g. 608/708).

For the purpose of determining the [cascade](https://www.w3.org/TR/css-cascade-4/#cascade){link-type="dfn"} of the color and background classes, the order of appearance determines the cascade of the classes.

::: {#example-a15d9824 .example}
[](#example-a15d9824){.self-link}

This example shows how to use the classes.

    WEBVTT

    02:00.000 --> 02:05.000
    <c.yellow.bg_blue>This is yellow text on a blue background</c>

    04:00.000 --> 04:05.000
    <c.yellow.bg_blue.magenta.bg_black>This is magenta text on a black background</c>
:::

Default classes can be changed by authors, e.g. ::cue(.yellow) {color:cyan} would change all .yellow classed text to cyan.

## [6. ]{.secno}[Parsing]{.content}[](#parsing){.self-link} {#parsing .heading .settled level="6"}

WebVTT file parsing is the same for all types of WebVTT files, including captions, subtitles, chapters, or metadata. Most of the steps will be skipped for chapters or metadata files.

### [6.1. ]{.secno}[WebVTT file parsing]{.content}[](#file-parsing){.self-link} {#file-parsing .heading .settled .algorithm algorithm="WebVTT file parsing" level="6.1"}

A [WebVTT parser]{#webvtt-parser .dfn .dfn-paneled dfn-type="dfn" noexport=""}, given an input byte stream, a [text track list of cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-cues){link-type="dfn"} `output`{.variable}, and a collection of [CSS style sheets](https://www.w3.org/TR/cssom-1/#css-style-sheet){link-type="dfn"} `stylesheets`{.variable}, must decode the byte stream using the [UTF-8 decode](https://www.w3.org/TR/encoding/#utf-8-decode){link-type="dfn"} algorithm, and then must parse the resulting string according to the [WebVTT parser algorithm](#webvtt-parser-algorithm){#ref-for-webvtt-parser-algorithm-1 link-type="dfn"} below. This results in [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-18 link-type="dfn"} being added to `output`{.variable}, and [CSS style sheets](https://www.w3.org/TR/cssom-1/#css-style-sheet){link-type="dfn"} being added to `stylesheets`{.variable}. [\[RFC3629\]](#biblio-rfc3629){link-type="biblio"}

A [WebVTT parser](#webvtt-parser){#ref-for-webvtt-parser-2 link-type="dfn"}, specifically its conversion and parsing steps, is typically run asynchronously, with the input byte stream being updated incrementally as the resource is downloaded; this is called an [incremental WebVTT parser]{#incremental-webvtt-parser .dfn .dfn-paneled dfn-type="dfn" noexport=""}.

A [WebVTT parser](#webvtt-parser){#ref-for-webvtt-parser-3 link-type="dfn"} verifies a file signature before parsing the provided byte stream. If the stream lacks this WebVTT file signature, then the parser aborts.

The [WebVTT parser algorithm]{#webvtt-parser-algorithm .dfn .dfn-paneled dfn-type="dfn" noexport=""} is as follows:

1.  Let `input`{.variable} be the string being parsed, after conversion to Unicode, and with the following transformations applied:

    -   Replace all U+0000 NULL characters by U+FFFD REPLACEMENT CHARACTERs.

    -   Replace each U+000D CARRIAGE RETURN U+000A LINE FEED (CRLF) character pair by a single U+000A LINE FEED (LF) character.

    -   Replace all remaining U+000D CARRIAGE RETURN characters by U+000A LINE FEED (LF) characters.

2.  Let `position`{.variable} be a pointer into `input`{.variable}, initially pointing at the start of the string. In an [incremental WebVTT parser](#incremental-webvtt-parser){#ref-for-incremental-webvtt-parser-1 link-type="dfn"}, when this algorithm (or further algorithms that it uses) moves the `position`{.variable} pointer, the user agent must wait until appropriate further characters from the byte stream have been added to `input`{.variable} before moving the pointer, so that the algorithm never reads past the end of the `input`{.variable} string. Once the byte stream has ended, and all characters have been added to `input`{.variable}, then the `position`{.variable} pointer may, when so instructed by the algorithms, be moved past the end of `input`{.variable}.

3.  Let `seen cue`{.variable} be false.

4.  If `input`{.variable} is less than six characters long, then abort these steps. The file does not start with the correct [WebVTT file](#webvtt-file){#ref-for-webvtt-file-14 link-type="dfn"} signature and was therefore not successfully processed.

5.  If `input`{.variable} is exactly six characters long but does not exactly equal \"`WEBVTT`\", then abort these steps. The file does not start with the correct [WebVTT file](#webvtt-file){#ref-for-webvtt-file-15 link-type="dfn"} signature and was therefore not successfully processed.

6.  If `input`{.variable} is more than six characters long but the first six characters do not exactly equal \"`WEBVTT`\", or the seventh character is not a U+0020 SPACE character, a U+0009 CHARACTER TABULATION (tab) character, or a U+000A LINE FEED (LF) character, then abort these steps. The file does not start with the correct [WebVTT file](#webvtt-file){#ref-for-webvtt-file-16 link-type="dfn"} signature and was therefore not successfully processed.

7.  [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are *not* U+000A LINE FEED (LF) characters.

8.  If `position`{.variable} is past the end of `input`{.variable}, then abort these steps. The file was successfully processed, but it contains no useful data and so no [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-19 link-type="dfn"} were added to `output`{.variable}.

9.  The character indicated by `position`{.variable} is a U+000A LINE FEED (LF) character. Advance `position`{.variable} to the next character in `input`{.variable}.

10. If `position`{.variable} is past the end of `input`{.variable}, then abort these steps. The file was successfully processed, but it contains no useful data and so no [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-20 link-type="dfn"} were added to `output`{.variable}.

11. *Header*: If the character indicated by `position`{.variable} is not a U+000A LINE FEED (LF) character, then [collect a WebVTT block](#collect-a-webvtt-block){#ref-for-collect-a-webvtt-block-1 link-type="dfn"} with the *in header* flag set. Otherwise, advance `position`{.variable} to the next character in `input`{.variable}.

12. [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are U+000A LINE FEED (LF) characters.

13. Let `regions`{.variable} be an empty [text track list of regions](#text-track-list-of-regions){#ref-for-text-track-list-of-regions-1 link-type="dfn"}.

14. *Block loop*: While `position`{.variable} doesn't point past the end of `input`{.variable}:

    1.  [Collect a WebVTT block](#collect-a-webvtt-block){#ref-for-collect-a-webvtt-block-2 link-type="dfn"}, and let `block`{.variable} be the returned value.

    2.  If `block`{.variable} is a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-21 link-type="dfn"}, add `block`{.variable} to the [text track list of cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-cues){link-type="dfn"} `output`{.variable}.

    3.  Otherwise, if `block`{.variable} is a [CSS style sheet](https://www.w3.org/TR/cssom-1/#css-style-sheet){link-type="dfn"}, add `block`{.variable} to `stylesheets`{.variable}.

    4.  Otherwise, if `block`{.variable} is a [WebVTT region object](#webvtt-region-object){#ref-for-webvtt-region-object-1 link-type="dfn"}, add `block`{.variable} to `regions`{.variable}.

    5.  [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are U+000A LINE FEED (LF) characters.

15. *End*: The file has ended. Abort these steps. The [WebVTT parser](#webvtt-parser){#ref-for-webvtt-parser-4 link-type="dfn"} has finished. The file was successfully processed.

When the algorithm above says to [collect a WebVTT block]{#collect-a-webvtt-block .dfn .dfn-paneled dfn-type="dfn" noexport=""}, optionally with a flag *in header* set, the user agent must run the following steps:

1.  Let `input`{.variable}, `position`{.variable}, `seen cue`{.variable} and `regions`{.variable} be the same variables as those of the same name in the algorithm that invoked these steps.

2.  Let `line count`{.variable} be zero.

3.  Let `previous position`{.variable} be `position`{.variable}.

4.  Let `line`{.variable} be the empty string.

5.  Let `buffer`{.variable} be the empty string.

6.  Let `seen EOF`{.variable} be false.

7.  Let `seen arrow`{.variable} be false.

8.  Let `cue`{.variable} be null.

9.  Let `stylesheet`{.variable} be null.

10. Let `region`{.variable} be null.

11. *Loop*: Run these substeps in a loop:

    1.  [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are *not* U+000A LINE FEED (LF) characters. Let `line`{.variable} be those characters, if any.

    2.  Increment `line count`{.variable} by 1.

    3.  If `position`{.variable} is past the end of `input`{.variable}, let `seen EOF`{.variable} be true. Otherwise, the character indicated by `position`{.variable} is a U+000A LINE FEED (LF) character; advance `position`{.variable} to the next character in `input`{.variable}.

    4.  If `line`{.variable} contains the three-character substring \"`-->`\" (U+002D HYPHEN-MINUS, U+002D HYPHEN-MINUS, U+003E GREATER-THAN SIGN), then run these substeps:

        1.  If *in header* is not set and at least one of the following conditions are true:

            -   `line count`{.variable} is 1

            -   `line count`{.variable} is 2 and `seen arrow`{.variable} is false

            \...then run these substeps:

            1.  Let `seen arrow`{.variable} be true.

            2.  Let `previous position`{.variable} be `position`{.variable}.

            3.  *Cue creation*: Let `cue`{.variable} be a new [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-22 link-type="dfn"} and initialize it as follows:

                1.  Let `cue`{.variable}'s [text track cue identifier](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-identifier){link-type="dfn"} be `buffer`{.variable}.

                2.  Let `cue`{.variable}'s [text track cue pause-on-exit flag](https://www.w3.org/TR/html51/semantics-embedded-content.html#pause-on-exit-flag){link-type="dfn"} be false.

                3.  Let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-2 link-type="dfn"} be null.

                4.  Let `cue`{.variable}'s [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-13 link-type="dfn"} be [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-13 link-type="dfn"}.

                5.  Let `cue`{.variable}'s [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-8 link-type="dfn"} be true.

                6.  Let `cue`{.variable}'s [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-21 link-type="dfn"} be [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-4 link-type="dfn"}.

                7.  Let `cue`{.variable}'s [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-6 link-type="dfn"} be [start alignment](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-4 link-type="dfn"}.

                8.  Let `cue`{.variable}'s [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-20 link-type="dfn"} be [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-6 link-type="dfn"}.

                9.  Let `cue`{.variable}'s [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-7 link-type="dfn"} be [auto](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-3 link-type="dfn"}.

                10. Let `cue`{.variable}'s [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-7 link-type="dfn"} be 100.

                11. Let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-15 link-type="dfn"} be [center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-5 link-type="dfn"}.

                12. Let `cue`{.variable}'s [cue text](#cue-text){#ref-for-cue-text-7 link-type="dfn"} be the empty string.

            4.  [Collect WebVTT cue timings and settings](#collect-webvtt-cue-timings-and-settings){#ref-for-collect-webvtt-cue-timings-and-settings-1 link-type="dfn"} from `line`{.variable} using `regions`{.variable} for `cue`{.variable}. If that fails, let `cue`{.variable} be null. Otherwise, let `buffer`{.variable} be the empty string and let `seen cue`{.variable} be true.

            Otherwise, let `position`{.variable} be `previous position`{.variable} and break out of *loop*.

    5.  Otherwise, if `line`{.variable} is the empty string, break out of *loop*.

    6.  Otherwise, run these substeps:

        1.  If *in header* is not set and `line count`{.variable} is 2, run these substeps:

            1.  If `seen cue`{.variable} is false and `buffer`{.variable} starts with the substring \"`STYLE`\" (U+0053 LATIN CAPITAL LETTER S, U+0054 LATIN CAPITAL LETTER T, U+0059 LATIN CAPITAL LETTER Y, U+004C LATIN CAPITAL LETTER L, U+0045 LATIN CAPITAL LETTER E), and the remaining characters in `buffer`{.variable} (if any) are all [ASCII whitespace](https://www.w3.org/TR/html51/infrastructure.html#space-characters){link-type="dfn"}, then run these substeps:

                1.  Let `stylesheet`{.variable} be the result of [creating a CSS style sheet](https://www.w3.org/TR/cssom-1/#create-a-css-style-sheet){link-type="dfn"}, with the following properties: [\[CSSOM\]](#biblio-cssom){link-type="biblio"}

                    [location](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-location){link-type="dfn"}
                    :   null

                    [parent CSS style sheet](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-parent-css-style-sheet){link-type="dfn"}
                    :   null

                    [owner node](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-owner-node){link-type="dfn"}
                    :   null

                    [owner CSS rule](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-owner-css-rule){link-type="dfn"}
                    :   null

                    [media](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-media){link-type="dfn"}
                    :   The empty string.

                    [title](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-title){link-type="dfn"}
                    :   The empty string.

                    [alternate flag](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-alternate-flag){link-type="dfn"}
                    :   Unset.

                    [origin-clean flag](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-origin-clean-flag){link-type="dfn"}
                    :   Set.

                2.  Let `buffer`{.variable} be the empty string.

            2.  Otherwise, if `seen cue`{.variable} is false and `buffer`{.variable} starts with the substring \"`REGION`\" (U+0052 LATIN CAPITAL LETTER R, U+0045 LATIN CAPITAL LETTER E, U+0047 LATIN CAPITAL LETTER G, U+0049 LATIN CAPITAL LETTER I, U+004F LATIN CAPITAL LETTER O, U+004E LATIN CAPITAL LETTER N), and the remaining characters in `buffer`{.variable} (if any) are all [ASCII whitespace](https://www.w3.org/TR/html51/infrastructure.html#space-characters){link-type="dfn"}, then run these substeps:

                1.  *Region creation*: Let `region`{.variable} be a new [WebVTT region](#webvtt-region){#ref-for-webvtt-region-9 link-type="dfn"}.

                2.  Let `region`{.variable}'s [identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-2 link-type="dfn"} be the empty string.

                3.  Let `region`{.variable}'s [width](#webvtt-region-width){#ref-for-webvtt-region-width-1 link-type="dfn"} be 100.

                4.  Let `region`{.variable}'s [lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-1 link-type="dfn"} be 3.

                5.  Let `region`{.variable}'s [anchor point](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-1 link-type="dfn"} be (0,100).

                6.  Let `region`{.variable}'s [viewport anchor point](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-1 link-type="dfn"} be (0,100).

                7.  Let `region`{.variable}'s [scroll value](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-1 link-type="dfn"} be [none](#webvtt-region-scroll-none){#ref-for-webvtt-region-scroll-none-1 link-type="dfn"}.

                8.  Let `buffer`{.variable} be the empty string.

        2.  If `buffer`{.variable} is not the empty string, append a U+000A LINE FEED (LF) character to `buffer`{.variable}.

        3.  Append `line`{.variable} to `buffer`{.variable}.

        4.  Let `previous position`{.variable} be `position`{.variable}.

    7.  If `seen EOF`{.variable} is true, break out of *loop*.

12. If `cue`{.variable} is not null, let the [cue text](#cue-text){#ref-for-cue-text-8 link-type="dfn"} of `cue`{.variable} be `buffer`{.variable}, and return `cue`{.variable}.

13. Otherwise, if `stylesheet`{.variable} is not null, then [Parse a stylesheet](https://www.w3.org/TR/css-syntax-3/#parse-a-stylesheet0){link-type="dfn"} from `buffer`{.variable}. If it returned a list of rules, assign the list as `stylesheet`{.variable}'s [CSS rules](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-css-rules){link-type="dfn"}; otherwise, set `stylesheet`{.variable}'s [CSS rules](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-css-rules){link-type="dfn"} to an empty list. [\[CSSOM\]](#biblio-cssom){link-type="biblio"} [\[CSS-SYNTAX-3\]](#biblio-css-syntax-3){link-type="biblio"} Finally, return `stylesheet`{.variable}.

14. Otherwise, if `region`{.variable} is not null, then [collect WebVTT region settings](#collect-webvtt-region-settings){#ref-for-collect-webvtt-region-settings-1 link-type="dfn"} from `buffer`{.variable} using `region`{.variable} for the results. Construct a [WebVTT Region Object](#webvtt-region-object){#ref-for-webvtt-region-object-2 link-type="dfn"} from `region`{.variable}, and return it.

15. Otherwise, return null.

### [6.2. ]{.secno}[WebVTT region settings parsing]{.content}[](#region-settings-parsing){.self-link} {#region-settings-parsing .heading .settled .algorithm algorithm="WebVTT region settings parsing" level="6.2"}

When the [WebVTT parser algorithm](#webvtt-parser-algorithm){#ref-for-webvtt-parser-algorithm-2 link-type="dfn"} says to [collect WebVTT region settings]{#collect-webvtt-region-settings .dfn .dfn-paneled dfn-type="dfn" noexport=""} from a string `input`{.variable} for a [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}, the user agent must run the following algorithm.

A [WebVTT region object]{#webvtt-region-object .dfn .dfn-paneled dfn-type="dfn" noexport=""} is a conceptual construct to represent a [WebVTT region](#webvtt-region){#ref-for-webvtt-region-10 link-type="dfn"} that is used as a root node for [lists of WebVTT node objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-1 link-type="dfn"}. This algorithm returns a list of [WebVTT Region Objects](#webvtt-region-object){#ref-for-webvtt-region-object-3 link-type="dfn"}.

1.  Let `settings`{.variable} be the result of [splitting `input`{.variable} on spaces](https://www.w3.org/TR/html51/infrastructure.html#split-a-string-on-spaces){link-type="dfn"}.

2.  For each token `setting`{.variable} in the list `settings`{.variable}, run the following substeps:
    1.  If `setting`{.variable} does not contain a U+003A COLON character (:), or if the first U+003A COLON character (:) in `setting`{.variable} is either the first or last character of `setting`{.variable}, then jump to the step labeled *next setting*.

    2.  Let `name`{.variable} be the leading substring of `setting`{.variable} up to and excluding the first U+003A COLON character (:) in that string.

    3.  Let `value`{.variable} be the trailing substring of `setting`{.variable} starting from the character immediately after the first U+003A COLON character (:) in that string.

    4.  Run the appropriate substeps that apply for the value of `name`{.variable}, as follows:

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`id`\"

        Let `region`{.variable}'s [identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-3 link-type="dfn"} be `value`{.variable}.

        Otherwise if `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`width`\"

        If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-1 link-type="dfn"} from `value`{.variable} returns a `percentage`{.variable}, let `region`{.variable}'s [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-2 link-type="dfn"} be `percentage`{.variable}.

        Otherwise if `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`lines`\"

        1.  If `value`{.variable} contains any characters other than [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, then jump to the step labeled *next setting*.

        2.  Interpret `value`{.variable} as an integer, and let `number`{.variable} be that number.

        3.  Let `region`{.variable}'s [WebVTT region lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-2 link-type="dfn"} be `number`{.variable}.

        Otherwise if `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`regionanchor`\"

        1.  If `value`{.variable} does not contain a U+002C COMMA character (,), then jump to the step labeled *next setting*.

        2.  Let `anchorX`{.variable} be the leading substring of `value`{.variable} up to and excluding the first U+002C COMMA character (,) in that string.

        3.  Let `anchorY`{.variable} be the trailing substring of `value`{.variable} starting from the character immediately after the first U+002C COMMA character (,) in that string.

        4.  If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-2 link-type="dfn"} from `anchorX`{.variable} or [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-3 link-type="dfn"} from `anchorY`{.variable} don't return a `percentage`{.variable}, then jump to the step labeled *next setting*.

        5.  Let `region`{.variable}'s [WebVTT region anchor point](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-2 link-type="dfn"} be the tuple of the `percentage`{.variable} values calculated from `anchorX`{.variable} and `anchorY`{.variable}.

        Otherwise if `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`viewportanchor`\"

        1.  If `value`{.variable} does not contain a U+002C COMMA character (,), then jump to the step labeled *next setting*.

        2.  Let `viewportanchorX`{.variable} be the leading substring of `value`{.variable} up to and excluding the first U+002C COMMA character (,) in that string.

        3.  Let `viewportanchorY`{.variable} be the trailing substring of `value`{.variable} starting from the character immediately after the first U+002C COMMA character (,) in that string.

        4.  If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-4 link-type="dfn"} from `viewportanchorX`{.variable} or [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-5 link-type="dfn"} from `viewportanchorY`{.variable} don't return a `percentage`{.variable}, then jump to the step labeled *next setting*.

        5.  Let `region`{.variable}'s [WebVTT region viewport anchor point](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-2 link-type="dfn"} be the tuple of the `percentage`{.variable} values calculated from `viewportanchorX`{.variable} and `viewportanchorY`{.variable}.

        Otherwise if `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`scroll`\"

        1.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`up`\", then let `region`{.variable}'s [scroll value](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-2 link-type="dfn"} be [up](#webvtt-region-scroll-up){#ref-for-webvtt-region-scroll-up-1 link-type="dfn"}.

    5.  *Next setting*: Continue to the next setting, if any.

The rules to [parse a percentage string]{#parse-a-percentage-string .dfn .dfn-paneled dfn-type="dfn" noexport=""} are as follows. This will return either a number in the range 0..100, or nothing. If at any point the algorithm says that it \"fails\", this means that it is aborted at that point and returns nothing.

1.  Let `input`{.variable} be the string being parsed.

2.  If `input`{.variable} does not match the syntax for a [WebVTT percentage](#webvtt-percentage){#ref-for-webvtt-percentage-10 link-type="dfn"}, then fail.

3.  Remove the last character from `input`{.variable}.

4.  Let `percentage`{.variable} be the result of parsing `input`{.variable} using the [rules for parsing floating-point number values](https://www.w3.org/TR/html51/infrastructure.html#rules-for-parsing-floating-point-number-values){link-type="dfn"}. [\[HTML51\]](#biblio-html51){link-type="biblio"}

5.  If `percentage`{.variable} is an error, is less than 0, or is greater than 100, then fail.

6.  Return `percentage`{.variable}.

### [6.3. ]{.secno}[WebVTT cue timings and settings parsing]{.content}[](#cue-timings-and-settings-parsing){.self-link} {#cue-timings-and-settings-parsing .heading .settled .algorithm algorithm="WebVTT cue timings and settings parsing" level="6.3"}

When the algorithm above says to [collect WebVTT cue timings and settings]{#collect-webvtt-cue-timings-and-settings .dfn .dfn-paneled dfn-type="dfn" noexport=""} from a string `input`{.variable} using a [text track list of regions](#text-track-list-of-regions){#ref-for-text-track-list-of-regions-2 link-type="dfn"} `regions`{.variable} for a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-23 link-type="dfn"} `cue`{.variable}, the user agent must run the following algorithm.

1.  Let `input`{.variable} be the string being parsed.

2.  Let `position`{.variable} be a pointer into `input`{.variable}, initially pointing at the start of the string.

3.  [Skip whitespace](https://www.w3.org/TR/html51/infrastructure.html#skip-whitespace){link-type="dfn"}.

4.  [Collect a WebVTT timestamp](#collect-a-webvtt-timestamp){#ref-for-collect-a-webvtt-timestamp-1 link-type="dfn"}. If that algorithm fails, then abort these steps and return failure. Otherwise, let `cue`{.variable}'s [text track cue start time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-start-time){link-type="dfn"} be the collected time.

5.  [Skip whitespace](https://www.w3.org/TR/html51/infrastructure.html#skip-whitespace){link-type="dfn"}.

6.  If the character at `position`{.variable} is not a U+002D HYPHEN-MINUS character (-) then abort these steps and return failure. Otherwise, move `position`{.variable} forwards one character.

7.  If the character at `position`{.variable} is not a U+002D HYPHEN-MINUS character (-) then abort these steps and return failure. Otherwise, move `position`{.variable} forwards one character.

8.  If the character at `position`{.variable} is not a U+003E GREATER-THAN SIGN character (\>) then abort these steps and return failure. Otherwise, move `position`{.variable} forwards one character.

9.  [Skip whitespace](https://www.w3.org/TR/html51/infrastructure.html#skip-whitespace){link-type="dfn"}.

10. [Collect a WebVTT timestamp](#collect-a-webvtt-timestamp){#ref-for-collect-a-webvtt-timestamp-2 link-type="dfn"}. If that algorithm fails, then abort these steps and return failure. Otherwise, let `cue`{.variable}'s [text track cue end time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-end-time){link-type="dfn"} be the collected time.

11. Let `remainder`{.variable} be the trailing substring of `input`{.variable} starting at `position`{.variable}.

12. [Parse the WebVTT cue settings](#parse-the-webvtt-cue-settings){#ref-for-parse-the-webvtt-cue-settings-1 link-type="dfn"} from `remainder`{.variable} using `regions`{.variable} for `cue`{.variable}.

When the user agent is to [parse the WebVTT cue settings]{#parse-the-webvtt-cue-settings .dfn .dfn-paneled dfn-type="dfn" noexport=""} from a string `input`{.variable} using a [text track list of regions](#text-track-list-of-regions){#ref-for-text-track-list-of-regions-3 link-type="dfn"} `regions`{.variable} for a [text track cue](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"} `cue`{.variable}, the user agent must run the following steps:

1.  Let `settings`{.variable} be the result of [splitting `input`{.variable} on spaces](https://www.w3.org/TR/html51/infrastructure.html#split-a-string-on-spaces){link-type="dfn"}.

2.  For each token `setting`{.variable} in the list `settings`{.variable}, run the following substeps:

    1.  If `setting`{.variable} does not contain a U+003A COLON character (:), or if the first U+003A COLON character (:) in `setting`{.variable} is either the first or last character of `setting`{.variable}, then jump to the step labeled *next setting*.

    2.  Let `name`{.variable} be the leading substring of `setting`{.variable} up to and excluding the first U+003A COLON character (:) in that string.

    3.  Let `value`{.variable} be the trailing substring of `setting`{.variable} starting from the character immediately after the first U+003A COLON character (:) in that string.

    4.  Run the appropriate substeps that apply for the value of `name`{.variable}, as follows:

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`region`\"

        :   1.  Let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-3 link-type="dfn"} be the last [WebVTT region](#webvtt-region){#ref-for-webvtt-region-11 link-type="dfn"} in `regions`{.variable} whose [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-4 link-type="dfn"} is `value`{.variable}, if any, or null otherwise.

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`vertical`\"

        :   1.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`rl`\", then let `cue`{.variable}'s [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-14 link-type="dfn"} be [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-4 link-type="dfn"}.

            2.  Otherwise, if `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`lr`\", then let `cue`{.variable}'s [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-15 link-type="dfn"} be [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-4 link-type="dfn"}.

            3.  If `cue`{.variable}'s [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-16 link-type="dfn"} is not [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-14 link-type="dfn"}, let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-4 link-type="dfn"} be null (there are no vertical regions).

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`line`\"

        :   1.  If `value`{.variable} contains a U+002C COMMA character (,), then let `linepos`{.variable} be the leading substring of `value`{.variable} up to and excluding the first U+002C COMMA character (,) in that string and let `linealign`{.variable} be the trailing substring of `value`{.variable} starting from the character immediately after the first U+002C COMMA character (,) in that string.

            2.  Otherwise let `linepos`{.variable} be the full `value`{.variable} string and `linealign`{.variable} be null.

            3.  If `linepos`{.variable} does not contain at least one [ASCII digit](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, then jump to the step labeled *next setting*.

            4.  If the last character in `linepos`{.variable} is a U+0025 PERCENT SIGN character (%)

                If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-6 link-type="dfn"} from `linepos`{.variable} doesn't fail, let `number`{.variable} be the returned `percentage`{.variable}, otherwise jump to the step labeled *next setting*.

                Otherwise

                1.  If `linepos`{.variable} contains any characters other than U+002D HYPHEN-MINUS characters (-), [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, and U+002E DOT character (.), then jump to the step labeled *next setting*.

                2.  If any character in `linepos`{.variable} other than the first character is a U+002D HYPHEN-MINUS character (-), then jump to the step labeled *next setting*.

                3.  If there are more than one U+002E DOT characters (.), then jump to the step labeled *next setting*.

                4.  If there is a U+002E DOT character (.) and the character before or the character after is not an [ASCII digit](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, or if the U+002E DOT character (.) is the first or the last character, then jump to the step labeled *next setting*.

                5.  Let `number`{.variable} be the result of parsing `linepos`{.variable} using the [rules for parsing floating-point number values](https://www.w3.org/TR/html51/infrastructure.html#rules-for-parsing-floating-point-number-values){link-type="dfn"}. [\[HTML51\]](#biblio-html51){link-type="biblio"}

                6.  If `number`{.variable} is an error, then jump to the step labeled *next setting*.

            5.  If `linealign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`start`\", then let `cue`{.variable}'s [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-7 link-type="dfn"} be [start alignment](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-5 link-type="dfn"}.

            6.  Otherwise, if `linealign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`center`\", then let `cue`{.variable}'s [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-8 link-type="dfn"} be [center alignment](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-2 link-type="dfn"}.

            7.  Otherwise, if `linealign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`end`\", then let `cue`{.variable}'s [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-9 link-type="dfn"} be [end alignment](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-2 link-type="dfn"}.

            8.  Otherwise, if `linealign`{.variable} is not null, then jump to the step labeled *next setting*.

            9.  Let `cue`{.variable}'s [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-22 link-type="dfn"} be `number`{.variable}.

            10. If the last character in `linepos`{.variable} is a U+0025 PERCENT SIGN character (%), then let `cue`{.variable}'s [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-9 link-type="dfn"} be false. Otherwise, let it be true.

            11. If `cue`{.variable}'s [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-23 link-type="dfn"} is not [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-5 link-type="dfn"}, let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-5 link-type="dfn"} be null (the cue has been explicitly positioned with a line offset and thus drops out of the region).

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`position`\"

        :   1.  If `value`{.variable} contains a U+002C COMMA character (,), then let `colpos`{.variable} be the leading substring of `value`{.variable} up to and excluding the first U+002C COMMA character (,) in that string and let `colalign`{.variable} be the trailing substring of `value`{.variable} starting from the character immediately after the first U+002C COMMA character (,) in that string.

            2.  Otherwise let `colpos`{.variable} be the full `value`{.variable} string and `colalign`{.variable} be null.

            3.  If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-7 link-type="dfn"} from `colpos`{.variable} doesn't fail, let `number`{.variable} be the returned `percentage`{.variable}, otherwise jump to the step labeled *next setting* ([position](#webvtt-cue-position){#ref-for-webvtt-cue-position-21 link-type="dfn"}'s value remains the special value [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-7 link-type="dfn"}).

            4.  If `colalign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`line-left`\", then let `cue`{.variable}'s [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-8 link-type="dfn"} be [line-left alignment](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-6 link-type="dfn"}.

            5.  Otherwise, if `colalign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`center`\", then let `cue`{.variable}'s [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-9 link-type="dfn"} be [center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-2 link-type="dfn"}.

            6.  Otherwise, if `colalign`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`line-right`\", then let `cue`{.variable}'s [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-10 link-type="dfn"} be [line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-5 link-type="dfn"}.

            7.  Otherwise, if `colalign`{.variable} is not null, then jump to the step labeled *next setting*.

            8.  Let `cue`{.variable}'s [position](#webvtt-cue-position){#ref-for-webvtt-cue-position-22 link-type="dfn"} be `number`{.variable}.

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`size`\"

        :   1.  If [parse a percentage string](#parse-a-percentage-string){#ref-for-parse-a-percentage-string-8 link-type="dfn"} from `value`{.variable} doesn't fail, let `number`{.variable} be the returned `percentage`{.variable}, otherwise jump to the step labeled *next setting*.

            2.  Let `cue`{.variable}'s [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-8 link-type="dfn"} be `number`{.variable}.

            3.  If `cue`{.variable}'s [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-9 link-type="dfn"} is not 100, let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-6 link-type="dfn"} be null (the cue has been explicitly sized and thus drops out of the region).

        If `name`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for \"`align`\"

        :   1.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`start`\", then let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-16 link-type="dfn"} be [start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-7 link-type="dfn"}.

            2.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`center`\", then let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-17 link-type="dfn"} be [center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-6 link-type="dfn"}.

            3.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`end`\", then let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-18 link-type="dfn"} be [end alignment](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-6 link-type="dfn"}.

            4.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`left`\", then let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-19 link-type="dfn"} be [left alignment](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-5 link-type="dfn"}.

            5.  If `value`{.variable} is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the string \"`right`\", then let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-20 link-type="dfn"} be [right alignment](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-5 link-type="dfn"}.

    5.  *Next setting*: Continue to the next token, if any.

When this specification says that a user agent is to [collect a WebVTT timestamp]{#collect-a-webvtt-timestamp .dfn .dfn-paneled dfn-type="dfn" noexport=""}, the user agent must run the following steps:

1.  Let `input`{.variable} and `position`{.variable} be the same variables as those of the same name in the algorithm that invoked these steps.

2.  Let `most significant units`{.variable} be *minutes*.

3.  If `position`{.variable} is past the end of `input`{.variable}, return an error and abort these steps.

4.  If the character indicated by `position`{.variable} is not an [ASCII digit](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, then return an error and abort these steps.

5.  [Collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, and let `string`{.variable} be the collected substring.

6.  Interpret `string`{.variable} as a base-ten integer. Let `value`{.variable}~`1`{.variable}~ be that integer.

7.  If `string`{.variable} is not exactly two characters in length, or if `value`{.variable}~`1`{.variable}~ is greater than 59, let `most significant units`{.variable} be *hours*.

8.  If `position`{.variable} is beyond the end of `input`{.variable} or if the character at `position`{.variable} is not a U+003A COLON character (:), then return an error and abort these steps. Otherwise, move `position`{.variable} forwards one character.

9.  [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, and let `string`{.variable} be the collected substring.

10. If `string`{.variable} is not exactly two characters in length, return an error and abort these steps.

11. Interpret `string`{.variable} as a base-ten integer. Let `value`{.variable}~`2`{.variable}~ be that integer.

12. If `most significant units`{.variable} is *hours*, or if `position`{.variable} is not beyond the end of `input`{.variable} and the character at `position`{.variable} is a U+003A COLON character (:), run these substeps:

    1.  If `position`{.variable} is beyond the end of `input`{.variable} or if the character at `position`{.variable} is not a U+003A COLON character (:), then return an error and abort these steps. Otherwise, move `position`{.variable} forwards one character.

    2.  [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, and let `string`{.variable} be the collected substring.

    3.  If `string`{.variable} is not exactly two characters in length, return an error and abort these steps.

    4.  Interpret `string`{.variable} as a base-ten integer. Let `value`{.variable}~`3`{.variable}~ be that integer.

    Otherwise (if `most significant units`{.variable} is not *hours*, and either `position`{.variable} is beyond the end of `input`{.variable}, or the character at `position`{.variable} is not a U+003A COLON character (:)), let `value`{.variable}~`3`{.variable}~ have the value of `value`{.variable}~`2`{.variable}~, then `value`{.variable}~`2`{.variable}~ have the value of `value`{.variable}~`1`{.variable}~, then let `value`{.variable}~`1`{.variable}~ equal zero.

13. If `position`{.variable} is beyond the end of `input`{.variable} or if the character at `position`{.variable} is not a U+002E FULL STOP character (.), then return an error and abort these steps. Otherwise, move `position`{.variable} forwards one character.

14. [collect a sequence of code points](https://www.w3.org/TR/html51/infrastructure.html#collect-a-sequence-of-characters){link-type="dfn"} that are [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}, and let `string`{.variable} be the collected substring.

15. If `string`{.variable} is not exactly three characters in length, return an error and abort these steps.

16. Interpret `string`{.variable} as a base-ten integer. Let `value`{.variable}~`4`{.variable}~ be that integer.

17. If `value`{.variable}~`2`{.variable}~ is greater than 59 or if `value`{.variable}~`3`{.variable}~ is greater than 59, return an error and abort these steps.

18. Let `result`{.variable} be `value`{.variable}~`1`{.variable}~×60×60 + `value`{.variable}~`2`{.variable}~×60 + `value`{.variable}~`3`{.variable}~ + `value`{.variable}~`4`{.variable}~∕1000.

19. Return `result`{.variable}.

### [6.4. ]{.secno}[WebVTT cue text parsing rules]{.content}[](#cue-text-parsing-rules){.self-link} {#cue-text-parsing-rules .heading .settled .algorithm algorithm="WebVTT cue text parsing rules" level="6.4"}

A [WebVTT Node Object]{#webvtt-node-object .dfn .dfn-paneled dfn-type="dfn" noexport=""} is a conceptual construct used to represent components of [cue text](#cue-text){#ref-for-cue-text-9 link-type="dfn"} so that its processing can be described without reference to the underlying syntax.

There are two broad classes of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-1 link-type="dfn"}: [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-1 link-type="dfn"} and [WebVTT Leaf Node Objects](#webvtt-leaf-node-object){#ref-for-webvtt-leaf-node-object-1 link-type="dfn"}.

[WebVTT Internal Node Objects]{#webvtt-internal-node-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Internal Node Object" noexport=""} are those that can contain further [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-2 link-type="dfn"}. They are conceptually similar to elements in HTML or the DOM. [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-2 link-type="dfn"} have an ordered list of child [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-3 link-type="dfn"}. The [WebVTT Internal Node Object](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-3 link-type="dfn"} is said to be the *parent* of the children. Cycles do not occur; the parent-child relationships so constructed form a tree structure. [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-4 link-type="dfn"} also have an ordered list of [class names](#cue-component-class-names){#ref-for-cue-component-class-names-6 link-type="dfn"}, known as their [applicable classes]{#webvtt-node-objects-applicable-classes .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Node Object’s applicable classes" noexport=""}, and a language, known as their [applicable language]{#webvtt-node-objects-applicable-language .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Node Object’s applicable
language" noexport=""}, which is to be interpreted as a BCP 47 language tag. [\[BCP47\]](#biblio-bcp47){link-type="biblio"}

User agents will add a language tag as the [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-1 link-type="dfn"} even if it is not a valid or not even well-formed language tag. [\[BCP47\]](#biblio-bcp47){link-type="biblio"}

There are several concrete classes of [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-5 link-type="dfn"}:

[Lists of WebVTT Node Objects]{#list-of-webvtt-node-objects .dfn .dfn-paneled dfn-type="dfn" lt="List of WebVTT Node Objects" noexport=""}

:   These are used as root nodes for trees of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-4 link-type="dfn"}.

[WebVTT Class Objects]{#webvtt-class-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Class Object" noexport=""}

:   These represent spans of text (a [WebVTT cue class span](#webvtt-cue-class-span){#ref-for-webvtt-cue-class-span-2 link-type="dfn"}) in [cue text](#cue-text){#ref-for-cue-text-10 link-type="dfn"}, and are used to annotate parts of the cue with [applicable classes](#webvtt-node-objects-applicable-classes){#ref-for-webvtt-node-objects-applicable-classes-1 link-type="dfn"} without implying further meaning (such as italics or bold).

[WebVTT Italic Objects]{#webvtt-italic-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Italic Object" noexport=""}

:   These represent spans of italic text (a [WebVTT cue italics span](#webvtt-cue-italics-span){#ref-for-webvtt-cue-italics-span-2 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-5 link-type="dfn"}.

[WebVTT Bold Objects]{#webvtt-bold-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Bold Object" noexport=""}

:   These represent spans of bold text (a [WebVTT cue bold span](#webvtt-cue-bold-span){#ref-for-webvtt-cue-bold-span-2 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-6 link-type="dfn"}.

[WebVTT Underline Objects]{#webvtt-underline-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Underline Object" noexport=""}

:   These represent spans of underline text (a [WebVTT cue underline span](#webvtt-cue-underline-span){#ref-for-webvtt-cue-underline-span-2 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-7 link-type="dfn"}.

[WebVTT Ruby Objects]{#webvtt-ruby-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Ruby Object" noexport=""}

:   These represent spans of ruby (a [WebVTT cue ruby span](#webvtt-cue-ruby-span){#ref-for-webvtt-cue-ruby-span-3 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-8 link-type="dfn"}.

[WebVTT Ruby Text Objects]{#webvtt-ruby-text-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Ruby Text Object" noexport=""}

:   These represent spans of ruby text (a [WebVTT cue ruby text span](#webvtt-cue-ruby-text-span){#ref-for-webvtt-cue-ruby-text-span-1 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-9 link-type="dfn"}.

[WebVTT Voice Objects]{#webvtt-voice-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Voice Object" noexport=""}

:   These represent spans of text associated with a specific voice (a [WebVTT cue voice span](#webvtt-cue-voice-span){#ref-for-webvtt-cue-voice-span-3 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-10 link-type="dfn"}. A [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-1 link-type="dfn"} has a value, which is the name of the voice.

[WebVTT Language Objects]{#webvtt-language-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Language Object" noexport=""}

:   These represent spans of text (a [WebVTT cue language span](#webvtt-cue-language-span){#ref-for-webvtt-cue-language-span-2 link-type="dfn"}) in [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-11 link-type="dfn"}, and are used to annotate parts of the cue where the [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-2 link-type="dfn"} might be different than the surrounding text's, without implying further meaning (such as italics or bold).

[WebVTT Leaf Node Objects]{#webvtt-leaf-node-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Leaf Node Object" noexport=""} are those that contain data, such as text, and cannot contain child [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-5 link-type="dfn"}.

There are two concrete classes of [WebVTT Leaf Node Objects](#webvtt-leaf-node-object){#ref-for-webvtt-leaf-node-object-2 link-type="dfn"}:

[WebVTT Text Objects]{#webvtt-text-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Text Object" noexport=""}

:   A fragment of text. A [WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-1 link-type="dfn"} has a value, which is the text it represents.

[WebVTT Timestamp Objects]{#webvtt-timestamp-object .dfn .dfn-paneled dfn-type="dfn" lt="WebVTT Timestamp Object" noexport=""}

:   A timestamp. A [WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-1 link-type="dfn"} has a value, in seconds and fractions of a second, which is the time represented by the timestamp.

The [WebVTT cue text parsing rules]{#webvtt-cue-text-parsing-rules .dfn .dfn-paneled dfn-type="dfn" noexport=""} consist of the following algorithm. The input is a string `input`{.variable} supposedly containing [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text){#ref-for-webvtt-caption-or-subtitle-cue-text-12 link-type="dfn"}, and optionally a fallback language `language`{.variable}. This algorithm returns a [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-2 link-type="dfn"}.

1.  Let `input`{.variable} be the string being parsed.

2.  Let `position`{.variable} be a pointer into `input`{.variable}, initially pointing at the start of the string.

3.  Let `result`{.variable} be a [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-3 link-type="dfn"}, initially empty.

4.  Let `current`{.variable} be the [WebVTT Internal Node Object](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-6 link-type="dfn"} `result`{.variable}.

5.  Let `language stack`{.variable} be a stack of language tags, initially empty.

6.  If `language`{.variable} is set, set `result`{.variable}'s [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-3 link-type="dfn"} to `language`{.variable}, and push `language`{.variable} onto the `language stack`{.variable}.

7.  *Loop*: If `position`{.variable} is past the end of `input`{.variable}, return `result`{.variable} and abort these steps.

8.  Let `token`{.variable} be the result of invoking the [WebVTT cue text tokenizer](#webvtt-cue-text-tokenizer){#ref-for-webvtt-cue-text-tokenizer-1 link-type="dfn"}.

9.  Run the appropriate steps given the type of `token`{.variable}:

    If `token`{.variable} is a string

    :   1.  Create a [WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-2 link-type="dfn"} whose value is the value of the string token `token`{.variable}.

        2.  Append the newly created [WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-3 link-type="dfn"} to `current`{.variable}.

    If `token`{.variable} is a start tag

    :   How the start tag token `token`{.variable} is processed depends on its tag name, as follows:

        If the tag name is \"`c`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-1 link-type="dfn"} a [WebVTT Class Object](#webvtt-class-object){#ref-for-webvtt-class-object-1 link-type="dfn"}.

        If the tag name is \"`i`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-2 link-type="dfn"} a [WebVTT Italic Object](#webvtt-italic-object){#ref-for-webvtt-italic-object-1 link-type="dfn"}.

        If the tag name is \"`b`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-3 link-type="dfn"} a [WebVTT Bold Object](#webvtt-bold-object){#ref-for-webvtt-bold-object-2 link-type="dfn"}.

        If the tag name is \"`u`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-4 link-type="dfn"} a [WebVTT Underline Object](#webvtt-underline-object){#ref-for-webvtt-underline-object-1 link-type="dfn"}.

        If the tag name is \"`ruby`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-5 link-type="dfn"} a [WebVTT Ruby Object](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-1 link-type="dfn"}.

        If the tag name is \"`rt`\"

        :   If `current`{.variable} is a [WebVTT Ruby Object](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-2 link-type="dfn"}, then [attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-6 link-type="dfn"} a [WebVTT Ruby Text Object](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-1 link-type="dfn"}.

        If the tag name is \"`v`\"

        :   [Attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-7 link-type="dfn"} a [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-2 link-type="dfn"}, and set its value to the token's annotation string, or the empty string if there is no annotation string.

        If the tag name is \"`lang`\"

        :   Push the value of the token's annotation string, or the empty string if there is no annotation string, onto the `language stack`{.variable}; then [attach](#attach-a-webvtt-internal-node-object){#ref-for-attach-a-webvtt-internal-node-object-8 link-type="dfn"} a [WebVTT Language Object](#webvtt-language-object){#ref-for-webvtt-language-object-1 link-type="dfn"}.

        Otherwise

        :   Ignore the token.

        When the steps above say to [attach a WebVTT Internal Node Object]{#attach-a-webvtt-internal-node-object .dfn .dfn-paneled dfn-type="dfn" noexport=""} of a particular concrete class, the user agent must run the following steps:

        1.  Create a new [WebVTT Internal Node Object](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-7 link-type="dfn"} of the specified concrete class.

        2.  Set the new object's list of [applicable classes](#webvtt-node-objects-applicable-classes){#ref-for-webvtt-node-objects-applicable-classes-2 link-type="dfn"} to the list of classes in the token, excluding any classes that are the empty string.

        3.  Set the new object's [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-4 link-type="dfn"} to the top entry on the `language stack`{.variable}, if the stack is not empty.

        4.  Append the newly created node object to `current`{.variable}.

        5.  Let `current`{.variable} be the newly created node object.

    If `token`{.variable} is an end tag

    :   If any of the following conditions is true, then let `current`{.variable} be the parent node of `current`{.variable}.

        -   The tag name of the end tag token `token`{.variable} is \"`c`\" and `current`{.variable} is a [WebVTT Class Object](#webvtt-class-object){#ref-for-webvtt-class-object-2 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`i`\" and `current`{.variable} is a [WebVTT Italic Object](#webvtt-italic-object){#ref-for-webvtt-italic-object-2 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`b`\" and `current`{.variable} is a [WebVTT Bold Object](#webvtt-bold-object){#ref-for-webvtt-bold-object-3 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`u`\" and `current`{.variable} is a [WebVTT Underline Object](#webvtt-underline-object){#ref-for-webvtt-underline-object-2 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`ruby`\" and `current`{.variable} is a [WebVTT Ruby Object](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-3 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`rt`\" and `current`{.variable} is a [WebVTT Ruby Text Object](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-2 link-type="dfn"}.
        -   The tag name of the end tag token `token`{.variable} is \"`v`\" and `current`{.variable} is a [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-3 link-type="dfn"}.

        Otherwise, if the tag name of the end tag token `token`{.variable} is \"`lang`\" and `current`{.variable} is a [WebVTT Language Object](#webvtt-language-object){#ref-for-webvtt-language-object-2 link-type="dfn"}, then let `current`{.variable} be the parent node of `current`{.variable}, and pop the top value from the `language stack`{.variable}.

        Otherwise, if the tag name of the end tag token `token`{.variable} is \"`ruby`\" and `current`{.variable} is a [WebVTT Ruby Text Object](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-3 link-type="dfn"}, then let `current`{.variable} be the parent node of the parent node of `current`{.variable}.

        Otherwise, ignore the token.

    If `token`{.variable} is a timestamp tag

    :   1.  Let `input`{.variable} be the tag value.

        2.  Let `position`{.variable} be a pointer into `input`{.variable}, initially pointing at the start of the string.

        3.  [Collect a WebVTT timestamp](#collect-a-webvtt-timestamp){#ref-for-collect-a-webvtt-timestamp-3 link-type="dfn"}.

        4.  If that algorithm does not fail, and if `position`{.variable} now points at the end of `input`{.variable} (i.e. there are no trailing characters after the timestamp), then create a [WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-2 link-type="dfn"} whose value is the collected time, then append it to `current`{.variable}.

            Otherwise, ignore the token.

10. Jump to the step labeled *loop*.

The [WebVTT cue text tokenizer]{#webvtt-cue-text-tokenizer .dfn .dfn-paneled dfn-type="dfn" noexport=""} is as follows. It emits a token, which is either a string (whose value is a sequence of characters), a start tag (with a tag name, a list of classes, and optionally an annotation), an end tag (with a tag name), or a timestamp tag (with a tag value).

1.  Let `input`{.variable} and `position`{.variable} be the same variables as those of the same name in the algorithm that invoked these steps.

2.  Let `tokenizer state`{.variable} be [WebVTT data state](#webvtt-data-state){#ref-for-webvtt-data-state-1 link-type="dfn"}.

3.  Let `result`{.variable} be the empty string.

4.  Let `classes`{.variable} be an empty list.

5.  *Loop*: If `position`{.variable} is past the end of `input`{.variable}, let `c`{.variable} be an end-of-file marker. Otherwise, let `c`{.variable} be the character in `input`{.variable} pointed to by `position`{.variable}.

    An end-of-file marker is not a Unicode character, it is used to end the tokenizer.

6.  Jump to the state given by `tokenizer state`{.variable}:

    [WebVTT data state]{#webvtt-data-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+0026 AMPERSAND (&)

        :   Set `tokenizer state`{.variable} to the [HTML character reference in data state](#html-character-reference-in-data-state){#ref-for-html-character-reference-in-data-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        U+003C LESS-THAN SIGN (\<)

        :   If `result`{.variable} is the empty string, then set `tokenizer state`{.variable} to the [WebVTT tag state](#webvtt-tag-state){#ref-for-webvtt-tag-state-1 link-type="dfn"} and jump to the step labeled *next*.

            Otherwise, return a string token whose value is `result`{.variable} and abort these steps.

        End-of-file marker

        :   Return a string token whose value is `result`{.variable} and abort these steps.

        Anything else

        :   Append `c`{.variable} to `result`{.variable} and jump to the step labeled *next*.

    [HTML character reference in data state]{#html-character-reference-in-data-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Attempt to [consume an HTML character reference](#consume-an-html-character-reference){#ref-for-consume-an-html-character-reference-1 link-type="dfn"}, with no [additional allowed character](https://www.w3.org/TR/html51/syntax.html#additional-allowed-character){link-type="dfn"}.

        If nothing is returned, append a U+0026 AMPERSAND character (&) to `result`{.variable}.

        Otherwise, append the data of the character tokens that were returned to `result`{.variable}.

        Then, in any case, set `tokenizer state`{.variable} to the [WebVTT data state](#webvtt-data-state){#ref-for-webvtt-data-state-2 link-type="dfn"}, and jump to the step labeled *next*.

    [WebVTT tag state]{#webvtt-tag-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+0009 CHARACTER TABULATION (tab) character\
        U+000A LINE FEED (LF) character\
        U+000C FORM FEED (FF) character\
        U+0020 SPACE character

        :   Set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        U+002E FULL STOP character (.)

        :   Set `tokenizer state`{.variable} to the [WebVTT start tag class state](#webvtt-start-tag-class-state){#ref-for-webvtt-start-tag-class-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        U+002F SOLIDUS character (/)

        :   Set `tokenizer state`{.variable} to the [WebVTT end tag state](#webvtt-end-tag-state){#ref-for-webvtt-end-tag-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        [ASCII digits](https://www.w3.org/TR/html51/infrastructure.html#ascii-digits){link-type="dfn"}

        :   Set `result`{.variable} to `c`{.variable}, set `tokenizer state`{.variable} to the [WebVTT timestamp tag state](#webvtt-timestamp-tag-state){#ref-for-webvtt-timestamp-tag-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Return a start tag whose tag name is the empty string, with no classes and no annotation, and abort these steps.

        Anything else

        :   Set `result`{.variable} to `c`{.variable}, set `tokenizer state`{.variable} to the [WebVTT start tag state](#webvtt-start-tag-state){#ref-for-webvtt-start-tag-state-1 link-type="dfn"}, and jump to the step labeled *next*.

    [WebVTT start tag state]{#webvtt-start-tag-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+0009 CHARACTER TABULATION (tab) character\
        U+000C FORM FEED (FF) character\
        U+0020 SPACE character

        :   Set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-2 link-type="dfn"}, and jump to the step labeled *next*.

        U+000A LINE FEED (LF) character

        :   Set `buffer`{.variable} to `c`{.variable}, set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-3 link-type="dfn"}, and jump to the step labeled *next*.

        U+002E FULL STOP character (.)

        :   Set `tokenizer state`{.variable} to the [WebVTT start tag class state](#webvtt-start-tag-class-state){#ref-for-webvtt-start-tag-class-state-2 link-type="dfn"}, and jump to the step labeled *next*.

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Return a start tag whose tag name is `result`{.variable}, with no classes and no annotation, and abort these steps.

        Anything else

        :   Append `c`{.variable} to `result`{.variable} and jump to the step labeled *next*.

    [WebVTT start tag class state]{#webvtt-start-tag-class-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+0009 CHARACTER TABULATION (tab) character\
        U+000C FORM FEED (FF) character\
        U+0020 SPACE character

        :   Append to `classes`{.variable} an entry whose value is `buffer`{.variable}, set `buffer`{.variable} to the empty string, set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-4 link-type="dfn"}, and jump to the step labeled *next*.

        U+000A LINE FEED (LF) character

        :   Append to `classes`{.variable} an entry whose value is `buffer`{.variable}, set `buffer`{.variable} to `c`{.variable}, set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-5 link-type="dfn"}, and jump to the step labeled *next*.

        U+002E FULL STOP character (.)

        :   Append to `classes`{.variable} an entry whose value is `buffer`{.variable}, set `buffer`{.variable} to the empty string, and jump to the step labeled *next*.

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Append to `classes`{.variable} an entry whose value is `buffer`{.variable}, then return a start tag whose tag name is `result`{.variable}, with the classes given in `classes`{.variable} but no annotation, and abort these steps.

        Anything else

        :   Append `c`{.variable} to `buffer`{.variable} and jump to the step labeled *next*.

    [WebVTT start tag annotation state]{#webvtt-start-tag-annotation-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+0026 AMPERSAND (&)

        :   Set `tokenizer state`{.variable} to the [HTML character reference in annotation state](#html-character-reference-in-annotation-state){#ref-for-html-character-reference-in-annotation-state-1 link-type="dfn"}, and jump to the step labeled *next*.

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Remove any leading or trailing [ASCII whitespace](https://www.w3.org/TR/html51/infrastructure.html#space-characters){link-type="dfn"} characters from `buffer`{.variable}, and replace any sequence of one or more consecutive [ASCII whitespace](https://www.w3.org/TR/html51/infrastructure.html#space-characters){link-type="dfn"} characters in `buffer`{.variable} with a single U+0020 SPACE character; then, return a start tag whose tag name is `result`{.variable}, with the classes given in `classes`{.variable}, and with `buffer`{.variable} as the annotation, and abort these steps.

        Anything else

        :   Append `c`{.variable} to `buffer`{.variable} and jump to the step labeled *next*.

    [HTML character reference in annotation state]{#html-character-reference-in-annotation-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Attempt to [consume an HTML character reference](#consume-an-html-character-reference){#ref-for-consume-an-html-character-reference-2 link-type="dfn"}, with the [additional allowed character](https://www.w3.org/TR/html51/syntax.html#additional-allowed-character){link-type="dfn"} being U+003E GREATER-THAN SIGN (\>).

        If nothing is returned, append a U+0026 AMPERSAND character (&) to `buffer`{.variable}.

        Otherwise, append the data of the character tokens that were returned to `buffer`{.variable}.

        Then, in any case, set `tokenizer state`{.variable} to the [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state){#ref-for-webvtt-start-tag-annotation-state-6 link-type="dfn"}, and jump to the step labeled *next*.

    [WebVTT end tag state]{#webvtt-end-tag-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Return an end tag whose tag name is `result`{.variable} and abort these steps.

        Anything else

        :   Append `c`{.variable} to `result`{.variable} and jump to the step labeled *next*.

    [WebVTT timestamp tag state]{#webvtt-timestamp-tag-state .dfn .dfn-paneled dfn-type="dfn" noexport=""}

    :   Jump to the entry that matches the value of `c`{.variable}:

        U+003E GREATER-THAN SIGN character (\>)

        :   Advance `position`{.variable} to the next character in `input`{.variable}, then jump to the next \"end-of-file marker\" entry below.

        End-of-file marker

        :   Return a timestamp tag whose tag name is `result`{.variable} and abort these steps.

        Anything else

        :   Append `c`{.variable} to `result`{.variable} and jump to the step labeled *next*.

7.  *Next*: Advance `position`{.variable} to the next character in `input`{.variable}.

8.  Jump to the step labeled *loop*.

When the algorithm above says to attempt to [consume an HTML character reference]{#consume-an-html-character-reference .dfn .dfn-paneled dfn-type="dfn" noexport=""}, it means to attempt to [consume a character reference](https://www.w3.org/TR/html51/syntax.html#consume-a-character-reference){link-type="dfn"} as defined in HTML. [\[HTML51\]](#biblio-html51){link-type="biblio"}

When the HTML specification says to consume a character, in this context, it means to advance `position`{.variable} to the next character in `input`{.variable}. When it says to unconsume a character, it means to move `position`{.variable} back to the previous character in `input`{.variable}. \"EOF\" is equivalent to the end-of-file marker in this specification. Finally, this context is *not* \"as part of an attribute\" (when it comes to handling a missing semicolon).

### [6.5. ]{.secno}[[WebVTT cue text DOM construction rules]{#webvtt-cue-text-dom-construction-rules .dfn .dfn-paneled dfn-type="dfn" noexport=""}]{.content}[](#dom-construction-rules){.self-link} {#dom-construction-rules .heading .settled level="6.5"}

For the purpose of retrieving a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-24 link-type="dfn"}'s content via the [`getCueAsHTML()`{.idl}](#dom-vttcue-getcueashtml){#ref-for-dom-vttcue-getcueashtml-1 link-type="idl"} method of the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-1 link-type="idl"} interface, it needs to be parsed to a [`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"}. This section describes how.

To convert a [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-4 link-type="dfn"} to a DOM tree for [`Document`{.idl}](https://www.w3.org/TR/dom/#document){link-type="idl"} `owner`{.variable}, user agents must create a tree of DOM nodes that is isomorphous to the tree of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-6 link-type="dfn"}, with the following mapping of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-7 link-type="dfn"} to DOM nodes:

[WebVTT Node Object](#webvtt-node-object){#ref-for-webvtt-node-object-8 link-type="dfn"}

DOM node

[List of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-5 link-type="dfn"}

[`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"} node.

[WebVTT Region Object](#webvtt-region-object){#ref-for-webvtt-region-object-4 link-type="dfn"}

[`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"} node.

[WebVTT Class Object](#webvtt-class-object){#ref-for-webvtt-class-object-3 link-type="dfn"}

HTML [span](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-span){link-type="element"} element.

[WebVTT Italic Object](#webvtt-italic-object){#ref-for-webvtt-italic-object-3 link-type="dfn"}

HTML [i](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-i){link-type="element"} element.

[WebVTT Bold Object](#webvtt-bold-object){#ref-for-webvtt-bold-object-4 link-type="dfn"}

HTML [b](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-b){link-type="element"} element.

[WebVTT Underline Object](#webvtt-underline-object){#ref-for-webvtt-underline-object-3 link-type="dfn"}

HTML [u](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-u){link-type="element"} element.

[WebVTT Ruby Object](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-4 link-type="dfn"}

HTML [ruby](https://www.w3.org/TR/html51/textlevel-semantics.html#the-ruby-element){link-type="element"} element.

[WebVTT Ruby Text Object](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-4 link-type="dfn"}

HTML [rt](https://www.w3.org/TR/html51/textlevel-semantics.html#the-rt-element){link-type="element"} element.

[WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-4 link-type="dfn"}

HTML [span](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-span){link-type="element"} element with a [title](https://www.w3.org/TR/html51/dom.html#the-title-attribute){link-type="element-attr"} attribute set to the [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-5 link-type="dfn"}'s value.

[WebVTT Language Object](#webvtt-language-object){#ref-for-webvtt-language-object-3 link-type="dfn"}

HTML [span](https://www.w3.org/TR/html51/textlevel-semantics.html#elementdef-span){link-type="element"} element with a [lang](https://www.w3.org/TR/html51/dom.html#element-attrdef-global-lang){link-type="element-attr"} attribute set to the [WebVTT Language Object](#webvtt-language-object){#ref-for-webvtt-language-object-4 link-type="dfn"}'s [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-5 link-type="dfn"}.

[WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-4 link-type="dfn"}

[`Text`{.idl}](https://www.w3.org/TR/dom/#text){link-type="idl"} node whose [`data`{.idl}](https://www.w3.org/TR/dom/#concept-cd-data){link-type="idl"} is the value of the [WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-5 link-type="dfn"}.

[WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-3 link-type="dfn"}

[`ProcessingInstruction`{.idl}](https://www.w3.org/TR/dom/#processinginstruction){link-type="idl"} node whose [`target`{.idl}](https://www.w3.org/TR/dom/#dom-event-target){link-type="idl"} is \"`timestamp`\" and whose [`data`{.idl}](https://www.w3.org/TR/dom/#concept-cd-data){link-type="idl"} is a [WebVTT timestamp](#webvtt-timestamp){#ref-for-webvtt-timestamp-8 link-type="dfn"} representing the value of the [WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-4 link-type="dfn"}, with all optional components included, with one leading zero if the `hours`{.variable} component is less than ten, and with no leading zeros otherwise.

HTML elements created as part of the mapping described above must have their [`namespaceURI`{.idl}](https://www.w3.org/TR/dom/#dom-element-namespaceuri){link-type="idl"} set to the [HTML namespace](https://www.w3.org/TR/html51/infrastructure.html#html-namespace){link-type="dfn"}, use the appropriate IDL interface as defined in the HTML specification, and, if the corresponding [WebVTT Internal Node Object](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-8 link-type="dfn"} has any [applicable classes](#webvtt-node-objects-applicable-classes){#ref-for-webvtt-node-objects-applicable-classes-3 link-type="dfn"}, must have a [class](https://www.w3.org/TR/html51/dom.html#classes){link-type="element-attr"} attribute set to the string obtained by concatenating all those classes, each separated from the next by a single U+0020 SPACE character.

The [`ownerDocument`{.idl}](https://www.w3.org/TR/dom/#dom-node-ownerdocument){link-type="idl"} attribute of all nodes in the DOM tree must be set to the given document `owner`{.variable}.

All characteristics of the DOM nodes that are not described above or dependent on characteristics defined above must be left at their initial values.

### [6.6. ]{.secno}[WebVTT rules for extracting the chapter title]{.content}[](#rules-for-extracting-the-chapter-title){.self-link} {#rules-for-extracting-the-chapter-title .heading .settled .algorithm algorithm="WebVTT rules for extracting the chapter
title" level="6.6"}

The [WebVTT rules for extracting the chapter title]{#webvtt-rules-for-extracting-the-chapter-title .dfn .dfn-paneled dfn-type="dfn" noexport=""} for a [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-25 link-type="dfn"} `cue`{.variable} are as follows:

1.  Let `nodes`{.variable} be the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-6 link-type="dfn"} obtained by applying the [WebVTT cue text parsing rules](#webvtt-cue-text-parsing-rules){#ref-for-webvtt-cue-text-parsing-rules-1 link-type="dfn"} to the `cue`{.variable}'s [cue text](#cue-text){#ref-for-cue-text-11 link-type="dfn"}.

2.  Return the concatenation of the values of each [WebVTT Text Object](#webvtt-text-object){#ref-for-webvtt-text-object-6 link-type="dfn"} in `nodes`{.variable}, in a pre-order, depth-first traversal, excluding [WebVTT Ruby Text Objects](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-5 link-type="dfn"} and their descendants.

## [7. ]{.secno}[Rendering]{.content}[](#rendering){.self-link} {#rendering .heading .settled level="7"}

This section describes in some detail how to visually render [WebVTT caption or subtitle cues](#webvtt-caption-or-subtitle-cue){#ref-for-webvtt-caption-or-subtitle-cue-2 link-type="dfn"} in a user agent. The processing model is quite tightly linked to media elements in HTML, where CSS is available. [User agents that do not support CSS](#user-agents-that-do-not-support-css){#ref-for-user-agents-that-do-not-support-css-1 link-type="dfn"} are expected to render plain text only, without styling and positioning features. [User agents that do not support a full HTML CSS engine](#user-agents-that-do-not-support-a-full-html-css-engine){#ref-for-user-agents-that-do-not-support-a-full-html-css-engine-2 link-type="dfn"} are expected to render an equivalent visual representation to what a user agent with a full CSS engine would render.

### [7.1. ]{.secno}[Processing model]{.content}[](#processing-model){.self-link} {#processing-model .heading .settled .algorithm algorithm="Processing model" level="7.1"}

The [rules for updating the display of WebVTT text tracks]{#rules-for-updating-the-display-of-webvtt-text-tracks .dfn .dfn-paneled dfn-type="dfn" noexport=""} render the [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} of a [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} (specifically, a [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element), or of another playback mechanism, by applying the steps below. All the [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} that use these rules for a given [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"}, or other playback mechanism, are rendered together, to avoid overlapping subtitles from multiple tracks. A fallback language `language`{.variable} may be set when calling this algorithm.

In HTML, audio elements don't have a visual rendering area and therefore, this algorithm will abort for audio elements. When authors do create WebVTT captions or subtitles for audio resources, they need to publish them in a video element for rendering by the user agent.

The output of the steps below is a set of CSS boxes that covers the rendering area of the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} or other playback mechanism, which user agents are expected to render in a manner suiting the user.

The rules are as follows:

1.  If the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} is an [audio](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-audio-element){link-type="element"} element, or is another playback mechanism with no rendering area, abort these steps.

2.  Let `video`{.variable} be the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} or other playback mechanism.

3.  Let `output`{.variable} be an empty list of absolutely positioned CSS block boxes.

4.  If the user agent is [exposing a user interface](https://www.w3.org/TR/html51/semantics-embedded-content.html#exposing-a-user-interface){link-type="dfn"} for `video`{.variable}, add to `output`{.variable} one or more completely transparent positioned CSS block boxes that cover the same region as the user interface.

5.  If the last time these rules were run, the user agent was not [exposing a user interface](https://www.w3.org/TR/html51/semantics-embedded-content.html#exposing-a-user-interface){link-type="dfn"} for `video`{.variable}, but now it is, optionally let `reset`{.variable} be true. Otherwise, let `reset`{.variable} be false.

6.  Let `tracks`{.variable} be the subset of `video`{.variable}'s [list of text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-text-tracks){link-type="dfn"} that have as their [rules for updating the text track rendering](https://www.w3.org/TR/html51/semantics-embedded-content.html#rules-for-updating-the-text-track-rendering){link-type="dfn"} these [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-3 link-type="dfn"}, and whose [text track mode](https://www.w3.org/TR/html51/semantics-embedded-content.html#a-mode){link-type="dfn"} is [showing](https://www.w3.org/TR/html51/semantics-embedded-content.html#modedef-track-showing){link-type="dfn"}.

7.  Let `cues`{.variable} be an empty list of [text track cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"}.

8.  For each track `track`{.variable} in `tracks`{.variable}, append to `cues`{.variable} all the [cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"} from `track`{.variable}'s [list of cues](https://www.w3.org/TR/html51/semantics-embedded-content.html#list-of-cues){link-type="dfn"} that have their [text track cue active flag](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-active-flag){link-type="dfn"} set.

9.  Let `regions`{.variable} be an empty list of [WebVTT regions](#webvtt-region){#ref-for-webvtt-region-12 link-type="dfn"}.

10. For each track `track`{.variable} in `tracks`{.variable}, append to `regions`{.variable} all the [regions](#webvtt-region){#ref-for-webvtt-region-13 link-type="dfn"} with an identifier from `track`{.variable}'s [list of regions](#text-track-list-of-regions){#ref-for-text-track-list-of-regions-4 link-type="dfn"}.

11. If `reset`{.variable} is false, then, for each [WebVTT region](#webvtt-region){#ref-for-webvtt-region-14 link-type="dfn"} `region`{.variable} in `regions`{.variable} let `regionNode`{.variable} be a [WebVTT region object](#webvtt-region-object){#ref-for-webvtt-region-object-5 link-type="dfn"}.

12. Apply the following steps for each `regionNode`{.variable}:

    1.  Prepare some variables for the application of CSS properties to `regionNode`{.variable} as follows:

        -   Let `regionWidth`{.variable} be the [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-3 link-type="dfn"}. Let `width`{.variable} be [`regionWidth`{.variable} vw]{.css} ([vw](https://drafts.csswg.org/css-values-4/#vw){.css link-type="maybe"} is a CSS unit). [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"}

        -   Let `lineHeight`{.variable} be [6vh]{.css} ([vh](https://drafts.csswg.org/css-values-4/#vh){.css link-type="maybe"} is a CSS unit) [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"} and `regionHeight`{.variable} be the [WebVTT region lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-3 link-type="dfn"}. Let `lines`{.variable} be `lineHeight`{.variable} multiplied by `regionHeight`{.variable}.

        -   Let `viewportAnchorX`{.variable} be the x dimension of the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-3 link-type="dfn"} and `regionAnchorX`{.variable} be the x dimension of the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-4 link-type="dfn"}. Let `leftOffset`{.variable} be `regionAnchorX`{.variable} multiplied by `width`{.variable} divided by 100.0. Let `left`{.variable} be `leftOffset`{.variable} subtracted from [`viewportAnchorX`{.variable} vw]{.css}.

        -   Let `viewportAnchorY`{.variable} be the y dimension of the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-5 link-type="dfn"} and `regionAnchorY`{.variable} be the y dimension of the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-6 link-type="dfn"}. Let `topOffset`{.variable} be `regionAnchorY`{.variable} multiplied by `lines`{.variable} divided by 100.0. Let `top`{.variable} be `topOffset`{.variable} subtracted from [`viewportAnchorY`{.variable} vh]{.css}.

    2.  Apply the terms of the CSS specifications to `regionNode`{.variable} within the following constraints, thus obtaining a CSS box `box`{.variable} positioned relative to an initial containing block:

        1.  No style sheets are associated with `regionNode`{.variable}. (The regionNodes are subsequently restyled using style sheets after their boxes are generated, as described below.)

        2.  Properties on `regionNode`{.variable} have their values set as defined in the next section. (That section uses some of the variables whose values were calculated earlier in this algorithm.)

        3.  The video viewport (and initial containing block) is video's rendering area.

    3.  Add the CSS box `box`{.variable} to `output`{.variable}.

13. If `reset`{.variable} is false, then, for each [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-26 link-type="dfn"} `cue`{.variable} in `cues`{.variable}: if `cue`{.variable}'s [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"} has a set of CSS boxes, then:

    -   If `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-7 link-type="dfn"} is not null, add those boxes to that region's `box`{.variable} and remove `cue`{.variable} from `cues`{.variable}.

    -   Otherwise, add those boxes to `output`{.variable} and remove `cue`{.variable} from `cues`{.variable}.

14. For each [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-27 link-type="dfn"} `cue`{.variable} in `cues`{.variable} that has not yet had corresponding CSS boxes added to `output`{.variable}, in [text track cue order](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-order){link-type="dfn"}, run the following substeps:

    1.  Let `nodes`{.variable} be the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-7 link-type="dfn"} obtained by applying the [WebVTT cue text parsing rules](#webvtt-cue-text-parsing-rules){#ref-for-webvtt-cue-text-parsing-rules-2 link-type="dfn"}, with the fallback language `language`{.variable} if provided, to the `cue`{.variable}'s [cue text](#cue-text){#ref-for-cue-text-12 link-type="dfn"}.

    2.  If `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-8 link-type="dfn"} is null, run the following substeps:

        1.  [Apply WebVTT cue settings](#apply-webvtt-cue-settings){#ref-for-apply-webvtt-cue-settings-1 link-type="dfn"} to obtain CSS boxes `boxes`{.variable} from `nodes`{.variable}.

        2.  Let `cue`{.variable}'s [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"} have the CSS boxes in `boxes`{.variable}.

        3.  Add the CSS boxes in `boxes`{.variable} to `output`{.variable}.

    3.  Otherwise, run the following substeps:

        1.  Let `region`{.variable} be `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-9 link-type="dfn"}.

        2.  If `region`{.variable}'s [WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-3 link-type="dfn"} setting is [up](#webvtt-region-scroll-up){#ref-for-webvtt-region-scroll-up-2 link-type="dfn"} and `region`{.variable} already has one child, set `region`{.variable}'s [transition-property](https://www.w3.org/TR/css3-transitions/#propdef-transition-property){.property link-type="propdesc"} to [top]{.css} and [transition-duration](https://www.w3.org/TR/css3-transitions/#propdef-transition-duration){.property link-type="propdesc"} to [0.433s]{.css}.

        3.  Let `offset`{.variable} be `cue`{.variable}'s [computed position](#cue-computed-position){#ref-for-cue-computed-position-1 link-type="dfn"} multiplied by `region`{.variable}'s [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-4 link-type="dfn"} and divided by 100 (i.e. interpret it as a percentage of the region width).

        4.  Adjust `offset`{.variable} using `cue`{.variable}'s [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-2 link-type="dfn"} as follows:

            If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-3 link-type="dfn"} is [center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-3 link-type="dfn"}

            :   Subtract half of `region`{.variable}'s [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-5 link-type="dfn"} from `offset`{.variable}.

            If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-4 link-type="dfn"} is [line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-6 link-type="dfn"}

            :   Subtract `region`{.variable}'s [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-6 link-type="dfn"} from `offset`{.variable}.

        5.  Let `left`{.variable} be [`offset`{.variable} %]{.css}. [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"}

        6.  [Obtain a set of CSS boxes](#obtain-a-set-of-css-boxes){#ref-for-obtain-a-set-of-css-boxes-1 link-type="dfn"} `boxes`{.variable} positioned relative to an initial containing block.

        7.  If there are no line boxes in `boxes`{.variable}, skip the remainder of these substeps for `cue`{.variable}. The cue is ignored.

        8.  Let `cue`{.variable}'s [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"} have the CSS boxes in `boxes`{.variable}.

        9.  Add the CSS boxes in `boxes`{.variable} to `region`{.variable}.

        10. If the CSS boxes `boxes`{.variable} together have a height less than the height of the `region`{.variable} box, let `diff`{.variable} be the absolute difference between the two height values. Increase `top`{.variable} by `diff`{.variable} and re-apply it to `regionNode`{.variable}.

15. Return `output`{.variable}.

User agents may allow the user to override the above algorithm's positioning of cues, e.g. by dragging them to another location on the [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"}, or even off the [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} entirely.

### [7.2. ]{.secno}[Processing cue settings]{.content}[](#processing-cue-settings){.self-link} {#processing-cue-settings .heading .settled .algorithm algorithm="Processing cue settings" level="7.2"}

When the processing algorithm above requires that the user agent [apply WebVTT cue settings]{#apply-webvtt-cue-settings .dfn .dfn-paneled dfn-type="dfn" lt="apply WebVTT cue settings" noexport=""} to obtain CSS boxes from a [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-8 link-type="dfn"} `nodes`{.variable}, the user agent must run the following algorithm.

1.  If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-17 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-15 link-type="dfn"}, then let `writing-mode`{.variable} be \"horizontal-tb\". Otherwise, if the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-18 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-5 link-type="dfn"}, then let `writing-mode`{.variable} be \"vertical-rl\". Otherwise, the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-19 link-type="dfn"} is [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-5 link-type="dfn"}; let `writing-mode`{.variable} be \"vertical-lr\".

2.  Determine the value of `maximum size`{.variable} for `cue`{.variable} as per the appropriate rules from the following list:

    If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-5 link-type="dfn"} is [line-left](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-7 link-type="dfn"}

    :   Let `maximum size`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-2 link-type="dfn"} subtracted from 100.

    If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-6 link-type="dfn"} is [line-right](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-7 link-type="dfn"}

    :   Let `maximum size`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-3 link-type="dfn"}.

    If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-7 link-type="dfn"} is [center](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-4 link-type="dfn"}, and the [computed position](#cue-computed-position){#ref-for-cue-computed-position-4 link-type="dfn"} is less than or equal to 50

    :   Let `maximum size`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-5 link-type="dfn"} multiplied by two.

    If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-8 link-type="dfn"} is [center](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-5 link-type="dfn"}, and the [computed position](#cue-computed-position){#ref-for-cue-computed-position-6 link-type="dfn"} is greater than 50

    :   Let `maximum size`{.variable} be the result of subtracting [computed position](#cue-computed-position){#ref-for-cue-computed-position-7 link-type="dfn"} from 100 and then multiplying the result by two.

3.  If the [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-10 link-type="dfn"} is less than `maximum size`{.variable}, then let `size`{.variable} be [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-11 link-type="dfn"}. Otherwise, let `size`{.variable} be `maximum size`{.variable}.

4.  If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-20 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-16 link-type="dfn"}, then let `width`{.variable} be [`size`{.variable} vw]{.css} and `height`{.variable} be [auto](https://drafts.csswg.org/css-sizing-3/#valdef-width-auto){.css link-type="maybe"}. Otherwise, let `width`{.variable} be [auto](https://drafts.csswg.org/css-sizing-3/#valdef-width-auto){.css link-type="maybe"} and `height`{.variable} be [`size`{.variable} vh]{.css}. (These are CSS values used by the next section to set CSS properties for the rendering; [vw](https://drafts.csswg.org/css-values-4/#vw){.css link-type="maybe"} and [vh](https://drafts.csswg.org/css-values-4/#vh){.css link-type="maybe"} are CSS units.) [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"}

5.  Determine the value of `x-position`{.variable} or `y-position`{.variable} for `cue`{.variable} as per the appropriate rules from the following list:

    If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-21 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-17 link-type="dfn"}

    :

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-9 link-type="dfn"} is [line-left alignment](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-8 link-type="dfn"}

        :   Let `x-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-8 link-type="dfn"}.

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-10 link-type="dfn"} is [center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-6 link-type="dfn"}

        :   Let `x-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-9 link-type="dfn"} minus half of `size`{.variable}.

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-11 link-type="dfn"} is [line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-8 link-type="dfn"}

        :   Let `x-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-10 link-type="dfn"} minus `size`{.variable}.

    If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-22 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-6 link-type="dfn"} or [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-6 link-type="dfn"}

    :

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-12 link-type="dfn"} is [line-left alignment](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-9 link-type="dfn"}

        :   Let `y-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-11 link-type="dfn"}.

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-13 link-type="dfn"} is [center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-7 link-type="dfn"}

        :   Let `y-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-12 link-type="dfn"} minus half of `size`{.variable}.

        If the [computed position alignment](#cue-computed-position-alignment){#ref-for-cue-computed-position-alignment-14 link-type="dfn"} is [line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-9 link-type="dfn"}

        :   Let `y-position`{.variable} be the [computed position](#cue-computed-position){#ref-for-cue-computed-position-13 link-type="dfn"} minus `size`{.variable}.

6.  Determine the value of whichever of `x-position`{.variable} or `y-position`{.variable} is not yet calculated for `cue`{.variable} as per the appropriate rules from the following list:

    If the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-10 link-type="dfn"} is false

    :

        If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-23 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-18 link-type="dfn"}

        :   Let `y-position`{.variable} be the [computed line](#cue-computed-line){#ref-for-cue-computed-line-2 link-type="dfn"}.

        If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-24 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-7 link-type="dfn"} or [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-7 link-type="dfn"}

        :   Let `x-position`{.variable} be the [computed line](#cue-computed-line){#ref-for-cue-computed-line-3 link-type="dfn"}.

    If the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-11 link-type="dfn"} is true

    :

        If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-25 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-19 link-type="dfn"}

        :   Let `y-position`{.variable} be 0.

        If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-26 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-8 link-type="dfn"} or [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-8 link-type="dfn"}

        :   Let `x-position`{.variable} be 0.

    These are not final positions, they are merely temporary positions used to calculate box dimensions below.

7.  Let `left`{.variable} be [`x-position`{.variable} vw]{.css} and `top`{.variable} be [`y-position`{.variable} vh]{.css}. (These are CSS values used by the next section to set CSS properties for the rendering; [vw](https://drafts.csswg.org/css-values-4/#vw){.css link-type="maybe"} and [vh](https://drafts.csswg.org/css-values-4/#vh){.css link-type="maybe"} are CSS units.) [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"}

8.  [Obtain a set of CSS boxes](#obtain-a-set-of-css-boxes){#ref-for-obtain-a-set-of-css-boxes-2 link-type="dfn"} `boxes`{.variable} positioned relative to an initial containing block.

9.  If there are no line boxes in `boxes`{.variable}, skip the remainder of these substeps for `cue`{.variable}. The cue is ignored.

10. Adjust the positions of `boxes`{.variable} according to the appropriate steps from the following list:

    If `cue`{.variable}'s [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-12 link-type="dfn"} is true

    :   Many of the steps in this algorithm vary according to the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-27 link-type="dfn"}. Steps labeled \"**Horizontal**\" must be followed only when the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-28 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-20 link-type="dfn"}, steps labeled \"**Vertical**\" must be followed when the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-29 link-type="dfn"} is either [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-9 link-type="dfn"} or [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-9 link-type="dfn"}, steps labeled \"**Vertical Growing Left**\" must be followed only when the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-30 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-10 link-type="dfn"}, and steps labeled \"**Vertical Growing Right**\" must be followed only when the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-31 link-type="dfn"} is [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-10 link-type="dfn"}.

        1.  **Horizontal**: Let `full dimension`{.variable} be the height of `video`{.variable}'s rendering area.

            **Vertical**: Let `full dimension`{.variable} be the width of `video`{.variable}'s rendering area.

        2.  **Horizontal**: Let `step`{.variable} be the height of the first line box in `boxes`{.variable}.

            **Vertical**: Let `step`{.variable} be the width of the first line box in `boxes`{.variable}.

        3.  If `step`{.variable} is zero, then jump to the step labeled *done positioning* below.

        4.  Let `line`{.variable} be `cue`{.variable}'s [computed line](#cue-computed-line){#ref-for-cue-computed-line-4 link-type="dfn"}.

        5.  Round `line`{.variable} to an integer by adding 0.5 and then flooring it.

        6.  **Vertical Growing Left**: Add one to `line`{.variable} then negate it.

        7.  Let `position`{.variable} be the result of multiplying `step`{.variable} and `line`{.variable}.

        8.  **Vertical Growing Left**: Decrease `position`{.variable} by the width of the bounding box of the boxes in `boxes`{.variable}, then increase `position`{.variable} by `step`{.variable}.

        9.  If `line`{.variable} is less than zero then increase `position`{.variable} by `max dimension`{.variable}, and negate `step`{.variable}.

        10. **Horizontal**: Move all the boxes in `boxes`{.variable} down by the distance given by `position`{.variable}.

            **Vertical**: Move all the boxes in `boxes`{.variable} right by the distance given by `position`{.variable}.

        11. Remember the position of all the boxes in `boxes`{.variable} as their `specified position`{.variable}.

        12. Let `title area`{.variable} be a box that covers all of the `video`{.variable}'s rendering area.

        13. *Step loop*: If none of the boxes in `boxes`{.variable} would overlap any of the boxes in `output`{.variable}, and all of the boxes in `boxes`{.variable} are entirely within the `title area`{.variable} box, then jump to the step labeled *done positioning* below.

        14. **Horizontal**: If `step`{.variable} is negative and the top of the first line box in `boxes`{.variable} is now above the top of the `title area`{.variable}, or if `step`{.variable} is positive and the bottom of the first line box in `boxes`{.variable} is now below the bottom of the `title area`{.variable}, jump to the step labeled *switch direction*.

            **Vertical**: If `step`{.variable} is negative and the left edge of the first line box in `boxes`{.variable} is now to the left of the left edge of the `title area`{.variable}, or if `step`{.variable} is positive and the right edge of the first line box in `boxes`{.variable} is now to the right of the right edge of the `title area`{.variable}, jump to the step labeled *switch direction*.

        15. **Horizontal**: Move all the boxes in `boxes`{.variable} down by the distance given by `step`{.variable}. (If `step`{.variable} is negative, then this will actually result in an upwards movement of the boxes in absolute terms.)

            **Vertical**: Move all the boxes in `boxes`{.variable} right by the distance given by `step`{.variable}. (If `step`{.variable} is negative, then this will actually result in a leftwards movement of the boxes in absolute terms.)

        16. Jump back to the step labeled *step loop*.

        17. *Switch direction*: If `switched`{.variable} is true, then remove all the boxes in `boxes`{.variable}, and jump to the step labeled *done positioning* below.

        18. Otherwise, move all the boxes in `boxes`{.variable} back to their `specified position`{.variable} as determined in the earlier step.

        19. Negate `step`{.variable}.

        20. Set `switched`{.variable} to true.

        21. Jump back to the step labeled *step loop*.

    If `cue`{.variable}'s [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-13 link-type="dfn"} is false

    :   1.  Let `bounding box`{.variable} be the bounding box of the boxes in `boxes`{.variable}.

        2.  Run the appropriate steps from the following list:

            If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-32 link-type="dfn"} is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-21 link-type="dfn"}

            :

                If the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-10 link-type="dfn"} is [center alignment](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-3 link-type="dfn"}

                :   Move all the boxes in `boxes`{.variable} up by half of the height of `bounding box`{.variable}.

                If the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-11 link-type="dfn"} is [end alignment](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-3 link-type="dfn"}

                :   Move all the boxes in `boxes`{.variable} up by the height of `bounding box`{.variable}.

            If the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-33 link-type="dfn"} is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-11 link-type="dfn"} or [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-11 link-type="dfn"}

            :

                If the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-12 link-type="dfn"} is [center alignment](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-4 link-type="dfn"}

                :   Move all the boxes in `boxes`{.variable} left by half of the width of `bounding box`{.variable}.

                If the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-13 link-type="dfn"} is [end alignment](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-4 link-type="dfn"}

                :   Move all the boxes in `boxes`{.variable} left by the width of `bounding box`{.variable}.

        3.  If none of the boxes in `boxes`{.variable} would overlap any of the boxes in `output`{.variable}, and all the boxes in `boxes`{.variable} are within the `video`{.variable}'s rendering area, then jump to the step labeled *done positioning* below.

        4.  If there is a position to which the boxes in `boxes`{.variable} can be moved while maintaining the relative positions of the boxes in `boxes`{.variable} to each other such that none of the boxes in `boxes`{.variable} would overlap any of the boxes in `output`{.variable}, and all the boxes in `boxes`{.variable} would be within the `video`{.variable}'s rendering area, then move the boxes in `boxes`{.variable} to the closest such position to their current position, and then jump to the step labeled *done positioning* below. If there are multiple such positions that are equidistant from their current position, use the highest one amongst them; if there are several at that height, then use the leftmost one amongst them.

        5.  Otherwise, jump to the step labeled *done positioning* below. (The boxes will unfortunately overlap.)

11. *Done positioning*: Return `boxes`{.variable}.

### [7.3. ]{.secno}[Obtaining CSS boxes]{.content}[](#obtaining-css-boxes){.self-link} {#obtaining-css-boxes .heading .settled .algorithm algorithm="Obtaining CSS boxes" level="7.3"}

When the processing algorithm above requires that the user agent [obtain a set of CSS boxes]{#obtain-a-set-of-css-boxes .dfn .dfn-paneled dfn-type="dfn" lt="obtain a set of CSS boxes" noexport=""} `boxes`{.variable}, then apply the terms of the CSS specifications to `nodes`{.variable} within the following constraints: [\[CSS22\]](#biblio-css22){link-type="biblio"}

-   The *document tree* is the tree of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-9 link-type="dfn"} rooted at `nodes`{.variable}.

-   For the purpose of selectors in STYLE blocks of a WebVTT file, the style sheet must apply to a hypothetical document that contains a single empty element with no explicit name, no namespace, no attributes, no classes, no IDs, and unknown primary language, that acts like the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} for the [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} that were sourced from the given WebVTT file. The selectors must not match other [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} for the same [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"}. In this hypothetical document, the element must not match any selector that would match the element itself.

    This element exists only to be the [originating element](https://www.w3.org/TR/selectors4/#originating-element){link-type="dfn"} for the [::cue]{.css}, [::cue()]{.css}, [::cue-region]{.css} and [::cue-region()]{.css} pseudo-elements.

-   For the purpose of determining the [cascade](https://www.w3.org/TR/css-cascade-4/#cascade){link-type="dfn"} of the declarations in STYLE blocks of a WebVTT file, the relative order of appearance of the style sheets must be the same order as they were added to the collection, and the order of appearance of the collection must be after any style sheets that apply to the associated [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element's document.

    ::: {#example-01d14f75 .example}
    [](#example-01d14f75){.self-link}
    For example, given the following (invalid) HTML document:

        <!doctype html>
        <title>Invalid cascade example</title>
        <video controls autoplay src="video.webm">
         <track default src="track.vtt">
        </video>
        <style>
         ::cue { color:red }
        </style>

    \...and the \"track.vtt\" file contains:

        WEBVTT

        STYLE
        ::cue { color:lime }

        00:00:00.000 --> 00:00:25.000
        Red or green?

    The [color:lime]{.css} declaration would win, because it is last in the [cascade](https://www.w3.org/TR/css-cascade-4/#cascade){link-type="dfn"}, even though the [style](https://www.w3.org/TR/html51/document-metadata.html#the-style-element){link-type="element"} element is after the [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element in the document order.
    :::

-   For the purpose of resolving URLs in STYLE blocks of a WebVTT file, or any URLs in resources referenced from STYLE blocks of a WebVTT file, if the URL's scheme is not \"`data`\", then the user agent must act as if the URL failed to resolve.

    **Supporting external resources with [\@import](https://www.w3.org/TR/css-cascade-4/#at-ruledef-import){.css link-type="maybe"} or [background-image](https://www.w3.org/TR/css3-background/#propdef-background-image){.property link-type="propdesc"} would be a new ability for [media elements](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} and [track](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-track-element){link-type="element"} elements to issue network requests as the user watches the video, which could be a privacy issue.**

-   For the purposes of processing by the CSS specification, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-9 link-type="dfn"} are equivalent to elements with the same contents.

-   For the purposes of processing by the CSS specification, [WebVTT Text Objects](#webvtt-text-object){#ref-for-webvtt-text-object-7 link-type="dfn"} are equivalent to [`Text`{.idl}](https://www.w3.org/TR/dom/#text){link-type="idl"} nodes.

-   No style sheets are associated with `nodes`{.variable}. (The nodes are subsequently restyled using style sheets after their boxes are generated, as described below.)

-   The children of the `nodes`{.variable} must be wrapped in an anonymous box whose [display](https://www.w3.org/TR/css-display-3/#propdef-display){.property link-type="propdesc"} property has the value [inline](https://www.w3.org/TR/css-display-3/#valdef-display-inline){.css link-type="maybe"}. This is the [WebVTT cue background box]{#webvtt-cue-background-box .dfn .dfn-paneled dfn-type="dfn" noexport=""}.

-   Runs of children of [WebVTT Ruby Objects](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-5 link-type="dfn"} that are not [WebVTT Ruby Text Objects](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-6 link-type="dfn"} must be wrapped in anonymous boxes whose [display](https://www.w3.org/TR/css-display-3/#propdef-display){.property link-type="propdesc"} property has the value [ruby-base](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby-base){.css link-type="maybe"}. [\[CSS3-RUBY\]](#biblio-css3-ruby){link-type="biblio"}

-   Properties on [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-10 link-type="dfn"} have their values set as defined in the next section. (That section uses some of the variables whose values were calculated earlier in this algorithm.)

-   Text runs must be wrapped according to the CSS line-wrapping rules.

-   The video viewport (and initial containing block) is `video`{.variable}'s rendering area.

Let `boxes`{.variable} be the boxes generated as descendants of the initial containing block, along with their positions.

### [7.4. ]{.secno}[Applying CSS properties to [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-11 link-type="dfn"}]{.content}[](#applying-css-properties){.self-link} {#applying-css-properties .heading .settled .algorithm algorithm="Applying CSS properties to WebVTT Node Objects" level="7.4"}

When following the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-4 link-type="dfn"}, user agents must set properties of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-12 link-type="dfn"} at the CSS user agent cascade layer as defined in this section. [\[CSS22\]](#biblio-css22){link-type="biblio"}

Initialize the (root) [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-9 link-type="dfn"} with the following CSS settings:

-   the [position](https://www.w3.org/TR/css3-positioning/#propdef-position){.property link-type="propdesc"} property must be set to [absolute](https://www.w3.org/TR/css3-positioning/#valdef-position-absolute){.css link-type="maybe"}
-   the [unicode-bidi](https://www.w3.org/TR/css-writing-modes-3/#propdef-unicode-bidi){.property link-type="propdesc"} property must be set to [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext){.css link-type="maybe"}
-   the [writing-mode](https://drafts.csswg.org/css-writing-modes-4/#propdef-writing-mode){.property link-type="propdesc"} property must be set to `writing-mode`{.variable}
-   the [top](https://www.w3.org/TR/css3-positioning/#propdef-top){.property link-type="propdesc"} property must be set to `top`{.variable}
-   the [left](https://www.w3.org/TR/css3-positioning/#propdef-left){.property link-type="propdesc"} property must be set to `left`{.variable}
-   the [width](https://www.w3.org/TR/CSS22/visudet.html#propdef-width){.property link-type="propdesc"} property must be set to `width`{.variable}
-   the [height](https://www.w3.org/TR/CSS22/visudet.html#propdef-height){.property link-type="propdesc"} property must be set to `height`{.variable}
-   the [overflow-wrap](https://www.w3.org/TR/css-text-3/#propdef-overflow-wrap){.property link-type="propdesc"} property must be set to [break-word](https://www.w3.org/TR/css-text-3/#valdef-overflow-wrap-break-word){.css link-type="maybe"}
-   the [text-wrap]{.property link-type="propdesc"} property must be set to [balance]{.css} [\[CSS-TEXT-4\]](#biblio-css-text-4){link-type="biblio"}

The variables `writing-mode`{.variable}, `top`{.variable}, `left`{.variable}, `width`{.variable}, and `height`{.variable} are the values with those names determined by the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-5 link-type="dfn"} for the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-28 link-type="dfn"} from whose [text](#cue-text){#ref-for-cue-text-13 link-type="dfn"} the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-10 link-type="dfn"} was constructed.

The [text-align](https://www.w3.org/TR/css-text-3/#propdef-text-align){.property link-type="propdesc"} property on the (root) [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-11 link-type="dfn"} must be set to the value in the second cell of the row of the table below whose first cell is the value of the corresponding [cue](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-21 link-type="dfn"}:

[WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-22 link-type="dfn"}

[text-align](https://www.w3.org/TR/css-text-3/#propdef-text-align){.property link-type="propdesc"} value

[Start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-8 link-type="dfn"}

[start](https://www.w3.org/TR/css-text-3/#valdef-text-align-start){.css link-type="maybe"}

[Center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-7 link-type="dfn"}

[center](https://www.w3.org/TR/css-text-3/#valdef-text-align-center){.css link-type="maybe"}

[End alignment](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-7 link-type="dfn"}

[end](https://www.w3.org/TR/css-text-3/#valdef-text-align-end){.css link-type="maybe"}

[Left alignment](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-6 link-type="dfn"}

[left](https://www.w3.org/TR/css-text-3/#valdef-text-align-left){.css link-type="maybe"}

[Right alignment](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-6 link-type="dfn"}

[right](https://www.w3.org/TR/css-text-3/#valdef-text-align-right){.css link-type="maybe"}

The [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand property on the (root) [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-12 link-type="dfn"} must be set to [5vh sans-serif]{.css}. [\[CSS-VALUES\]](#biblio-css-values){link-type="biblio"}

The [color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"} property on the (root) [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-13 link-type="dfn"} must be set to [rgba(255,255,255,1)]{.css}. [\[CSS3-COLOR\]](#biblio-css3-color){link-type="biblio"}

The [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand property on the [WebVTT cue background box](#webvtt-cue-background-box){#ref-for-webvtt-cue-background-box-1 link-type="dfn"} and on [WebVTT Ruby Text Objects](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-7 link-type="dfn"} must be set to [rgba(0,0,0,0.8)]{.css}. [\[CSS3-COLOR\]](#biblio-css3-color){link-type="biblio"}

The [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space){.property link-type="propdesc"} property on the (root) [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-14 link-type="dfn"} must be set to [pre-line](https://www.w3.org/TR/css-text-3/#valdef-white-space-pre-line){.css link-type="maybe"}. [\[CSS22\]](#biblio-css22){link-type="biblio"}

The [font-style](https://www.w3.org/TR/css-fonts-3/#propdef-font-style){.property link-type="propdesc"} property on [WebVTT Italic Objects](#webvtt-italic-object){#ref-for-webvtt-italic-object-4 link-type="dfn"} must be set to [italic](https://www.w3.org/TR/css-fonts-4/#valdef-font-style-italic){.css link-type="maybe"}.

The [font-weight](https://www.w3.org/TR/css-fonts-3/#propdef-font-weight){.property link-type="propdesc"} property on [WebVTT Bold Objects](#webvtt-bold-object){#ref-for-webvtt-bold-object-5 link-type="dfn"} must be set to [bold](https://www.w3.org/TR/css-fonts-4/#valdef-font-weight-bold){.css link-type="maybe"}.

The [text-decoration](https://www.w3.org/TR/css-text-decor-3/#text-decoration-property){.property link-type="propdesc"} property on [WebVTT Underline Objects](#webvtt-underline-object){#ref-for-webvtt-underline-object-4 link-type="dfn"} must be set to [underline]{.css}.

The [display](https://www.w3.org/TR/css-display-3/#propdef-display){.property link-type="propdesc"} property on [WebVTT Ruby Objects](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-6 link-type="dfn"} must be set to [ruby](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby){.css link-type="maybe"}. [\[CSS3-RUBY\]](#biblio-css3-ruby){link-type="biblio"}

The [display](https://www.w3.org/TR/css-display-3/#propdef-display){.property link-type="propdesc"} property on [WebVTT Ruby Text Objects](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-8 link-type="dfn"} must be set to [ruby-text](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby-text){.css link-type="maybe"}. [\[CSS3-RUBY\]](#biblio-css3-ruby){link-type="biblio"}

Every [WebVTT region object](#webvtt-region-object){#ref-for-webvtt-region-object-6 link-type="dfn"} is initialized with the following CSS settings:

-   the [position](https://www.w3.org/TR/css3-positioning/#propdef-position){.property link-type="propdesc"} property must be set to [absolute](https://www.w3.org/TR/css3-positioning/#valdef-position-absolute){.css link-type="maybe"}
-   the [writing-mode](https://drafts.csswg.org/css-writing-modes-4/#propdef-writing-mode){.property link-type="propdesc"} property must be set to [horizontal-tb](https://drafts.csswg.org/css-writing-modes-4/#valdef-writing-mode-horizontal-tb){.css link-type="maybe"}
-   the [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand property must be set to [rgba(0,0,0,0.8)]{.css}
-   the [overflow-wrap](https://www.w3.org/TR/css-text-3/#propdef-overflow-wrap){.property link-type="propdesc"} property must be set to [break-word](https://www.w3.org/TR/css-text-3/#valdef-overflow-wrap-break-word){.css link-type="maybe"}
-   the [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand property must be set to [5vh sans-serif]{.css}
-   the [color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"} property must be set to [rgba(255,255,255,1)]{.css}
-   the [overflow](https://www.w3.org/TR/css-overflow-3/#propdef-overflow){.property link-type="propdesc"} property must be set to [hidden](https://www.w3.org/TR/css-overflow-3/#valdef-overflow-hidden){.css link-type="maybe"}
-   the [width](https://www.w3.org/TR/CSS22/visudet.html#propdef-width){.property link-type="propdesc"} property must be set to `width`{.variable}
-   the [min-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-min-height){.property link-type="propdesc"} property must be set to [0px]{.css}
-   the [max-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-max-height){.property link-type="propdesc"} property must be set to `height`{.variable}
-   the [left](https://www.w3.org/TR/css3-positioning/#propdef-left){.property link-type="propdesc"} property must be set to `left`{.variable}
-   the [top](https://www.w3.org/TR/css3-positioning/#propdef-top){.property link-type="propdesc"} property must be set to `top`{.variable}
-   the [display](https://www.w3.org/TR/css-display-3/#propdef-display){.property link-type="propdesc"} property must be set to [inline-flex](https://www.w3.org/TR/css-flexbox-1/#valdef-display-inline-flex){.css link-type="maybe"}
-   the [flex-flow](https://www.w3.org/TR/css-flexbox-1/#propdef-flex-flow){.property link-type="propdesc"} property must be set to [column]{.css}
-   the [justify-content](https://www.w3.org/TR/css3-align/#propdef-justify-content){.property link-type="propdesc"} property must be set to [flex-end](https://www.w3.org/TR/css-flexbox-1/#valdef-justify-content-flex-end){.css link-type="maybe"}

The variables `width`{.variable}, `height`{.variable}, `top`{.variable}, and `left`{.variable} are the values with those names determined by the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-6 link-type="dfn"} for the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-15 link-type="dfn"} from which the [WebVTT region object](#webvtt-region-object){#ref-for-webvtt-region-object-7 link-type="dfn"} was constructed.

The children of every [WebVTT region object](#webvtt-region-object){#ref-for-webvtt-region-object-8 link-type="dfn"} are further initialized with these CSS settings:

-   the [position](https://www.w3.org/TR/css3-positioning/#propdef-position){.property link-type="propdesc"} property must be set to [relative](https://www.w3.org/TR/css3-positioning/#valdef-position-relative){.css link-type="maybe"}
-   the [unicode-bidi](https://www.w3.org/TR/css-writing-modes-3/#propdef-unicode-bidi){.property link-type="propdesc"} property must be set to [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext){.css link-type="maybe"}
-   the [width](https://www.w3.org/TR/CSS22/visudet.html#propdef-width){.property link-type="propdesc"} property must be set to [auto](https://drafts.csswg.org/css-sizing-3/#valdef-width-auto){.css link-type="maybe"}
-   the [height](https://www.w3.org/TR/CSS22/visudet.html#propdef-height){.property link-type="propdesc"} property must be set to `height`{.variable}
-   the [left](https://www.w3.org/TR/css3-positioning/#propdef-left){.property link-type="propdesc"} property must be set to `left`{.variable}
-   the [text-align](https://www.w3.org/TR/css-text-3/#propdef-text-align){.property link-type="propdesc"} property must be set as described for the root [List of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-15 link-type="dfn"} not part of a region

All other non-inherited properties must be set to their initial values; inherited properties on the root [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-16 link-type="dfn"} must inherit their values from the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} for which the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-29 link-type="dfn"} is being rendered, if any. If there is no [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} (i.e. if the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} is being rendered for another media playback mechanism), then inherited properties on the root [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-17 link-type="dfn"} and the [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-9 link-type="dfn"} must take their initial values.

If there are style sheets that apply to the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} or other playback mechanism, then they must be interpreted as defined in the next section.

## [8. ]{.secno}[CSS extensions]{.content}[](#css-extensions){.self-link} {#css-extensions .heading .settled level="8"}

This section specifies some CSS pseudo-elements and pseudo-classes and how they apply to WebVTT. This section does not apply to [user agents that do not support CSS](#user-agents-that-do-not-support-css){#ref-for-user-agents-that-do-not-support-css-2 link-type="dfn"}.

### [8.1. ]{.secno}[Introduction]{.content}[](#css-extensions-introduction){.self-link} {#css-extensions-introduction .heading .settled level="8.1"}

*This section is non-normative.*

The [::cue]{.css} pseudo-element represents a cue.

The [::cue(`selector`{.variable})]{.css} pseudo-element represents a cue or element inside a cue that match the given selector.

The [::cue-region]{.css} pseudo-element represents a region.

The [::cue-region(`selector`{.variable})]{.css} pseudo-element represents a region or element inside a region that match the given selector.

Similarly to all other pseudo-elements, these pseudo-elements are not directly present in the [`video`](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element's document tree.

The [:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes can be used in [::cue(`selector`{.variable})]{.css} to match [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-10 link-type="dfn"} based on the [current playback position](https://www.w3.org/TR/html51/semantics-embedded-content.html#current-position){link-type="dfn"}.

::: {#example-cue-selector .example}
[](#example-cue-selector){.self-link}

The following table shows examples of what can be selected with a given selector, together with WebVTT syntax to produce the relevant objects.

Selector (CSS syntax example)

Matches (WebVTT syntax example)

[::cue]{.css}

    video::cue {
      color: yellow;
    }

Any [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-18 link-type="dfn"}.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    Yellow!

    00:00:08.000 --> 00:00:16.000
    Also yellow!

[ID selector](https://www.w3.org/TR/selectors4/#id-selector){link-type="dfn"} in [::cue()]{.css}

    video::cue(#cue1) {
      color: yellow;
    }

Any [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-19 link-type="dfn"} with the cue's [text track cue identifier](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-identifier){link-type="dfn"} matching the given ID.

    WEBVTT

    cue1
    00:00:00.000 --> 00:00:08.000
    Yellow!

[Type selector](https://www.w3.org/TR/selectors4/#type-selector){link-type="dfn"} in [::cue()]{.css}

    video::cue(c),
    video::cue(i),
    video::cue(b),
    video::cue(u),
    video::cue(ruby),
    video::cue(rt),
    video::cue(v),
    video::cue(lang) {
      color: yellow;
    }

[WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-11 link-type="dfn"} (except the root [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-20 link-type="dfn"}) with the given name.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    <c>Yellow!</c>
    <i>Yellow!</i>
    <u>Yellow!</u>
    <b>Yellow!</b>
    <u>Yellow!</u>
    <ruby>Yellow! <rt>Yellow!</rt></ruby>
    <v Kathryn>Yellow!</v>
    <lang en>Yellow!</lang>

[Class selector](https://www.w3.org/TR/selectors4/#class-selector){link-type="dfn"} in [::cue()]{.css}

    video::cue(.loud) {
      color: yellow;
    }

[WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-12 link-type="dfn"} (except the root [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-21 link-type="dfn"}) with the given [applicable classes](#webvtt-node-objects-applicable-classes){#ref-for-webvtt-node-objects-applicable-classes-4 link-type="dfn"}.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    <c.loud>Yellow!</c>
    <i.loud>Yellow!</i>
    <u.loud>Yellow!</u>
    <b.loud>Yellow!</b>
    <u.loud>Yellow!</u>
    <ruby.loud>Yellow! <rt.loud>Yellow!</rt></ruby>
    <v.loud Kathryn>Yellow!</v>
    <lang.loud en>Yellow!</lang>

[Attribute selector](https://www.w3.org/TR/selectors4/#attribute-selector){link-type="dfn"} in [::cue()]{.css}

    video::cue([lang="en-US"]) {
      color: yellow;
    }
    video::cue(lang[lang="en-GB"]) {
      color: cyan;
    }
    video::cue(v[voice="Kathryn"] {
      color: lime;
    }

For \"lang\", the root [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-22 link-type="dfn"} or [WebVTT Language Object](#webvtt-language-object){#ref-for-webvtt-language-object-5 link-type="dfn"} with the given [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-6 link-type="dfn"}; for \"voice\", the [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-6 link-type="dfn"} with the given voice.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    Yellow!

    00:00:08.000 --> 00:00:16.000
    <lang en-GB>Cyan!</lang>

    00:00:16.000 --> 00:00:24.000
    <v Kathryn>I like lime.</v>

The [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-7 link-type="dfn"} for the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-23 link-type="dfn"} can be set by the [`srclang`](https://www.w3.org/TR/html51/semantics-embedded-content.html#dom-htmltrackelement-srclang){link-type="element-sub"} attribute in HTML.

    <video ...>
     <track src="example-attr.vtt"
            srclang="en-US" default>
    </video>

[:lang()](https://www.w3.org/TR/selectors4/#lang-pseudo){.css link-type="maybe"} pseudo-class in [::cue()]{.css}

    video::cue(:lang(en)) {
      color: yellow;
    }
    video::cue(:lang(en-GB)) {
      color: cyan;
    }

[WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-13 link-type="dfn"} with an [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-8 link-type="dfn"} matching the given language range.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    Yellow!

    00:00:08.000 --> 00:00:16.000
    <lang en-GB>Cyan!</lang>

As above, the [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-9 link-type="dfn"} for the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-24 link-type="dfn"} can be set by the [`srclang`](https://www.w3.org/TR/html51/semantics-embedded-content.html#dom-htmltrackelement-srclang){link-type="element-sub"} attribute in HTML.

[:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes in [::cue()]{.css}

    video::cue(:past) {
      color: yellow;
    }
    video::cue(:future) {
      color: cyan;
    }

In cues that have [WebVTT Timestamp Objects](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-5 link-type="dfn"}, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-14 link-type="dfn"}, depending on the [current playback position](https://www.w3.org/TR/html51/semantics-embedded-content.html#current-position){link-type="dfn"}.

    WEBVTT

    00:00:00.000 --> 00:00:08.000
    <c>No match (no timestamps)</c>

    00:00:08.000 --> 00:00:16.000
    No match <00:00:12.000> (no elements)

    00:00:16.000 --> 00:00:24.000
    <00:00:16.000> <c>This</c>
    <00:00:18.000> <c>can</c>
    <00:00:20.000> <c>match</c>
    <00:00:22.000> <c>:past/:future</c>
    <00:00:24.000>

[::cue-region]{.css}

    video::cue-region {
      color: yellow;
    }

Any region (list of [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-10 link-type="dfn"}).

    WEBVTT

    REGION
    id:editor-comments
    regionanchor:0%,0%
    viewportanchor:0%,0%

    00:00:00.000 --> 00:00:08.000
    No match (normal cue)

    00:00:08.000 --> 00:00:16.000 region:editor-comments
    Yellow!

[ID selector](https://www.w3.org/TR/selectors4/#id-selector){link-type="dfn"} in [::cue-region()]{.css}

    video::cue-region(#scroll) {
      color: cyan;
    }

Any region (list of [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-11 link-type="dfn"}) with a [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-5 link-type="dfn"} matching the given ID.

    WEBVTT

    REGION
    id:editor-comments
    width: 40%
    regionanchor:0%,100%
    viewportanchor:10%,90%

    REGION
    id:scroll
    width: 40%
    regionanchor:100%,100%
    viewportanchor:90%,90%
    scroll:up

    00:00:00.000 --> 00:00:08.000
    No match (normal cue)

    00:00:08.000 --> 00:00:16.000 region:editor-comments
    Yellow!

    00:00:10.000 --> 00:00:16.000 region:scroll
    Over here it’s Cyan!
:::

### [8.2. ]{.secno}[Processing model]{.content}[](#css-extensions-processing-model){.self-link} {#css-extensions-processing-model .heading .settled level="8.2"}

When a user agent is rendering one or more [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-30 link-type="dfn"} according to the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-7 link-type="dfn"}, [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-13 link-type="dfn"} in the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-25 link-type="dfn"} used in the rendering can be matched by certain pseudo-selectors as defined below. These selectors can begin or stop matching individual [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-14 link-type="dfn"} while a [cue](https://www.w3.org/TR/html51/semantics-embedded-content.html#cue){link-type="dfn"} is being rendered, even in between applications of the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-8 link-type="dfn"} (which are only run when the set of active cues changes). User agents that support the pseudo-element described below must dynamically update renderings accordingly. When either [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space){.property link-type="propdesc"} or one of the properties corresponding to the [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand (including [line-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-line-height){.property link-type="propdesc"}) changes value, then the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-31 link-type="dfn"}'s [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"} must be emptied and the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}'s [rules for updating the text track rendering](https://www.w3.org/TR/html51/semantics-embedded-content.html#rules-for-updating-the-text-track-rendering){link-type="dfn"} must be immediately rerun.

Pseudo-elements apply to elements that are matched by selectors. For the purpose of this section, that element is the *matched element*. The pseudo-elements defined in the following sections affect the styling of parts of [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-32 link-type="dfn"} that are being rendered for the *matched element*.

If the *matched element* is not a [video](https://www.w3.org/TR/html51/semantics-embedded-content.html#the-video-element){link-type="element"} element, the pseudo-elements defined below won't have any effect according to this specification.

A CSS user agent that implements the [text tracks](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"} model must implement the [::cue]{.css}, [::cue(`selector`{.variable})]{.css}, [::cue-region]{.css} and [::cue-region(`selector`{.variable})]{.css} pseudo-elements, and the [:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes.

#### [8.2.1. ]{.secno}[The [::cue]{.css} pseudo-element]{.content}[](#the-cue-pseudo-element){.self-link} {#the-cue-pseudo-element .heading .settled level="8.2.1"}

The [::cue[](#cue){.self-link}]{#cue .dfn dfn-type="dfn" noexport=""} pseudo-element (with no argument) matches any [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-26 link-type="dfn"} constructed for the *matched element*, with the exception that the properties corresponding to the [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand must be applied to the [WebVTT cue background box](#webvtt-cue-background-box){#ref-for-webvtt-cue-background-box-2 link-type="dfn"} rather than the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-27 link-type="dfn"}.

The following properties apply to the [::cue]{.css} pseudo-element with no argument; other properties set on the pseudo-element must be ignored:

-   [color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"}
-   [opacity](https://www.w3.org/TR/css-color-4/#propdef-opacity){.property link-type="propdesc"}
-   [visibility](https://www.w3.org/TR/CSS22/visufx.html#propdef-visibility){.property link-type="propdesc"}
-   the properties corresponding to the [text-decoration](https://www.w3.org/TR/css-text-decor-3/#text-decoration-property){.property link-type="propdesc"} shorthand
-   [text-shadow](https://www.w3.org/TR/css-text-decor-3/#text-shadow-property){.property link-type="propdesc"}
-   the properties corresponding to the [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand
-   the properties corresponding to the [outline](https://drafts.csswg.org/css-ui-4/#propdef-outline){.property link-type="propdesc"} shorthand
-   the properties corresponding to the [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand, including [line-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-line-height){.property link-type="propdesc"}
-   [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space){.property link-type="propdesc"}
-   [text-combine-upright](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-combine-upright){.property link-type="propdesc"}
-   [ruby-position](https://www.w3.org/TR/css-ruby-1/#propdef-ruby-position){.property link-type="propdesc"}

The [::cue(`selector`{.variable})[](#cue-selector){.self-link}]{#cue-selector .dfn dfn-type="dfn" noexport=""} pseudo-element with an argument must have an argument that consists of a CSS selector [\[SELECTORS4\]](#biblio-selectors4){link-type="biblio"}. It matches any [WebVTT Internal Node Object](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-15 link-type="dfn"} constructed for the *matched element* that also matches the given CSS selector, with the nodes being treated as follows:

-   The *document tree* against which the selectors are matched is the tree of [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-15 link-type="dfn"} rooted at the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-28 link-type="dfn"} for the cue.

-   [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-16 link-type="dfn"} are elements in the tree.

-   [WebVTT Leaf Node Objects](#webvtt-leaf-node-object){#ref-for-webvtt-leaf-node-object-3 link-type="dfn"} cannot be matched.

-   For the purposes of element type selectors, the names of [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-17 link-type="dfn"} are as given by the following table, where objects having the concrete class given in a cell in the first column have the name given by the second column of the same row:

    Concrete class

    Name

    [WebVTT Class Objects](#webvtt-class-object){#ref-for-webvtt-class-object-4 link-type="dfn"}

    `c`

    [WebVTT Italic Objects](#webvtt-italic-object){#ref-for-webvtt-italic-object-5 link-type="dfn"}

    `i`

    [WebVTT Bold Objects](#webvtt-bold-object){#ref-for-webvtt-bold-object-6 link-type="dfn"}

    `b`

    [WebVTT Underline Objects](#webvtt-underline-object){#ref-for-webvtt-underline-object-5 link-type="dfn"}

    `u`

    [WebVTT Ruby Objects](#webvtt-ruby-object){#ref-for-webvtt-ruby-object-7 link-type="dfn"}

    `ruby`

    [WebVTT Ruby Text Objects](#webvtt-ruby-text-object){#ref-for-webvtt-ruby-text-object-9 link-type="dfn"}

    `rt`

    [WebVTT Voice Objects](#webvtt-voice-object){#ref-for-webvtt-voice-object-7 link-type="dfn"}

    `v`

    [WebVTT Language Objects](#webvtt-language-object){#ref-for-webvtt-language-object-6 link-type="dfn"}

    `lang`

    Other elements (specifically, [lists of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-29 link-type="dfn"})

    No explicit name.

-   For the purposes of element type and universal selectors, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-18 link-type="dfn"} are considered as being in the namespace expressed as the empty string.

-   For the purposes of attribute selector matching, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-19 link-type="dfn"} have no attributes, except for [WebVTT Voice Objects](#webvtt-voice-object){#ref-for-webvtt-voice-object-8 link-type="dfn"}, which have a single attribute named \"`voice`\" whose value is the value of the [WebVTT Voice Object](#webvtt-voice-object){#ref-for-webvtt-voice-object-9 link-type="dfn"}, [WebVTT Language Objects](#webvtt-language-object){#ref-for-webvtt-language-object-7 link-type="dfn"}, which have a single attribute named \"`lang`\" whose value is the object's [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-10 link-type="dfn"}, and [lists of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-30 link-type="dfn"} that have a non-empty [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-11 link-type="dfn"}, which have a single attribute named \"`lang`\" whose value is the object's [applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-12 link-type="dfn"}.

-   For the purposes of class selector matching, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-20 link-type="dfn"} have the classes described as the [WebVTT Node Object's applicable classes](#webvtt-node-objects-applicable-classes){#ref-for-webvtt-node-objects-applicable-classes-5 link-type="dfn"}.

-   For the purposes of the [:lang()](https://www.w3.org/TR/selectors4/#lang-pseudo){.css link-type="maybe"} pseudo-class, [WebVTT Internal Node Objects](#webvtt-internal-node-object){#ref-for-webvtt-internal-node-object-21 link-type="dfn"} have the language described as the [WebVTT Node Object's applicable language](#webvtt-node-objects-applicable-language){#ref-for-webvtt-node-objects-applicable-language-13 link-type="dfn"}.

-   For the purposes of ID selector matching, [lists of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-31 link-type="dfn"} have the ID given by the cue's [text track cue identifier](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-identifier){link-type="dfn"}, if any.

The following properties apply to the [::cue()]{.css} pseudo-element with an argument:

-   [color](https://www.w3.org/TR/css-color-4/#propdef-color){.property link-type="propdesc"}
-   [opacity](https://www.w3.org/TR/css-color-4/#propdef-opacity){.property link-type="propdesc"}
-   [visibility](https://www.w3.org/TR/CSS22/visufx.html#propdef-visibility){.property link-type="propdesc"}
-   the properties corresponding to the [text-decoration](https://www.w3.org/TR/css-text-decor-3/#text-decoration-property){.property link-type="propdesc"} shorthand
-   [text-shadow](https://www.w3.org/TR/css-text-decor-3/#text-shadow-property){.property link-type="propdesc"}
-   the properties corresponding to the [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand
-   the properties corresponding to the [outline](https://drafts.csswg.org/css-ui-4/#propdef-outline){.property link-type="propdesc"} shorthand
-   properties relating to the transition and animation features

In addition, the following properties apply to the [::cue()]{.css} pseudo-element with an argument when the selector does not contain the [:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes:

-   the properties corresponding to the [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand, including [line-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-line-height){.property link-type="propdesc"}
-   [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space){.property link-type="propdesc"}
-   [text-combine-upright](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-combine-upright){.property link-type="propdesc"}
-   [ruby-position](https://www.w3.org/TR/css-ruby-1/#propdef-ruby-position){.property link-type="propdesc"}

Properties that do not apply must be ignored.

As a special exception, the properties corresponding to the [background](https://www.w3.org/TR/css3-background/#propdef-background){.property link-type="propdesc"} shorthand, when they would have been applied to the [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-32 link-type="dfn"}, must instead be applied to the [WebVTT cue background box](#webvtt-cue-background-box){#ref-for-webvtt-cue-background-box-3 link-type="dfn"}.

#### [8.2.2. ]{.secno}[The [:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes]{.content}[](#the-past-and-future-pseudo-classes){.self-link} {#the-past-and-future-pseudo-classes .heading .settled level="8.2.2"}

The [:past](https://www.w3.org/TR/selectors4/#past-pseudo){.css link-type="maybe"} and [:future](https://www.w3.org/TR/selectors4/#future-pseudo){.css link-type="maybe"} pseudo-classes sometimes match [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-16 link-type="dfn"}. [\[SELECTORS4\]](#biblio-selectors4){link-type="biblio"}

The [:past[](#past){.self-link}]{#past .dfn dfn-type="dfn" noexport=""} pseudo-class only matches [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-17 link-type="dfn"} that are *in the past*.

A [WebVTT Node Object](#webvtt-node-object){#ref-for-webvtt-node-object-18 link-type="dfn"} `c`{.variable} is [in the past[](#in-the-past){.self-link}]{#in-the-past .dfn dfn-type="dfn" noexport=""} if, in a pre-order, depth-first traversal of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-33 link-type="dfn"}'s [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-33 link-type="dfn"}, there exists a [WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-6 link-type="dfn"} whose value is less than the [current playback position](https://www.w3.org/TR/html51/semantics-embedded-content.html#current-position){link-type="dfn"} of the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} that is the *matched element*, entirely after the [WebVTT Node Object](#webvtt-node-object){#ref-for-webvtt-node-object-19 link-type="dfn"} `c`{.variable}.

The [:future[](#future){.self-link}]{#future .dfn dfn-type="dfn" noexport=""} pseudo-class only matches [WebVTT Node Objects](#webvtt-node-object){#ref-for-webvtt-node-object-20 link-type="dfn"} that are *in the future*.

A [WebVTT Node Object](#webvtt-node-object){#ref-for-webvtt-node-object-21 link-type="dfn"} `c`{.variable} is [in the future[](#in-the-future){.self-link}]{#in-the-future .dfn dfn-type="dfn" noexport=""} if, in a pre-order, depth-first traversal of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-34 link-type="dfn"}'s [list of WebVTT Node Objects](#list-of-webvtt-node-objects){#ref-for-list-of-webvtt-node-objects-34 link-type="dfn"}, there exists a [WebVTT Timestamp Object](#webvtt-timestamp-object){#ref-for-webvtt-timestamp-object-7 link-type="dfn"} whose value is greater than the [current playback position](https://www.w3.org/TR/html51/semantics-embedded-content.html#current-position){link-type="dfn"} of the [media element](https://www.w3.org/TR/html51/semantics-embedded-content.html#media-element){link-type="dfn"} that is the *matched element*, entirely before the [WebVTT Node Object](#webvtt-node-object){#ref-for-webvtt-node-object-22 link-type="dfn"} `c`{.variable}.

#### [8.2.3. ]{.secno}[The [::cue-region]{.css} pseudo-element]{.content}[](#the-cue-region-pseudo-element){.self-link} {#the-cue-region-pseudo-element .heading .settled level="8.2.3"}

Pseudo-elements apply to elements that are matched by selectors. For the purpose of this section, that element is the matched element. The pseudo-element defined below affects the styling of text track regions that are being rendered for the matched element.

If the matched element is not a video element, the pseudo-element defined below won't have any effect according to this specification.

The [::cue-region[](#cue-region){.self-link}]{#cue-region .dfn dfn-type="dfn" noexport=""} pseudo-element (with no argument) matches any list of [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-12 link-type="dfn"} constructed for the *matched element*.

The [::cue-region(selector)[](#cue-region-selector){.self-link}]{#cue-region-selector .dfn dfn-type="dfn" noexport=""} pseudo-element with an argument must have an argument that consists of a CSS selector [\[SELECTORS4\]](#biblio-selectors4){link-type="biblio"}. It matches any list of [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-13 link-type="dfn"} constructed for the *matched element* that also matches the given CSS selector as follows:

-   Any region (list of [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-14 link-type="dfn"}) with a [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-6 link-type="dfn"} matching the given ID.

No other selector matching is defined for [::cue-region(`selector`{.variable})]{.css}.

The same properties that apply to [::cue]{.css} apply to the [::cue-region]{.css} pseudo-element; other properties set on the pseudo-element must be ignored.

When a user agent is rendering one or more text track regions according to the [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks){#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-9 link-type="dfn"}, [WebVTT region objects](#webvtt-region-object){#ref-for-webvtt-region-object-15 link-type="dfn"} used in the rendering can be matched by the above pseudo-element. User agents that support the pseudo-element must dynamically update renderings accordingly. When either [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space){.property link-type="propdesc"} or one of the properties corresponding to the [font](https://www.w3.org/TR/css-fonts-3/#propdef-font){.property link-type="propdesc"} shorthand (including [line-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-line-height){.property link-type="propdesc"}) changes value, then the [text track cue display state](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-display-state){link-type="dfn"} of all the [WebVTT cues](#webvtt-cue){#ref-for-webvtt-cue-35 link-type="dfn"} in the region must be emptied and the [text track](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-tracks){link-type="dfn"}'s [rules for updating the text track rendering](https://www.w3.org/TR/html51/semantics-embedded-content.html#rules-for-updating-the-text-track-rendering){link-type="dfn"} must be immediately rerun.

## [9. ]{.secno}[API]{.content}[](#api){.self-link} {#api .heading .settled level="9"}

### [9.1. ]{.secno}[The [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-2 link-type="idl"} interface]{.content}[](#the-vttcue-interface){.self-link} {#the-vttcue-interface .heading .settled .algorithm algorithm="The VTTCue interface" level="9.1"}

The following interface is used to expose WebVTT cues in the DOM API:

``` {.idl .highlight .def}
enum AutoKeyword { "auto" };
typedef (double or AutoKeyword) LineAndPositionSetting;
enum DirectionSetting { "" /* horizontal */, "rl", "lr" };
enum LineAlignSetting { "start", "center", "end" };
enum PositionAlignSetting { "line-left", "center", "line-right", "auto" };
enum AlignSetting { "start", "center", "end", "left", "right" };
[Exposed=Window,
 Constructor(double startTime, double endTime, DOMString text)]
interface VTTCue : TextTrackCue {
  attribute VTTRegion? region;
  attribute DirectionSetting vertical;
  attribute boolean snapToLines;
  attribute LineAndPositionSetting line;
  attribute LineAlignSetting lineAlign;
  attribute LineAndPositionSetting position;
  attribute PositionAlignSetting positionAlign;
  attribute double size;
  attribute AlignSetting align;
  attribute DOMString text;
  DocumentFragment getCueAsHTML();
};
```

`cue`{.variable} = new [VTTCue](#dom-vttcue-vttcue){#ref-for-dom-vttcue-vttcue-2 .idl-code link-type="constructor"}( `startTime`{.variable}, `endTime`{.variable}, `text`{.variable} )

:   Returns a new [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-3 link-type="idl"} object, for use with the [`addCue()`{.idl}](https://www.w3.org/TR/html51/semantics-embedded-content.html#dom-texttrack-addcue){link-type="idl"} method.

    The `startTime`{.variable} argument sets the [text track cue start time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-start-time){link-type="dfn"}.

    The `endTime`{.variable} argument sets the [text track cue end time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-end-time){link-type="dfn"}.

    The `text`{.variable} argument sets the [cue text](#cue-text){#ref-for-cue-text-14 link-type="dfn"}.

`cue`{.variable} . [`region`{.idl}](#dom-vttcue-region){#ref-for-dom-vttcue-region-2 link-type="idl"}

:   Returns the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-2 link-type="idl"} object to which this cue belongs, if any, or null otherwise.

    Can be set.

`cue`{.variable} . [`vertical`{.idl}](#dom-vttcue-vertical){#ref-for-dom-vttcue-vertical-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns a string representing the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-34 link-type="dfn"}, as follows:

    If it is [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-22 link-type="dfn"}

    :   The empty string.

    If it is [vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-12 link-type="dfn"}

    :   The string \"`rl`\".

    If it is [vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-12 link-type="dfn"}

    :   The string \"`lr`\".

    Can be set.

`cue`{.variable} . [`snapToLines`{.idl}](#dom-vttcue-snaptolines){#ref-for-dom-vttcue-snaptolines-3 link-type="idl"} \[ = `value`{.variable} \]

:   Returns true if the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-14 link-type="dfn"} is true, false otherwise.

    Can be set.

`cue`{.variable} . [`line`{.idl}](#dom-vttcue-line){#ref-for-dom-vttcue-line-3 link-type="idl"} \[ = `value`{.variable} \]

:   Returns the [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-24 link-type="dfn"}. In the case of the value being [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-6 link-type="dfn"}, the string \"`auto`\" is returned.

    Can be set.

`cue`{.variable} . [`lineAlign`{.idl}](#dom-vttcue-linealign){#ref-for-dom-vttcue-linealign-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns a string representing the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-14 link-type="dfn"}, as follows:

    If it is [start alignment](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-6 link-type="dfn"}

    :   The string \"`start`\".

    If it is [center alignment](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-5 link-type="dfn"}

    :   The string \"`center`\".

    If it is [end alignment](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-5 link-type="dfn"}

    :   The string \"`end`\".

    Can be set.

`cue`{.variable} . [`position`{.idl}](#dom-vttcue-position){#ref-for-dom-vttcue-position-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns the [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-23 link-type="dfn"}. In the case of the value being [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-8 link-type="dfn"}, the string \"`auto`\" is returned.

    Can be set.

`cue`{.variable} . [`positionAlign`{.idl}](#dom-vttcue-positionalign){#ref-for-dom-vttcue-positionalign-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns a string representing the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-11 link-type="dfn"}, as follows:

    If it is [line-left alignment](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-10 link-type="dfn"}

    :   The string \"`line-left`\".

    If it is [center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-8 link-type="dfn"}

    :   The string \"`center`\".

    If it is [line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-10 link-type="dfn"}

    :   The string \"`line-right`\".

    If it is [automatic alignment](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-4 link-type="dfn"}

    :   The string \"`auto`\".

    Can be set.

`cue`{.variable} . [`size`{.idl}](#dom-vttcue-size){#ref-for-dom-vttcue-size-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns the [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-12 link-type="dfn"}.

    Can be set.

`cue`{.variable} . [`align`{.idl}](#dom-vttcue-align){#ref-for-dom-vttcue-align-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns a string representing the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-23 link-type="dfn"}, as follows:

    If it is [start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-9 link-type="dfn"}

    :   The string \"`start`\".

    If it is [center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-8 link-type="dfn"}

    :   The string \"`center`\".

    If it is [end alignment](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-8 link-type="dfn"}

    :   The string \"`end`\".

    If it is [left alignment](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-7 link-type="dfn"}

    :   The string \"`left`\".

    If it is [right alignment](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-7 link-type="dfn"}

    :   The string \"`right`\".

    Can be set.

`cue`{.variable} . [`text`{.idl}](#dom-vttcue-text){#ref-for-dom-vttcue-text-2 link-type="idl"} \[ = `value`{.variable} \]

:   Returns the [cue text](#cue-text){#ref-for-cue-text-15 link-type="dfn"} in raw unparsed form.

    Can be set.

`fragment`{.variable} = `cue`{.variable} . [getCueAsHTML](#dom-vttcue-getcueashtml){#ref-for-dom-vttcue-getcueashtml-3 .idl-code link-type="method"}()

:   Returns the [cue text](#cue-text){#ref-for-cue-text-16 link-type="dfn"} as a [`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"} of [HTML elements](https://www.w3.org/TR/html51/infrastructure.html#html-element){link-type="dfn"} and other DOM nodes.

The [`VTTCue(``startTime`{.variable}`, ``endTime`{.variable}`, ``text`{.variable}`)`]{#dom-vttcue-vttcue .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="constructor" export="" lt="VTTCue(startTime, endTime, text)"} constructor, when invoked, must run the following steps:

1.  Create a new [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-36 link-type="dfn"}. Let `cue`{.variable} be that [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-37 link-type="dfn"}.

2.  Let `cue`{.variable}'s [text track cue start time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-start-time){link-type="dfn"} be the value of the `startTime`{.variable} argument, interpreted as a time in seconds.

3.  Let `cue`{.variable}'s [text track cue end time](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-end-time){link-type="dfn"} be the value of the `endTime`{.variable} argument, interpreted as a time in seconds.

4.  Let `cue`{.variable}'s [cue text](#cue-text){#ref-for-cue-text-17 link-type="dfn"} be the value of the `text`{.variable} argument, and let the [rules for extracting the chapter title](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-rules-for-extracting-the-chapter-title){link-type="dfn"} be the [WebVTT rules for extracting the chapter title](#webvtt-rules-for-extracting-the-chapter-title){#ref-for-webvtt-rules-for-extracting-the-chapter-title-1 link-type="dfn"}.

5.  Let `cue`{.variable}'s [text track cue identifier](https://www.w3.org/TR/html51/semantics-embedded-content.html#text-track-cue-identifier){link-type="dfn"} be the empty string.

6.  Let `cue`{.variable}'s [text track cue pause-on-exit flag](https://www.w3.org/TR/html51/semantics-embedded-content.html#pause-on-exit-flag){link-type="dfn"} be false.

7.  Let `cue`{.variable}'s [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-10 link-type="dfn"} be null.

8.  Let `cue`{.variable}'s [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-35 link-type="dfn"} be [horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-23 link-type="dfn"}.

9.  Let `cue`{.variable}'s [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-15 link-type="dfn"} be true.

10. Let `cue`{.variable}'s [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-25 link-type="dfn"} be [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-7 link-type="dfn"}.

11. Let `cue`{.variable}'s [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-15 link-type="dfn"} be [start alignment](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-7 link-type="dfn"}.

12. Let `cue`{.variable}'s [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-24 link-type="dfn"} be [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-9 link-type="dfn"}.

13. Let `cue`{.variable}'s [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-12 link-type="dfn"} be [auto](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-5 link-type="dfn"}.

14. Let `cue`{.variable}'s [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-13 link-type="dfn"} be 100.

15. Let `cue`{.variable}'s [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-24 link-type="dfn"} be [center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-9 link-type="dfn"}.

16. Return the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-4 link-type="idl"} object representing `cue`{.variable}.

The [`region`]{#dom-vttcue-region .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-3 link-type="idl"} object representing the [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-11 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-38 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-5 link-type="idl"} object represents, if any; or null otherwise. On setting, the [WebVTT cue region](#webvtt-cue-region){#ref-for-webvtt-cue-region-12 link-type="dfn"} must be set to the new value.

The [`vertical`]{#dom-vttcue-vertical .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the string from the second cell of the row in the table below whose first cell is the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-36 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-39 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-6 link-type="idl"} object represents:

[WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-37 link-type="dfn"}

[`vertical`{.idl}](#dom-vttcue-vertical){#ref-for-dom-vttcue-vertical-3 link-type="idl"} value

[Horizontal](#webvtt-cue-horizontal-writing-direction){#ref-for-webvtt-cue-horizontal-writing-direction-24 link-type="dfn"}

\"\" (the empty string)

[Vertical growing left](#webvtt-cue-vertical-growing-left-writing-direction){#ref-for-webvtt-cue-vertical-growing-left-writing-direction-13 link-type="dfn"}

\"`rl`\"

[Vertical growing right](#webvtt-cue-vertical-growing-right-writing-direction){#ref-for-webvtt-cue-vertical-growing-right-writing-direction-13 link-type="dfn"}

\"`lr`\"

On setting, the [WebVTT cue writing direction](#webvtt-cue-writing-direction){#ref-for-webvtt-cue-writing-direction-38 link-type="dfn"} must be set to the value given in the first cell of the row in the table above whose second cell is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the new value.

The [`snapToLines`]{#dom-vttcue-snaptolines .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return true if the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-16 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-40 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-7 link-type="idl"} object represents is true; or false otherwise. On setting, the [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag){#ref-for-webvtt-cue-snap-to-lines-flag-17 link-type="dfn"} must be set to the new value.

The [`line`]{#dom-vttcue-line .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-26 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-41 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-8 link-type="idl"} object represents. The special value [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-8 link-type="dfn"} must be represented as the string \"`auto`\". On setting, the [WebVTT cue line](#webvtt-cue-line){#ref-for-webvtt-cue-line-27 link-type="dfn"} must be set to the new value; if the new value is the string \"`auto`\", then it must be interpreted as the special value [auto](#webvtt-cue-line-automatic){#ref-for-webvtt-cue-line-automatic-9 link-type="dfn"}.

In order to be able to set the [`snapToLines`{.idl}](#dom-vttcue-snaptolines){#ref-for-dom-vttcue-snaptolines-4 link-type="idl"} and [`line`{.idl}](#dom-vttcue-line){#ref-for-dom-vttcue-line-4 link-type="idl"} attributes in any order, the API does not reject setting [`snapToLines`{.idl}](#dom-vttcue-snaptolines){#ref-for-dom-vttcue-snaptolines-5 link-type="idl"} to false when [`line`{.idl}](#dom-vttcue-line){#ref-for-dom-vttcue-line-5 link-type="idl"} has a value outside the range 0..100, or vice versa.

The [`lineAlign`]{#dom-vttcue-linealign .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the string from the second cell of the row in the table below whose first cell is the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-16 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-42 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-9 link-type="idl"} object represents:

[WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-17 link-type="dfn"}

[`lineAlign`{.idl}](#dom-vttcue-linealign){#ref-for-dom-vttcue-linealign-3 link-type="idl"} value

[Start alignment](#webvtt-cue-line-start-alignment){#ref-for-webvtt-cue-line-start-alignment-8 link-type="dfn"}

\"`start`\"

[Center alignment](#webvtt-cue-line-center-alignment){#ref-for-webvtt-cue-line-center-alignment-6 link-type="dfn"}

\"`center`\"

[End alignment](#webvtt-cue-line-end-alignment){#ref-for-webvtt-cue-line-end-alignment-6 link-type="dfn"}

\"`end`\"

On setting, the [WebVTT cue line alignment](#webvtt-cue-line-alignment){#ref-for-webvtt-cue-line-alignment-18 link-type="dfn"} must be set to the value given in the first cell of the row in the table above whose second cell is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the new value.

The [`position`]{#dom-vttcue-position .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-25 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-43 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-10 link-type="idl"} object represents. The special value [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-10 link-type="dfn"} must be represented as the string \"`auto`\". On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT cue position](#webvtt-cue-position){#ref-for-webvtt-cue-position-26 link-type="dfn"} must be set to the new value; if the new value is the string \"`auto`\", then it must be interpreted as the special value [auto](#webvtt-cue-automatic-position){#ref-for-webvtt-cue-automatic-position-11 link-type="dfn"}.

The [`positionAlign`]{#dom-vttcue-positionalign .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the string from the second cell of the row in the table below whose first cell is the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-13 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-44 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-11 link-type="idl"} object represents:

[WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-14 link-type="dfn"}

[`positionAlign`{.idl}](#dom-vttcue-positionalign){#ref-for-dom-vttcue-positionalign-3 link-type="idl"} value

[Line-left alignment](#webvtt-cue-position-line-left-alignment){#ref-for-webvtt-cue-position-line-left-alignment-11 link-type="dfn"}

\"`line-left`\"

[Center alignment](#webvtt-cue-position-center-alignment){#ref-for-webvtt-cue-position-center-alignment-9 link-type="dfn"}

\"`center`\"

[Line-right alignment](#webvtt-cue-position-line-right-alignment){#ref-for-webvtt-cue-position-line-right-alignment-11 link-type="dfn"}

\"`line-right`\"

[Automatic alignment](#webvtt-cue-position-automatic-alignment){#ref-for-webvtt-cue-position-automatic-alignment-6 link-type="dfn"}

\"`auto`\"

On setting, the [WebVTT cue position alignment](#webvtt-cue-position-alignment){#ref-for-webvtt-cue-position-alignment-15 link-type="dfn"} must be set to the value given in the first cell of the row in the table above whose second cell is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the new value.

The [`size`]{#dom-vttcue-size .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-14 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-45 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-12 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT cue size](#webvtt-cue-size){#ref-for-webvtt-cue-size-15 link-type="dfn"} must be set to the new value.

The [`align`]{#dom-vttcue-align .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the string from the second cell of the row in the table below whose first cell is the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-25 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-46 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-13 link-type="idl"} object represents:

[WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-26 link-type="dfn"}

[`align`{.idl}](#dom-vttcue-align){#ref-for-dom-vttcue-align-3 link-type="idl"} value

[Start alignment](#webvtt-cue-start-alignment){#ref-for-webvtt-cue-start-alignment-10 link-type="dfn"}

\"`start`\"

[Center alignment](#webvtt-cue-center-alignment){#ref-for-webvtt-cue-center-alignment-10 link-type="dfn"}

\"`center`\"

[End alignment](#webvtt-cue-end-alignment){#ref-for-webvtt-cue-end-alignment-9 link-type="dfn"}

\"`end`\"

[Left alignment](#webvtt-cue-left-alignment){#ref-for-webvtt-cue-left-alignment-8 link-type="dfn"}

\"`left`\"

[Right alignment](#webvtt-cue-right-alignment){#ref-for-webvtt-cue-right-alignment-8 link-type="dfn"}

\"`right`\"

On setting, the [WebVTT cue text alignment](#webvtt-cue-text-alignment){#ref-for-webvtt-cue-text-alignment-27 link-type="dfn"} must be set to the value given in the first cell of the row in the table above whose second cell is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the new value.

The [`text`]{#dom-vttcue-text .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="attribute" export=""} attribute, on getting, must return the raw [cue text](#cue-text){#ref-for-cue-text-18 link-type="dfn"} of the [WebVTT cue](#webvtt-cue){#ref-for-webvtt-cue-47 link-type="dfn"} that the [`VTTCue`{.idl}](#vttcue){#ref-for-vttcue-14 link-type="idl"} object represents. On setting, the [cue text](#cue-text){#ref-for-cue-text-19 link-type="dfn"} must be set to the new value.

The [`getCueAsHTML()`]{#dom-vttcue-getcueashtml .dfn .dfn-paneled .idl-code dfn-for="VTTCue" dfn-type="method" export=""} method must convert the [cue text](#cue-text){#ref-for-cue-text-20 link-type="dfn"} to a [`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"} for the [responsible document](https://www.w3.org/TR/html51/webappapis.html#responsible-document){link-type="dfn"} specified by the [entry settings object](https://www.w3.org/TR/html51/webappapis.html#entry-settings-object){link-type="dfn"} by applying the [WebVTT cue text DOM construction rules](#webvtt-cue-text-dom-construction-rules){#ref-for-webvtt-cue-text-dom-construction-rules-1 link-type="dfn"} to the result of applying the [WebVTT cue text parsing rules](#webvtt-cue-text-parsing-rules){#ref-for-webvtt-cue-text-parsing-rules-3 link-type="dfn"} to the [cue text](#cue-text){#ref-for-cue-text-21 link-type="dfn"}.

A fallback language is not provided for [`getCueAsHTML()`{.idl}](#dom-vttcue-getcueashtml){#ref-for-dom-vttcue-getcueashtml-4 link-type="idl"} since a [`DocumentFragment`{.idl}](https://www.w3.org/TR/dom/#documentfragment){link-type="idl"} cannot expose language information.

### [9.2. ]{.secno}[The [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-4 link-type="idl"} interface]{.content}[](#the-vttregion-interface){.self-link} {#the-vttregion-interface .heading .settled .algorithm algorithm="The VTTRegion interface" level="9.2"}

The following interface is used to expose WebVTT regions in the DOM API:

``` {.idl .highlight .def}
enum ScrollSetting { "" /* none */, "up" };
[Exposed=Window,
 Constructor]
interface VTTRegion {
  attribute DOMString id;
  attribute double width;
  attribute unsigned long lines;
  attribute double regionAnchorX;
  attribute double regionAnchorY;
  attribute double viewportAnchorX;
  attribute double viewportAnchorY;
  attribute ScrollSetting scroll;
};
```

`region`{.variable} = new [VTTRegion](#dom-vttregion-vttregion){#ref-for-dom-vttregion-vttregion-2 .idl-code link-type="constructor"}()

:   Returns a new [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-5 link-type="idl"} object.

`region`{.variable} . [`id`{.idl}](#dom-vttregion-id){#ref-for-dom-vttregion-id-2 link-type="idl"}

:   Returns the text track region identifier. Can be set.

`region`{.variable} . [`width`{.idl}](#dom-vttregion-width){#ref-for-dom-vttregion-width-2 link-type="idl"}

:   Returns the WebVTT region width as a percentage of the video width. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is not in the range 0..100.

`region`{.variable} . [`lines`{.idl}](#dom-vttregion-lines){#ref-for-dom-vttregion-lines-2 link-type="idl"}

:   Returns the text track region height as a number of lines. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is negative.

`region`{.variable} . [`regionAnchorX`{.idl}](#dom-vttregion-regionanchorx){#ref-for-dom-vttregion-regionanchorx-2 link-type="idl"}

:   Returns the WebVTT region anchor X offset as a percentage of the region width. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is not in the range 0..100.

`region`{.variable} . [`regionAnchorY`{.idl}](#dom-vttregion-regionanchory){#ref-for-dom-vttregion-regionanchory-2 link-type="idl"}

:   Returns the WebVTT region anchor Y offset as a percentage of the region height. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is not in the range 0..100.

`region`{.variable} . [`viewportAnchorX`{.idl}](#dom-vttregion-viewportanchorx){#ref-for-dom-vttregion-viewportanchorx-2 link-type="idl"}

:   Returns the WebVTT region viewport anchor X offset as a percentage of the video width. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is not in the range 0..100.

`region`{.variable} . [`viewportAnchorY`{.idl}](#dom-vttregion-viewportanchory){#ref-for-dom-vttregion-viewportanchory-2 link-type="idl"}

:   Returns the WebVTT region viewport anchor Y offset as a percentage of the video height. Can be set. Throws an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} if the new value is not in the range 0..100.

`region`{.variable} . [`scroll`{.idl}](#dom-vttregion-scroll){#ref-for-dom-vttregion-scroll-2 link-type="idl"}

:   Returns a string representing the [WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-4 link-type="dfn"} as follows:

    If it is unset

    :   The empty string.

    If it is up

    :   The string \"`up`\".

    Can be set.

The [`VTTRegion()`]{#dom-vttregion-vttregion .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="constructor" export=""} constructor, when invoked, must run the following steps:

1.  Create a new [WebVTT region](#webvtt-region){#ref-for-webvtt-region-16 link-type="dfn"}. Let `region`{.variable} be that [WebVTT region](#webvtt-region){#ref-for-webvtt-region-17 link-type="dfn"}.

2.  Let `region`{.variable}'s [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-7 link-type="dfn"} be the empty string.

3.  Let `region`{.variable}'s [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-7 link-type="dfn"} be 100.

4.  Let `region`{.variable}'s [WebVTT region lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-4 link-type="dfn"} be 3.

5.  Let `region`{.variable}'s [text track region regionAnchorX](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-7 link-type="dfn"} be 0.

6.  Let `region`{.variable}'s [text track region regionAnchorY](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-8 link-type="dfn"} be 100.

7.  Let `region`{.variable}'s [text track region viewportAnchorX](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-3 link-type="dfn"} be 0.

8.  Let `region`{.variable}'s [text track region viewportAnchorY](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-4 link-type="dfn"} be 100.

9.  Let `region`{.variable}'s [WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-5 link-type="dfn"} be the empty string.

10. Return the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-6 link-type="idl"} object representing `region`{.variable}.

The [`id`]{#dom-vttregion-id .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-8 link-type="dfn"} of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-18 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-7 link-type="idl"} object represents. On setting, the [WebVTT region identifier](#webvtt-region-identifier){#ref-for-webvtt-region-identifier-9 link-type="dfn"} must be set to the new value.

The [`width`]{#dom-vttregion-width .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-8 link-type="dfn"} of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-19 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-8 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT region width](#webvtt-region-width){#ref-for-webvtt-region-width-9 link-type="dfn"} must be set to the new value.

The [`lines`]{#dom-vttregion-lines .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-5 link-type="dfn"} of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-20 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-9 link-type="idl"} object represents. On setting, the [WebVTT region lines](#webvtt-region-lines){#ref-for-webvtt-region-lines-6 link-type="dfn"} must be set to the new value.

The [`regionAnchorX`]{#dom-vttregion-regionanchorx .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-9 link-type="dfn"} X offset of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-21 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-10 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-10 link-type="dfn"} X distance must be set to the new value.

The [`regionAnchorY`]{#dom-vttregion-regionanchory .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-11 link-type="dfn"} Y offset of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-22 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-11 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT region anchor](#webvtt-region-anchor){#ref-for-webvtt-region-anchor-12 link-type="dfn"} Y distance must be set to the new value.

The [`viewportAnchorX`]{#dom-vttregion-viewportanchorx .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region viewport anchor](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-5 link-type="dfn"} X offset of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-23 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-12 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT region viewport anchor](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-6 link-type="dfn"} X distance must be set to the new value.

The [`viewportAnchorY`]{#dom-vttregion-viewportanchory .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the [WebVTT region viewport anchor](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-7 link-type="dfn"} Y offset of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-24 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-13 link-type="idl"} object represents. On setting, if the new value is negative or greater than 100, then an [`IndexSizeError`{.idl}](https://www.w3.org/TR/WebIDL-1/#indexsizeerror){link-type="idl"} exception must be thrown. Otherwise, the [WebVTT region viewport anchor](#webvtt-region-viewport-anchor){#ref-for-webvtt-region-viewport-anchor-8 link-type="dfn"} Y distance must be set to the new value.

The [`scroll`]{#dom-vttregion-scroll .dfn .dfn-paneled .idl-code dfn-for="VTTRegion" dfn-type="attribute" export=""} attribute, on getting, must return the string from the second cell of the row in the table below whose first cell is the [WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-6 link-type="dfn"} setting of the [WebVTT region](#webvtt-region){#ref-for-webvtt-region-25 link-type="dfn"} that the [`VTTRegion`{.idl}](#vttregion){#ref-for-vttregion-14 link-type="idl"} object represents:

[WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-7 link-type="dfn"}

[`scroll`{.idl}](#dom-vttregion-scroll){#ref-for-dom-vttregion-scroll-3 link-type="idl"} value

[None](#webvtt-region-scroll-none){#ref-for-webvtt-region-scroll-none-2 link-type="dfn"}

\"\" (the empty string)

[Up](#webvtt-region-scroll-up){#ref-for-webvtt-region-scroll-up-3 link-type="dfn"}

\"`up`\"

On setting, the [WebVTT region scroll](#webvtt-region-scroll){#ref-for-webvtt-region-scroll-8 link-type="dfn"} must be set to the value given on the first cell of the row in the table above whose second cell is a [case-sensitive](https://www.w3.org/TR/html51/infrastructure.html#case-sensitive){link-type="dfn"} match for the new value.

## [10. ]{.secno}[IANA considerations]{.content}[](#iana){.self-link} {#iana .heading .settled level="10"}

### [10.1. ]{.secno}[[`text/vtt`]{#text-vtt .dfn .dfn-paneled dfn-type="dfn" noexport=""}]{.content}[](#iana-text-vtt){.self-link} {#iana-text-vtt .heading .settled level="10.1"}

This registration is for community review and will be submitted to the IESG for review, approval, and registration with IANA.

Type name:
:   text

Subtype name:
:   vtt

Required parameters:
:   No parameters

Optional parameters:
:   No parameters

Encoding considerations:
:   8bit (always UTF-8)

Security considerations:

:   Text track files themselves pose no immediate risk unless sensitive information is included within the data. Implementations, however, are required to follow specific rules when processing text tracks, to ensure that certain origin-based restrictions are honored. Failure to correctly implement these rules can result in information leakage, cross-site scripting attacks, and the like.

Interoperability considerations:

:   Rules for processing both conforming and non-conforming content are defined in this specification.

Published specification:
:   This document is the relevant specification.

Applications that use this media type:
:   Web browsers and other video players.

Additional information:

:

    Magic number(s):

    :   WebVTT files all begin with one of the following byte sequences (where \"EOF\" means the end of the file):

        -   EF BB BF 57 45 42 56 54 54 0A
        -   EF BB BF 57 45 42 56 54 54 0D
        -   EF BB BF 57 45 42 56 54 54 20
        -   EF BB BF 57 45 42 56 54 54 09
        -   EF BB BF 57 45 42 56 54 54 EOF
        -   57 45 42 56 54 54 0A
        -   57 45 42 56 54 54 0D
        -   57 45 42 56 54 54 20
        -   57 45 42 56 54 54 09
        -   57 45 42 56 54 54 EOF

        (An optional UTF-8 BOM, the ASCII string \"`WEBVTT`\", and finally a space, tab, line break, or the end of the file.)

    File extension(s):
    :   \"`vtt`\"

    Macintosh file type code(s):
    :   No specific Macintosh file type codes are recommended for this type.

Person & email address to contact for further information:
:   Silvia Pfeiffer \<silviapfeiffer1@gmail.com\>

Intended usage:
:   Common

Restrictions on usage:
:   No restrictions apply.

Authors:
:   Silvia Pfeiffer \<silviapfeiffer1@gmail.com\>, Simon Pieters \<simonp@opera.com\>, Philip Jägenstedt \<philipj@opera.com\>, Ian Hickson \<ian@hixie.ch\>

Change controller:
:   W3C

Fragment identifiers have no meaning with `text/vtt` resources.

## [Privacy and Security Considerations]{.content}[](#privacy-and-security-considerations){.self-link} {#privacy-and-security-considerations .no-num .heading .settled}

### [Text-based format security]{.content}[](#fromat-security){.self-link} {#fromat-security .heading .settled}

As with any text-based format, it is possible to construct malicious content that might cause buffer over-runs, value overflows (e.g. string representations of integers that overflow a given word length), and the like. Implementers should take care in implementing a parser that over-long lines, field values, or encoded values do not cause security problems.

### [Styling-related privacy and security]{.content}[](#styling-security){.self-link} {#styling-security .heading .settled}

WebVTT can embed CSS style sheets, which will be applied in user agents that support CSS. Under these circumstances, the privacy and security considerations of CSS apply, with the following caveats.

Such style sheets [cannot fetch any external resources](#style-no-external-resources), and it is important for privacy that user agents do not allow this. Otherwise, WebVTT files could be authored such that a third party is notified when the user watches a particular video, and even the current time in that video.

It is possible for a user agent to offer user style sheets, but their presence and nature will not be detectable by scripts running in the same user agent (e.g. browser) since the CSS object model for such style sheets is not exposed to script and there is no way to get the computed style for pseudo-elements other than [::before](https://www.w3.org/TR/css3-selectors/#sel-before){.css link-type="maybe"} and [::after](https://www.w3.org/TR/css3-selectors/#sel-after){.css link-type="maybe"} with the [`getComputedStyle()`{.idl}](https://www.w3.org/TR/cssom-1/#dom-window-getcomputedstyle){link-type="idl"} API. [\[CSSOM\]](#biblio-cssom){link-type="biblio"}

### [Scripting-related security]{.content}[](#scripting-security){.self-link} {#scripting-security .heading .settled}

WebVTT does not include or enable scripting. It is important that user agents do not support a way to execute script embedded in a WebVTT file.

However, it is possible to construct and deliver a file that is designed not to present captions or subtitles, but instead to provide timed input ('triggers') to a script system. A poorly-written script or script system might then cause security, privacy or other problems; however, this consideration really applies to the script system. Since WebVTT supplies these triggers at their timestamps, a malicious file might present such triggers very rapidly, perhaps causing undue resource consumption.

### [Privacy of preference]{.content}[](#privacy-of-preference){.self-link} {#privacy-of-preference .heading .settled}

A user agent that selects, and causes to download or interpret a WebVTT file, might indicate to the origin server that the user has a need for captions or subtitles, and also the [language preference](https://www.w3.org/TR/html51/semantics-embedded-content.html#honor-user-preferences-for-automatic-text-track-selection){link-type="dfn"} of the user for captions or subtitles. That is a (small) piece of information about the user. However, the offering of a caption file, and the choice whether to retrieve and consume it, are really characteristics of the format or protocol which does the offer (e.g. the HTML element), rather than of the caption format itself. [\[HTML51\]](#biblio-html51){link-type="biblio"}

## [Acknowledgements]{.content}[](#acknowledgements){.self-link} {#acknowledgements .no-num .heading .settled}

Thanks to the SubRip community, including in particular Zuggy and ai4spam, for their work on the SubRip software program whose SRT file format was used as the basis for the WebVTT text track file format.

Thanks to Ian Hickson and many others for their work on the HTML standard, where WebVTT was originally specified. [\[HTML51\]](#biblio-html51){link-type="biblio"}

Thanks to Addison Phillips, Alastor Wu, Andreas Tai, Anna Cavender, Anne van Kesteren, Benjamin Schaaf, Brian Quass, Caitlin Potter, Courtney Kennedy, Cyril Concolato, Dae Kim, David Singer, Eric Carlson, fantasai, Frank Olivier, Fredrik Söderquist, Giuseppe Pascale, Glenn Adams, Glenn Maynard, John Foliot, Kyle Huey, Lawrence Forooghian, Loretta Guarino Reid, Ms2ger, Nigel Megitt, Ralph Giles, Richard Ishida, Rick Eyre, Ronny Mennerich, Theresa O'Connor, and Victor Cărbune for their useful comments.
:::

## [Index]{.content}[](#index){.self-link} {#index .no-num .no-ref .heading .settled}

### [Terms defined by this specification]{.content}[](#index-defined-here){.self-link} {#index-defined-here .no-num .no-ref .heading .settled}

-   \"\"
    -   [enum-value for DirectionSetting](#dom-directionsetting), in §9.1
    -   [enum-value for ScrollSetting](#dom-scrollsetting), in §9.2
-   [align](#dom-vttcue-align), in §9.1
-   [AlignSetting](#enumdef-alignsetting), in §9.1
-   [apply WebVTT cue settings](#apply-webvtt-cue-settings), in §7.2
-   [attach a WebVTT Internal Node Object](#attach-a-webvtt-internal-node-object), in §6.4
-   auto
    -   [enum-value for AutoKeyword](#dom-autokeyword-auto), in §9.1
    -   [enum-value for PositionAlignSetting](#dom-positionalignsetting-auto), in §9.1
-   \"auto\"
    -   [enum-value for AutoKeyword](#dom-autokeyword-auto), in §9.1
    -   [enum-value for PositionAlignSetting](#dom-positionalignsetting-auto), in §9.1
-   [AutoKeyword](#enumdef-autokeyword), in §9.1
-   \"center\"
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-center), in §9.1
    -   [enum-value for PositionAlignSetting](#dom-positionalignsetting-center), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-center), in §9.1
-   center
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-center), in §9.1
    -   [enum-value for PositionAlignSetting](#dom-positionalignsetting-center), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-center), in §9.1
-   [collect a WebVTT block](#collect-a-webvtt-block), in §6.1
-   [collect a WebVTT timestamp](#collect-a-webvtt-timestamp), in §6.3
-   [collect WebVTT cue timings and settings](#collect-webvtt-cue-timings-and-settings), in §6.3
-   [collect WebVTT region settings](#collect-webvtt-region-settings), in §6.2
-   [consume an HTML character reference](#consume-an-html-character-reference), in §6.4
-   [::cue](#cue), in §8.2.1
-   [cue component class names](#cue-component-class-names), in §4.2.2
-   [cue computed line](#cue-computed-line), in §3.3
-   [cue computed position](#cue-computed-position), in §3.3
-   [cue computed position alignment](#cue-computed-position-alignment), in §3.3
-   [cue payload](#cue-payload), in §4.1
-   [::cue-region](#cue-region), in §8.2.3
-   [::cue-region(selector)](#cue-region-selector), in §8.2.3
-   [::cue(selector)](#cue-selector), in §8.2.1
-   [cue text](#cue-text), in §3.2
-   [DirectionSetting](#enumdef-directionsetting), in §9.1
-   \"end\"
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-end), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-end), in §9.1
-   end
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-end), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-end), in §9.1
-   [:future](#future), in §8.2.2
-   [getCueAsHTML()](#dom-vttcue-getcueashtml), in §9.1
-   [HTML character reference in annotation state](#html-character-reference-in-annotation-state), in §6.4
-   [HTML character reference in data state](#html-character-reference-in-data-state), in §6.4
-   [id](#dom-vttregion-id), in §9.2
-   [incremental WebVTT parser](#incremental-webvtt-parser), in §6.1
-   [in the future](#in-the-future), in §8.2.2
-   [in the past](#in-the-past), in §8.2.2
-   [\"left\"](#dom-alignsetting-left), in §9.1
-   [left](#dom-alignsetting-left), in §9.1
-   [line](#dom-vttcue-line), in §9.1
-   [lineAlign](#dom-vttcue-linealign), in §9.1
-   [LineAlignSetting](#enumdef-linealignsetting), in §9.1
-   [LineAndPositionSetting](#typedefdef-lineandpositionsetting), in §9.1
-   [\"line-left\"](#dom-positionalignsetting-line-left), in §9.1
-   [line-left](#dom-positionalignsetting-line-left), in §9.1
-   [line-right](#dom-positionalignsetting-line-right), in §9.1
-   [\"line-right\"](#dom-positionalignsetting-line-right), in §9.1
-   [lines](#dom-vttregion-lines), in §9.2
-   [List of WebVTT Node Objects](#list-of-webvtt-node-objects), in §6.4
-   [lr](#dom-directionsetting-lr), in §9.1
-   [\"lr\"](#dom-directionsetting-lr), in §9.1
-   [obtain a set of CSS boxes](#obtain-a-set-of-css-boxes), in §7.3
-   [parse a percentage string](#parse-a-percentage-string), in §6.2
-   [parse the WebVTT cue settings](#parse-the-webvtt-cue-settings), in §6.3
-   [:past](#past), in §8.2.2
-   [position](#dom-vttcue-position), in §9.1
-   [positionAlign](#dom-vttcue-positionalign), in §9.1
-   [PositionAlignSetting](#enumdef-positionalignsetting), in §9.1
-   [region](#dom-vttcue-region), in §9.1
-   [regionAnchorX](#dom-vttregion-regionanchorx), in §9.2
-   [regionAnchorY](#dom-vttregion-regionanchory), in §9.2
-   [right](#dom-alignsetting-right), in §9.1
-   [\"right\"](#dom-alignsetting-right), in §9.1
-   [rl](#dom-directionsetting-rl), in §9.1
-   [\"rl\"](#dom-directionsetting-rl), in §9.1
-   [rules for updating the display of WebVTT text tracks](#rules-for-updating-the-display-of-webvtt-text-tracks), in §7.1
-   [scroll](#dom-vttregion-scroll), in §9.2
-   [ScrollSetting](#enumdef-scrollsetting), in §9.2
-   [size](#dom-vttcue-size), in §9.1
-   [snapToLines](#dom-vttcue-snaptolines), in §9.1
-   \"start\"
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-start), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-start), in §9.1
-   start
    -   [enum-value for LineAlignSetting](#dom-linealignsetting-start), in §9.1
    -   [enum-value for AlignSetting](#dom-alignsetting-start), in §9.1
-   [text](#dom-vttcue-text), in §9.1
-   [text track list of regions](#text-track-list-of-regions), in §3.4
-   [text/vtt](#text-vtt), in §10.1
-   [up](#dom-scrollsetting-up), in §9.2
-   [\"up\"](#dom-scrollsetting-up), in §9.2
-   [User agents that do not support a full HTML CSS engine](#user-agents-that-do-not-support-a-full-html-css-engine), in §2.1
-   [User agents that do not support CSS](#user-agents-that-do-not-support-css), in §2.1
-   [User agents that support a full HTML CSS engine](#user-agents-that-support-a-full-html-css-engine), in §2.1
-   [vertical](#dom-vttcue-vertical), in §9.1
-   [viewportAnchorX](#dom-vttregion-viewportanchorx), in §9.2
-   [viewportAnchorY](#dom-vttregion-viewportanchory), in §9.2
-   [VTTCue](#vttcue), in §9.1
-   [VTTCue(startTime, endTime, text)](#dom-vttcue-vttcue), in §9.1
-   [VTTRegion()](#dom-vttregion-vttregion), in §9.2
-   [VTTRegion](#vttregion), in §9.2
-   [WebVTT](#webvtt), in §1
-   [WebVTT alignment cue setting](#webvtt-alignment-cue-setting), in §4.4
-   [WebVTT Bold Object](#webvtt-bold-object), in §6.4
-   [WebVTT caption or subtitle cue](#webvtt-caption-or-subtitle-cue), in §3.3
-   [WebVTT caption or subtitle cue components](#webvtt-caption-or-subtitle-cue-components), in §4.2.2
-   [WebVTT caption or subtitle cue text](#webvtt-caption-or-subtitle-cue-text), in §4.2.2
-   [WebVTT chapter cue](#webvtt-chapter-cue), in §3.5
-   [WebVTT chapter title text](#webvtt-chapter-title-text), in §4.2.3
-   [WebVTT Class Object](#webvtt-class-object), in §6.4
-   [WebVTT comment block](#webvtt-comment-block), in §4.1
-   [WebVTT cue](#webvtt-cue), in §3.2
-   [WebVTT cue automatic position](#webvtt-cue-automatic-position), in §3.3
-   [WebVTT cue background box](#webvtt-cue-background-box), in §7.3
-   [WebVTT cue block](#webvtt-cue-block), in §4.1
-   [WebVTT cue bold span](#webvtt-cue-bold-span), in §4.2.2
-   [WebVTT cue box](#webvtt-cue-box), in §3.3
-   [WebVTT cue center alignment](#webvtt-cue-center-alignment), in §3.3
-   [WebVTT cue class span](#webvtt-cue-class-span), in §4.2.2
-   [WebVTT cue end alignment](#webvtt-cue-end-alignment), in §3.3
-   [WebVTT cue horizontal writing direction](#webvtt-cue-horizontal-writing-direction), in §3.3
-   [WebVTT cue identifier](#webvtt-cue-identifier), in §4.1
-   [WebVTT cue internal text](#webvtt-cue-internal-text), in §4.2.2
-   [WebVTT cue italics span](#webvtt-cue-italics-span), in §4.2.2
-   [WebVTT cue language span](#webvtt-cue-language-span), in §4.2.2
-   [WebVTT cue left alignment](#webvtt-cue-left-alignment), in §3.3
-   [WebVTT cue line](#webvtt-cue-line), in §3.3
-   [WebVTT cue line alignment](#webvtt-cue-line-alignment), in §3.3
-   [WebVTT cue line automatic](#webvtt-cue-line-automatic), in §3.3
-   [WebVTT cue line center alignment](#webvtt-cue-line-center-alignment), in §3.3
-   [WebVTT cue line end alignment](#webvtt-cue-line-end-alignment), in §3.3
-   [WebVTT cue line start alignment](#webvtt-cue-line-start-alignment), in §3.3
-   [WebVTT cue position](#webvtt-cue-position), in §3.3
-   [WebVTT cue position alignment](#webvtt-cue-position-alignment), in §3.3
-   [WebVTT cue position automatic alignment](#webvtt-cue-position-automatic-alignment), in §3.3
-   [WebVTT cue position center alignment](#webvtt-cue-position-center-alignment), in §3.3
-   [WebVTT cue position line-left alignment](#webvtt-cue-position-line-left-alignment), in §3.3
-   [WebVTT cue position line-right alignment](#webvtt-cue-position-line-right-alignment), in §3.3
-   [WebVTT cue region](#webvtt-cue-region), in §3.3
-   [WebVTT cue right alignment](#webvtt-cue-right-alignment), in §3.3
-   [WebVTT cue ruby span](#webvtt-cue-ruby-span), in §4.2.2
-   [WebVTT cue ruby text span](#webvtt-cue-ruby-text-span), in §4.2.2
-   [WebVTT cue setting](#webvtt-cue-setting), in §4.1
-   [WebVTT cue setting name](#webvtt-cue-setting-name), in §4.1
-   [WebVTT cue settings list](#webvtt-cue-settings-list), in §4.1
-   [WebVTT cue setting value](#webvtt-cue-setting-value), in §4.1
-   [WebVTT cue size](#webvtt-cue-size), in §3.3
-   [WebVTT cue snap-to-lines flag](#webvtt-cue-snap-to-lines-flag), in §3.3
-   [WebVTT cue span end tag](#webvtt-cue-span-end-tag), in §4.2.2
-   [WebVTT cue span start tag](#webvtt-cue-span-start-tag), in §4.2.2
-   [WebVTT cue span start tag annotation text](#webvtt-cue-span-start-tag-annotation-text), in §4.2.2
-   [WebVTT cue start alignment](#webvtt-cue-start-alignment), in §3.3
-   [WebVTT cue text alignment](#webvtt-cue-text-alignment), in §3.3
-   [WebVTT cue text DOM construction rules](#webvtt-cue-text-dom-construction-rules), in §6.5
-   [WebVTT cue text parsing rules](#webvtt-cue-text-parsing-rules), in §6.4
-   [WebVTT cue text span](#webvtt-cue-text-span), in §4.2.2
-   [WebVTT cue text tokenizer](#webvtt-cue-text-tokenizer), in §6.4
-   [WebVTT cue timestamp](#webvtt-cue-timestamp), in §4.2.2
-   [WebVTT cue timings](#webvtt-cue-timings), in §4.1
-   [WebVTT cue underline span](#webvtt-cue-underline-span), in §4.2.2
-   [WebVTT cue vertical growing left writing direction](#webvtt-cue-vertical-growing-left-writing-direction), in §3.3
-   [WebVTT cue vertical growing right writing direction](#webvtt-cue-vertical-growing-right-writing-direction), in §3.3
-   [WebVTT cue voice span](#webvtt-cue-voice-span), in §4.2.2
-   [WebVTT cue writing direction](#webvtt-cue-writing-direction), in §3.3
-   [WebVTT data state](#webvtt-data-state), in §6.4
-   [WebVTT end tag state](#webvtt-end-tag-state), in §6.4
-   [WebVTT file](#webvtt-file), in §4.1
-   [WebVTT file body](#webvtt-file-body), in §4.1
-   [WebVTT file using caption or subtitle cue text](#webvtt-file-using-caption-or-subtitle-cue-text), in §4.6.3
-   [WebVTT file using chapter title text](#webvtt-file-using-chapter-title-text), in §4.6.2
-   [WebVTT file using metadata content](#webvtt-file-using-metadata-content), in §4.6.1
-   [WebVTT file using only nested cues](#webvtt-file-using-only-nested-cues), in §4.5.1
-   [WebVTT Internal Node Object](#webvtt-internal-node-object), in §6.4
-   [WebVTT Italic Object](#webvtt-italic-object), in §6.4
-   [WebVTT Language Object](#webvtt-language-object), in §6.4
-   [WebVTT Leaf Node Object](#webvtt-leaf-node-object), in §6.4
-   [WebVTT line cue setting](#webvtt-line-cue-setting), in §4.4
-   [WebVTT line terminator](#webvtt-line-terminator), in §4.1
-   [WebVTT metadata cue](#webvtt-metadata-cue), in §3.6
-   [WebVTT metadata text](#webvtt-metadata-text), in §4.2.1
-   [WebVTT Node Object](#webvtt-node-object), in §6.4
-   [WebVTT Node Object's applicable classes](#webvtt-node-objects-applicable-classes), in §6.4
-   [WebVTT Node Object's applicable language](#webvtt-node-objects-applicable-language), in §6.4
-   [WebVTT parser](#webvtt-parser), in §6.1
-   [WebVTT parser algorithm](#webvtt-parser-algorithm), in §6.1
-   [WebVTT percentage](#webvtt-percentage), in §4.1
-   [WebVTT position cue setting](#webvtt-position-cue-setting), in §4.4
-   [WebVTT region](#webvtt-region), in §3.4
-   [WebVTT region anchor](#webvtt-region-anchor), in §3.4
-   [WebVTT region anchor setting](#webvtt-region-anchor-setting), in §4.3
-   [WebVTT region cue setting](#webvtt-region-cue-setting), in §4.4
-   [WebVTT region definition block](#webvtt-region-definition-block), in §4.1
-   [WebVTT region identifier](#webvtt-region-identifier), in §3.4
-   [WebVTT region identifier setting](#webvtt-region-identifier-setting), in §4.3
-   [WebVTT region lines](#webvtt-region-lines), in §3.4
-   [WebVTT region lines setting](#webvtt-region-lines-setting), in §4.3
-   [WebVTT region object](#webvtt-region-object), in §6.2
-   [WebVTT region scroll](#webvtt-region-scroll), in §3.4
-   [WebVTT region scroll none](#webvtt-region-scroll-none), in §3.4
-   [WebVTT region scroll setting](#webvtt-region-scroll-setting), in §4.3
-   [WebVTT region scroll up](#webvtt-region-scroll-up), in §3.4
-   [WebVTT region settings list](#webvtt-region-settings-list), in §4.3
-   [WebVTT region viewport anchor](#webvtt-region-viewport-anchor), in §3.4
-   [WebVTT region viewport anchor setting](#webvtt-region-viewport-anchor-setting), in §4.3
-   [WebVTT region width](#webvtt-region-width), in §3.4
-   [WebVTT region width setting](#webvtt-region-width-setting), in §4.3
-   [WebVTT Ruby Object](#webvtt-ruby-object), in §6.4
-   [WebVTT Ruby Text Object](#webvtt-ruby-text-object), in §6.4
-   [WebVTT rules for extracting the chapter title](#webvtt-rules-for-extracting-the-chapter-title), in §6.6
-   [WebVTT size cue setting](#webvtt-size-cue-setting), in §4.4
-   [WebVTT start tag annotation state](#webvtt-start-tag-annotation-state), in §6.4
-   [WebVTT start tag class state](#webvtt-start-tag-class-state), in §6.4
-   [WebVTT start tag state](#webvtt-start-tag-state), in §6.4
-   [WebVTT style block](#webvtt-style-block), in §4.1
-   [WebVTT tag state](#webvtt-tag-state), in §6.4
-   [WebVTT Text Object](#webvtt-text-object), in §6.4
-   [WebVTT timestamp](#webvtt-timestamp), in §4.1
-   [WebVTT Timestamp Object](#webvtt-timestamp-object), in §6.4
-   [WebVTT timestamp tag state](#webvtt-timestamp-tag-state), in §6.4
-   [WebVTT Underline Object](#webvtt-underline-object), in §6.4
-   [WebVTT vertical text cue setting](#webvtt-vertical-text-cue-setting), in §4.4
-   [WebVTT Voice Object](#webvtt-voice-object), in §6.4
-   [width](#dom-vttregion-width), in §9.2

### [Terms defined by reference]{.content}[](#index-defined-elsewhere){.self-link} {#index-defined-elsewhere .no-num .no-ref .heading .settled}

-   [\[css-align-3\]]{link-type="biblio"} defines the following terms:
    -   [justify-content](https://www.w3.org/TR/css3-align/#propdef-justify-content)
-   [\[css-backgrounds-3\]]{link-type="biblio"} defines the following terms:
    -   [background](https://www.w3.org/TR/css3-background/#propdef-background)
    -   [background-color](https://www.w3.org/TR/css3-background/#propdef-background-color)
    -   [background-image](https://www.w3.org/TR/css3-background/#propdef-background-image)
-   [\[css-cascade-4\]]{link-type="biblio"} defines the following terms:
    -   [\@import](https://www.w3.org/TR/css-cascade-4/#at-ruledef-import)
    -   [cascade](https://www.w3.org/TR/css-cascade-4/#cascade)
-   [\[css-color-4\]]{link-type="biblio"} defines the following terms:
    -   [color](https://www.w3.org/TR/css-color-4/#propdef-color)
    -   [green](https://www.w3.org/TR/css-color-4/#valdef-color-green)
    -   [opacity](https://www.w3.org/TR/css-color-4/#propdef-opacity)
-   [\[css-display-3\]]{link-type="biblio"} defines the following terms:
    -   [display](https://www.w3.org/TR/css-display-3/#propdef-display)
    -   [inline](https://www.w3.org/TR/css-display-3/#valdef-display-inline)
-   [\[css-flexbox-1\]]{link-type="biblio"} defines the following terms:
    -   [flex-end](https://www.w3.org/TR/css-flexbox-1/#valdef-justify-content-flex-end)
    -   [flex-flow](https://www.w3.org/TR/css-flexbox-1/#propdef-flex-flow)
    -   [inline-flex](https://www.w3.org/TR/css-flexbox-1/#valdef-display-inline-flex)
-   [\[css-fonts-3\]]{link-type="biblio"} defines the following terms:
    -   [font](https://www.w3.org/TR/css-fonts-3/#propdef-font)
    -   [font-style](https://www.w3.org/TR/css-fonts-3/#propdef-font-style)
    -   [font-weight](https://www.w3.org/TR/css-fonts-3/#propdef-font-weight)
-   [\[css-fonts-4\]]{link-type="biblio"} defines the following terms:
    -   [bold](https://www.w3.org/TR/css-fonts-4/#valdef-font-weight-bold)
    -   [italic](https://www.w3.org/TR/css-fonts-4/#valdef-font-style-italic)
-   [\[css-overflow-3\]]{link-type="biblio"} defines the following terms:
    -   [hidden](https://www.w3.org/TR/css-overflow-3/#valdef-overflow-hidden)
    -   [overflow](https://www.w3.org/TR/css-overflow-3/#propdef-overflow)
-   [\[css-position-3\]]{link-type="biblio"} defines the following terms:
    -   [absolute](https://www.w3.org/TR/css3-positioning/#valdef-position-absolute)
    -   [left](https://www.w3.org/TR/css3-positioning/#propdef-left)
    -   [position](https://www.w3.org/TR/css3-positioning/#propdef-position)
    -   [relative](https://www.w3.org/TR/css3-positioning/#valdef-position-relative)
    -   [top](https://www.w3.org/TR/css3-positioning/#propdef-top)
-   [\[css-sizing-3\]]{link-type="biblio"} defines the following terms:
    -   [auto](https://drafts.csswg.org/css-sizing-3/#valdef-width-auto)
-   [\[CSS-SYNTAX-3\]]{link-type="biblio"} defines the following terms:
    -   [parse a stylesheet](https://www.w3.org/TR/css-syntax-3/#parse-a-stylesheet0)
-   [\[css-text-3\]]{link-type="biblio"} defines the following terms:
    -   [break-word](https://www.w3.org/TR/css-text-3/#valdef-overflow-wrap-break-word)
    -   [center](https://www.w3.org/TR/css-text-3/#valdef-text-align-center)
    -   [end](https://www.w3.org/TR/css-text-3/#valdef-text-align-end)
    -   [left](https://www.w3.org/TR/css-text-3/#valdef-text-align-left)
    -   [overflow-wrap](https://www.w3.org/TR/css-text-3/#propdef-overflow-wrap)
    -   [pre-line](https://www.w3.org/TR/css-text-3/#valdef-white-space-pre-line)
    -   [right](https://www.w3.org/TR/css-text-3/#valdef-text-align-right)
    -   [start](https://www.w3.org/TR/css-text-3/#valdef-text-align-start)
    -   [text-align](https://www.w3.org/TR/css-text-3/#propdef-text-align)
    -   [white-space](https://www.w3.org/TR/css-text-3/#propdef-white-space)
-   [\[css-text-decor-3\]]{link-type="biblio"} defines the following terms:
    -   [text-decoration](https://www.w3.org/TR/css-text-decor-3/#text-decoration-property)
    -   [text-shadow](https://www.w3.org/TR/css-text-decor-3/#text-shadow-property)
-   [\[css-transitions-1\]]{link-type="biblio"} defines the following terms:
    -   [transition-duration](https://www.w3.org/TR/css3-transitions/#propdef-transition-duration)
    -   [transition-property](https://www.w3.org/TR/css3-transitions/#propdef-transition-property)
-   [\[css-ui-4\]]{link-type="biblio"} defines the following terms:
    -   [outline](https://drafts.csswg.org/css-ui-4/#propdef-outline)
-   [\[CSS-VALUES\]]{link-type="biblio"} defines the following terms:
    -   [vh](https://drafts.csswg.org/css-values-4/#vh)
    -   [vw](https://drafts.csswg.org/css-values-4/#vw)
-   [\[CSS-WRITING-MODES-3\]]{link-type="biblio"} defines the following terms:
    -   [unicode-bidi](https://www.w3.org/TR/css-writing-modes-3/#propdef-unicode-bidi)
-   [\[css-writing-modes-4\]]{link-type="biblio"} defines the following terms:
    -   [horizontal-tb](https://drafts.csswg.org/css-writing-modes-4/#valdef-writing-mode-horizontal-tb)
    -   [plaintext](https://drafts.csswg.org/css-writing-modes-4/#valdef-unicode-bidi-plaintext)
    -   [text-combine-upright](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-combine-upright)
    -   [writing-mode](https://drafts.csswg.org/css-writing-modes-4/#propdef-writing-mode)
-   [\[CSS22\]]{link-type="biblio"} defines the following terms:
    -   [height](https://www.w3.org/TR/CSS22/visudet.html#propdef-height)
    -   [line-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-line-height)
    -   [max-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-max-height)
    -   [min-height](https://www.w3.org/TR/CSS22/visudet.html#propdef-min-height)
    -   [visibility](https://www.w3.org/TR/CSS22/visufx.html#propdef-visibility)
    -   [width](https://www.w3.org/TR/CSS22/visudet.html#propdef-width)
-   [\[CSS3-RUBY\]]{link-type="biblio"} defines the following terms:
    -   [ruby](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby)
    -   [ruby-base](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby-base)
    -   [ruby-position](https://www.w3.org/TR/css-ruby-1/#propdef-ruby-position)
    -   [ruby-text](https://drafts.csswg.org/css-ruby-1/#valdef-display-ruby-text)
-   [\[CSSOM\]]{link-type="biblio"} defines the following terms:
    -   [alternate flag](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-alternate-flag)
    -   [create a css style sheet](https://www.w3.org/TR/cssom-1/#create-a-css-style-sheet)
    -   [css rules](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-css-rules)
    -   [css style sheet](https://www.w3.org/TR/cssom-1/#css-style-sheet)
    -   [getComputedStyle(elt, pseudoElt)](https://www.w3.org/TR/cssom-1/#dom-window-getcomputedstyle)
    -   [location](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-location)
    -   [media](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-media)
    -   [origin-clean flag](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-origin-clean-flag)
    -   [owner css rule](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-owner-css-rule)
    -   [owner node](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-owner-node)
    -   [parent css style sheet](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-parent-css-style-sheet)
    -   [title](https://www.w3.org/TR/cssom-1/#concept-css-style-sheet-title)
-   [\[dom-20151119\]]{link-type="biblio"} defines the following terms:
    -   [Document](https://www.w3.org/TR/dom/#document)
    -   [DocumentFragment](https://www.w3.org/TR/dom/#documentfragment)
    -   [ProcessingInstruction](https://www.w3.org/TR/dom/#processinginstruction)
    -   [Text](https://www.w3.org/TR/dom/#text)
    -   [data](https://www.w3.org/TR/dom/#concept-cd-data)
    -   [namespaceURI](https://www.w3.org/TR/dom/#dom-element-namespaceuri)
    -   [ownerDocument](https://www.w3.org/TR/dom/#dom-node-ownerdocument)
    -   [target](https://www.w3.org/TR/dom/#dom-event-target)
-   [\[ENCODING-CR\]]{link-type="biblio"} defines the following terms:
    -   [utf-8 decode](https://www.w3.org/TR/encoding/#utf-8-decode)
-   [\[HTML\]]{link-type="biblio"} defines the following terms:
    -   [presentational hints](https://html.spec.whatwg.org/multipage/rendering.html#presentational-hints)
-   [\[selectors-3\]]{link-type="biblio"} defines the following terms:
    -   [::after](https://www.w3.org/TR/css3-selectors/#sel-after)
    -   [::before](https://www.w3.org/TR/css3-selectors/#sel-before)
-   [\[SELECTORS4\]]{link-type="biblio"} defines the following terms:
    -   [:future](https://www.w3.org/TR/selectors4/#future-pseudo)
    -   [:lang()](https://www.w3.org/TR/selectors4/#lang-pseudo)
    -   [:past](https://www.w3.org/TR/selectors4/#past-pseudo)
    -   [attribute selector](https://www.w3.org/TR/selectors4/#attribute-selector)
    -   [class selector](https://www.w3.org/TR/selectors4/#class-selector)
    -   [id selector](https://www.w3.org/TR/selectors4/#id-selector)
    -   [originating element](https://www.w3.org/TR/selectors4/#originating-element)
    -   [type selector](https://www.w3.org/TR/selectors4/#type-selector)
-   [\[WebIDL\]]{link-type="biblio"} defines the following terms:
    -   [Exposed](https://heycam.github.io/webidl/#Exposed)
    -   [unsigned long](https://heycam.github.io/webidl/#idl-unsigned-long)
-   [\[WEBIDL-1\]]{link-type="biblio"} defines the following terms:
    -   [DOMString](https://www.w3.org/TR/WebIDL-1/#idl-DOMString)
    -   [IndexSizeError](https://www.w3.org/TR/WebIDL-1/#indexsizeerror)
    -   [boolean](https://www.w3.org/TR/WebIDL-1/#idl-boolean)
    -   [double](https://www.w3.org/TR/WebIDL-1/#idl-double)

## [References]{.content}[](#references){.self-link} {#references .no-num .no-ref .heading .settled}

### [Normative References]{.content}[](#normative){.self-link} {#normative .no-num .no-ref .heading .settled}

\[BCP47\]
:   A. Phillips; M. Davis. [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). September 2009. IETF Best Current Practice. URL: <https://tools.ietf.org/html/bcp47>

\[BIDI\]
:   Mark Davis; Aharon Lanin; Andrew Glass. [Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/tr9-37.html). 14 May 2017. Unicode Standard Annex #9. URL: <https://www.unicode.org/reports/tr9/tr9-37.html>

\[CSS-ALIGN-3\]
:   Elika Etemad; Tab Atkins Jr.. [CSS Box Alignment Module Level 3](https://www.w3.org/TR/css-align-3/). URL: <https://www.w3.org/TR/css-align-3/>

\[CSS-BACKGROUNDS-3\]
:   Bert Bos; Elika Etemad; Brad Kemper. [CSS Backgrounds and Borders Module Level 3](https://www.w3.org/TR/css-backgrounds-3/). URL: <https://www.w3.org/TR/css-backgrounds-3/>

\[CSS-CASCADE-4\]
:   Elika Etemad; Tab Atkins Jr.. [CSS Cascading and Inheritance Level 4](https://www.w3.org/TR/css-cascade-4/). URL: <https://www.w3.org/TR/css-cascade-4/>

\[CSS-COLOR-4\]
:   Tab Atkins Jr.; Chris Lilley. [CSS Color Module Level 4](https://www.w3.org/TR/css-color-4/). URL: <https://www.w3.org/TR/css-color-4/>

\[CSS-DISPLAY-3\]
:   Elika Etemad. [CSS Display Module Level 3](https://www.w3.org/TR/css-display-3/). URL: <https://www.w3.org/TR/css-display-3/>

\[CSS-FLEXBOX-1\]
:   Tab Atkins Jr.; Elika Etemad; Rossen Atanassov. [CSS Flexible Box Layout Module Level 1](https://www.w3.org/TR/css-flexbox-1/). URL: <https://www.w3.org/TR/css-flexbox-1/>

\[CSS-FONTS-3\]
:   John Daggett. [CSS Fonts Module Level 3](https://www.w3.org/TR/css-fonts-3/). URL: <https://www.w3.org/TR/css-fonts-3/>

\[CSS-FONTS-4\]
:   John Daggett; Myles Maxfield. [CSS Fonts Module Level 4](https://www.w3.org/TR/css-fonts-4/). URL: <https://www.w3.org/TR/css-fonts-4/>

\[CSS-OVERFLOW-3\]
:   David Baron; Florian Rivoal. [CSS Overflow Module Level 3](https://www.w3.org/TR/css-overflow-3/). URL: <https://www.w3.org/TR/css-overflow-3/>

\[CSS-POSITION-3\]
:   Rossen Atanassov; Arron Eicholz. [CSS Positioned Layout Module Level 3](https://www.w3.org/TR/css-position-3/). URL: <https://www.w3.org/TR/css-position-3/>

\[CSS-SIZING-3\]
:   Elika Etemad. [CSS Intrinsic & Extrinsic Sizing Module Level 3](https://www.w3.org/TR/css-sizing-3/). URL: <https://www.w3.org/TR/css-sizing-3/>

\[CSS-SYNTAX-3\]
:   Tab Atkins Jr.; Simon Sapin. [CSS Syntax Module Level 3](https://www.w3.org/TR/css-syntax-3/). URL: <https://www.w3.org/TR/css-syntax-3/>

\[CSS-TEXT-3\]
:   Elika Etemad; Koji Ishii. [CSS Text Module Level 3](https://www.w3.org/TR/css-text-3/). URL: <https://www.w3.org/TR/css-text-3/>

\[CSS-TEXT-4\]
:   Elika Etemad; Koji Ishii; Alan Stearns. [CSS Text Module Level 4](https://www.w3.org/TR/css-text-4/). URL: <https://www.w3.org/TR/css-text-4/>

\[CSS-TEXT-DECOR-3\]
:   Elika Etemad; Koji Ishii. [CSS Text Decoration Module Level 3](https://www.w3.org/TR/css-text-decor-3/). URL: <https://www.w3.org/TR/css-text-decor-3/>

\[CSS-TRANSITIONS-1\]
:   David Baron; Dean Jackson; Brian Birtles. [CSS Transitions](https://www.w3.org/TR/css-transitions-1/). URL: <https://www.w3.org/TR/css-transitions-1/>

\[CSS-UI-4\]
:   Florian Rivoal. [CSS Basic User Interface Module Level 4](https://www.w3.org/TR/css-ui-4/). URL: <https://www.w3.org/TR/css-ui-4/>

\[CSS-VALUES\]
:   Tab Atkins Jr.; Elika Etemad. [CSS Values and Units Module Level 3](https://www.w3.org/TR/css-values-3/). URL: <https://www.w3.org/TR/css-values-3/>

\[CSS-WRITING-MODES-3\]
:   Elika Etemad; Koji Ishii. [CSS Writing Modes Level 3](https://www.w3.org/TR/css-writing-modes-3/). URL: <https://www.w3.org/TR/css-writing-modes-3/>

\[CSS-WRITING-MODES-4\]
:   Elika Etemad; Koji Ishii. [CSS Writing Modes Level 4](https://www.w3.org/TR/css-writing-modes-4/). URL: <https://www.w3.org/TR/css-writing-modes-4/>

\[CSS22\]
:   Bert Bos. [Cascading Style Sheets Level 2 Revision 2 (CSS 2.2) Specification](https://www.w3.org/TR/CSS22/). URL: <https://www.w3.org/TR/CSS22/>

\[CSS3-COLOR\]
:   Tantek Çelik; Chris Lilley; David Baron. [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/). 5 December 2017. CR. URL: <https://www.w3.org/TR/css-color-3/>

\[CSS3-RUBY\]
:   Elika Etemad; Koji Ishii. [CSS Ruby Layout Module Level 1](https://www.w3.org/TR/css-ruby-1/). URL: <https://www.w3.org/TR/css-ruby-1/>

\[CSSOM\]
:   Simon Pieters; Glenn Adams. [CSS Object Model (CSSOM)](https://www.w3.org/TR/cssom-1/). URL: <https://www.w3.org/TR/cssom-1/>

\[DOM-20151119\]
:   Anne van Kesteren; et al. [W3C DOM4](https://www.w3.org/TR/2015/REC-dom-20151119/). 19 November 2015. REC. URL: <https://www.w3.org/TR/2015/REC-dom-20151119/>

\[ENCODING-CR\]
:   Anne van Kesteren; Joshua Bell; Addison Phillips. [Encoding](https://www.w3.org/TR/2017/CR-encoding-20170413/). 13 April 2017. CR. URL: <https://www.w3.org/TR/2017/CR-encoding-20170413/>

\[HTML\]
:   Anne van Kesteren; et al. [HTML Standard](https://html.spec.whatwg.org/multipage/). Living Standard. URL: <https://html.spec.whatwg.org/multipage/>

\[HTML51\]
:   Steve Faulkner; et al. [HTML 5.1 2nd Edition](https://www.w3.org/TR/html51/). URL: <https://www.w3.org/TR/html51/>

\[RFC2119\]
:   S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). March 1997. Best Current Practice. URL: <https://tools.ietf.org/html/rfc2119>

\[RFC3629\]
:   F. Yergeau. [UTF-8, a transformation format of ISO 10646](https://tools.ietf.org/html/rfc3629). November 2003. Internet Standard. URL: <https://tools.ietf.org/html/rfc3629>

\[SELECTORS-3\]
:   Tantek Çelik; et al. [Selectors Level 3](https://www.w3.org/TR/selectors-3/). URL: <https://www.w3.org/TR/selectors-3/>

\[SELECTORS4\]
:   Elika Etemad; Tab Atkins Jr.. [Selectors Level 4](https://www.w3.org/TR/selectors-4/). URL: <https://www.w3.org/TR/selectors-4/>

\[WebIDL\]
:   Cameron McCormack; Boris Zbarsky; Tobie Langel. [Web IDL](https://heycam.github.io/webidl/). URL: <https://heycam.github.io/webidl/>

\[WEBIDL-1\]
:   Cameron McCormack. [WebIDL Level 1](https://www.w3.org/TR/2016/REC-WebIDL-1-20161215/). URL: <https://www.w3.org/TR/2016/REC-WebIDL-1-20161215/>

### [Informative References]{.content}[](#informative){.self-link} {#informative .no-num .no-ref .heading .settled}

\[MAUR\]
:   Shane McCarron; Michael Cooper; Mark Sadecki. [Media Accessibility User Requirements](https://www.w3.org/TR/media-accessibility-reqs/). WD. URL: [http://www.w3.org/TR/media-accessibility-reqs/](https://www.w3.org/TR/media-accessibility-reqs/)

\[WCAG20\]
:   Ben Caldwell; et al. [Web Content Accessibility Guidelines (WCAG) 2.0](https://www.w3.org/TR/WCAG20/). 11 December 2008. REC. URL: <https://www.w3.org/TR/WCAG20/>

## [IDL Index]{.content}[](#idl-index){.self-link} {#idl-index .no-num .no-ref .heading .settled}

``` {.idl .highlight .def}
enum AutoKeyword { "auto" };
typedef (double or AutoKeyword) LineAndPositionSetting;
enum DirectionSetting { "" /* horizontal */, "rl", "lr" };
enum LineAlignSetting { "start", "center", "end" };
enum PositionAlignSetting { "line-left", "center", "line-right", "auto" };
enum AlignSetting { "start", "center", "end", "left", "right" };
[Exposed=Window,
 Constructor(double startTime, double endTime, DOMString text)]
interface VTTCue : TextTrackCue {
  attribute VTTRegion? region;
  attribute DirectionSetting vertical;
  attribute boolean snapToLines;
  attribute LineAndPositionSetting line;
  attribute LineAlignSetting lineAlign;
  attribute LineAndPositionSetting position;
  attribute PositionAlignSetting positionAlign;
  attribute double size;
  attribute AlignSetting align;
  attribute DOMString text;
  DocumentFragment getCueAsHTML();
};

enum ScrollSetting { "" /* none */, "up" };
[Exposed=Window,
 Constructor]
interface VTTRegion {
  attribute DOMString id;
  attribute double width;
  attribute unsigned long lines;
  attribute double regionAnchorX;
  attribute double regionAnchorY;
  attribute double viewportAnchorX;
  attribute double viewportAnchorY;
  attribute ScrollSetting scroll;
};
```

**[#webvtt](#webvtt)Referenced in:**

-   [2.1. Conformance classes](#ref-for-webvtt-1)

**[#user-agents-that-do-not-support-css](#user-agents-that-do-not-support-css)Referenced in:**

-   [7. Rendering](#ref-for-user-agents-that-do-not-support-css-1)
-   [8. CSS extensions](#ref-for-user-agents-that-do-not-support-css-2)

**[#user-agents-that-do-not-support-a-full-html-css-engine](#user-agents-that-do-not-support-a-full-html-css-engine)Referenced in:**

-   [2.1. Conformance classes](#ref-for-user-agents-that-do-not-support-a-full-html-css-engine-1)
-   [7. Rendering](#ref-for-user-agents-that-do-not-support-a-full-html-css-engine-2)

**[#webvtt-cue](#webvtt-cue)Referenced in:**

-   [1.1. A simple caption file](#ref-for-webvtt-cue-1)
-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-2) [(2)](#ref-for-webvtt-cue-3) [(3)](#ref-for-webvtt-cue-4) [(4)](#ref-for-webvtt-cue-5) [(5)](#ref-for-webvtt-cue-6) [(6)](#ref-for-webvtt-cue-7) [(7)](#ref-for-webvtt-cue-8) [(8)](#ref-for-webvtt-cue-9) [(9)](#ref-for-webvtt-cue-10) [(10)](#ref-for-webvtt-cue-11) [(11)](#ref-for-webvtt-cue-12) [(12)](#ref-for-webvtt-cue-13)
-   [3.5. WebVTT chapter cues](#ref-for-webvtt-cue-14)
-   [3.6. WebVTT metadata cues](#ref-for-webvtt-cue-15)
-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-16)
-   [4.3. WebVTT region settings](#ref-for-webvtt-cue-17)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-18) [(2)](#ref-for-webvtt-cue-19) [(3)](#ref-for-webvtt-cue-20) [(4)](#ref-for-webvtt-cue-21) [(5)](#ref-for-webvtt-cue-22)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-23)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-cue-24)
-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-webvtt-cue-25)
-   [7.1. Processing model](#ref-for-webvtt-cue-26) [(2)](#ref-for-webvtt-cue-27)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-28) [(2)](#ref-for-webvtt-cue-29)
-   [8.2. Processing model](#ref-for-webvtt-cue-30) [(2)](#ref-for-webvtt-cue-31) [(3)](#ref-for-webvtt-cue-32)
-   [8.2.2. The :past and :future pseudo-classes](#ref-for-webvtt-cue-33) [(2)](#ref-for-webvtt-cue-34)
-   [8.2.3. The ::cue-region pseudo-element](#ref-for-webvtt-cue-35)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-36) [(2)](#ref-for-webvtt-cue-37) [(3)](#ref-for-webvtt-cue-38) [(4)](#ref-for-webvtt-cue-39) [(5)](#ref-for-webvtt-cue-40) [(6)](#ref-for-webvtt-cue-41) [(7)](#ref-for-webvtt-cue-42) [(8)](#ref-for-webvtt-cue-43) [(9)](#ref-for-webvtt-cue-44) [(10)](#ref-for-webvtt-cue-45) [(11)](#ref-for-webvtt-cue-46) [(12)](#ref-for-webvtt-cue-47)

**[#cue-text](#cue-text)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-cue-text-1) [(2)](#ref-for-cue-text-2) [(3)](#ref-for-cue-text-3)
-   [3.5. WebVTT chapter cues](#ref-for-cue-text-4)
-   [3.6. WebVTT metadata cues](#ref-for-cue-text-5)
-   [4.2.3. WebVTT chapter title text](#ref-for-cue-text-6)
-   [6.1. WebVTT file parsing](#ref-for-cue-text-7) [(2)](#ref-for-cue-text-8)
-   [6.4. WebVTT cue text parsing rules](#ref-for-cue-text-9) [(2)](#ref-for-cue-text-10)
-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-cue-text-11)
-   [7.1. Processing model](#ref-for-cue-text-12)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-cue-text-13)
-   [9.1. The VTTCue interface](#ref-for-cue-text-14) [(2)](#ref-for-cue-text-15) [(3)](#ref-for-cue-text-16) [(4)](#ref-for-cue-text-17) [(5)](#ref-for-cue-text-18) [(6)](#ref-for-cue-text-19) [(7)](#ref-for-cue-text-20) [(8)](#ref-for-cue-text-21)

**[#webvtt-caption-or-subtitle-cue](#webvtt-caption-or-subtitle-cue)Referenced in:**

-   [3.4. WebVTT caption or subtitle regions](#ref-for-webvtt-caption-or-subtitle-cue-1)
-   [7. Rendering](#ref-for-webvtt-caption-or-subtitle-cue-2)

**[#webvtt-cue-box](#webvtt-cue-box)Referenced in:**

-   [1.4. Other caption and subtitling features](#ref-for-webvtt-cue-box-1) [(2)](#ref-for-webvtt-cue-box-2) [(3)](#ref-for-webvtt-cue-box-3) [(4)](#ref-for-webvtt-cue-box-4) [(5)](#ref-for-webvtt-cue-box-5)
-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-box-6) [(2)](#ref-for-webvtt-cue-box-7) [(3)](#ref-for-webvtt-cue-box-8) [(4)](#ref-for-webvtt-cue-box-9) [(5)](#ref-for-webvtt-cue-box-10) [(6)](#ref-for-webvtt-cue-box-11) [(7)](#ref-for-webvtt-cue-box-12) [(8)](#ref-for-webvtt-cue-box-13) [(9)](#ref-for-webvtt-cue-box-14) [(10)](#ref-for-webvtt-cue-box-15) [(11)](#ref-for-webvtt-cue-box-16) [(12)](#ref-for-webvtt-cue-box-17) [(13)](#ref-for-webvtt-cue-box-18) [(14)](#ref-for-webvtt-cue-box-19) [(15)](#ref-for-webvtt-cue-box-20) [(16)](#ref-for-webvtt-cue-box-21) [(17)](#ref-for-webvtt-cue-box-22) [(18)](#ref-for-webvtt-cue-box-23)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-box-24) [(2)](#ref-for-webvtt-cue-box-25) [(3)](#ref-for-webvtt-cue-box-26)

**[#webvtt-cue-writing-direction](#webvtt-cue-writing-direction)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-writing-direction-1) [(2)](#ref-for-webvtt-cue-writing-direction-2) [(3)](#ref-for-webvtt-cue-writing-direction-3) [(4)](#ref-for-webvtt-cue-writing-direction-4) [(5)](#ref-for-webvtt-cue-writing-direction-5) [(6)](#ref-for-webvtt-cue-writing-direction-6) [(7)](#ref-for-webvtt-cue-writing-direction-7) [(8)](#ref-for-webvtt-cue-writing-direction-8) [(9)](#ref-for-webvtt-cue-writing-direction-9) [(10)](#ref-for-webvtt-cue-writing-direction-10) [(11)](#ref-for-webvtt-cue-writing-direction-11)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-writing-direction-12)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-writing-direction-13)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-writing-direction-14) [(2)](#ref-for-webvtt-cue-writing-direction-15) [(3)](#ref-for-webvtt-cue-writing-direction-16)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-writing-direction-17) [(2)](#ref-for-webvtt-cue-writing-direction-18) [(3)](#ref-for-webvtt-cue-writing-direction-19) [(4)](#ref-for-webvtt-cue-writing-direction-20) [(5)](#ref-for-webvtt-cue-writing-direction-21) [(6)](#ref-for-webvtt-cue-writing-direction-22) [(7)](#ref-for-webvtt-cue-writing-direction-23) [(8)](#ref-for-webvtt-cue-writing-direction-24) [(9)](#ref-for-webvtt-cue-writing-direction-25) [(10)](#ref-for-webvtt-cue-writing-direction-26) [(11)](#ref-for-webvtt-cue-writing-direction-27) [(12)](#ref-for-webvtt-cue-writing-direction-28) [(13)](#ref-for-webvtt-cue-writing-direction-29) [(14)](#ref-for-webvtt-cue-writing-direction-30) [(15)](#ref-for-webvtt-cue-writing-direction-31) [(16)](#ref-for-webvtt-cue-writing-direction-32) [(17)](#ref-for-webvtt-cue-writing-direction-33)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-writing-direction-34) [(2)](#ref-for-webvtt-cue-writing-direction-35) [(3)](#ref-for-webvtt-cue-writing-direction-36) [(4)](#ref-for-webvtt-cue-writing-direction-37) [(5)](#ref-for-webvtt-cue-writing-direction-38)

**[#webvtt-cue-horizontal-writing-direction](#webvtt-cue-horizontal-writing-direction)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-horizontal-writing-direction-1) [(2)](#ref-for-webvtt-cue-horizontal-writing-direction-2) [(3)](#ref-for-webvtt-cue-horizontal-writing-direction-3) [(4)](#ref-for-webvtt-cue-horizontal-writing-direction-4) [(5)](#ref-for-webvtt-cue-horizontal-writing-direction-5) [(6)](#ref-for-webvtt-cue-horizontal-writing-direction-6) [(7)](#ref-for-webvtt-cue-horizontal-writing-direction-7) [(8)](#ref-for-webvtt-cue-horizontal-writing-direction-8) [(9)](#ref-for-webvtt-cue-horizontal-writing-direction-9) [(10)](#ref-for-webvtt-cue-horizontal-writing-direction-10) [(11)](#ref-for-webvtt-cue-horizontal-writing-direction-11) [(12)](#ref-for-webvtt-cue-horizontal-writing-direction-12)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-horizontal-writing-direction-13)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-horizontal-writing-direction-14)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-horizontal-writing-direction-15) [(2)](#ref-for-webvtt-cue-horizontal-writing-direction-16) [(3)](#ref-for-webvtt-cue-horizontal-writing-direction-17) [(4)](#ref-for-webvtt-cue-horizontal-writing-direction-18) [(5)](#ref-for-webvtt-cue-horizontal-writing-direction-19) [(6)](#ref-for-webvtt-cue-horizontal-writing-direction-20) [(7)](#ref-for-webvtt-cue-horizontal-writing-direction-21)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-horizontal-writing-direction-22) [(2)](#ref-for-webvtt-cue-horizontal-writing-direction-23) [(3)](#ref-for-webvtt-cue-horizontal-writing-direction-24)

**[#webvtt-cue-vertical-growing-left-writing-direction](#webvtt-cue-vertical-growing-left-writing-direction)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-1) [(2)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-2) [(3)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-3)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-4)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-5) [(2)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-6) [(3)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-7) [(4)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-8) [(5)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-9) [(6)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-10) [(7)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-11)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-12) [(2)](#ref-for-webvtt-cue-vertical-growing-left-writing-direction-13)

**[#webvtt-cue-vertical-growing-right-writing-direction](#webvtt-cue-vertical-growing-right-writing-direction)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-1) [(2)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-2) [(3)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-3)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-4)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-5) [(2)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-6) [(3)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-7) [(4)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-8) [(5)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-9) [(6)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-10) [(7)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-11)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-12) [(2)](#ref-for-webvtt-cue-vertical-growing-right-writing-direction-13)

**[#webvtt-cue-snap-to-lines-flag](#webvtt-cue-snap-to-lines-flag)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-snap-to-lines-flag-1) [(2)](#ref-for-webvtt-cue-snap-to-lines-flag-2) [(3)](#ref-for-webvtt-cue-snap-to-lines-flag-3) [(4)](#ref-for-webvtt-cue-snap-to-lines-flag-4) [(5)](#ref-for-webvtt-cue-snap-to-lines-flag-5) [(6)](#ref-for-webvtt-cue-snap-to-lines-flag-6) [(7)](#ref-for-webvtt-cue-snap-to-lines-flag-7)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-snap-to-lines-flag-8)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-snap-to-lines-flag-9)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-snap-to-lines-flag-10) [(2)](#ref-for-webvtt-cue-snap-to-lines-flag-11) [(3)](#ref-for-webvtt-cue-snap-to-lines-flag-12) [(4)](#ref-for-webvtt-cue-snap-to-lines-flag-13)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-snap-to-lines-flag-14) [(2)](#ref-for-webvtt-cue-snap-to-lines-flag-15) [(3)](#ref-for-webvtt-cue-snap-to-lines-flag-16) [(4)](#ref-for-webvtt-cue-snap-to-lines-flag-17)

**[#webvtt-cue-line](#webvtt-cue-line)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-line-1) [(2)](#ref-for-webvtt-cue-line-2) [(3)](#ref-for-webvtt-cue-line-3) [(4)](#ref-for-webvtt-cue-line-4) [(5)](#ref-for-webvtt-cue-line-5) [(6)](#ref-for-webvtt-cue-line-6) [(7)](#ref-for-webvtt-cue-line-7) [(8)](#ref-for-webvtt-cue-line-8) [(9)](#ref-for-webvtt-cue-line-9) [(10)](#ref-for-webvtt-cue-line-10) [(11)](#ref-for-webvtt-cue-line-11) [(12)](#ref-for-webvtt-cue-line-12) [(13)](#ref-for-webvtt-cue-line-13) [(14)](#ref-for-webvtt-cue-line-14) [(15)](#ref-for-webvtt-cue-line-15) [(16)](#ref-for-webvtt-cue-line-16) [(17)](#ref-for-webvtt-cue-line-17) [(18)](#ref-for-webvtt-cue-line-18) [(19)](#ref-for-webvtt-cue-line-19) [(20)](#ref-for-webvtt-cue-line-20)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-line-21)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-22) [(2)](#ref-for-webvtt-cue-line-23)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-24) [(2)](#ref-for-webvtt-cue-line-25) [(3)](#ref-for-webvtt-cue-line-26) [(4)](#ref-for-webvtt-cue-line-27)

**[#webvtt-cue-line-automatic](#webvtt-cue-line-automatic)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-line-automatic-1) [(2)](#ref-for-webvtt-cue-line-automatic-2) [(3)](#ref-for-webvtt-cue-line-automatic-3)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-line-automatic-4)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-automatic-5)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-automatic-6) [(2)](#ref-for-webvtt-cue-line-automatic-7) [(3)](#ref-for-webvtt-cue-line-automatic-8) [(4)](#ref-for-webvtt-cue-line-automatic-9)

**[#cue-computed-line](#cue-computed-line)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-cue-computed-line-1)
-   [7.2. Processing cue settings](#ref-for-cue-computed-line-2) [(2)](#ref-for-cue-computed-line-3) [(3)](#ref-for-cue-computed-line-4)

**[#webvtt-cue-line-alignment](#webvtt-cue-line-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-line-alignment-1) [(2)](#ref-for-webvtt-cue-line-alignment-2) [(3)](#ref-for-webvtt-cue-line-alignment-3) [(4)](#ref-for-webvtt-cue-line-alignment-4)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-line-alignment-5)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-line-alignment-6)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-alignment-7) [(2)](#ref-for-webvtt-cue-line-alignment-8) [(3)](#ref-for-webvtt-cue-line-alignment-9)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-line-alignment-10) [(2)](#ref-for-webvtt-cue-line-alignment-11) [(3)](#ref-for-webvtt-cue-line-alignment-12) [(4)](#ref-for-webvtt-cue-line-alignment-13)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-alignment-14) [(2)](#ref-for-webvtt-cue-line-alignment-15) [(3)](#ref-for-webvtt-cue-line-alignment-16) [(4)](#ref-for-webvtt-cue-line-alignment-17) [(5)](#ref-for-webvtt-cue-line-alignment-18)

**[#webvtt-cue-line-start-alignment](#webvtt-cue-line-start-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-line-start-alignment-1)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-line-start-alignment-2) [(2)](#ref-for-webvtt-cue-line-start-alignment-3)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-line-start-alignment-4)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-start-alignment-5)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-start-alignment-6) [(2)](#ref-for-webvtt-cue-line-start-alignment-7) [(3)](#ref-for-webvtt-cue-line-start-alignment-8)

**[#webvtt-cue-line-center-alignment](#webvtt-cue-line-center-alignment)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-line-center-alignment-1)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-center-alignment-2)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-line-center-alignment-3) [(2)](#ref-for-webvtt-cue-line-center-alignment-4)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-center-alignment-5) [(2)](#ref-for-webvtt-cue-line-center-alignment-6)

**[#webvtt-cue-line-end-alignment](#webvtt-cue-line-end-alignment)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-line-end-alignment-1)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-line-end-alignment-2)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-line-end-alignment-3) [(2)](#ref-for-webvtt-cue-line-end-alignment-4)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-line-end-alignment-5) [(2)](#ref-for-webvtt-cue-line-end-alignment-6)

**[#webvtt-cue-position](#webvtt-cue-position)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-position-1) [(2)](#ref-for-webvtt-cue-position-2) [(3)](#ref-for-webvtt-cue-position-3) [(4)](#ref-for-webvtt-cue-position-4) [(5)](#ref-for-webvtt-cue-position-5) [(6)](#ref-for-webvtt-cue-position-6) [(7)](#ref-for-webvtt-cue-position-7) [(8)](#ref-for-webvtt-cue-position-8) [(9)](#ref-for-webvtt-cue-position-9) [(10)](#ref-for-webvtt-cue-position-10) [(11)](#ref-for-webvtt-cue-position-11) [(12)](#ref-for-webvtt-cue-position-12) [(13)](#ref-for-webvtt-cue-position-13) [(14)](#ref-for-webvtt-cue-position-14) [(15)](#ref-for-webvtt-cue-position-15) [(16)](#ref-for-webvtt-cue-position-16) [(17)](#ref-for-webvtt-cue-position-17) [(18)](#ref-for-webvtt-cue-position-18) [(19)](#ref-for-webvtt-cue-position-19)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-position-20)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-position-21) [(2)](#ref-for-webvtt-cue-position-22)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-23) [(2)](#ref-for-webvtt-cue-position-24) [(3)](#ref-for-webvtt-cue-position-25) [(4)](#ref-for-webvtt-cue-position-26)

**[#webvtt-cue-automatic-position](#webvtt-cue-automatic-position)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-automatic-position-1) [(2)](#ref-for-webvtt-cue-automatic-position-2) [(3)](#ref-for-webvtt-cue-automatic-position-3) [(4)](#ref-for-webvtt-cue-automatic-position-4) [(5)](#ref-for-webvtt-cue-automatic-position-5)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-automatic-position-6)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-automatic-position-7)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-automatic-position-8) [(2)](#ref-for-webvtt-cue-automatic-position-9) [(3)](#ref-for-webvtt-cue-automatic-position-10) [(4)](#ref-for-webvtt-cue-automatic-position-11)

**[#cue-computed-position](#cue-computed-position)Referenced in:**

-   [7.1. Processing model](#ref-for-cue-computed-position-1)
-   [7.2. Processing cue settings](#ref-for-cue-computed-position-2) [(2)](#ref-for-cue-computed-position-3) [(3)](#ref-for-cue-computed-position-4) [(4)](#ref-for-cue-computed-position-5) [(5)](#ref-for-cue-computed-position-6) [(6)](#ref-for-cue-computed-position-7) [(7)](#ref-for-cue-computed-position-8) [(8)](#ref-for-cue-computed-position-9) [(9)](#ref-for-cue-computed-position-10) [(10)](#ref-for-cue-computed-position-11) [(11)](#ref-for-cue-computed-position-12) [(12)](#ref-for-cue-computed-position-13)

**[#webvtt-cue-position-alignment](#webvtt-cue-position-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-position-alignment-1) [(2)](#ref-for-webvtt-cue-position-alignment-2) [(3)](#ref-for-webvtt-cue-position-alignment-3) [(4)](#ref-for-webvtt-cue-position-alignment-4) [(5)](#ref-for-webvtt-cue-position-alignment-5) [(6)](#ref-for-webvtt-cue-position-alignment-6)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-position-alignment-7)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-position-alignment-8) [(2)](#ref-for-webvtt-cue-position-alignment-9) [(3)](#ref-for-webvtt-cue-position-alignment-10)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-alignment-11) [(2)](#ref-for-webvtt-cue-position-alignment-12) [(3)](#ref-for-webvtt-cue-position-alignment-13) [(4)](#ref-for-webvtt-cue-position-alignment-14) [(5)](#ref-for-webvtt-cue-position-alignment-15)

**[#webvtt-cue-position-line-left-alignment](#webvtt-cue-position-line-left-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-position-line-left-alignment-1) [(2)](#ref-for-webvtt-cue-position-line-left-alignment-2) [(3)](#ref-for-webvtt-cue-position-line-left-alignment-3) [(4)](#ref-for-webvtt-cue-position-line-left-alignment-4)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-position-line-left-alignment-5)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-position-line-left-alignment-6)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-position-line-left-alignment-7) [(2)](#ref-for-webvtt-cue-position-line-left-alignment-8) [(3)](#ref-for-webvtt-cue-position-line-left-alignment-9)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-line-left-alignment-10) [(2)](#ref-for-webvtt-cue-position-line-left-alignment-11)

**[#webvtt-cue-position-center-alignment](#webvtt-cue-position-center-alignment)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-position-center-alignment-1)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-position-center-alignment-2)
-   [7.1. Processing model](#ref-for-webvtt-cue-position-center-alignment-3)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-position-center-alignment-4) [(2)](#ref-for-webvtt-cue-position-center-alignment-5) [(3)](#ref-for-webvtt-cue-position-center-alignment-6) [(4)](#ref-for-webvtt-cue-position-center-alignment-7)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-center-alignment-8) [(2)](#ref-for-webvtt-cue-position-center-alignment-9)

**[#webvtt-cue-position-line-right-alignment](#webvtt-cue-position-line-right-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-position-line-right-alignment-1) [(2)](#ref-for-webvtt-cue-position-line-right-alignment-2) [(3)](#ref-for-webvtt-cue-position-line-right-alignment-3)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-position-line-right-alignment-4)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-position-line-right-alignment-5)
-   [7.1. Processing model](#ref-for-webvtt-cue-position-line-right-alignment-6)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-position-line-right-alignment-7) [(2)](#ref-for-webvtt-cue-position-line-right-alignment-8) [(3)](#ref-for-webvtt-cue-position-line-right-alignment-9)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-line-right-alignment-10) [(2)](#ref-for-webvtt-cue-position-line-right-alignment-11)

**[#webvtt-cue-position-automatic-alignment](#webvtt-cue-position-automatic-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-position-automatic-alignment-1) [(2)](#ref-for-webvtt-cue-position-automatic-alignment-2)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-position-automatic-alignment-3)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-position-automatic-alignment-4) [(2)](#ref-for-webvtt-cue-position-automatic-alignment-5) [(3)](#ref-for-webvtt-cue-position-automatic-alignment-6)

**[#cue-computed-position-alignment](#cue-computed-position-alignment)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-cue-computed-position-alignment-1)
-   [7.1. Processing model](#ref-for-cue-computed-position-alignment-2) [(2)](#ref-for-cue-computed-position-alignment-3) [(3)](#ref-for-cue-computed-position-alignment-4)
-   [7.2. Processing cue settings](#ref-for-cue-computed-position-alignment-5) [(2)](#ref-for-cue-computed-position-alignment-6) [(3)](#ref-for-cue-computed-position-alignment-7) [(4)](#ref-for-cue-computed-position-alignment-8) [(5)](#ref-for-cue-computed-position-alignment-9) [(6)](#ref-for-cue-computed-position-alignment-10) [(7)](#ref-for-cue-computed-position-alignment-11) [(8)](#ref-for-cue-computed-position-alignment-12) [(9)](#ref-for-cue-computed-position-alignment-13) [(10)](#ref-for-cue-computed-position-alignment-14)

**[#webvtt-cue-size](#webvtt-cue-size)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-size-1) [(2)](#ref-for-webvtt-cue-size-2) [(3)](#ref-for-webvtt-cue-size-3) [(4)](#ref-for-webvtt-cue-size-4) [(5)](#ref-for-webvtt-cue-size-5) [(6)](#ref-for-webvtt-cue-size-6)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-size-7)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-size-8) [(2)](#ref-for-webvtt-cue-size-9)
-   [7.2. Processing cue settings](#ref-for-webvtt-cue-size-10) [(2)](#ref-for-webvtt-cue-size-11)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-size-12) [(2)](#ref-for-webvtt-cue-size-13) [(3)](#ref-for-webvtt-cue-size-14) [(4)](#ref-for-webvtt-cue-size-15)

**[#webvtt-cue-text-alignment](#webvtt-cue-text-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-text-alignment-1) [(2)](#ref-for-webvtt-cue-text-alignment-2) [(3)](#ref-for-webvtt-cue-text-alignment-3) [(4)](#ref-for-webvtt-cue-text-alignment-4) [(5)](#ref-for-webvtt-cue-text-alignment-5) [(6)](#ref-for-webvtt-cue-text-alignment-6) [(7)](#ref-for-webvtt-cue-text-alignment-7) [(8)](#ref-for-webvtt-cue-text-alignment-8) [(9)](#ref-for-webvtt-cue-text-alignment-9) [(10)](#ref-for-webvtt-cue-text-alignment-10) [(11)](#ref-for-webvtt-cue-text-alignment-11) [(12)](#ref-for-webvtt-cue-text-alignment-12) [(13)](#ref-for-webvtt-cue-text-alignment-13) [(14)](#ref-for-webvtt-cue-text-alignment-14)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-text-alignment-15)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-text-alignment-16) [(2)](#ref-for-webvtt-cue-text-alignment-17) [(3)](#ref-for-webvtt-cue-text-alignment-18) [(4)](#ref-for-webvtt-cue-text-alignment-19) [(5)](#ref-for-webvtt-cue-text-alignment-20)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-text-alignment-21) [(2)](#ref-for-webvtt-cue-text-alignment-22)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-text-alignment-23) [(2)](#ref-for-webvtt-cue-text-alignment-24) [(3)](#ref-for-webvtt-cue-text-alignment-25) [(4)](#ref-for-webvtt-cue-text-alignment-26) [(5)](#ref-for-webvtt-cue-text-alignment-27)

**[#webvtt-cue-start-alignment](#webvtt-cue-start-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-start-alignment-1) [(2)](#ref-for-webvtt-cue-start-alignment-2) [(3)](#ref-for-webvtt-cue-start-alignment-3) [(4)](#ref-for-webvtt-cue-start-alignment-4) [(5)](#ref-for-webvtt-cue-start-alignment-5) [(6)](#ref-for-webvtt-cue-start-alignment-6)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-start-alignment-7)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-start-alignment-8)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-start-alignment-9) [(2)](#ref-for-webvtt-cue-start-alignment-10)

**[#webvtt-cue-center-alignment](#webvtt-cue-center-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-center-alignment-1) [(2)](#ref-for-webvtt-cue-center-alignment-2) [(3)](#ref-for-webvtt-cue-center-alignment-3) [(4)](#ref-for-webvtt-cue-center-alignment-4)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-center-alignment-5)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-center-alignment-6)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-center-alignment-7)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-center-alignment-8) [(2)](#ref-for-webvtt-cue-center-alignment-9) [(3)](#ref-for-webvtt-cue-center-alignment-10)

**[#webvtt-cue-end-alignment](#webvtt-cue-end-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-end-alignment-1) [(2)](#ref-for-webvtt-cue-end-alignment-2) [(3)](#ref-for-webvtt-cue-end-alignment-3) [(4)](#ref-for-webvtt-cue-end-alignment-4) [(5)](#ref-for-webvtt-cue-end-alignment-5)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-end-alignment-6)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-end-alignment-7)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-end-alignment-8) [(2)](#ref-for-webvtt-cue-end-alignment-9)

**[#webvtt-cue-left-alignment](#webvtt-cue-left-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-left-alignment-1) [(2)](#ref-for-webvtt-cue-left-alignment-2) [(3)](#ref-for-webvtt-cue-left-alignment-3) [(4)](#ref-for-webvtt-cue-left-alignment-4)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-left-alignment-5)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-left-alignment-6)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-left-alignment-7) [(2)](#ref-for-webvtt-cue-left-alignment-8)

**[#webvtt-cue-right-alignment](#webvtt-cue-right-alignment)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-right-alignment-1) [(2)](#ref-for-webvtt-cue-right-alignment-2) [(3)](#ref-for-webvtt-cue-right-alignment-3) [(4)](#ref-for-webvtt-cue-right-alignment-4)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-right-alignment-5)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-right-alignment-6)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-right-alignment-7) [(2)](#ref-for-webvtt-cue-right-alignment-8)

**[#webvtt-cue-region](#webvtt-cue-region)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-cue-region-1)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-cue-region-2)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-cue-region-3) [(2)](#ref-for-webvtt-cue-region-4) [(3)](#ref-for-webvtt-cue-region-5) [(4)](#ref-for-webvtt-cue-region-6)
-   [7.1. Processing model](#ref-for-webvtt-cue-region-7) [(2)](#ref-for-webvtt-cue-region-8) [(3)](#ref-for-webvtt-cue-region-9)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-region-10) [(2)](#ref-for-webvtt-cue-region-11) [(3)](#ref-for-webvtt-cue-region-12)

**[#webvtt-region](#webvtt-region)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-region-1) [(2)](#ref-for-webvtt-region-2) [(3)](#ref-for-webvtt-region-3)
-   [3.4. WebVTT caption or subtitle regions](#ref-for-webvtt-region-4) [(2)](#ref-for-webvtt-region-5)
-   [4.3. WebVTT region settings](#ref-for-webvtt-region-6) [(2)](#ref-for-webvtt-region-7) [(3)](#ref-for-webvtt-region-8)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-9)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-10)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-region-11)
-   [7.1. Processing model](#ref-for-webvtt-region-12) [(2)](#ref-for-webvtt-region-13) [(3)](#ref-for-webvtt-region-14)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-region-15)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-16) [(2)](#ref-for-webvtt-region-17) [(3)](#ref-for-webvtt-region-18) [(4)](#ref-for-webvtt-region-19) [(5)](#ref-for-webvtt-region-20) [(6)](#ref-for-webvtt-region-21) [(7)](#ref-for-webvtt-region-22) [(8)](#ref-for-webvtt-region-23) [(9)](#ref-for-webvtt-region-24) [(10)](#ref-for-webvtt-region-25)

**[#webvtt-region-identifier](#webvtt-region-identifier)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-region-identifier-1)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-identifier-2)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-identifier-3)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-webvtt-region-identifier-4)
-   [8.1. Introduction](#ref-for-webvtt-region-identifier-5)
-   [8.2.3. The ::cue-region pseudo-element](#ref-for-webvtt-region-identifier-6)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-identifier-7) [(2)](#ref-for-webvtt-region-identifier-8) [(3)](#ref-for-webvtt-region-identifier-9)

**[#webvtt-region-width](#webvtt-region-width)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-width-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-width-2)
-   [7.1. Processing model](#ref-for-webvtt-region-width-3) [(2)](#ref-for-webvtt-region-width-4) [(3)](#ref-for-webvtt-region-width-5) [(4)](#ref-for-webvtt-region-width-6)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-width-7) [(2)](#ref-for-webvtt-region-width-8) [(3)](#ref-for-webvtt-region-width-9)

**[#webvtt-region-lines](#webvtt-region-lines)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-lines-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-lines-2)
-   [7.1. Processing model](#ref-for-webvtt-region-lines-3)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-lines-4) [(2)](#ref-for-webvtt-region-lines-5) [(3)](#ref-for-webvtt-region-lines-6)

**[#webvtt-region-anchor](#webvtt-region-anchor)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-anchor-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-anchor-2)
-   [7.1. Processing model](#ref-for-webvtt-region-anchor-3) [(2)](#ref-for-webvtt-region-anchor-4) [(3)](#ref-for-webvtt-region-anchor-5) [(4)](#ref-for-webvtt-region-anchor-6)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-anchor-7) [(2)](#ref-for-webvtt-region-anchor-8) [(3)](#ref-for-webvtt-region-anchor-9) [(4)](#ref-for-webvtt-region-anchor-10) [(5)](#ref-for-webvtt-region-anchor-11) [(6)](#ref-for-webvtt-region-anchor-12)

**[#webvtt-region-viewport-anchor](#webvtt-region-viewport-anchor)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-viewport-anchor-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-viewport-anchor-2)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-viewport-anchor-3) [(2)](#ref-for-webvtt-region-viewport-anchor-4) [(3)](#ref-for-webvtt-region-viewport-anchor-5) [(4)](#ref-for-webvtt-region-viewport-anchor-6) [(5)](#ref-for-webvtt-region-viewport-anchor-7) [(6)](#ref-for-webvtt-region-viewport-anchor-8)

**[#webvtt-region-scroll](#webvtt-region-scroll)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-scroll-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-scroll-2)
-   [7.1. Processing model](#ref-for-webvtt-region-scroll-3)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-scroll-4) [(2)](#ref-for-webvtt-region-scroll-5) [(3)](#ref-for-webvtt-region-scroll-6) [(4)](#ref-for-webvtt-region-scroll-7) [(5)](#ref-for-webvtt-region-scroll-8)

**[#webvtt-region-scroll-none](#webvtt-region-scroll-none)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-scroll-none-1)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-scroll-none-2)

**[#webvtt-region-scroll-up](#webvtt-region-scroll-up)Referenced in:**

-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-scroll-up-1)
-   [7.1. Processing model](#ref-for-webvtt-region-scroll-up-2)
-   [9.2. The VTTRegion interface](#ref-for-webvtt-region-scroll-up-3)

**[#text-track-list-of-regions](#text-track-list-of-regions)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-text-track-list-of-regions-1)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-text-track-list-of-regions-2) [(2)](#ref-for-text-track-list-of-regions-3)
-   [7.1. Processing model](#ref-for-text-track-list-of-regions-4)

**[#webvtt-file](#webvtt-file)Referenced in:**

-   [2.1. Conformance classes](#ref-for-webvtt-file-1) [(2)](#ref-for-webvtt-file-2) [(3)](#ref-for-webvtt-file-3) [(4)](#ref-for-webvtt-file-4) [(5)](#ref-for-webvtt-file-5) [(6)](#ref-for-webvtt-file-6)
-   [4.1. WebVTT file structure](#ref-for-webvtt-file-7) [(2)](#ref-for-webvtt-file-8)
-   [4.3. WebVTT region settings](#ref-for-webvtt-file-9)
-   [4.5.1. WebVTT file using only nested cues](#ref-for-webvtt-file-10)
-   [4.6. Types of WebVTT files](#ref-for-webvtt-file-11)
-   [4.6.1. WebVTT file using metadata content](#ref-for-webvtt-file-12)
-   [4.6.3. WebVTT file using caption or subtitle cue text](#ref-for-webvtt-file-13)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-file-14) [(2)](#ref-for-webvtt-file-15) [(3)](#ref-for-webvtt-file-16)

**[#webvtt-file-body](#webvtt-file-body)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-file-body-1)

**[#webvtt-line-terminator](#webvtt-line-terminator)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-line-terminator-1) [(2)](#ref-for-webvtt-line-terminator-2) [(3)](#ref-for-webvtt-line-terminator-3) [(4)](#ref-for-webvtt-line-terminator-4) [(5)](#ref-for-webvtt-line-terminator-5) [(6)](#ref-for-webvtt-line-terminator-6) [(7)](#ref-for-webvtt-line-terminator-7) [(8)](#ref-for-webvtt-line-terminator-8) [(9)](#ref-for-webvtt-line-terminator-9) [(10)](#ref-for-webvtt-line-terminator-10) [(11)](#ref-for-webvtt-line-terminator-11) [(12)](#ref-for-webvtt-line-terminator-12) [(13)](#ref-for-webvtt-line-terminator-13) [(14)](#ref-for-webvtt-line-terminator-14) [(15)](#ref-for-webvtt-line-terminator-15) [(16)](#ref-for-webvtt-line-terminator-16)
-   [4.2.1. WebVTT metadata text](#ref-for-webvtt-line-terminator-17) [(2)](#ref-for-webvtt-line-terminator-18) [(3)](#ref-for-webvtt-line-terminator-19)
-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-line-terminator-20) [(2)](#ref-for-webvtt-line-terminator-21) [(3)](#ref-for-webvtt-line-terminator-22) [(4)](#ref-for-webvtt-line-terminator-23) [(5)](#ref-for-webvtt-line-terminator-24)
-   [4.2.3. WebVTT chapter title text](#ref-for-webvtt-line-terminator-25)
-   [4.3. WebVTT region settings](#ref-for-webvtt-line-terminator-26) [(2)](#ref-for-webvtt-line-terminator-27)

**[#webvtt-region-definition-block](#webvtt-region-definition-block)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-region-definition-block-1)
-   [4.3. WebVTT region settings](#ref-for-webvtt-region-definition-block-2)

**[#webvtt-style-block](#webvtt-style-block)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-style-block-1)

**[#webvtt-cue-block](#webvtt-cue-block)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-block-1) [(2)](#ref-for-webvtt-cue-block-2) [(3)](#ref-for-webvtt-cue-block-3) [(4)](#ref-for-webvtt-cue-block-4)

**[#cue-payload](#cue-payload)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-cue-payload-1)
-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-cue-payload-2)
-   [4.6.1. WebVTT file using metadata content](#ref-for-cue-payload-3)
-   [4.6.2. WebVTT file using chapter title text](#ref-for-cue-payload-4)
-   [4.6.3. WebVTT file using caption or subtitle cue text](#ref-for-cue-payload-5)

**[#webvtt-cue-identifier](#webvtt-cue-identifier)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-identifier-1) [(2)](#ref-for-webvtt-cue-identifier-2) [(3)](#ref-for-webvtt-cue-identifier-3) [(4)](#ref-for-webvtt-cue-identifier-4)

**[#webvtt-cue-timings](#webvtt-cue-timings)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-timings-1) [(2)](#ref-for-webvtt-cue-timings-2)

**[#webvtt-timestamp](#webvtt-timestamp)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-timestamp-1) [(2)](#ref-for-webvtt-timestamp-2) [(3)](#ref-for-webvtt-timestamp-3) [(4)](#ref-for-webvtt-timestamp-4) [(5)](#ref-for-webvtt-timestamp-5)
-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-timestamp-6) [(2)](#ref-for-webvtt-timestamp-7)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-timestamp-8)

**[#webvtt-cue-settings-list](#webvtt-cue-settings-list)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-settings-list-1)
-   [4.3. WebVTT region settings](#ref-for-webvtt-cue-settings-list-2) [(2)](#ref-for-webvtt-cue-settings-list-3)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-settings-list-4) [(2)](#ref-for-webvtt-cue-settings-list-5) [(3)](#ref-for-webvtt-cue-settings-list-6)

**[#webvtt-cue-setting](#webvtt-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-setting-1) [(2)](#ref-for-webvtt-cue-setting-2) [(3)](#ref-for-webvtt-cue-setting-3)

**[#webvtt-cue-setting-name](#webvtt-cue-setting-name)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-setting-name-1)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-setting-name-2) [(2)](#ref-for-webvtt-cue-setting-name-3) [(3)](#ref-for-webvtt-cue-setting-name-4) [(4)](#ref-for-webvtt-cue-setting-name-5) [(5)](#ref-for-webvtt-cue-setting-name-6) [(6)](#ref-for-webvtt-cue-setting-name-7)

**[#webvtt-cue-setting-value](#webvtt-cue-setting-value)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-cue-setting-value-1)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-cue-setting-value-2) [(2)](#ref-for-webvtt-cue-setting-value-3) [(3)](#ref-for-webvtt-cue-setting-value-4) [(4)](#ref-for-webvtt-cue-setting-value-5) [(5)](#ref-for-webvtt-cue-setting-value-6) [(6)](#ref-for-webvtt-cue-setting-value-7)

**[#webvtt-percentage](#webvtt-percentage)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-percentage-1)
-   [4.3. WebVTT region settings](#ref-for-webvtt-percentage-2) [(2)](#ref-for-webvtt-percentage-3) [(3)](#ref-for-webvtt-percentage-4) [(4)](#ref-for-webvtt-percentage-5) [(5)](#ref-for-webvtt-percentage-6)
-   [4.4. WebVTT cue settings](#ref-for-webvtt-percentage-7) [(2)](#ref-for-webvtt-percentage-8) [(3)](#ref-for-webvtt-percentage-9)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-percentage-10)

**[#webvtt-comment-block](#webvtt-comment-block)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-comment-block-1) [(2)](#ref-for-webvtt-comment-block-2) [(3)](#ref-for-webvtt-comment-block-3)

**[#webvtt-metadata-text](#webvtt-metadata-text)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-metadata-text-1)
-   [4.2.1. WebVTT metadata text](#ref-for-webvtt-metadata-text-2)
-   [4.6.1. WebVTT file using metadata content](#ref-for-webvtt-metadata-text-3)

**[#webvtt-caption-or-subtitle-cue-text](#webvtt-caption-or-subtitle-cue-text)Referenced in:**

-   [2.1. Conformance classes](#ref-for-webvtt-caption-or-subtitle-cue-text-1)
-   [4.1. WebVTT file structure](#ref-for-webvtt-caption-or-subtitle-cue-text-2)
-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-caption-or-subtitle-cue-text-3)
-   [4.6.3. WebVTT file using caption or subtitle cue text](#ref-for-webvtt-caption-or-subtitle-cue-text-4)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-caption-or-subtitle-cue-text-5) [(2)](#ref-for-webvtt-caption-or-subtitle-cue-text-6) [(3)](#ref-for-webvtt-caption-or-subtitle-cue-text-7) [(4)](#ref-for-webvtt-caption-or-subtitle-cue-text-8) [(5)](#ref-for-webvtt-caption-or-subtitle-cue-text-9) [(6)](#ref-for-webvtt-caption-or-subtitle-cue-text-10) [(7)](#ref-for-webvtt-caption-or-subtitle-cue-text-11) [(8)](#ref-for-webvtt-caption-or-subtitle-cue-text-12)

**[#webvtt-caption-or-subtitle-cue-components](#webvtt-caption-or-subtitle-cue-components)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-caption-or-subtitle-cue-components-1) [(2)](#ref-for-webvtt-caption-or-subtitle-cue-components-2) [(3)](#ref-for-webvtt-caption-or-subtitle-cue-components-3) [(4)](#ref-for-webvtt-caption-or-subtitle-cue-components-4)
-   [5. Default classes for WebVTT Caption or Subtitle Cue Components](#ref-for-webvtt-caption-or-subtitle-cue-components-5)
-   [5.1. Default text colors](#ref-for-webvtt-caption-or-subtitle-cue-components-6)
-   [5.2. Default text background colors](#ref-for-webvtt-caption-or-subtitle-cue-components-7)

**[#cue-component-class-names](#cue-component-class-names)Referenced in:**

-   [5. Default classes for WebVTT Caption or Subtitle Cue Components](#ref-for-cue-component-class-names-1)
-   [5.1. Default text colors](#ref-for-cue-component-class-names-2) [(2)](#ref-for-cue-component-class-names-3)
-   [5.2. Default text background colors](#ref-for-cue-component-class-names-4) [(2)](#ref-for-cue-component-class-names-5)
-   [6.4. WebVTT cue text parsing rules](#ref-for-cue-component-class-names-6)

**[#webvtt-cue-internal-text](#webvtt-cue-internal-text)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-internal-text-1) [(2)](#ref-for-webvtt-cue-internal-text-2) [(3)](#ref-for-webvtt-cue-internal-text-3) [(4)](#ref-for-webvtt-cue-internal-text-4) [(5)](#ref-for-webvtt-cue-internal-text-5) [(6)](#ref-for-webvtt-cue-internal-text-6) [(7)](#ref-for-webvtt-cue-internal-text-7) [(8)](#ref-for-webvtt-cue-internal-text-8)

**[#webvtt-cue-class-span](#webvtt-cue-class-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-class-span-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-class-span-2)

**[#webvtt-cue-italics-span](#webvtt-cue-italics-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-italics-span-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-italics-span-2)

**[#webvtt-cue-bold-span](#webvtt-cue-bold-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-bold-span-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-bold-span-2)

**[#webvtt-cue-underline-span](#webvtt-cue-underline-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-underline-span-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-underline-span-2)

**[#webvtt-cue-ruby-span](#webvtt-cue-ruby-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-ruby-span-1) [(2)](#ref-for-webvtt-cue-ruby-span-2)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-ruby-span-3)

**[#webvtt-cue-ruby-text-span](#webvtt-cue-ruby-text-span)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-ruby-text-span-1)

**[#webvtt-cue-voice-span](#webvtt-cue-voice-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-voice-span-1) [(2)](#ref-for-webvtt-cue-voice-span-2)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-voice-span-3)

**[#webvtt-cue-language-span](#webvtt-cue-language-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-language-span-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-language-span-2)

**[#webvtt-cue-span-start-tag](#webvtt-cue-span-start-tag)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-span-start-tag-1) [(2)](#ref-for-webvtt-cue-span-start-tag-2) [(3)](#ref-for-webvtt-cue-span-start-tag-3) [(4)](#ref-for-webvtt-cue-span-start-tag-4) [(5)](#ref-for-webvtt-cue-span-start-tag-5) [(6)](#ref-for-webvtt-cue-span-start-tag-6) [(7)](#ref-for-webvtt-cue-span-start-tag-7) [(8)](#ref-for-webvtt-cue-span-start-tag-8)

**[#webvtt-cue-span-end-tag](#webvtt-cue-span-end-tag)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-span-end-tag-1) [(2)](#ref-for-webvtt-cue-span-end-tag-2) [(3)](#ref-for-webvtt-cue-span-end-tag-3) [(4)](#ref-for-webvtt-cue-span-end-tag-4) [(5)](#ref-for-webvtt-cue-span-end-tag-5) [(6)](#ref-for-webvtt-cue-span-end-tag-6) [(7)](#ref-for-webvtt-cue-span-end-tag-7) [(8)](#ref-for-webvtt-cue-span-end-tag-8)

**[#webvtt-cue-timestamp](#webvtt-cue-timestamp)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-timestamp-1) [(2)](#ref-for-webvtt-cue-timestamp-2)

**[#webvtt-cue-text-span](#webvtt-cue-text-span)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-text-span-1)
-   [4.2.3. WebVTT chapter title text](#ref-for-webvtt-cue-text-span-2)

**[#webvtt-cue-span-start-tag-annotation-text](#webvtt-cue-span-start-tag-annotation-text)Referenced in:**

-   [4.2.2. WebVTT caption or subtitle cue text](#ref-for-webvtt-cue-span-start-tag-annotation-text-1)

**[#webvtt-chapter-title-text](#webvtt-chapter-title-text)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-chapter-title-text-1)
-   [4.6.2. WebVTT file using chapter title text](#ref-for-webvtt-chapter-title-text-2)

**[#webvtt-region-settings-list](#webvtt-region-settings-list)Referenced in:**

-   [4.1. WebVTT file structure](#ref-for-webvtt-region-settings-list-1)
-   [4.3. WebVTT region settings](#ref-for-webvtt-region-settings-list-2) [(2)](#ref-for-webvtt-region-settings-list-3)

**[#webvtt-region-identifier-setting](#webvtt-region-identifier-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-identifier-setting-1) [(2)](#ref-for-webvtt-region-identifier-setting-2) [(3)](#ref-for-webvtt-region-identifier-setting-3) [(4)](#ref-for-webvtt-region-identifier-setting-4) [(5)](#ref-for-webvtt-region-identifier-setting-5)

**[#webvtt-region-width-setting](#webvtt-region-width-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-width-setting-1) [(2)](#ref-for-webvtt-region-width-setting-2)

**[#webvtt-region-lines-setting](#webvtt-region-lines-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-lines-setting-1) [(2)](#ref-for-webvtt-region-lines-setting-2)

**[#webvtt-region-anchor-setting](#webvtt-region-anchor-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-anchor-setting-1) [(2)](#ref-for-webvtt-region-anchor-setting-2) [(3)](#ref-for-webvtt-region-anchor-setting-3)

**[#webvtt-region-viewport-anchor-setting](#webvtt-region-viewport-anchor-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-viewport-anchor-setting-1) [(2)](#ref-for-webvtt-region-viewport-anchor-setting-2)

**[#webvtt-region-scroll-setting](#webvtt-region-scroll-setting)Referenced in:**

-   [4.3. WebVTT region settings](#ref-for-webvtt-region-scroll-setting-1) [(2)](#ref-for-webvtt-region-scroll-setting-2)

**[#webvtt-vertical-text-cue-setting](#webvtt-vertical-text-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-vertical-text-cue-setting-1) [(2)](#ref-for-webvtt-vertical-text-cue-setting-2) [(3)](#ref-for-webvtt-vertical-text-cue-setting-3)

**[#webvtt-line-cue-setting](#webvtt-line-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-line-cue-setting-1) [(2)](#ref-for-webvtt-line-cue-setting-2) [(3)](#ref-for-webvtt-line-cue-setting-3) [(4)](#ref-for-webvtt-line-cue-setting-4)

**[#webvtt-position-cue-setting](#webvtt-position-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-position-cue-setting-1) [(2)](#ref-for-webvtt-position-cue-setting-2) [(3)](#ref-for-webvtt-position-cue-setting-3) [(4)](#ref-for-webvtt-position-cue-setting-4) [(5)](#ref-for-webvtt-position-cue-setting-5)

**[#webvtt-size-cue-setting](#webvtt-size-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-size-cue-setting-1) [(2)](#ref-for-webvtt-size-cue-setting-2) [(3)](#ref-for-webvtt-size-cue-setting-3)

**[#webvtt-alignment-cue-setting](#webvtt-alignment-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-alignment-cue-setting-1) [(2)](#ref-for-webvtt-alignment-cue-setting-2) [(3)](#ref-for-webvtt-alignment-cue-setting-3)

**[#webvtt-region-cue-setting](#webvtt-region-cue-setting)Referenced in:**

-   [4.4. WebVTT cue settings](#ref-for-webvtt-region-cue-setting-1) [(2)](#ref-for-webvtt-region-cue-setting-2)

**[#webvtt-file-using-only-nested-cues](#webvtt-file-using-only-nested-cues)Referenced in:**

-   [4.5.1. WebVTT file using only nested cues](#ref-for-webvtt-file-using-only-nested-cues-1) [(2)](#ref-for-webvtt-file-using-only-nested-cues-2)
-   [4.6.2. WebVTT file using chapter title text](#ref-for-webvtt-file-using-only-nested-cues-3)

**[#webvtt-parser](#webvtt-parser)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-webvtt-parser-1)
-   [6.1. WebVTT file parsing](#ref-for-webvtt-parser-2) [(2)](#ref-for-webvtt-parser-3) [(3)](#ref-for-webvtt-parser-4)

**[#incremental-webvtt-parser](#incremental-webvtt-parser)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-incremental-webvtt-parser-1)

**[#webvtt-parser-algorithm](#webvtt-parser-algorithm)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-parser-algorithm-1)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-parser-algorithm-2)

**[#collect-a-webvtt-block](#collect-a-webvtt-block)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-collect-a-webvtt-block-1) [(2)](#ref-for-collect-a-webvtt-block-2)

**[#collect-webvtt-region-settings](#collect-webvtt-region-settings)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-collect-webvtt-region-settings-1)

**[#webvtt-region-object](#webvtt-region-object)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-webvtt-region-object-1) [(2)](#ref-for-webvtt-region-object-2)
-   [6.2. WebVTT region settings parsing](#ref-for-webvtt-region-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-region-object-4)
-   [7.1. Processing model](#ref-for-webvtt-region-object-5)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-region-object-6) [(2)](#ref-for-webvtt-region-object-7) [(3)](#ref-for-webvtt-region-object-8) [(4)](#ref-for-webvtt-region-object-9)
-   [8.1. Introduction](#ref-for-webvtt-region-object-10) [(2)](#ref-for-webvtt-region-object-11)
-   [8.2.3. The ::cue-region pseudo-element](#ref-for-webvtt-region-object-12) [(2)](#ref-for-webvtt-region-object-13) [(3)](#ref-for-webvtt-region-object-14) [(4)](#ref-for-webvtt-region-object-15)

**[#parse-a-percentage-string](#parse-a-percentage-string)Referenced in:**

-   [6.2. WebVTT region settings parsing](#ref-for-parse-a-percentage-string-1) [(2)](#ref-for-parse-a-percentage-string-2) [(3)](#ref-for-parse-a-percentage-string-3) [(4)](#ref-for-parse-a-percentage-string-4) [(5)](#ref-for-parse-a-percentage-string-5)
-   [6.3. WebVTT cue timings and settings parsing](#ref-for-parse-a-percentage-string-6) [(2)](#ref-for-parse-a-percentage-string-7) [(3)](#ref-for-parse-a-percentage-string-8)

**[#collect-webvtt-cue-timings-and-settings](#collect-webvtt-cue-timings-and-settings)Referenced in:**

-   [6.1. WebVTT file parsing](#ref-for-collect-webvtt-cue-timings-and-settings-1)

**[#parse-the-webvtt-cue-settings](#parse-the-webvtt-cue-settings)Referenced in:**

-   [6.3. WebVTT cue timings and settings parsing](#ref-for-parse-the-webvtt-cue-settings-1)

**[#collect-a-webvtt-timestamp](#collect-a-webvtt-timestamp)Referenced in:**

-   [6.3. WebVTT cue timings and settings parsing](#ref-for-collect-a-webvtt-timestamp-1) [(2)](#ref-for-collect-a-webvtt-timestamp-2)
-   [6.4. WebVTT cue text parsing rules](#ref-for-collect-a-webvtt-timestamp-3)

**[#webvtt-node-object](#webvtt-node-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-node-object-1) [(2)](#ref-for-webvtt-node-object-2) [(3)](#ref-for-webvtt-node-object-3) [(4)](#ref-for-webvtt-node-object-4) [(5)](#ref-for-webvtt-node-object-5)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-node-object-6) [(2)](#ref-for-webvtt-node-object-7) [(3)](#ref-for-webvtt-node-object-8)
-   [7.3. Obtaining CSS boxes](#ref-for-webvtt-node-object-9) [(2)](#ref-for-webvtt-node-object-10)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-node-object-11) [(2)](#ref-for-webvtt-node-object-12)
-   [8.2. Processing model](#ref-for-webvtt-node-object-13) [(2)](#ref-for-webvtt-node-object-14)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-node-object-15)
-   [8.2.2. The :past and :future pseudo-classes](#ref-for-webvtt-node-object-16) [(2)](#ref-for-webvtt-node-object-17) [(3)](#ref-for-webvtt-node-object-18) [(4)](#ref-for-webvtt-node-object-19) [(5)](#ref-for-webvtt-node-object-20) [(6)](#ref-for-webvtt-node-object-21) [(7)](#ref-for-webvtt-node-object-22)

**[#webvtt-internal-node-object](#webvtt-internal-node-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-internal-node-object-1) [(2)](#ref-for-webvtt-internal-node-object-2) [(3)](#ref-for-webvtt-internal-node-object-3) [(4)](#ref-for-webvtt-internal-node-object-4) [(5)](#ref-for-webvtt-internal-node-object-5) [(6)](#ref-for-webvtt-internal-node-object-6) [(7)](#ref-for-webvtt-internal-node-object-7)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-internal-node-object-8)
-   [7.3. Obtaining CSS boxes](#ref-for-webvtt-internal-node-object-9)
-   [8.1. Introduction](#ref-for-webvtt-internal-node-object-10) [(2)](#ref-for-webvtt-internal-node-object-11) [(3)](#ref-for-webvtt-internal-node-object-12) [(4)](#ref-for-webvtt-internal-node-object-13) [(5)](#ref-for-webvtt-internal-node-object-14)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-internal-node-object-15) [(2)](#ref-for-webvtt-internal-node-object-16) [(3)](#ref-for-webvtt-internal-node-object-17) [(4)](#ref-for-webvtt-internal-node-object-18) [(5)](#ref-for-webvtt-internal-node-object-19) [(6)](#ref-for-webvtt-internal-node-object-20) [(7)](#ref-for-webvtt-internal-node-object-21)

**[#webvtt-node-objects-applicable-classes](#webvtt-node-objects-applicable-classes)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-node-objects-applicable-classes-1) [(2)](#ref-for-webvtt-node-objects-applicable-classes-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-node-objects-applicable-classes-3)
-   [8.1. Introduction](#ref-for-webvtt-node-objects-applicable-classes-4)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-node-objects-applicable-classes-5)

**[#webvtt-node-objects-applicable-language](#webvtt-node-objects-applicable-language)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-node-objects-applicable-language-1) [(2)](#ref-for-webvtt-node-objects-applicable-language-2) [(3)](#ref-for-webvtt-node-objects-applicable-language-3) [(4)](#ref-for-webvtt-node-objects-applicable-language-4)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-node-objects-applicable-language-5)
-   [8.1. Introduction](#ref-for-webvtt-node-objects-applicable-language-6) [(2)](#ref-for-webvtt-node-objects-applicable-language-7) [(3)](#ref-for-webvtt-node-objects-applicable-language-8) [(4)](#ref-for-webvtt-node-objects-applicable-language-9)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-node-objects-applicable-language-10) [(2)](#ref-for-webvtt-node-objects-applicable-language-11) [(3)](#ref-for-webvtt-node-objects-applicable-language-12) [(4)](#ref-for-webvtt-node-objects-applicable-language-13)

**[#list-of-webvtt-node-objects](#list-of-webvtt-node-objects)Referenced in:**

-   [6.2. WebVTT region settings parsing](#ref-for-list-of-webvtt-node-objects-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-list-of-webvtt-node-objects-2) [(2)](#ref-for-list-of-webvtt-node-objects-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-list-of-webvtt-node-objects-4) [(2)](#ref-for-list-of-webvtt-node-objects-5)
-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-list-of-webvtt-node-objects-6)
-   [7.1. Processing model](#ref-for-list-of-webvtt-node-objects-7)
-   [7.2. Processing cue settings](#ref-for-list-of-webvtt-node-objects-8)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-list-of-webvtt-node-objects-9) [(2)](#ref-for-list-of-webvtt-node-objects-10) [(3)](#ref-for-list-of-webvtt-node-objects-11) [(4)](#ref-for-list-of-webvtt-node-objects-12) [(5)](#ref-for-list-of-webvtt-node-objects-13) [(6)](#ref-for-list-of-webvtt-node-objects-14) [(7)](#ref-for-list-of-webvtt-node-objects-15) [(8)](#ref-for-list-of-webvtt-node-objects-16) [(9)](#ref-for-list-of-webvtt-node-objects-17)
-   [8.1. Introduction](#ref-for-list-of-webvtt-node-objects-18) [(2)](#ref-for-list-of-webvtt-node-objects-19) [(3)](#ref-for-list-of-webvtt-node-objects-20) [(4)](#ref-for-list-of-webvtt-node-objects-21) [(5)](#ref-for-list-of-webvtt-node-objects-22) [(6)](#ref-for-list-of-webvtt-node-objects-23) [(7)](#ref-for-list-of-webvtt-node-objects-24)
-   [8.2. Processing model](#ref-for-list-of-webvtt-node-objects-25)
-   [8.2.1. The ::cue pseudo-element](#ref-for-list-of-webvtt-node-objects-26) [(2)](#ref-for-list-of-webvtt-node-objects-27) [(3)](#ref-for-list-of-webvtt-node-objects-28) [(4)](#ref-for-list-of-webvtt-node-objects-29) [(5)](#ref-for-list-of-webvtt-node-objects-30) [(6)](#ref-for-list-of-webvtt-node-objects-31) [(7)](#ref-for-list-of-webvtt-node-objects-32)
-   [8.2.2. The :past and :future pseudo-classes](#ref-for-list-of-webvtt-node-objects-33) [(2)](#ref-for-list-of-webvtt-node-objects-34)

**[#webvtt-class-object](#webvtt-class-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-class-object-1) [(2)](#ref-for-webvtt-class-object-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-class-object-3)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-class-object-4)

**[#webvtt-italic-object](#webvtt-italic-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-italic-object-1) [(2)](#ref-for-webvtt-italic-object-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-italic-object-3)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-italic-object-4)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-italic-object-5)

**[#webvtt-bold-object](#webvtt-bold-object)Referenced in:**

-   [1.3. Styling captions](#ref-for-webvtt-bold-object-1)
-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-bold-object-2) [(2)](#ref-for-webvtt-bold-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-bold-object-4)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-bold-object-5)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-bold-object-6)

**[#webvtt-underline-object](#webvtt-underline-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-underline-object-1) [(2)](#ref-for-webvtt-underline-object-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-underline-object-3)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-underline-object-4)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-underline-object-5)

**[#webvtt-ruby-object](#webvtt-ruby-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-ruby-object-1) [(2)](#ref-for-webvtt-ruby-object-2) [(3)](#ref-for-webvtt-ruby-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-ruby-object-4)
-   [7.3. Obtaining CSS boxes](#ref-for-webvtt-ruby-object-5)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-ruby-object-6)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-ruby-object-7)

**[#webvtt-ruby-text-object](#webvtt-ruby-text-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-ruby-text-object-1) [(2)](#ref-for-webvtt-ruby-text-object-2) [(3)](#ref-for-webvtt-ruby-text-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-ruby-text-object-4)
-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-webvtt-ruby-text-object-5)
-   [7.3. Obtaining CSS boxes](#ref-for-webvtt-ruby-text-object-6)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-ruby-text-object-7) [(2)](#ref-for-webvtt-ruby-text-object-8)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-ruby-text-object-9)

**[#webvtt-voice-object](#webvtt-voice-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-voice-object-1) [(2)](#ref-for-webvtt-voice-object-2) [(3)](#ref-for-webvtt-voice-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-voice-object-4) [(2)](#ref-for-webvtt-voice-object-5)
-   [8.1. Introduction](#ref-for-webvtt-voice-object-6)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-voice-object-7) [(2)](#ref-for-webvtt-voice-object-8) [(3)](#ref-for-webvtt-voice-object-9)

**[#webvtt-language-object](#webvtt-language-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-language-object-1) [(2)](#ref-for-webvtt-language-object-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-language-object-3) [(2)](#ref-for-webvtt-language-object-4)
-   [8.1. Introduction](#ref-for-webvtt-language-object-5)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-language-object-6) [(2)](#ref-for-webvtt-language-object-7)

**[#webvtt-leaf-node-object](#webvtt-leaf-node-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-leaf-node-object-1) [(2)](#ref-for-webvtt-leaf-node-object-2)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-leaf-node-object-3)

**[#webvtt-text-object](#webvtt-text-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-text-object-1) [(2)](#ref-for-webvtt-text-object-2) [(3)](#ref-for-webvtt-text-object-3)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-text-object-4) [(2)](#ref-for-webvtt-text-object-5)
-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-webvtt-text-object-6)
-   [7.3. Obtaining CSS boxes](#ref-for-webvtt-text-object-7)

**[#webvtt-timestamp-object](#webvtt-timestamp-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-timestamp-object-1) [(2)](#ref-for-webvtt-timestamp-object-2)
-   [6.5. WebVTT cue text DOM construction rules](#ref-for-webvtt-timestamp-object-3) [(2)](#ref-for-webvtt-timestamp-object-4)
-   [8.1. Introduction](#ref-for-webvtt-timestamp-object-5)
-   [8.2.2. The :past and :future pseudo-classes](#ref-for-webvtt-timestamp-object-6) [(2)](#ref-for-webvtt-timestamp-object-7)

**[#webvtt-cue-text-parsing-rules](#webvtt-cue-text-parsing-rules)Referenced in:**

-   [6.6. WebVTT rules for extracting the chapter title](#ref-for-webvtt-cue-text-parsing-rules-1)
-   [7.1. Processing model](#ref-for-webvtt-cue-text-parsing-rules-2)
-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-text-parsing-rules-3)

**[#attach-a-webvtt-internal-node-object](#attach-a-webvtt-internal-node-object)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-attach-a-webvtt-internal-node-object-1) [(2)](#ref-for-attach-a-webvtt-internal-node-object-2) [(3)](#ref-for-attach-a-webvtt-internal-node-object-3) [(4)](#ref-for-attach-a-webvtt-internal-node-object-4) [(5)](#ref-for-attach-a-webvtt-internal-node-object-5) [(6)](#ref-for-attach-a-webvtt-internal-node-object-6) [(7)](#ref-for-attach-a-webvtt-internal-node-object-7) [(8)](#ref-for-attach-a-webvtt-internal-node-object-8)

**[#webvtt-cue-text-tokenizer](#webvtt-cue-text-tokenizer)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-cue-text-tokenizer-1)

**[#webvtt-data-state](#webvtt-data-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-data-state-1) [(2)](#ref-for-webvtt-data-state-2)

**[#html-character-reference-in-data-state](#html-character-reference-in-data-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-html-character-reference-in-data-state-1)

**[#webvtt-tag-state](#webvtt-tag-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-tag-state-1)

**[#webvtt-start-tag-state](#webvtt-start-tag-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-start-tag-state-1)

**[#webvtt-start-tag-class-state](#webvtt-start-tag-class-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-start-tag-class-state-1) [(2)](#ref-for-webvtt-start-tag-class-state-2)

**[#webvtt-start-tag-annotation-state](#webvtt-start-tag-annotation-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-start-tag-annotation-state-1) [(2)](#ref-for-webvtt-start-tag-annotation-state-2) [(3)](#ref-for-webvtt-start-tag-annotation-state-3) [(4)](#ref-for-webvtt-start-tag-annotation-state-4) [(5)](#ref-for-webvtt-start-tag-annotation-state-5) [(6)](#ref-for-webvtt-start-tag-annotation-state-6)

**[#html-character-reference-in-annotation-state](#html-character-reference-in-annotation-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-html-character-reference-in-annotation-state-1)

**[#webvtt-end-tag-state](#webvtt-end-tag-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-end-tag-state-1)

**[#webvtt-timestamp-tag-state](#webvtt-timestamp-tag-state)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-webvtt-timestamp-tag-state-1)

**[#consume-an-html-character-reference](#consume-an-html-character-reference)Referenced in:**

-   [6.4. WebVTT cue text parsing rules](#ref-for-consume-an-html-character-reference-1) [(2)](#ref-for-consume-an-html-character-reference-2)

**[#webvtt-cue-text-dom-construction-rules](#webvtt-cue-text-dom-construction-rules)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-webvtt-cue-text-dom-construction-rules-1)

**[#webvtt-rules-for-extracting-the-chapter-title](#webvtt-rules-for-extracting-the-chapter-title)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-webvtt-rules-for-extracting-the-chapter-title-1)

**[#rules-for-updating-the-display-of-webvtt-text-tracks](#rules-for-updating-the-display-of-webvtt-text-tracks)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-1) [(2)](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-2)
-   [7.1. Processing model](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-3)
-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-4) [(2)](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-5) [(3)](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-6)
-   [8.2. Processing model](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-7) [(2)](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-8)
-   [8.2.3. The ::cue-region pseudo-element](#ref-for-rules-for-updating-the-display-of-webvtt-text-tracks-9)

**[#apply-webvtt-cue-settings](#apply-webvtt-cue-settings)Referenced in:**

-   [7.1. Processing model](#ref-for-apply-webvtt-cue-settings-1)

**[#obtain-a-set-of-css-boxes](#obtain-a-set-of-css-boxes)Referenced in:**

-   [7.1. Processing model](#ref-for-obtain-a-set-of-css-boxes-1)
-   [7.2. Processing cue settings](#ref-for-obtain-a-set-of-css-boxes-2)

**[#webvtt-cue-background-box](#webvtt-cue-background-box)Referenced in:**

-   [7.4. Applying CSS properties to WebVTT Node Objects](#ref-for-webvtt-cue-background-box-1)
-   [8.2.1. The ::cue pseudo-element](#ref-for-webvtt-cue-background-box-2) [(2)](#ref-for-webvtt-cue-background-box-3)

**[#enumdef-autokeyword](#enumdef-autokeyword)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-enumdef-autokeyword-1)

**[#typedefdef-lineandpositionsetting](#typedefdef-lineandpositionsetting)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-typedefdef-lineandpositionsetting-1) [(2)](#ref-for-typedefdef-lineandpositionsetting-2)

**[#enumdef-directionsetting](#enumdef-directionsetting)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-enumdef-directionsetting-1)

**[#enumdef-linealignsetting](#enumdef-linealignsetting)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-enumdef-linealignsetting-1)

**[#enumdef-positionalignsetting](#enumdef-positionalignsetting)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-enumdef-positionalignsetting-1)

**[#enumdef-alignsetting](#enumdef-alignsetting)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-enumdef-alignsetting-1)

**[#vttcue](#vttcue)Referenced in:**

-   [6.5. WebVTT cue text DOM construction rules](#ref-for-vttcue-1)
-   [9.1. The VTTCue interface](#ref-for-vttcue-2) [(2)](#ref-for-vttcue-3) [(3)](#ref-for-vttcue-4) [(4)](#ref-for-vttcue-5) [(5)](#ref-for-vttcue-6) [(6)](#ref-for-vttcue-7) [(7)](#ref-for-vttcue-8) [(8)](#ref-for-vttcue-9) [(9)](#ref-for-vttcue-10) [(10)](#ref-for-vttcue-11) [(11)](#ref-for-vttcue-12) [(12)](#ref-for-vttcue-13) [(13)](#ref-for-vttcue-14)

**[#dom-vttcue-vttcue](#dom-vttcue-vttcue)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-vttcue-1) [(2)](#ref-for-dom-vttcue-vttcue-2)

**[#dom-vttcue-region](#dom-vttcue-region)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-region-1) [(2)](#ref-for-dom-vttcue-region-2)

**[#dom-vttcue-vertical](#dom-vttcue-vertical)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-vertical-1) [(2)](#ref-for-dom-vttcue-vertical-2) [(3)](#ref-for-dom-vttcue-vertical-3)

**[#dom-vttcue-snaptolines](#dom-vttcue-snaptolines)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-dom-vttcue-snaptolines-1)
-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-snaptolines-2) [(2)](#ref-for-dom-vttcue-snaptolines-3) [(3)](#ref-for-dom-vttcue-snaptolines-4) [(4)](#ref-for-dom-vttcue-snaptolines-5)

**[#dom-vttcue-line](#dom-vttcue-line)Referenced in:**

-   [3.3. WebVTT caption or subtitle cues](#ref-for-dom-vttcue-line-1)
-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-line-2) [(2)](#ref-for-dom-vttcue-line-3) [(3)](#ref-for-dom-vttcue-line-4) [(4)](#ref-for-dom-vttcue-line-5)

**[#dom-vttcue-linealign](#dom-vttcue-linealign)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-linealign-1) [(2)](#ref-for-dom-vttcue-linealign-2) [(3)](#ref-for-dom-vttcue-linealign-3)

**[#dom-vttcue-position](#dom-vttcue-position)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-position-1) [(2)](#ref-for-dom-vttcue-position-2)

**[#dom-vttcue-positionalign](#dom-vttcue-positionalign)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-positionalign-1) [(2)](#ref-for-dom-vttcue-positionalign-2) [(3)](#ref-for-dom-vttcue-positionalign-3)

**[#dom-vttcue-size](#dom-vttcue-size)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-size-1) [(2)](#ref-for-dom-vttcue-size-2)

**[#dom-vttcue-align](#dom-vttcue-align)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-align-1) [(2)](#ref-for-dom-vttcue-align-2) [(3)](#ref-for-dom-vttcue-align-3)

**[#dom-vttcue-text](#dom-vttcue-text)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-text-1) [(2)](#ref-for-dom-vttcue-text-2)

**[#dom-vttcue-getcueashtml](#dom-vttcue-getcueashtml)Referenced in:**

-   [6.5. WebVTT cue text DOM construction rules](#ref-for-dom-vttcue-getcueashtml-1)
-   [9.1. The VTTCue interface](#ref-for-dom-vttcue-getcueashtml-2) [(2)](#ref-for-dom-vttcue-getcueashtml-3) [(3)](#ref-for-dom-vttcue-getcueashtml-4)

**[#enumdef-scrollsetting](#enumdef-scrollsetting)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-enumdef-scrollsetting-1)

**[#vttregion](#vttregion)Referenced in:**

-   [9.1. The VTTCue interface](#ref-for-vttregion-1) [(2)](#ref-for-vttregion-2) [(3)](#ref-for-vttregion-3)
-   [9.2. The VTTRegion interface](#ref-for-vttregion-4) [(2)](#ref-for-vttregion-5) [(3)](#ref-for-vttregion-6) [(4)](#ref-for-vttregion-7) [(5)](#ref-for-vttregion-8) [(6)](#ref-for-vttregion-9) [(7)](#ref-for-vttregion-10) [(8)](#ref-for-vttregion-11) [(9)](#ref-for-vttregion-12) [(10)](#ref-for-vttregion-13) [(11)](#ref-for-vttregion-14)

**[#dom-vttregion-vttregion](#dom-vttregion-vttregion)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-vttregion-1) [(2)](#ref-for-dom-vttregion-vttregion-2)

**[#dom-vttregion-id](#dom-vttregion-id)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-id-1) [(2)](#ref-for-dom-vttregion-id-2)

**[#dom-vttregion-width](#dom-vttregion-width)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-width-1) [(2)](#ref-for-dom-vttregion-width-2)

**[#dom-vttregion-lines](#dom-vttregion-lines)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-lines-1) [(2)](#ref-for-dom-vttregion-lines-2)

**[#dom-vttregion-regionanchorx](#dom-vttregion-regionanchorx)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-regionanchorx-1) [(2)](#ref-for-dom-vttregion-regionanchorx-2)

**[#dom-vttregion-regionanchory](#dom-vttregion-regionanchory)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-regionanchory-1) [(2)](#ref-for-dom-vttregion-regionanchory-2)

**[#dom-vttregion-viewportanchorx](#dom-vttregion-viewportanchorx)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-viewportanchorx-1) [(2)](#ref-for-dom-vttregion-viewportanchorx-2)

**[#dom-vttregion-viewportanchory](#dom-vttregion-viewportanchory)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-viewportanchory-1) [(2)](#ref-for-dom-vttregion-viewportanchory-2)

**[#dom-vttregion-scroll](#dom-vttregion-scroll)Referenced in:**

-   [9.2. The VTTRegion interface](#ref-for-dom-vttregion-scroll-1) [(2)](#ref-for-dom-vttregion-scroll-2) [(3)](#ref-for-dom-vttregion-scroll-3)

**[#text-vtt](#text-vtt)Referenced in:**

-   [2.1. Conformance classes](#ref-for-text-vtt-1)

[↑](#toc)
