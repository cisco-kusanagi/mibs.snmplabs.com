#
# PySNMP MIB module CISCO-VOICE-COMMON-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
callActiveSetupTime, callActiveIndex = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "callActiveSetupTime", "callActiveIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, TimeTicks, MibIdentifier, Integer32, Bits, Unsigned32, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "IpAddress", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoVoiceCommonDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 55))
ciscoVoiceCommonDialControlMIB.setRevisions(('2010-06-30 00:00', '2009-03-18 00:00', '2008-07-02 00:00', '2007-06-26 00:00', '2005-08-16 00:00', '2005-03-06 00:00', '2003-03-11 00:00', '2001-10-06 00:00', '2001-09-05 00:00', '2000-07-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setRevisionsDescriptions(('Added CvcCallReferenceIdOrZero textual convention. Added aaclc and aacld enum to CvcCoderTypeRate and CvcSpeechCoderRate textual conventions.', '[1] Added acronym for iSAC codec [2] Added iSAC enum to CvcSpeechCoderRate and CvcCoderTypeRate textual conventions.', "[1] Added '-- obsolete' to description of 'g722' enum from CvcCoderTypeRate. [2] Added new enum values 'g722r4800', 'g722r5600' and 'g722r6400' to CvcCoderTypeRate. [3] Added new enum values 'g722r4800', 'g722r5600' and 'g722r6400' to CvcSpeechCoderRate.", '[1] Imported TEXTUAL-CONVENTION from SNMPv2-TC. [2] Added acronyms for GSM AMR-NB and iLBC codecs [3] Added llcc, gsmAmrNb, iLBC, iLBCr15200 and iLBCr13330 enums to CvcSpeechCoderRate textual conventions. [4] Added llcc, gsmAmrNb, g722, iLBC, iLBCr15200 and iLBCr13330 enums to CvcCoderTypeRate textual conventions. [5] Added REFERENCE clause to CvcSpeechCoderRate and CvcCoderTypeRate textual conventions for GSM AMR-NB and iLBC codecs.', 'Added CvcH320CallType and CvcVideoCoderRate objects. Added g722 enum to CvcCoderTypeRate textual conventions.', 'Added gsmAmrNb enum to CvcSpeechCoderRate and CvcCoderTypeRate textual conventions.', "Added new enum value 'llcc', to CvcSpeechCoderRate and CvcCoderTypeRate textual-conventions.", "[1] Added new enum value 'g726r40000',to CvcSpeechCoderRate's and CvcCoderTypeRate's textual-conventions. [2] Replaced 'clearch' enum with 'clearChannel' enum. [3] Replaced 'codec is disabled' comment for clearChannel enum with 'CLEAR channel codec'.", "[1] Added new enum value, 'clearch,' to CvcSpeechCoderRate's and CvcCoderTypeRate's textual-conventions. [2] Added new enum value, 'gr303,' to CvcInBandSignaling's textual-conventions [3] Modified cvCommonDcCallActiveInBandSignaling's and cvCommonDcCallHistoryInBandSignaling's description to indicate value is valid only for Connection Trunk calls.", 'Add new objects for handling the following features: [1] Calling Name display for call active and history table. [2] Caller ID Block, which indicates whether the Caller ID feature is in using, for call active and history table.',))
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setLastUpdated('201006300000Z')
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setDescription('This MIB module contains voice related objects that are common across more than one network encapsulation i.e VoIP, VoATM and VoFR. *** ABBREVIATIONS, ACRONYMS AND SYMBOLS *** GSM - Global System for Mobile Communication AMR-NB - Adaptive Multi Rate - Narrow Band iLBC - internet Low Bitrate Codec iSAC - internet Speech Audio Codec')
cvCommonDcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1))
cvCommonDcCallActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1))
cvCommonDcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2))
class CvcSpeechCoderRate(TextualConvention, Integer32):
    reference = '[1] RFC 3267: For introduction about GSM AMR-NB codec, section 3.1 [2] RFC 3952: For introduction about iLBC codec, section 2'
    description = 'This object specifies the most desirable codec of speech for the VoIP, VoATM or VoFR peer. g729r8000 - pre-IETF G.729 8000 bps g729Ar8000 - G.729 ANNEX-A 8000 bps g726r16000 - G.726 16000 bps g726r24000 - G.726 24000 bps g726r32000 - G.726 32000 bps g711ulawr64000 - G.711 u-Law 64000 bps g711Alawr64000 - G.711 A-Law 64000 bps g728r16000 - G.728 16000 bps g723r6300 - G.723.1 6300 bps g723r5300 - G.723.1 5300 bps gsmr13200 - GSM Full rate 13200 bps g729Br8000 - G.729 ANNEX-B 8000 bps g729ABr8000 - G.729 ANNEX-A & B 8000 bps g723Ar6300 - G723.1 Annex A 6300 bps g723Ar5300 - G723.1 Annex A 5300 bps g729IETFr8000 - IETF G.729 8000 bps gsmeEr12200 - GSM Enhanced Full Rate 12200 bps clearChannel - CLEAR Channel codec g726r40000 - G.726 40000 bps llcc - Lossless compression codec gsmAmrNb - GSM AMR-NB 4750 - 12200 bps iLBC - iILBC 13330 or 15200 bps iLBCr15200 - iLBC 15200 bps iLBCr13330 - iLBC 13330 bps g722r4800 - G.722 (modes 1, 2, 3) g722r5600 - G.722 (modes 1, 2) g722r6400 - G.722 (mode 1) iSAC - iSAC (10 to 32 kbps) aaclc - AAC-LC Advanced Audio Coding Low Complexity aacld - AAC-LD MPEG-4 Low Delay Audio Coder'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("g729r8000", 1), ("g729Ar8000", 2), ("g726r16000", 3), ("g726r24000", 4), ("g726r32000", 5), ("g711ulawr64000", 6), ("g711Alawr64000", 7), ("g728r16000", 8), ("g723r6300", 9), ("g723r5300", 10), ("gsmr13200", 11), ("g729Br8000", 12), ("g729ABr8000", 13), ("g723Ar6300", 14), ("g723Ar5300", 15), ("g729IETFr8000", 16), ("gsmeEr12200", 17), ("clearChannel", 18), ("g726r40000", 19), ("llcc", 20), ("gsmAmrNb", 21), ("iLBC", 22), ("iLBCr15200", 23), ("iLBCr13330", 24), ("g722r4800", 25), ("g722r5600", 26), ("g722r6400", 27), ("iSAC", 28), ("aaclc", 29), ("aacld", 30))

