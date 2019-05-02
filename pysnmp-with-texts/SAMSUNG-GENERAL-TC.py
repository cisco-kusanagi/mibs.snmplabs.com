#
# PySNMP MIB module SAMSUNG-GENERAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-GENERAL-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:00:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, IpAddress, Counter64, iso, ModuleIdentity, ObjectIdentity, Gauge32, Bits, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "Counter64", "iso", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Bits", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scmGeneralTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50))
if mibBuilder.loadTexts: scmGeneralTC.setLastUpdated('0407170000Z')
if mibBuilder.loadTexts: scmGeneralTC.setOrganization('Samsung Corporation - SCMI Working Group')
if mibBuilder.loadTexts: scmGeneralTC.setContactInfo(' SCMI Editors E-Mail: wono.song@samsung.com -- -- ')
if mibBuilder.loadTexts: scmGeneralTC.setDescription(" Version: 1.00 Samsung General Textual Conventions See section 9 'Supplement' of SCMI General TC for implementation and conformance guidance for this TC module. Copyright (C) 1995-2002 Samsung Corporation. All Rights Reserved.")
class Cardinal16(TextualConvention, Integer32):
    description = ' The representation for non-negative integers. Used for indices in small tables where 0 means not specified. It avoids use of the sign bit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32767)

class Cardinal32(TextualConvention, Integer32):
    description = ' The representation for non-negative integers. Used for indices in large tables where 0 means not specified. Same size as ISO 10175 (avoids use of sign bit).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Cardinal64High(TextualConvention, Integer32):
    description = ' The high-order 31 bits of a 62-bit non-negative integer (0..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Cardinal64Low(TextualConvention, Integer32):
    description = ' The low-order 31 bits of a 62-bit non-negative integer (0..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CodedCountry(TextualConvention, OctetString):
    description = ' A two character country or territory abbreviation from ISO/IEC 3166:1993 - Codes for the Representation of Names of Countries. Examples: US, FR, DE A null string SHALL indicate that the country or territory is not defined.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class CodedLanguage(TextualConvention, OctetString):
    description = ' A two character language abbreviation as defined in ISO/IEC 639:1988 - Codes For the Representation of Names of Languages. Examples EN, GB, CA, FR, DE. An empty string SHALL indicate that the language is not defined.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class CodeIndexedStringIndex(TextualConvention, Integer32):
    description = ' The representation of string data which the agent can provide in one or more character sets (but not further localized). Typically this representation is used because the string data is relatively dynamic, changing too rapidly for full localization; or because the data exists inherently in only one or a limited number of character sets and cannot meaningfully be further localized. The value is an index into a single global string table, scmGenCodeIndexedStringTable. A subsidiary index into the scmGenCodeIndexedStringTable is the IANA registered enum (see the CodedCharSet textual-convention in RFC 1759) for the coded character set desired by the management station (from among the coded character sets supported by the SNMP agent). A 0 index value SHALL indicate that there is no associated entry in the string table. 32 bits are needed because Jobs can use up 10-12 code-indexed strings per job.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Counter64High(TextualConvention, Counter32):
    description = ' The high-order 32 bits of a 63-bit counter (0..2**63-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'

class Counter64Low(TextualConvention, Integer32):
    description = ' The low-order 31 bits of a 63-bit counter (0..2**63-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Gauge64High(TextualConvention, Gauge32):
    description = ' The high-order 32 bits of a 63-bit gauge (0..2**63-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'

class Gauge64Low(TextualConvention, Integer32):
    description = ' The low-order 31 bits of a 63-bit gauge (0..2**63-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Integer64High(TextualConvention, Integer32):
    description = ' The high-order 32 bits of a 63-bit signed integer (-2**62..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'

class Integer64Low(TextualConvention, Integer32):
    description = ' The low-order 31 bits of a 63-bit signed integer (-2**62..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Ordinal16(TextualConvention, Integer32):
    description = ' The representation for positive integers. Used for indices in small tables where 0 is illegal. It avoids use of the sign bit..'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32767)

class Ordinal32(TextualConvention, Integer32):
    description = ' The representation for positive integers. Same size as ISO 10175 (avoids use of sign bit).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ordinal64High(TextualConvention, Integer32):
    description = ' The high-order 31 bits of a 62-bit positive integer (1..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Ordinal64Low(TextualConvention, Integer32):
    description = ' The low-order 31 bits of a 62-bit positive integer (1..2**62-1). A manager must get or set the high and low parts in the same operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

