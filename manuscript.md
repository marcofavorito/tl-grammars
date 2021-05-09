---
title: Standard Grammars for Temporal Logics
keywords:
- linear temporal logic
- linear dynamic logic
- standard grammar
lang: en-US
date-meta: '2021-05-09'
author-meta:
- Marco Favorito
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Standard Grammars for Temporal Logics" />
  <meta name="citation_title" content="Standard Grammars for Temporal Logics" />
  <meta property="og:title" content="Standard Grammars for Temporal Logics" />
  <meta property="twitter:title" content="Standard Grammars for Temporal Logics" />
  <meta name="dc.date" content="2021-05-09" />
  <meta name="citation_publication_date" content="2021-05-09" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Marco Favorito" />
  <meta name="citation_author_institution" content="Department of Computer, Control and Management Engineering - Sapienza University of Rome" />
  <meta name="citation_author_orcid" content="0000-0001-9566-3576" />
  <link rel="canonical" href="https://marcofavorito.github.io/tl-grammars/" />
  <meta property="og:url" content="https://marcofavorito.github.io/tl-grammars/" />
  <meta property="twitter:url" content="https://marcofavorito.github.io/tl-grammars/" />
  <meta name="citation_fulltext_html_url" content="https://marcofavorito.github.io/tl-grammars/" />
  <meta name="citation_pdf_url" content="https://marcofavorito.github.io/tl-grammars/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://marcofavorito.github.io/tl-grammars/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://marcofavorito.github.io/tl-grammars/v/b3e036807eebede116931db365ccc961d7677fb4/" />
  <meta name="manubot_html_url_versioned" content="https://marcofavorito.github.io/tl-grammars/v/b3e036807eebede116931db365ccc961d7677fb4/" />
  <meta name="manubot_pdf_url_versioned" content="https://marcofavorito.github.io/tl-grammars/v/b3e036807eebede116931db365ccc961d7677fb4/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.bib
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://marcofavorito.github.io/tl-grammars/v/b3e036807eebede116931db365ccc961d7677fb4/))
was automatically generated
from [marcofavorito/tl-grammars@b3e0368](https://github.com/marcofavorito/tl-grammars/tree/b3e036807eebede116931db365ccc961d7677fb4)
on May 9, 2021.
</em></small>

![ArXiv icon](images/arxiv.svg) [https://arxiv.org/abs/2012.13638](https://arxiv.org/abs/2012.13638)  
![GitHub icon](images/github.svg) [marcofavorito/tl-grammars](https://github.com/marcofavorito/tl-grammars)

Document version: v0.1.1

**WARNING**: this version v0.1.1 is a draft. 
You are encouraged
to email the contact author for any comment or suggestion.

## Authors



+ **Marco Favorito**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0001-9566-3576](https://orcid.org/0000-0001-9566-3576)
    · ![GitHub icon](images/github.svg){.inline_icon}
    [marcofavorito](https://github.com/marcofavorito)
    · ![Website icon](images/website.png){.inline_icon}
    [https://marcofavorito.me](https://marcofavorito.me)<br>
  <small>
     Department of Computer, Control and Management Engineering - Sapienza University of Rome
  </small>



## Abstract {.page_break_before}

The heterogeneity of tools that support temporal logic formulae poses several challenges in terms of interoperability. This document proposes standard grammars for Linear Temporal Logic (LTL) [@pnueli77] and Linear Dynamic Logic [@vardi2011rise;@degiacomo2013]

## Introduction

This section explains the motivations
behind the existence of this standard,
states the goals of the standard,
describes the notation conventions
used thorough the document,
and lists the normative references[^1].


[^1]: You can get the sources of this document at this repository:
      [https://github.com/marcofavorito/tl-grammars](https://github.com/marcofavorito/tl-grammars)


## Motivation
 
Temporal logics have a long history [@konur2010].
One of the most influential formalisms
is Linear Temporal Logic (LTL) [@pnueli77],
which has been applied for
program specification and verification.
The variant over finite
traces has been introduced in [@degiacomo2013].
Linear Dynamic Logic (LDL) [@vardi2011rise;@degiacomo2013]
is the extension of LTL with regular expressions (RE).
The idea behind LDL is to have a formalism that merges
the declarativeness and convenience of LTL,
as expressive as star-free RE,
with the expressive power of RE. 
The finite trace setting has been explored by
[@degiacomo2013] for LTL/LDL and 
[@degiacomo2020] for PLTL/PLDL. 
The syntax that naturally supports
empty traces has been employed in [@brafman2018] for LTL/LDL and 
[@degiacomo2020] for PLTL/PLDL.


The topic has gained 
more and more attention both in academia and industry,
also because 
such logics have been considered compelling 
also from a practical point of view. 
Among areas of Computer Science and Artificial Intelligence,
we encounter reactive synthesis [@degiacomo2015],
model checking [@clarke1986],
planning with temporal goal [@bacchus1998planning],
theory of Markov Decision Process with non-Markovian rewards
[@bacchus1996rewarding],
business processes specification
[@pevsic2010enacting], just to name a few.
For what concerns industry applications,
Intel proposed the industrial linear time 
specification language  `ForSpec` [@armoni2002forspec],
and the IEEE association standardized the
_Property Specification Language_ (PSL) [@ieee2010].
Both standards
witness the need of specifications based
on LTL and regular expressions.
Also, the research community has proposed a plethora of
software tools and libraries to handle LTL and/or LDL formulas 
for a variety of purposes:
`Spot` [@duret2016spot;@duret2016spotb],
`Owl` [@owl2018],
`SPIN` [@holzmann2011],
`Syft` [@Zhu_2017],
`Lisa` [@bansal2020hybrid],
`FLLOAT` [@flloat2015;@favorito2018reinforcement],
`LTLf2DFA` [@fuggitti_whitemechltlf2dfa_2018], and more.
Another related work is represented by
TLSF v1.1 [@jacobs2016high],
although its focus is on a format for LTL synthesis problems.

All these tools and formats assume the input formulae to be
written in a certain grammar.
Unfortunately, as often happens when dealing with parser implementations
with lack of coordination,
the grammars to represent the formulae 
have some form of discrepancies; e.g.
different alternative ways to denote 
boolean conjunctions or temporal operators,
different lexical rules to describe the allowed
atomic propositions or boolean constants,
underspecifications on how to handle 
special characters (linefeed, tab, newline, etc.),
how to handle associativity of the operators.

### Goals

To enhance interoperability between the aforementioned tools,
this document proposes a standard grammar
for writing temporal logic formulae.
In particular, we specify grammars for:

- Linear Temporal Logic (LTL)
- Linear Dynamic Logic (LDL)


In future versions of this standard, we 
would like to provide grammars for:

- Past Linear Temporal Logic (PLTL)
- Past Linear Dynamic Logic (PLDL)

We would like this standard to be:

- An _open_ standard, fostering collaboration and contributions from 
  the research community;
- As much compliant as possible to existing and widely used tools;
- Written by researchers, for researchers. In other words, 
  this is not strictly tight to industrial needs; for instance,
  we deliberately dropped the modeling of multiple clock 
  and reset signals of `ForSpec` and `PSL`, as these are constructs
  not relevant for domains outside formal verification.
- Tool-agnostic. Often, grammars are reported alongside
  software manuals and descriptions. Instead, our 
  aim is to propose a common denominator for
  all the grammars in use.


### Notation

We describe the syntax in Extended Backus-Naur Form (EBNF) [@backus1959syntax].
We follow the notation used for the 
specification of XML [@xml]; we discarded
the EBNF standard version ISO/IEC 14977 [@iso1996iso], 
as it has been often rejected by the community 
of those who write language specifications 
for a variety of reasons [@david_dont_2020;@zaytsev2012bnf].

### Normative

We refer to [@bradner1997key] 
for requirement level key words.
We also refer to
Unicode standard [@ISOUNICODE;@unicode2020]
to define legal characters.
For versioning this standard, we
use SemVerDocs [@tekampe_semantic_nodate],
inspired by SemVer [@preston-werner_semantic_nodate]. 



## Common definitions

In this section, we describe syntactic rules
shared across every logic formalism.

### Characters

Parsers MUST be able to accept sequence of _characters_ (see definition below)
which represent temporal logic formulae.
A _character_ 
is an atomic unit of text as specified by ISO/IEC 10646:2020
[@ISOUNICODE].
Legal characters are tab, carriage return, line feed, and the ASCII characters 
of Unicode and ISO/IEC 10646.

The range of characters to be supported
is defined as:
```
Char ::= #x9 | #xA | #xD | [#x20-#x7e]
```

That is, the character tabulation, line feed, carriage return,
and all the printable ASCII characters.

## Boolean constants

For LTL and PLTL,
we use `true` and `false` to denote boolean constants.
For LDL and PLDL, we make a further distinction 
between _propositional_ 
booleans, denoted by `true` and `false`,
and _logical_ booleans, denoted by `tt` and `ff`.

```
True  ::= "true"
False ::= "false"
TT    ::= "tt"
FF    ::= "ff"
PropBooleans  ::= TRUE | FALSE
LogicBooleans ::= TT | FF
```

### Atomic Propositions

An atomic proposition is a string of characters. 
In particular, it can be:

- any string of printable characters, excepted the quotation character used (see `QuotedName`)
- any string of at least one character that starts with `[A-Za-z_]`
  and continues with `[A-Za-z0-9_]`.

```
NameStartChar ::= [A-Z] | [a-z] | "_"
NameChar ::= NameStartChar | [0-9]
Name ::= NameStartChar (NameChar)*
QuotedName ::= ('"' [^"\n\t\r]* '"') | ("'" [^'\n\t\r]* "'")
Atom ::= Name | QuotedName
```

### Boolean operators

The supported boolean operations 
are: negation, conjunction, disjunction,
implication, equivalence and exclusion.

Follows the list of characters used
for each operator:

- negation: `!`, `~`;
- conjunction: `&`, `&&`;
- disjunction: `|`, `||`;
- implication: `->`, `=>`;
- equivalence: `<->`, `<=>`;
- exclusive disjunction: `^`;

```
Non   ::= "!" | "~"
And   ::= "&" | "&&"
Or    ::= "|" | "||"
Impl  ::= "->" | "=>"
Equiv ::= "<->" | "<=>"
Xor   ::= "^"
```

### Parenthesis

We use `(` and `)` for parenthesis.

```
LeftParen  ::= "("
RightParen ::= ")"
```

### White Spaces

It is often convenient to use "white spaces" 
(spaces, tabs, and blank lines) to set apart the formulae for greater readability.
These characters MUST be ignored when processing the text input.




## LTL

In this section, we specify a grammar for LTL.

### Atoms

An LTL formula is defined over a set of _atoms_.
In this context, an atom formula is defined by using 
the `Atom` regular language defined above:

```
LTLAtom ::= Atom
```

### Temporal operators

Here we specify the regular languages for the temporal operators.

- (Weak) Next: `X`;
- Strong Next: `X[!]`;
- (Strong) Until: `U`;
- Weak Until: `W`;
- (Weak) Release: `R`, `V`;
- Strong Release: `M`;
- Eventually: `F`;
- Always: `G`;

In EBNF format:
```
WeakNext      ::= "X"
Next          ::= "X[!]"
Until         ::= "U"
WeakUntil     ::= "W"
Release       ::= "R" | "V"
StrongRelease ::= "M"
Eventually    ::= "F"
Always        ::= "G"
```


### Grammar

```
ltl_formula ::= LTLAtom
                | True
                | False
                | LeftParen ltl_formula RightParen 
                | Not ltl_formula 
                | ltl_formula And ltl_formula
                | ltl_formula Or ltl_formula
                | ltl_formula Impl ltl_formula
                | ltl_formula Equiv ltl_formula
                | ltl_formula Xor ltl_formula
                | ltl_formula Until ltl_formula
                | ltl_formula WeakUntil ltl_formula
                | ltl_formula Release ltl_formula
                | ltl_formula StrongRelease ltl_formula
                | Eventually ltl_formula
                | Always ltl_formula
                | WeakNext ltl_formula
                | Next ltl_formula
```

For the semantics of these operators,
we refer to [@pnueli77] for the 
infinite setting, and [@degiacomo2013]
for the finite setting.


### Precedence and associativity of operators

The precedence and associativity of the LTL operators are 
described by the following table (priorities from lowest to highest).
For brevity, aliases for boolean operators
are omitted.

<center>

|associativity|operators|
|-|-|
|right|`->`, `<->`|
|left|`^`|
|left|`|`|
|left|`&`|
|right |`U`,`W`,`M`,`R`|
|right |`F`, `G`|
|right |`X`, `X[!]`|
|right |`!`|
</center>




## LDL 

In this section, we specify a grammar for LDL.

### Temporal operators

LDL supports two temporal operators:

- _Diamond_ operator: `<regex>ldl_formula`;
- _Box_ operator: `[regex]ldl_formula`;

`regex` will be presented in the next paragraph.

```
LeftDiam  ::= "<"
RightDiam ::= ">"
LeftBox   ::= "["
RightBox  ::= "]"
```

In EBNF format, an LDL formula is defined as follows:

```
ldl_formula ::= TT
              | FF
              | LeftParen ldl_formula RightParen
              | Not ldl_formula 
              | ldl_formula And ldl_formula
              | ldl_formula Or ldl_formula
              | ldl_formula Impl ldl_formula
              | ldl_formula Equiv ldl_formula
              | LeftDiam regex RightDiam ldl_formula
              | LeftBox regex RightBox ldl_formula
```

### Regular Expressions

In this section, we define the regular expression used by 
Diamond and Box operators.

A regular expression is defined inductively as:

- a _propositonal formula_ over as set of propositional atoms.
- a _test expression_: `ldl_formula?
- a _concatenation_ between two regular expressions: `regex_1 ; regex_2`
- a _union_ between two regular expressions: `regex_1 + regex_2`
- a _star_ operator over a regular expression: `regex*`

The symbols are listed below:

```
Test   ::= "?"
Concat ::= ";"
Union  ::= "+"
Star   ::= "*"
```

The EBNF grammar for a regular expression is:

```
propositional ::= Atom
                  | True
                  | False
                  | LeftParen propositional RightParen 
                  | Not propositional 
                  | propositional And propositional
                  | propositional Or propositional
                  | propositional Impl propositional
                  | propositional Equiv propositional
                  | propositional Xor propositional

regex ::= propositional
          | LeftParen regex RightParen
          | regex Test
          | regex Concat regex 
          | regex Union regex 
          | regex Star
``` 

For the semantics of the operators,
we refer to [@degiacomo2013].


### Precedence and associativity of operators

The precedence and associativity of the LDL operators are 
described by the following table (priorities from lowest to highest).
For brevity, aliases for boolean operators
are omitted.

<center>

|associativity|operators|
|-|-|
|right|`->`, `<->`|
|left|`^`|
|left|`|`|
|left|`&`|
|N/A|`<>`, `[]`|
|left|`;`|
|left|`+`|
|left|`*`|
|left|`?`|
|right|`!`|
</center>



## Future work

In future versions of this standard, we would like to add:

- `Spot`-like syntactic sugars for regular expressions (SERE) and 
  temporal operators [@duret2016spot;@jacobs2016high];
- Compatibility with the PSL standard [@ieee2010];
- Support full Unicode characters, so
  to use UTF-8 characters
  like $\circ$ (U+25CB) for the Next operator
  and $\diamond$ (U+25C7) for the Eventually operator etc.
  as alternative symbols.
- Grammars for PLTL and PLDL.



## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