class CvcFaxTransmitRate(TextualConvention, Integer32):
    description = "This object specifies the default transmit rate of FAX for the VoIP, VoATM or VOFR peer. If the value of this object is 'none', then the Fax relay feature is disabled ; otherwise the Fax relay feature is enabled. none - Fax relay is disabled. voiceRate - the fastest possible fax rate not exceed the configured voice rate. fax2400 - 2400 bps FAX transmit rate. fax4800 - 4800 bps FAX transmit rate. fax7200 - 7200 bps FAX transmit rate. fax9600 - 9600 bps FAX transmit rate. fax14400 - 14400 bps FAX transmit rate. fax12000 - 12000 bps FAX transmit rate."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("voiceRate", 2), ("fax2400", 3), ("fax4800", 4), ("fax7200", 5), ("fax9600", 6), ("fax14400", 7), ("fax12000", 8))

class CvcCoderTypeRate(TextualConvention, Integer32):
    reference = '[1] RFC 3267: For introduction about GSM AMR-NB codec, section 3.1 [2] RFC 3952: For introduction about iLBC codec, section 2'
    description = 'Represents the coder type-rate for voice/fax compression used during a call. *** ABBREVIATIONS, ACRONYMS AND SYMBOLS *** GSM - Global System for Mobile Communication AMR-NB - Adaptive Multi Rate - Narrow Band iLBC - internet Low Bitrate Codec iSAC - internet Speech Audio Codec other - none of the following. fax2400 - FAX 2400 bps fax4800 - FAX 4800 bps fax7200 - FAX 7200 bps fax9600 - FAX 9600 bps fax14400 - FAX 14400 bps fax12000 - FAX 12000 bps g729r8000 - G.729 8000 bps (pre-IETF bit ordering) g729Ar8000 - G.729 ANNEX-A 8000 bps g726r16000 - G.726 16000 bps g726r24000 - G.726 24000 bps g726r32000 - G.726 32000 bps g711ulawr64000 - G.711 u-Law 64000 bps g711Alawr64000 - G.711 A-Law 64000 bps g728r16000 - G.728 16000 bps g723r6300 - G.723.1 6300 bps g723r5300 - G.723.1 5300 bps gsmr13200 - GSM full rate 13200 bps g729Br8000 - G.729 ANNEX-B 8000 bps g729ABr8000 - G.729 ANNEX-A & B 8000 bps g723Ar6300 - G723.1 Annex A 6300 bps g723Ar5300 - G723.1 Annex A 5300 bps ietfg729r8000 - G.729 8000 bps (IETF bit ordering) gsmeEr12200 - GSM Enhanced Full Rate 12200 bps clearChannel - CLEAR channel codec g726r40000 - G.726 40000 bps llcc - Lossless compression codec gsmAmrNb - GSM AMR-NB 4750 - 12200 bps g722 - G.722 2400 - 6400 bps iLBC - iILBC 13330 or 15200 bps iLBCr15200 - iLBC 15200 bps iLBCr13330 - iLBC 13330 bps g722r4800 - G.722 (modes 1, 2, 3) g722r5600 - G.722 (modes 1, 2) g722r6400 - G.722 (mode 1) iSAC - iSAC (10 to 32 kbps) aaclc - AAC-LC Advanced Audio Coding Low Complexity aacld - AAC-LD MPEG-4 Low Delay Audio Coder'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("other", 1), ("fax2400", 2), ("fax4800", 3), ("fax7200", 4), ("fax9600", 5), ("fax14400", 6), ("fax12000", 7), ("g729r8000", 10), ("g729Ar8000", 11), ("g726r16000", 12), ("g726r24000", 13), ("g726r32000", 14), ("g711ulawr64000", 15), ("g711Alawr64000", 16), ("g728r16000", 17), ("g723r6300", 18), ("g723r5300", 19), ("gsmr13200", 20), ("g729Br8000", 21), ("g729ABr8000", 22), ("g723Ar6300", 23), ("g723Ar5300", 24), ("ietfg729r8000", 25), ("gsmeEr12200", 26), ("clearChannel", 27), ("g726r40000", 28), ("llcc", 29), ("gsmAmrNb", 30), ("g722", 31), ("iLBC", 32), ("iLBCr15200", 33), ("iLBCr13330", 34), ("g722r4800", 35), ("g722r5600", 36), ("g722r6400", 37), ("iSAC", 38), ("aaclc", 39), ("aacld", 40))