zeroDotZero = MibIdentifier((0, 0))
scmGenZeroDotZero = ObjectIdentity((0, 0, 0))
if mibBuilder.loadTexts: scmGenZeroDotZero.setStatus('current')
if mibBuilder.loadTexts: scmGenZeroDotZero.setDescription(" A value used for null object identifiers prior to SCMI v5.1. Do not use. Instead use the standard definition in RFC 1902/2578 - 'zeroDotZero' - left here for compatibility.")
class ScmFixedLocaleDisplayString(TextualConvention, OctetString):
    reference = " See: 'ScmFixedLocaleUtf8String' in this module. See: 'ScmNamedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    description = " This data type is used to model textual information in some localization (language, country, and character set), which is fixed (ie, NOT capable of being altered by management station request). This textual information SHALL be represented in the localization which is indicated by the current value of 'scmGenFixedLocalizationIndex'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmFixedLocaleUtf8String(TextualConvention, OctetString):
    reference = " See: 'UTF-8, a transformation of ISO 10646' (RFC 2279) and 'IETF Policy on Character Sets and Languages' (RFC 2277). See: 'ScmFixedLocaleDisplayString' in this module. See: 'ScmNamedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    description = " This data type is used to model textual information in the UTF-8 character set and some locale (language/country), which is fixed (ie, NOT capable of being altered by management station request). This textual information SHALL be represented in UTF-8 and the locale which is indicated by the current value of 'scmGenFixedLocalizationIndex'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmNamedLocaleUtf8String(TextualConvention, OctetString):
    reference = " See: 'UTF-8, a transformation of ISO 10646' (RFC 2279) and 'IETF Policy on Character Sets and Languages' (RFC 2277). See: 'ScmFixedLocaleDisplayString' in this module. See: 'ScmFixedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    description = ' This data type is used to model textual information in the UTF-8 character set and some locale (language/country), which is named (ie, explicitly named by a parallel column or attribute or by the operation context).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmGenGroupSupport(TextualConvention, Integer32):
    description = ' The terse conformance statement of ALL mandatory, conditionally mandatory, and optional SCMI General MIB object groups which are supported by this management agent implementation (ie, version) on this host system, specified in a bit-mask. The current set of values (which MAY be extended in the future) is given below: 1 : scmGenCurrentLocalizationGroup -- 2**0 2 : scmGenLocalizationGroup -- 2**1 4 : scmGenCodeIndexedStringGroup -- 2**2 8 : scmGenCodedCharSetGroup -- 2**3 16 : scmGenFixedLocalizationGroup -- 2**4 32 : scmGenLockGroup -- 2**5 64 : scmGenReconfGroup -- 2**6 128 : scmGenOptionGroup -- 2**7 256 : scmGenClientDataGroup -- 2**8 512 : scmGenTrapClientGroup -- 2**9 1024 : scmGenTrapViewGroup -- 2**10 2048 : scmGenBaseGroup -- 2**11 4096 : scmGenMessageMapGroup -- 2**12 8192 : scmGenMessageTextGroup -- 2**13 16384 : scmGenNotifyRuleGroup -- 2**14 32768 : scmGenNotifyDetailGroup -- 2**15 Usage: Conforming management agents SHALL accurately report their support for SCMI General MIB object groups.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenLogFullPolicy(TextualConvention, Integer32):
    description = " The current policy for handling job/request/event log 'full' (in MIBs, in shared RAM, on disk, etc), on this host system."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("disableService", 3), ("disableAndPauseService", 4), ("enableServiceAndFlushLog", 5), ("enableServiceAndFlushOldest", 6))

class ScmGenMessageMapStringLabel(TextualConvention, OctetString):
    reference = " See: 'scmGenMessageMapStringLabel' in SCMI General MIB. See: 'deviceLifetimeUsage', 'deviceAccountingUsage', 'deviceLifetimeErrorCount', and 'deviceLifetimeWarningCount' in 'ScmHrDevDetailType' textual convention in SCMI Host Resources Ext TC."
    description = " This syntax is used to specify a Samsung standard or experiemental message string label associated with the current value of the message string pointed to by 'scmGenMessageMapStringIndexOID'. Usage: Experimental message string labels SHOULD NOT be used in shipping versions of Samsung-branded products or services. They exist solely to facilitate rapid product development cycles. Usage: All Samsung message string label values SHALL be specified using display (NOT space) characters from the IANA registered charset 'utf-8' (ie, the UTF-8 octet-stream encoding of ISO-10646 UCS-4, described in RFC 2279). Usage: All Samsung message string label values SHALL contain no more than 64 UTF-8 display characters AND no more than 128 total octets (in some scripts, less than 64 characters in UTF-8 octet-stream encoding). Usage: All Samsung message string label values SHALL conform to the syntax specified below. A 'format', 'namespace', 'module', or 'field' component SHALL NOT contain hyphens. A 'format', 'namespace', or 'module' component SHALL use lowercase. A 'field' or 'qualifier' component MAY use mixed case (see examples below). A 'field' component MAY be use an abbreviated MIB object tag or other standardized identifier. ONLY a terminal 'qualifier' component MAY contain hyphens. Each component SHALL be separated by a hyphen '-' character. -- Samsung message string label general ABNF syntax msg_label = format '-' namespace '-' module '-' field '-' qualifier -- Samsung message string label alternatives ABNF syntax msg_label = std_label / exp_label Usage: All Samsung standard message string label values SHALL conform to the refined syntax specified below. -- Samsung standard message label refined ABNF syntax std_label = std_fmt '-' std_ns '-' module '-' field '-' qualifier -- Samsung standard format std_fmt = 'xs' -- Samsung standard format / 'x?' -- Samsung reserved formats (2 characters) -- Samsung standard namespace std_ns = 'ansi' -- American National Standards Institute / 'dmtf' -- Desktop Management Task Force / 'ecma' -- European Computer Manufacturers Assn / 'ieee' -- Institute Electrical/Electronic Engineers / 'ietf' -- Internet Engineering Task Force / 'iso' -- Int'l Organization for Standardization / 'itu' -- Int'l Telecommunication Union (aka CCITT) / 'omg' -- Object Management Group / 'pwg' -- Printer Working Group / 'scmi' -- Samsung Common Management Interface / 'xopen' -- X/Open (aka Open Group) / 'w3c' -- World Wide Web Consortium -- Samsung message label common components module = -- module identifier w/out hyphens field = -- field identifier w/out hyphens qualifier = -- qualifer (MAY contain hyphens) Examples of well-formed standard message string labels: -- Examples of ISO standard media sizes xs-iso-10175-mediaSize-iso-a4 -- 210 mm by 297 mm xs-iso-10175-mediaSize-iso-b4 -- 250 mm by 353 mm -- Examples of ISO standard media types xs-iso-10175-mediaType-envelope xs-iso-10175-mediaType-transparency -- Examples of ISO standard media colors xs-iso-10175-mediaColor-white xs-iso-10175-mediaColor-yellow -- Examples of standard MIB objects xs-ietf-rfc1759-alertDescription-coverOpen xs-pwg-jobmon-processingMessage-completed xs-scmi-11hostx-deviceDescription-dc230ST Usage: All Samsung experimental message string label values SHALL conform to the refined syntax specified below. -- Samsung experimental message label refined ABNF syntax exp_label = exp_fmt '-' exp_ns '-' module '-' field '-' qualifier -- Samsung experimental format exp_fmt = 'xx' -- Samsung experimental format -- Samsung experimental namespace exp_ns = std_ns '.' prod_ns std_ns = -- as defined above for standard labels prod_ns = -- 'official' / 'working' product identifier -- Samsung message label common components module = -- as defined above for standard labels field = -- as defined above for standard labels qualifier = -- as defined above for standard labels Examples of well-formed experimental message string labels: xx-ietf.dcs265-rfc1759-alertDescription-skyIsFalling xx-scmi.dc230-11hostx-deviceDescription-dc230ST xx-scmi.belize-11hostx-systemFaultString-missingWidgets Note: New or refined message label syntaxes MAY be defined in future versions of this SCMI General TC."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class ScmGenNotifyDetailType(TextualConvention, Integer32):
    reference = " See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify (draft-ietf-ipp-not-spec-06.txt). See: Section 5 'Service Attributes' (encoding rules) in Service Location Protocol v2 (RFC 2608)."
    description = " The type of notify detail stored in this conceptual row in 'scmGenNotifyDetailTable'. Usage: Conforming SCMI management stations and agents SHALL encode notify details as UTF-8 strings (like SLPv2, RFC 2608). - Integers SHALL be encoded as (signed) decimal strings. - Booleans SHALL be encoded as 'true' or 'false' strings. - Strings SHALL be encoded as UTF-8 character strings. - Binary data (e.g., 'userCertificate') SHALL be stored in SLPv2 opaque encoding (leading '\\FF' and escaped octets). Usage: Conformant implementations MUST encrypt passwords, keys, and other security information in 'scmGenNotifyDetailString'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 10, 20, 21, 22, 23, 30, 31, 32, 33))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notifyRecipientURI", 10), ("notifyEventNames", 20), ("notifyEventDelay", 21), ("notifySeverityFilter", 22), ("notifyTrainingFilter", 23), ("notifyMessageHeaderKeys", 30), ("notifyMessageHeaderText", 31), ("notifyMessageContentKeys", 32), ("notifyMessageContentText", 33))

