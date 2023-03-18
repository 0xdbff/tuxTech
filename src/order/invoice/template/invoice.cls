% http://www.latextemplates.com/template/minimal-invoice LICENCE AND COPYRIGHT NOTICE
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{CSMinimalInvoice}[2022/04/22 Creodocs Minimal Invoice Class v1.1]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}}
\ProcessOptions\relax
\LoadClass{extarticle}
\usepackage{fp}
\usepackage[
	detect-all, text-rm,
]{siunitx}
\usepackage{setspace}
\usepackage{etoolbox}
\usepackage[hidelinks]{hyperref}
\pagestyle{empty}
\newlength{\negativesign}
\settowidth{\negativesign}{--}
\setlength\parindent{0pt}
\usepackage[document]{ragged2e}
\usepackage[
	top=2.5cm,
	bottom=2.25cm,
	left=2cm,
	right=2cm,
]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[default]{lato}
\usepackage{textcomp}
\usepackage{tfrupee}
\usepackage{longtable}
\setlength{\LTpre}{0pt}
\setlength{\LTpost}{0pt
\setlength{\LTleft}{0pt}
\usepackage{array}
\renewcommand{\arraystretch}{1.7}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\setlength{\tabcolsep}{4pt}
\newcommand{\currencysymbol}{\$}
\newcommand{\determinecurrencysymbol}[1]{
	\expandafter\ifstrequal\expandafter{#1}{GBP}{\renewcommand{\currencysymbol}{\textsterling}}{}
	\ifboolexpr{ test {\expandafter\ifstrequal\expandafter{#1}{JPY}} or test {\expandafter\ifstrequal\expandafter{#1}{CNY}} }{\renewcommand{\currencysymbol}{\textyen}}{}
	\expandafter\ifstrequal\expandafter{#1}{EUR}{\renewcommand{\currencysymbol}{\texteuro}}{}
	\expandafter\ifstrequal\expandafter{#1}{BRL}{\renewcommand{\currencysymbol}{R\$}}{}
	\expandafter\ifstrequal\expandafter{#1}{INR}{\renewcommand{\currencysymbol}{\rupee}}{}
}
\usepackage{datenumber}
\newcommand{\duedatedays}[1]{
	\addtocounter{datenumber}{#1}
	\setdatebynumber{\thedatenumber}
	\datedate
}
\gdef\currentsubtotalglobal{0}
\gdef\totalbeforetaxglobal{0}
\gdef\totaltaxglobal{0}
\gdef\totalaftertaxglobal{0}
\newcommand{\calculatesubtotalandupdatetotals}[2]{
	\FPmul{\subtotal}{#1}{#2}
	\FPround{\subtotal}{\subtotal}{\roundcurrencytodecimals}
	\global\let\currentsubtotalglobal\subtotal
	\FPeval{\beforetax}{round(\totalbeforetaxglobal + \currentsubtotalglobal, \roundcurrencytodecimals)}
	\global\let\totalbeforetaxglobal\beforetax
	\ifdefempty{\taxrate}{}{
		\FPeval{\tax}{round(\totalbeforetaxglobal * (\taxrate / 100), \roundcurrencytodecimals)}
		\global\let\totaltaxglobal\tax
	}
	\FPeval{\aftertax}{round(\totalbeforetaxglobal + \totaltaxglobal, \roundcurrencytodecimals)}
	\global\let\totalaftertaxglobal\aftertax
}
\newcommand{\outputcurrency}[1]{
	\FPifneg{#1}
		\FPmul{\positivenumber}{#1}{-1}
		\hspace{-\negativesign}--\currencysymbol\FPeval{\roundedpositivenumber}{round(\positivenumber, \roundcurrencytodecimals)}\num{\roundedpositivenumber}\currencysuffix
	\else
		\currencysymbol\FPeval{\roundednumber}{round(#1, \roundcurrencytodecimals)}\num{\roundednumber}\currencysuffix
	\fi
}
\newcommand{\invoiceitem}[4]{
	\calculatesubtotalandupdatetotals{#2}{#3}
	#1 &
	\FPeval{\roundedquantity}{round(#2, \roundquantitytodecimals)}\num{\roundedquantity} &
	\outputcurrency{#3} &
	\outputcurrency{\currentsubtotalglobal} &
	{\small #4}\\
}
\newenvironment{invoicetable}{
	\vspace{0.02\textheight}
	\begin{longtable}[H]{@{} L{0.38\textwidth} R{0.15\textwidth} R{0.15\textwidth} R{0.15\textwidth} @{\hspace{16pt}} L{0.15\textwidth} @{}}
		\textbf{DESCRIPTION} & \textbf{QUANTITY} & \textbf{UNIT PRICE} & \textbf{SUBTOTAL} & \\
}{
		\\
		\ifdefempty{\taxrate}{}{& & \textbf{BEFORE TAX} & \outputcurrency{\totalbeforetaxglobal}\\}
		\ifdefempty{\taxrate}{}{& & \textbf{TAX (\taxrate\%)} & \outputcurrency{\totaltaxglobal}\\}
		& & \textbf{TOTAL\ifdefempty{\currencycode}{}{ (\currencycode)}} & \outputcurrency{\totalaftertaxglobal}\\
	\end{longtable}
	\vspace{0.02\textheight}
}
\newcommand{\outputheader}[2]{
	{\Huge\MakeUppercase{#1}}
	\vspace{0.015\textheight}
	\expandafter\ifstrequal\expandafter{#2}{}{}{{\large #2}}
	\vspace{0.1\textheight}
}
\newcommand{\outputinvoicenum}{
	\ifdefempty{\invoicenumber}{}{
		{\Huge\#\invoicenumber}
		\smallskip
	}
}
\newcommand{\invoiceconditions}[1]{
	\expandafter\ifstrequal\expandafter{#1}{}{}{
		{\justifying #1 \par}
	}
	\vspace{0.05\textheight}
}
\newcommand{\taxrate}[1]{\renewcommand{\taxrate}{#1}}
\newcommand{\currencycode}[1]{\renewcommand{\currencycode}{#1}}
\newcommand{\invoicenumber}[1]{\renewcommand{\invoicenumber}{#1}}
\newcommand{\currencysuffix}[1]{\renewcommand{\currencysuffix}{#1}}
\newcommand{\roundquantitytodecimals}[1]{\renewcommand{\roundquantitytodecimals}{#1}}
\newcommand{\roundcurrencytodecimals}[1]{\renewcommand{\roundcurrencytodecimals}{#1}}