class CvcGUid(TextualConvention, OctetString):
    description = 'Represents a Global Call Identifier. The global call identifier is used as an unique identifier for an end-to-end call. A zero length CvcGUid indicates no value for the global call identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class CvcInBandSignaling(TextualConvention, Integer32):
    description = 'Represents the type of in-band signaling used between the two end points of the call and is used to inform the router how interpret the ABCD signaling data bits passed as part of the voice payload data. cas - specifies interpret the signaling bits as North American Channel Associated signaling. none - specifies no in-band signaling or signaling is being done via an external method (e.g CCS). cept - specifies interpret the signaling bits as MELCAS transparent - specifies do not interpret or translate the signaling bits. gr303 - specifies interpret the signaling bits as GR303'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cas", 1), ("none", 2), ("cept", 3), ("transparent", 4), ("gr303", 5))

class CvcCallReferenceIdOrZero(TextualConvention, Unsigned32):
    description = 'A call reference ID correlates the video and audio call entries that belong to the same endpoint. In other words, if an audio call entry and a video call entry have the same call reference ID, these entries belong to the same endpoint. Because an audio-only endpoint creates only one call entry, call reference ID is not necessary and is set to zero. A call reference ID with value greater than zero signifies a video call, the value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero include audio calls.'
    status = 'current'