class ScmGenNotifySchemeSupport(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseNotifySchemeSupport' and 'scmGenBaseSNMPDomainSupport' in SCMI General MIB. See: Cited IETF URI/URL specifications."
    description = ' The terse conformance statement of ALL notification URI schemes which are supported by this management agent implementation (ie, version) on this host system, specified in a bit-mask. The current set of values (which MAY be extended in the future) is given below: 1 : uriNotifySNMP -- RFC 1215/1906 - 2**0 (SNMP) 2 : uriNotifyMailto -- RFC 1738/2368 - 2**1 (SMTP) 4 : uriNotifyHTTP -- RFC 1738/2616 - 2**2 (HTTP) 8 : uriNotifyHTTPS -- RFC 1738/2396 - 2**3 (HTTPS) 16 : uriNotifyFTP -- RFC 1738/959 - 2**4 (FTP) Usage: Conforming management agents SHALL accurately report their support for notification URI schemes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenNotifySeverityFilter(TextualConvention, Integer32):
    reference = " See: 'prtAlertSeverityLevel' in IETF Printer MIB (RFC 1759). See: 'scmGenBaseNotifySeveritySupport' and 'scmGenTrapViewNotifySeverity' in SCMI General MIB."
    description = " This type is used to specify a notification severity filter supported by this management agent for notification traffic in ALL domains specified by 'scmGenBaseSNMPDomainSupport' and 'scmGenBaseNotifySchemeSupport' (for URI-based notification), specified in a bit-mask. The current set of values (which MAY be extended in the future) is given below: 1 : severityReport -- 2**0 (informational) 2 : severityWarning -- 2**1 (eg, low toner) 4 : severitySoftError -- 2**2 (non-critical) 8 : severityHardError -- 2**3 (critical) 16 : severityTestReport -- 2**4 (product-specific) 32 : severityTestWarning -- 2**5 (product-specific) 64 : severityTestSoftError -- 2**6 (product-specific) 128 : severityTestHardError -- 2**7 (product-specific) 256 : severityInternalError -- 2**8 (product-specific) Usage: The terminology 'report', 'warning', and 'error' is coherent with the IETF IPP event notification work-in-progress and with the IETF Printer MIB (RFC 1759). Usage: Individual trap definitions MAY further constrain which notifications are 'in scope'. Usage: Conforming management agents SHALL accurately report their support for notification severity filters."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenNotifyTrainingFilter(TextualConvention, Integer32):
    reference = " See: 'prtAlertTrainingLevel' in IETF Printer MIB (RFC 1759). See: 'scmGenBaseNotifyTrainingSupport' and 'scmGenTrapViewNotifyTraining' in SCMI General MIB."
    description = " This type is used to specify a notification training filter supported by this management agent for notification traffic in ALL domains specified by 'scmGenBaseSNMPDomainSupport' and 'scmGenBaseNotifySchemeSupport' (for URI-based notification), specified in a bit-mask. The current set of values (which MAY be extended in the future) is given below: 1 : trainingOther -- 2**0 (extension) 2 : trainingUnknown -- 2**1 (unknown) 4 : trainingNone -- 2**2 (untrained) 8 : trainingTrained -- 2**3 (trained) 16 : trainingFieldService -- 2**4 (field service) 32 : trainingManagement -- 2**5 (management) 64 : trainingNoIntervention -- 2**6 (management) Usage: The terminology used here is coherent with the IETF Printer MIB (RFC 1759). Usage: Individual trap definitions MAY further constrain which notifications are 'in scope'. Usage: Conforming management agents SHALL accurately report their support for notification training filters."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenOptionValueSyntax(TextualConvention, Integer32):
    reference = " See: 'scmGenOptionTable' in SCMI General MIB See: 'scmCommsOptionTable' in SCMI Comms Config MIB See: 'scmHrDevDetailTable' in SCMI Host Resources Ext MIB See: 'scmHrStorageDetailTable' in SCMI Host Resources Ext MIB See: 'scmSvcMonServiceDetailTable' in SCMI Service Mon MIB See: 'scmSecProfileDetailTable' in SCMI Security MIB"
    description = " A reconfiguration option, device detail, storage detail, service detail, or security profile detail value syntax, used by system administrators and end users to specify the correct value syntax for this option or detail. Usage: This option or detail value syntax is used to select which of the three value objects SHALL be used to contain the value of this option or detail. * An option or detail value syntax of 'oidObject' indicates that 'scm...ValueOID' SHALL be used to specify an actual object type, defined with 'OBJECT-TYPE'. * An option or detail value syntax of 'oidAutonomous' indicates that 'scm...ValueOID' SHALL be used to specify an autonomous object type, defined with 'OBJECT-IDENTITY' or simply 'OBJECT IDENTIFIER'. * An option or detail value syntax of 'stringBinary' indicates that 'scm...ValueString' SHALL be used to specify a (possibly) 'binary' (or 'non-printing') value string. * An option or detail value syntax of 'stringDisplay' indicates that 'scm...ValueString' SHALL be used to specify a 'displayable' (or 'printing') value string. * An option or detail value syntax of 'stringLocalization' indicates that 'scm...ValueLocalization' (for options) or 'scmGenFixedLocalizationIndex' (for details) SHALL be used to control the localization of the value string (with an underlying type of 'ScmGenFixedLocaleDisplayString'). * An option or detail value syntax of 'stringCodedCharSet' indicates that 'scm...ValueCodedCharSet' (for options) or 'scmGenFixedLocalizationIndex' (for details) SHALL be used to control the character set ONLY of the value string (with an underlying type of 'CodeIndexedStringIndex'). * An option or detail value syntax of 'stringDynamicLocalization' indicates that 'scmGenCurrentLocalization' SHALL be used to control the localization of the value string (with an underlying type of 'InternationalDisplayString'). * An option or detail value syntax of 'stringUtf8Localization' indicates that 'scm...ValueLocalization' (for options) or 'scmGenFixedLocalizationIndex' (for details) SHALL be used to control the localization of the value string (with an underlying type of 'ScmGenFixedLocaleUtf8String')."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("integerNumber", 3), ("integerCounter", 4), ("integerEnum", 5), ("integerGauge", 6), ("integerIndex", 7), ("integerTruthValue", 8), ("oidObject", 9), ("oidAutonomous", 10), ("stringBinary", 11), ("stringDisplay", 12), ("stringLocalization", 13), ("stringCodedCharSet", 14), ("stringDynamicLocalization", 15), ("stringUtf8Localization", 16))

class ScmGenReconfOptionState(TextualConvention, Integer32):
    reference = " See: 'scmGenReconfError[Index|Status]'"
    description = " The processing state of ALL pending reconfiguration options of this host system. A write to this object by an (authorized) management station invokes a request for validation (or activation) of ALL pending reconfiguration options of this host system. A read of this object returns 'idle', 'validateInProgress', or 'activateInProgress' to report the processing state of the last 'validate...' or 'activate...' request. It is mandatory that a conforming management agent ensure that, at system initialization, this object SHALL be set to a value of 'idle'. * 'idle' - NO processing is 'in progress' for either 'validate...' or 'activate...' of any pending reconfiguration options. * 'validateForImmediateChange' - this management agent (and host system) SHALL perform ALL possible and appropriate validation of ALL pending reconfiguration options (reporting the FIRST error encountered during validation), so that reconfiguration could be performed successfully via 'activateForImmediateChange'. * 'validateForRebootChange' - this management agent (and host system) SHALL perform ALL possible and appropriate validation of ALL pending reconfiguration options (reporting the FIRST error encountered during validation), so that reconfiguration could be performed successfully via 'activateForRebootChange'. * 'validateForImmediateReboot' - this management agent (and host system) SHALL perform ALL possible and appropriate validation of ALL pending reconfiguration options (reporting the FIRST error encountered during validation), so that reconfiguration could be performed successfully via 'activateForImmediateReboot'. * 'validateInProgress' - indicates that this management agent (and host system) are currently performing validation of ALL pending reconfiguration options. Note: Conforming implementations NEED NOT support more than ONE of the above three 'validation...' operations. * 'activateForImmediateChange' - this management agent (and host system) SHALL perform immediate reconfiguration, NOT reboot, for ALL pending reconfiguration options (reporting the FIRST error encountered during validation). For all conforming implementations, this reconfiguration SHALL ALWAYS take effect immediately, WITHOUT host system reboot! Note: Conforming implementations are STRONGLY encouraged to consider supporting 'benign' reconfiguration in this manner. * 'activateForRebootChange' - this management agent (and host system) SHALL perform delayed reconfiguration, NOT reboot, for ALL pending reconfiguration options (reporting the FIRST error encountered during validation). For all conforming implementations, this reconfiguration SHALL ALWAYS take effect delayed, AFTER subsequent host system reboot! Note: Conforming implementations NEED NOT support 'caching' of multiple outstanding 'sets of reconfiguration' in this manner. * 'activateForImmediateReboot' - this management agent (and host system) SHALL perform immediate reconfiguration, AND reboot, for ALL pending reconfiguration options (reporting the FIRST error encountered during validation). For all conforming implementations, this reconfiguration SHALL ALWAYS take effect immediately, WITH host system reboot! Note: Conforming implementations are STRONGLY encouraged to consider secure alternatives (eg, Device Mgmt) for system reset. * 'activateInProgress' - indicates that this management agent (and host system) are currently performing activation of ALL pending reconfiguration options. Note: Conforming implementations NEED NOT support more than ONE of the above three 'activation...' operations."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("idle", 1), ("validateForImmediateChange", 2), ("validateForRebootChange", 3), ("validateForImmediateReboot", 4), ("validateInProgress", 5), ("activateForImmediateChange", 6), ("activateForRebootChange", 7), ("activateForImmediateReboot", 8), ("activateInProgress", 9))