class CvcH320CallType(TextualConvention, Integer32):
    description = 'This object specifies the H320 call type of a voice call.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("primary", 1), ("secondary", 2))

class CvcVideoCoderRate(TextualConvention, Integer32):
    description = 'This object specifies the encoding type used to compress the video data of the voice call.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("h261", 1), ("h263", 2), ("h263plus", 3), ("h264", 4))

cvCommonDcCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1), )
if mibBuilder.loadTexts: cvCommonDcCallActiveTable.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveTable.setDescription('This table is a common extension to the call active table of IETF Dial Control MIB. It contains common call leg information about a network call leg.')
cvCommonDcCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: cvCommonDcCallActiveEntry.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveEntry.setDescription('The common information regarding a single network call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the call establishment to a network dialpeer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted.')
cvCommonDcCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveConnectionId.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveConnectionId.setDescription('The global call identifier for the network call.')
cvCommonDcCallActiveVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveVADEnable.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveVADEnable.setDescription('The object indicates whether or not the VAD (Voice Activity Detection) is enabled for the voice call.')
cvCommonDcCallActiveCoderTypeRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 3), CvcCoderTypeRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCoderTypeRate.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveCoderTypeRate.setDescription('The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call.')
cvCommonDcCallActiveCodecBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCodecBytes.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveCodecBytes.setDescription('Specifies the payload size of the voice packet.')
cvCommonDcCallActiveInBandSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 5), CvcInBandSignaling()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveInBandSignaling.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveInBandSignaling.setDescription('Specifies the type of in-band signaling being used on the call. This object is instantiated only for Connection Trunk calls.')
cvCommonDcCallActiveCallingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCallingName.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveCallingName.setDescription('The calling party name this call is connected to. If the name is not available, then it will have a length of zero.')
cvCommonDcCallActiveCallerIDBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCallerIDBlock.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallActiveCallerIDBlock.setDescription('The object indicates whether or not the caller ID feature is blocked for this voice call.')
cvCommonDcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1), )
if mibBuilder.loadTexts: cvCommonDcCallHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryTable.setDescription('This table is the Common extension to the call history table of IETF Dial Control MIB. It contains Common call leg information about a network call leg.')
cvCommonDcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvCommonDcCallHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryEntry.setDescription('The common information regarding a single network call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains information for the call establishment to a network dialpeer. The entry is deleted when its associated call history entry in the IETF Dial Control MIB is deleted.')
cvCommonDcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryConnectionId.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryConnectionId.setDescription('The global call identifier for the gateway call.')
cvCommonDcCallHistoryVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryVADEnable.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryVADEnable.setDescription('The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call.')
cvCommonDcCallHistoryCoderTypeRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 3), CvcCoderTypeRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCoderTypeRate.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryCoderTypeRate.setDescription('The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call.')
cvCommonDcCallHistoryCodecBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCodecBytes.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryCodecBytes.setDescription('Specifies the payload size of the voice packet.')
cvCommonDcCallHistoryInBandSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 5), CvcInBandSignaling()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryInBandSignaling.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryInBandSignaling.setDescription('Specifies the type of in-band signaling used on the call. This object is instantiated only for Connection Trunk calls.')
cvCommonDcCallHistoryCallingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallingName.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallingName.setDescription('The calling party name this call is connected to. If the name is not available, then it will have a length of zero.')
cvCommonDcCallHistoryCallerIDBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallerIDBlock.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallerIDBlock.setDescription('The object indicates whether or not the caller ID feature is blocked for this voice call.')
cvCommonDcMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 2))
cvCommonDcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 2, 0))
cvCommonDcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3))
cvCommonDcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1))
cvCommonDcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2))
cvCommonDcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 1)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcMIBCompliance = cvCommonDcMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cvCommonDcMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO VOICE COMMON MIB')
cvCommonDcMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 2)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcMIBComplianceRev1 = cvCommonDcMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcMIBComplianceRev1.setDescription('The compliance statement for entities which implement the CISCO VOICE COMMON MIB')
cvCommonDcCallGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 1)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcCallGroup = cvCommonDcCallGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cvCommonDcCallGroup.setDescription('A collection of objects providing the common network call leg information.')
cvCommonDcCallGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 2)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallingName"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallerIDBlock"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallingName"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallerIDBlock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcCallGroup1 = cvCommonDcCallGroup1.setStatus('current')
if mibBuilder.loadTexts: cvCommonDcCallGroup1.setDescription('A collection of objects providing the common network call leg information.')
mibBuilder.exportSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", cvCommonDcCallHistoryCallingName=cvCommonDcCallHistoryCallingName, cvCommonDcCallActiveEntry=cvCommonDcCallActiveEntry, cvCommonDcCallHistoryCoderTypeRate=cvCommonDcCallHistoryCoderTypeRate, CvcVideoCoderRate=CvcVideoCoderRate, cvCommonDcCallHistoryVADEnable=cvCommonDcCallHistoryVADEnable, cvCommonDcCallHistoryInBandSignaling=cvCommonDcCallHistoryInBandSignaling, cvCommonDcMIBNotificationPrefix=cvCommonDcMIBNotificationPrefix, CvcCoderTypeRate=CvcCoderTypeRate, cvCommonDcCallActiveCodecBytes=cvCommonDcCallActiveCodecBytes, CvcGUid=CvcGUid, cvCommonDcCallHistoryCodecBytes=cvCommonDcCallHistoryCodecBytes, cvCommonDcMIBComplianceRev1=cvCommonDcMIBComplianceRev1, cvCommonDcCallActive=cvCommonDcCallActive, PYSNMP_MODULE_ID=ciscoVoiceCommonDialControlMIB, cvCommonDcCallHistory=cvCommonDcCallHistory, cvCommonDcCallActiveCallingName=cvCommonDcCallActiveCallingName, cvCommonDcCallActiveVADEnable=cvCommonDcCallActiveVADEnable, cvCommonDcCallActiveCallerIDBlock=cvCommonDcCallActiveCallerIDBlock, cvCommonDcCallHistoryCallerIDBlock=cvCommonDcCallHistoryCallerIDBlock, cvCommonDcMIBCompliance=cvCommonDcMIBCompliance, cvCommonDcCallGroup=cvCommonDcCallGroup, CvcSpeechCoderRate=CvcSpeechCoderRate, cvCommonDcMIBGroups=cvCommonDcMIBGroups, CvcInBandSignaling=CvcInBandSignaling, CvcCallReferenceIdOrZero=CvcCallReferenceIdOrZero, cvCommonDcMIBObjects=cvCommonDcMIBObjects, cvCommonDcMIBCompliances=cvCommonDcMIBCompliances, CvcH320CallType=CvcH320CallType, cvCommonDcCallHistoryEntry=cvCommonDcCallHistoryEntry, cvCommonDcCallActiveCoderTypeRate=cvCommonDcCallActiveCoderTypeRate, cvCommonDcCallGroup1=cvCommonDcCallGroup1, cvCommonDcCallHistoryTable=cvCommonDcCallHistoryTable, cvCommonDcCallActiveConnectionId=cvCommonDcCallActiveConnectionId, cvCommonDcMIBConformance=cvCommonDcMIBConformance, CvcFaxTransmitRate=CvcFaxTransmitRate, cvCommonDcMIBNotifications=cvCommonDcMIBNotifications, cvCommonDcCallActiveTable=cvCommonDcCallActiveTable, ciscoVoiceCommonDialControlMIB=ciscoVoiceCommonDialControlMIB, cvCommonDcCallActiveInBandSignaling=cvCommonDcCallActiveInBandSignaling, cvCommonDcCallHistoryConnectionId=cvCommonDcCallHistoryConnectionId)