class ScmGenRowPersistence(TextualConvention, Integer32):
    reference = " See: 'hrStorageType' in the Storage group of the IETF Host Resources MIB (RFC 2790). See: 'StorageType' textual convention in the Historic SNMPv2 Party MIB (RFC 1447). See: 'StorageType' textual convention in the IETF SNMPv2 Textual Conventions (RFC 2579)."
    description = " This type is used to specify the persistence of this conceptual row in a table. Usage: Conforming management agents SHALL interpret persistence as follows: 1) 'volatile' rows NEED NOT be saved across power cycles, MAY contain one or more 'read-[create|write|only]' objects, and their underlying storage MAY be removable, and conforming management agents NEED NOT delete such rows (eg, a block in RAM, PCMCIA card, etc); 2) 'nonvolatile' rows SHALL be saved across power cycles, MAY contain one or more 'read-[write|only]' objects, and their underlying storage MAY be removable, and conforming management agents MAY delete such rows (eg, a sector on CD-ROM, font cartridge, hard disk, etc); 3) 'permanent' rows SHALL be saved across power cycles, MAY contain one or more 'read-[write|only]' objects, and their underlying storage SHALL NOT be removable, and conforming management agents SHALL NOT delete such rows (eg, a sector on EEPROM, battery-backed RAM, bubble, etc); 4) 'readonly' rows SHALL be saved across power cycles, SHALL contain exclusively 'read-only' objects, and their underlying storage SHALL NOT be removable, and conforming management agents SHALL NOT delete such rows (eg, a sector on ROM, ASIC, etc). Usage: Dynamically created rows MAY ONLY be given 'volatile' or 'nonvolatile' persistence. Note: Equivalent to SNMPv2 'StorageType' textual convention, which has an unfortunately ambiguous name."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("volatile", 3), ("nonvolatile", 4), ("permanent", 5), ("readonly", 6))

class ScmGenSNMPDomain(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseSNMPDomainSupport' and 'scmGenTrapClientSNMPDomain' in SCMI General MIB. See: Cited IETF SNMP specifications."
    description = " This type is used to specify a transport domain (address and name space) which is supported by this management agent for SNMP protocol traffic (SNMP responses, SNMP traps, etc), in ALL versions specified by 'scmGenBaseSNMPVersionSupport'. This type is also used to allow the 'scmGenTrapClientTable' to be used with any URI scheme (e.g., 'mailto:') for notifications, by specifying 'uriNotifyDomain'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 10, 11, 20, 30))
    namedValues = NamedValues(("snmpUDPDomain", 1), ("snmpCLNSDomain", 2), ("snmpCONSDomain", 3), ("snmpDDPDomain", 4), ("snmpIPXDomain", 5), ("snmpNetBIOSDomain", 10), ("snmpNetBEUIDomain", 11), ("snmpTCPDomain", 20), ("uriNotifyDomain", 30))

class ScmGenSNMPVersion(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseSNMPVersionSupport' and 'scmGenTrapClientSNMPVersion' in SCMI General MIB. See: Cited IETF SNMP specifications."
    description = " This type is used to specify an SNMP version (RFC 1157, RFC 1905, etc) which is supported by this management agent for SNMP protocol traffic (SNMP responses, SNMP traps, etc), in ALL domains specified by 'scmGenBaseSNMPDomainSupport'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmpV1Community", 3), ("snmpV1Party", 4), ("snmpV2Party", 5), ("snmpV2Community", 6), ("snmpV2Usec", 7), ("snmpV2Star", 8), ("snmpV2Secure", 9), ("snmpV3Secure", 10))

class ScmGenSNMPv2ErrorStatus(TextualConvention, Integer32):
    reference = " See: 'error-status' in SNMPv2 Protocol (RFC 1448/1905)"
    description = " Usage: This type specifies the SMIv2 equivalent of the SMIv1 'ErrorStatus' textual convention as an enumerated type. Note: The enum of '0' (zero) in this textual convention is illegal in strict SMIv1 (see section 3.2.1.1 of RFC 1155), so this TC must be converted to an integer range for pure SMIv1."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

class ScmGlobalUniqueID(TextualConvention, OctetString):
    description = " A management station or management agent specifies an object of type 'GlobalUniqueID' to uniquely label a client job request, a system administration request, or ANY other managed object (or set of managed objects) which are required to be unambiguously identified in a distributed network environment. An object of type 'GlobalUniqueID' SHALL be a textual string representation in standard 'dotted decimal' form of an OID. An object of type 'GlobalUniqueID' SHALL be composed of three mandatory sections (plus zero or more optional sections), as follows: nodeID.userID.seqID[[.subID1]...[.subIDn]] Each of the sections SHALL be separated by a dot ('.'). The three mandatory sections and any specified optional sections (in left to right order) SHALL be: 1) A globally unambiguous (within at least the network domain of the Requestor and Responder host systems) dotted decimal 'nodeID' of the Requestor host system which explicitly or implicitly labelled this managed object, either: a) A domain specific network layer address (eg, IETF IP address for 'nodeIDTypeIP'); OR b) A domain specific datalink MAC sublayer address (eg, ISO 8802-5 MAC address for 'nodeIDType88025'). 2) A locally unambiguous (within at least the Requestor and/or Responder host systems) dotted decimal 'userID' (ie, user identifier) of the user who explicitly or implicitly labelled this managed object. 3) A locally unambiguous (within at least the Requestor and/or Responder host systems) dotted decimal 'seqID' (ie, sequence identifier) assigned by the host system or user who explicitly or implicitly labelled this managed object. 4) A locally unambiguous (within at least the Requestor and/or Responder host systems) dotted decimal 'subID' (ie, sequence sub-identifier) assigned by the host system or user who explicitly or implicitly labelled this managed object. Usage: Conforming implementations MAY use one or more optional sections in an 'ScmGlobalUniqueID', for example to assign a sub-job identifier for job distribution services (e.g., fax to multiple destinations specified in the PDL of an input 'print' job - using an original 'scmJobClientId' which is augmented by the server that splits up the destinations into separate jobs). Usage: Conforming implementations SHALL NOT specify BOTH the first ('nodeID') and second ('userID') sections as 'empty', but one OR the other section MAY take on an 'empty' value (see below). The third ('seqID') section SHALL NOT be 'empty'. Each of the three mandatory sections and any optional sections SHALL be composed of one mandatory and two optional subsections, as follows: sectionLength.sectionType.sectionValue Each of the subsections SHALL be separated by a dot ('.'). The three subsections (in left to right order) SHALL be: 1) A mandatory 'sectionLength', which specifies the decimal count of dotted decimal 'components' in the associated 'sectionValue' - this 'sectionLength' SHALL NOT be self-inclusive and SHALL NOT include the single 'component' of the 'sectionType' - a 'sectionLength' of decimal zero ('0') SHALL indicate an 'empty' section, and the associated two subsections ('sectionType' and 'sectionValue') SHALL be omitted. 2) An optional 'sectionType', selected from the standard 'sectionType' choices applicable to this section (below). 3) An optional 'sectionValue', specified as a dotted decimal string of 'components', each 'component' separated by a dot ('.'). The standard 'sectionType' choices (one set for each section) SHALL be as follows: 1) 'nodeIDType' -- for mandatory 'nodeID' section 1 : nodeIDTypeOther -- Other 2 : nodeIDTypeUnknown -- Unknown 11 : nodeIDTypeIP -- Internet IP 12 : nodeIDTypeCLNS -- OSI CLNS 13 : nodeIDTypeCONS -- OSI CONS 14 : nodeIDTypeDDP -- AppleTalk DDP 15 : nodeIDTypeIPX -- NetWare IPX 16 : nodeIDTypeNetBIOS -- IBM NetBIOS 31 : nodeIDType88023 -- ISO 8802-3 (Ethernet LAN) 32 : nodeIDType88024 -- ISO 8802-4 (TokenBus LAN) 33 : nodeIDType88025 -- ISO 8802-5 (TokenRing LAN) 34 : nodeIDType88026 -- ISO 8802-6 (SlottedRing MAN) 2) 'userIDType' -- for mandatory 'userID' section 1 : userIDTypeOther -- Other 2 : userIDTypeUnknown -- Unknown 11 : userIDTypeSystem -- System scope 12 : userIDTypeSubnet -- Subnet scope 13 : userIDTypeNetwork -- Network scope 14 : userIDTypeGlobal -- Global scope 3) 'seqIDType' -- for mandatory 'seqID' section 1 : seqIDTypeOther -- Other 2 : seqIDTypeUnknown -- Unknown 11 : seqIDTypeSystem -- System generated 12 : seqIDTypeProcess -- Process generated 13 : seqIDTypeThread -- Thread generated 4) 'subIDType' -- for optional 'subID' sections 1 : subIDTypeOther -- Other 2 : subIDTypeUnknown -- Unknown 11 : subIDTypeSystem -- System generated 12 : subIDTypeProcess -- Process generated 13 : subIDTypeThread -- Thread generated Usage: A 'seqID' of any type SHALL be system-unique. Usage: A 'seqID' of type 'seqIDTypeProcess' SHALL be prefixed (if necessary) by a system-unique dotted decimal 'processID'. Usage: A 'seqID' of type 'seqIDTypeThread' SHALL be prefixed (if necessary) by a system-unique dotted decimal 'threadID' (possibly itself prefixed by a system-unique 'processID'). Example: A request submitted from a client end system running the IETF Internet Protocol Suite (IPS), with an IP address of '13.240.128.21', without a specified dotted decimal 'userID', might include an 'scmJobClientId' of the following form: '4.11.13.240.128.21.0.1.11.3045.1.11.23' [GlobalUniqueID] |---------1--------|2|----3----|---4---| [Sections] 1) The mandatory first section ('nodeID') consists of: a) 'sectionLength' of '4'; b) 'sectionType' of '11' ('nodeIDTypeIP'); and c) 'sectionValue' of '13.240.128.21' (4 components). 2) The mandatory second section ('userID') consists of: a) 'sectionLength' of '0' (ie, 'empty' section). 3) The mandatory third section ('seqID') consists of: a) 'sectionLength' of '1'; b) 'sectionType' of '11' ('seqIDTypeSystem'); and c) 'sectionValue' of '3045' (one component). 4) The optional fourth section ('subID') consists of: a) 'sectionLength' of '1'; b) 'sectionType' of '11' ('subIDTypeSystem'); and c) 'sectionValue' of '23' (one component)."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

sCmGeneralDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999))
sCmGenCardinal16 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 1), Cardinal16())
if mibBuilder.loadTexts: sCmGenCardinal16.setStatus('current')
if mibBuilder.loadTexts: sCmGenCardinal16.setDescription('Dummy - DO NOT USE')
sCmGenCardinal32 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 2), Cardinal32())
if mibBuilder.loadTexts: sCmGenCardinal32.setStatus('current')
if mibBuilder.loadTexts: sCmGenCardinal32.setDescription('Dummy - DO NOT USE')
sCmGenCardinal64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 3), Cardinal64High())
if mibBuilder.loadTexts: sCmGenCardinal64High.setStatus('current')
if mibBuilder.loadTexts: sCmGenCardinal64High.setDescription('Dummy - DO NOT USE')
sCmGenCardinal64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 4), Cardinal64Low())
if mibBuilder.loadTexts: sCmGenCardinal64Low.setStatus('current')
if mibBuilder.loadTexts: sCmGenCardinal64Low.setDescription('Dummy - DO NOT USE')
sCmGenCodedCountry = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 5), CodedCountry())
if mibBuilder.loadTexts: sCmGenCodedCountry.setStatus('current')
if mibBuilder.loadTexts: sCmGenCodedCountry.setDescription('Dummy - DO NOT USE')
sCmGenCodedLanguage = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 6), CodedLanguage())
if mibBuilder.loadTexts: sCmGenCodedLanguage.setStatus('current')
if mibBuilder.loadTexts: sCmGenCodedLanguage.setDescription('Dummy - DO NOT USE')
sCmGenCodeIndexedStringIndex = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 7), CodeIndexedStringIndex())
if mibBuilder.loadTexts: sCmGenCodeIndexedStringIndex.setStatus('current')
if mibBuilder.loadTexts: sCmGenCodeIndexedStringIndex.setDescription('Dummy - DO NOT USE')
sCmGenCounter64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 8), Counter64High())
if mibBuilder.loadTexts: sCmGenCounter64High.setStatus('current')
if mibBuilder.loadTexts: sCmGenCounter64High.setDescription('Dummy - DO NOT USE')
sCmGenCounter64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 9), Counter64Low())
if mibBuilder.loadTexts: sCmGenCounter64Low.setStatus('current')
if mibBuilder.loadTexts: sCmGenCounter64Low.setDescription('Dummy - DO NOT USE')
sCmGenGauge64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 10), Gauge64High())
if mibBuilder.loadTexts: sCmGenGauge64High.setStatus('current')
if mibBuilder.loadTexts: sCmGenGauge64High.setDescription('Dummy - DO NOT USE')
sCmGenGauge64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 11), Gauge64Low())
if mibBuilder.loadTexts: sCmGenGauge64Low.setStatus('current')
if mibBuilder.loadTexts: sCmGenGauge64Low.setDescription('Dummy - DO NOT USE')
sCmGenInteger64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 12), Integer64High())
if mibBuilder.loadTexts: sCmGenInteger64High.setStatus('current')
if mibBuilder.loadTexts: sCmGenInteger64High.setDescription('Dummy - DO NOT USE')
sCmGenInteger64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 13), Integer64Low())
if mibBuilder.loadTexts: sCmGenInteger64Low.setStatus('current')
if mibBuilder.loadTexts: sCmGenInteger64Low.setDescription('Dummy - DO NOT USE')
sCmGenOrdinal16 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 14), Ordinal16())
if mibBuilder.loadTexts: sCmGenOrdinal16.setStatus('current')
if mibBuilder.loadTexts: sCmGenOrdinal16.setDescription('Dummy - DO NOT USE')
sCmGenOrdinal32 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 15), Ordinal32())
if mibBuilder.loadTexts: sCmGenOrdinal32.setStatus('current')
if mibBuilder.loadTexts: sCmGenOrdinal32.setDescription('Dummy - DO NOT USE')
sCmGenOrdinal64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 16), Ordinal64High())
if mibBuilder.loadTexts: sCmGenOrdinal64High.setStatus('current')
if mibBuilder.loadTexts: sCmGenOrdinal64High.setDescription('Dummy - DO NOT USE')
sCmGenOrdinal64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 17), Ordinal64Low())
if mibBuilder.loadTexts: sCmGenOrdinal64Low.setStatus('current')
if mibBuilder.loadTexts: sCmGenOrdinal64Low.setDescription('Dummy - DO NOT USE')
sCmGenFixedLocaleDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 18), ScmFixedLocaleDisplayString())
if mibBuilder.loadTexts: sCmGenFixedLocaleDisplayString.setStatus('current')
if mibBuilder.loadTexts: sCmGenFixedLocaleDisplayString.setDescription('Dummy - DO NOT USE')
sCmGenGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 19), ScmGenGroupSupport())
if mibBuilder.loadTexts: sCmGenGroupSupport.setStatus('current')
if mibBuilder.loadTexts: sCmGenGroupSupport.setDescription('Dummy - DO NOT USE')
sCmGenLogFullPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 20), ScmGenLogFullPolicy())
if mibBuilder.loadTexts: sCmGenLogFullPolicy.setStatus('current')
if mibBuilder.loadTexts: sCmGenLogFullPolicy.setDescription('Dummy - DO NOT USE')
sCmGenOptionValueSyntax = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 21), ScmGenOptionValueSyntax())
if mibBuilder.loadTexts: sCmGenOptionValueSyntax.setStatus('current')
if mibBuilder.loadTexts: sCmGenOptionValueSyntax.setDescription('Dummy - DO NOT USE')
sCmGenReconfOptionState = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 22), ScmGenReconfOptionState())
if mibBuilder.loadTexts: sCmGenReconfOptionState.setStatus('current')
if mibBuilder.loadTexts: sCmGenReconfOptionState.setDescription('Dummy - DO NOT USE')
sCmGenRowPersistence = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 23), ScmGenRowPersistence())
if mibBuilder.loadTexts: sCmGenRowPersistence.setStatus('current')
if mibBuilder.loadTexts: sCmGenRowPersistence.setDescription('Dummy - DO NOT USE')
sCmGenSNMPDomain = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 24), ScmGenSNMPDomain())
if mibBuilder.loadTexts: sCmGenSNMPDomain.setStatus('current')
if mibBuilder.loadTexts: sCmGenSNMPDomain.setDescription('Dummy - DO NOT USE')
sCmGenSNMPVersion = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 25), ScmGenSNMPVersion())
if mibBuilder.loadTexts: sCmGenSNMPVersion.setStatus('current')
if mibBuilder.loadTexts: sCmGenSNMPVersion.setDescription('Dummy - DO NOT USE')
sCmGenSNMPv2ErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 26), ScmGenSNMPv2ErrorStatus())
if mibBuilder.loadTexts: sCmGenSNMPv2ErrorStatus.setStatus('current')
if mibBuilder.loadTexts: sCmGenSNMPv2ErrorStatus.setDescription('Dummy - DO NOT USE')
sCmGenGlobalUniqueID = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 27), ScmGlobalUniqueID())
if mibBuilder.loadTexts: sCmGenGlobalUniqueID.setStatus('current')
if mibBuilder.loadTexts: sCmGenGlobalUniqueID.setDescription('Dummy - DO NOT USE')
sCmGenFixedLocaleUtf8String = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 28), ScmFixedLocaleUtf8String())
if mibBuilder.loadTexts: sCmGenFixedLocaleUtf8String.setStatus('current')
if mibBuilder.loadTexts: sCmGenFixedLocaleUtf8String.setDescription('Dummy - DO NOT USE')
sCmGenMessageMapStringLabel = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 29), ScmGenMessageMapStringLabel())
if mibBuilder.loadTexts: sCmGenMessageMapStringLabel.setStatus('current')
if mibBuilder.loadTexts: sCmGenMessageMapStringLabel.setDescription('Dummy - DO NOT USE')
sCmGenNamedLocaleUtf8String = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 30), ScmNamedLocaleUtf8String())
if mibBuilder.loadTexts: sCmGenNamedLocaleUtf8String.setStatus('current')
if mibBuilder.loadTexts: sCmGenNamedLocaleUtf8String.setDescription('Dummy - DO NOT USE')
sCmGenNotifySchemeSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 31), ScmGenNotifySchemeSupport())
if mibBuilder.loadTexts: sCmGenNotifySchemeSupport.setStatus('current')
if mibBuilder.loadTexts: sCmGenNotifySchemeSupport.setDescription('Dummy - DO NOT USE')
sCmGenNotifySeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 32), ScmGenNotifySeverityFilter())
if mibBuilder.loadTexts: sCmGenNotifySeverityFilter.setStatus('current')
if mibBuilder.loadTexts: sCmGenNotifySeverityFilter.setDescription('Dummy - DO NOT USE')
sCmGenNotifyTrainingFilter = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 33), ScmGenNotifyTrainingFilter())
if mibBuilder.loadTexts: sCmGenNotifyTrainingFilter.setStatus('current')
if mibBuilder.loadTexts: sCmGenNotifyTrainingFilter.setDescription('Dummy - DO NOT USE')
sCmGenNotifyDetailType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 34), ScmGenNotifyDetailType())
if mibBuilder.loadTexts: sCmGenNotifyDetailType.setStatus('current')
if mibBuilder.loadTexts: sCmGenNotifyDetailType.setDescription('Dummy - DO NOT USE')
mibBuilder.exportSymbols("SAMSUNG-GENERAL-TC", ScmGenNotifySeverityFilter=ScmGenNotifySeverityFilter, sCmGenCardinal16=sCmGenCardinal16, sCmGenOrdinal16=sCmGenOrdinal16, sCmGenCardinal64High=sCmGenCardinal64High, sCmGeneralDummy=sCmGeneralDummy, ScmGenNotifyDetailType=ScmGenNotifyDetailType, sCmGenReconfOptionState=sCmGenReconfOptionState, sCmGenOrdinal32=sCmGenOrdinal32, Cardinal64Low=Cardinal64Low, scmGeneralTC=scmGeneralTC, ScmFixedLocaleUtf8String=ScmFixedLocaleUtf8String, sCmGenOrdinal64Low=sCmGenOrdinal64Low, sCmGenGlobalUniqueID=sCmGenGlobalUniqueID, PYSNMP_MODULE_ID=scmGeneralTC, sCmGenFixedLocaleUtf8String=sCmGenFixedLocaleUtf8String, ScmGlobalUniqueID=ScmGlobalUniqueID, sCmGenInteger64High=sCmGenInteger64High, sCmGenOrdinal64High=sCmGenOrdinal64High, Ordinal64Low=Ordinal64Low, ScmGenRowPersistence=ScmGenRowPersistence, Integer64Low=Integer64Low, CodedCountry=CodedCountry, sCmGenCounter64Low=sCmGenCounter64Low, scmGenZeroDotZero=scmGenZeroDotZero, sCmGenFixedLocaleDisplayString=sCmGenFixedLocaleDisplayString, sCmGenRowPersistence=sCmGenRowPersistence, sCmGenLogFullPolicy=sCmGenLogFullPolicy, Cardinal32=Cardinal32, ScmGenSNMPv2ErrorStatus=ScmGenSNMPv2ErrorStatus, CodeIndexedStringIndex=CodeIndexedStringIndex, sCmGenCodedCountry=sCmGenCodedCountry, sCmGenNotifyTrainingFilter=sCmGenNotifyTrainingFilter, ScmGenOptionValueSyntax=ScmGenOptionValueSyntax, ScmGenGroupSupport=ScmGenGroupSupport, sCmGenNotifySeverityFilter=sCmGenNotifySeverityFilter, sCmGenGauge64High=sCmGenGauge64High, zeroDotZero=zeroDotZero, Ordinal32=Ordinal32, ScmFixedLocaleDisplayString=ScmFixedLocaleDisplayString, ScmGenMessageMapStringLabel=ScmGenMessageMapStringLabel, sCmGenCounter64High=sCmGenCounter64High, sCmGenGroupSupport=sCmGenGroupSupport, sCmGenInteger64Low=sCmGenInteger64Low, sCmGenGauge64Low=sCmGenGauge64Low, sCmGenNamedLocaleUtf8String=sCmGenNamedLocaleUtf8String, sCmGenNotifyDetailType=sCmGenNotifyDetailType, Integer64High=Integer64High, Cardinal16=Cardinal16, sCmGenCodeIndexedStringIndex=sCmGenCodeIndexedStringIndex, Cardinal64High=Cardinal64High, ScmGenReconfOptionState=ScmGenReconfOptionState, ScmGenNotifyTrainingFilter=ScmGenNotifyTrainingFilter, sCmGenCardinal64Low=sCmGenCardinal64Low, sCmGenCodedLanguage=sCmGenCodedLanguage, sCmGenOptionValueSyntax=sCmGenOptionValueSyntax, sCmGenNotifySchemeSupport=sCmGenNotifySchemeSupport, sCmGenMessageMapStringLabel=sCmGenMessageMapStringLabel, ScmGenSNMPVersion=ScmGenSNMPVersion, sCmGenSNMPDomain=sCmGenSNMPDomain, sCmGenSNMPVersion=sCmGenSNMPVersion, Gauge64High=Gauge64High, sCmGenCardinal32=sCmGenCardinal32, Ordinal16=Ordinal16, sCmGenSNMPv2ErrorStatus=sCmGenSNMPv2ErrorStatus, Counter64High=Counter64High, Counter64Low=Counter64Low, ScmNamedLocaleUtf8String=ScmNamedLocaleUtf8String, ScmGenLogFullPolicy=ScmGenLogFullPolicy, ScmGenNotifySchemeSupport=ScmGenNotifySchemeSupport, CodedLanguage=CodedLanguage, Gauge64Low=Gauge64Low, ScmGenSNMPDomain=ScmGenSNMPDomain, Ordinal64High=Ordinal64High)
