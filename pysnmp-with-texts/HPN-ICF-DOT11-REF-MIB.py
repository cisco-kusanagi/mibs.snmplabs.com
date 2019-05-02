#
# PySNMP MIB module HPN-ICF-DOT11-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DOT11-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, Counter64, Unsigned32, iso, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "Counter64", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfDot11 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75))
hpnicfDot11.setRevisions(('2010-01-07 20:00', '2009-05-07 20:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfDot11.setRevisionsDescriptions(('Modified for CMCC of GuangDong province.', 'Modified for CMCC of GuangDong province.', 'Modified for CMCC(China Mobile Communication Corporation) requirements.', 'Modified to add new TC.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfDot11.setLastUpdated('201001072000Z')
if mibBuilder.loadTexts: hpnicfDot11.setOrganization('')
if mibBuilder.loadTexts: hpnicfDot11.setContactInfo('')
if mibBuilder.loadTexts: hpnicfDot11.setDescription('This MIB defines the root node and TC for 802.11 features. By this way, the MIB series for 802.11 will be easily maintained. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. IEEE 802.11a This is a high speed physical layer extension to the 802.11 standard on the 5 GHz band. IEEE 802.11b High-rate wireless LAN standard for wireless data transfer at up to 11 Mbps. IEEE 802.11g Higher Speed Physical Layer (PHY) Extension to IEEE 802.11b, will boost wireless LAN speed to 54 Mbps by using OFDM (orthogonal frequency division multiplexing). The IEEE 802.11g specification is backward compatible with the widely deployed IEEE 802.11b standard. When configure radio with as bg mode, it means that radio will be compatible to 802.11b and 802.11g. When configure radio with as g mode, it means that radio will be only compatible to 802.11g. IEEE 802.11i As 802.11 has lot of deficiency in wireless security domain, especially for enterprise custom, IEEE defined a new standard 802.11i to extend security feature of 802.11 standard. AKM The authentication and key management method defined by 802.11i, and which includes 802.1x and pre-shared key.')
class HpnicfDot11ObjectIDType(TextualConvention, OctetString):
    description = 'Represents AP identifier value type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class HpnicfDot11RadioScopeType(TextualConvention, Integer32):
    description = 'Represents radio value scope.'
    status = 'current'

class HpnicfDot11RadioType(TextualConvention, Integer32):
    description = 'Represents AP 802.11 radio type of 802.11a/b/g/n/ac as per the standard. The following values are supported: dot11a - 802.11a dot11b - 802.11b dot11g - 802.11g dot11n - 802.11n dot11gn - 802.11gn dot11an - 802.11an dot11ac - 802.11ac '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11n", 8), ("dot11gn", 16), ("dot11an", 32), ("dot11ac", 64))

class HpnicfDot11RadioType2(TextualConvention, Integer32):
    description = 'Represents AP 802.11 radio type of 802.11a/b/g/an/gn/ac as per the standard. The following values are supported: dot11a - 802.11a dot11b - 802.11b dot11g - 802.11g dot11an - 802.11an dot11gn - 802.11gn dot11ac - 802.11ac '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11an", 8), ("dot11gn", 16), ("dot11ac", 32))

class HpnicfDot11MACModeType(TextualConvention, Integer32):
    description = 'CAPWAP defines three kinds MAC modes for fit AP. The management packet will be exchanged between AP and AC by CAPWAP control tunnel. For data packet, the following MAC mode are supported: split - AP will tunnel 802.11 data message - to AC by CAPWAP, localtunnel - AP will convert data to 802.3, then tunnel - it to AC by CAPWAP, localbridge - AP will directly handle data packet without - sending to AC to process, fatAP - For fat AP, it will handle all 802.11 frames - by itself.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("split", 1), ("localtunnel", 2), ("localbridge", 3), ("fatAP", 4))

class HpnicfDot11ChannelScopeType(TextualConvention, Integer32):
    description = 'Represents the channel scope which consists of 802.11a/b/g.'
    status = 'current'

class HpnicfDot11NotifyReasonType(TextualConvention, OctetString):
    description = 'The explanation string is for the event notification of dot11.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class HpnicfDot11SSIDStringType(TextualConvention, OctetString):
    description = 'SSID is a string to identify ESS for wireless network.'
    status = 'current'

class HpnicfDot11ServicePolicyIDType(TextualConvention, Integer32):
    description = 'Represents the type of service policy ID.'
    status = 'current'

class HpnicfDot11SSIDEncryptModeType(TextualConvention, Integer32):
    description = 'Represents encryption mode for the specific ESS: The following values are supported: cleartxt - clear txt, cipher - WPA and 802.11i, ext - ext.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("cipher", 2), ("ext", 3))

class HpnicfDot11PreambleType(TextualConvention, Integer32):
    description = 'Represents the current radio preamble type. The following values are supported: long - long preambles, short - short preambles.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("long", 1), ("short", 2))

class HpnicfDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    description = 'Represents the Tx power level scope for 802.11.'
    status = 'current'

class HpnicfDot11RFModeType(TextualConvention, Integer32):
    description = 'Represents RF management mode. The following values are supported: manual - Configure RF parameter by manual, auto - Automaticall configure.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class HpnicfDot11TunnelSecSchemType(TextualConvention, Integer32):
    description = 'Represents which security scheme option is available for CAPWAP tunnel. The following values are supported: cleartxt - No encryption protection, dtls - Encrypted by DTLS, ipsec - Encrypted by IPSEC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("dtls", 2), ("ipsec", 3))

class HpnicfDot11SecIEStatusType(TextualConvention, Integer32):
    description = 'To enable the WPA Information element in the beacon and probe response frames sent by AP. The following values are supported: none - both wpa and rsn are disabled, rsn - only enable rsn, wpa - only enable wpa, all - both wpa and rsn are enabled, ext - only enable ext.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("rsn", 2), ("wpa", 3), ("all", 4), ("ext", 5))

class HpnicfDot11CipherType(TextualConvention, Integer32):
    description = 'Represents the frame encryption cipher types for frames on IEEE 802.11 radio interfaces. The MIB defines TC by referring to the 802.11i protocol. The following values are supported: none - clear text or no cipher method is configure, wep40 - 40-bit WEP key, tkip - WPA Temporal Key encryption, aesccmp - WPA AES CCMP encryption, wep104 - 104-bit WEP key, wpisms4 - ext encryption, wep128 - 128-bit WEP key.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 16, 32, 64, 128))
    namedValues = NamedValues(("none", 1), ("wep40", 2), ("tkip", 4), ("aesccmp", 16), ("wep104", 32), ("wpisms4", 64), ("wep128", 128))

class HpnicfDot11AuthenType(TextualConvention, Integer32):
    description = 'Represents the Authentication mode defined by 802.11. The following values are supported: none - No authentication mode configured, opensystem - In fact,no real authentication happened, sharedkey - System will use challenge message to - authenticate the access user, all - both open system and shared key.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("opensystem", 2), ("sharedkey", 3), ("all", 4))

class HpnicfDot11AKMType(TextualConvention, Integer32):
    description = 'Represents the key management mode defined by 802.11i. The following values are supported: none - No key management mode configured, psk - pre-shared key authentication, dot1x - 802.1x authentication, ext - ext.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("psk", 2), ("dot1x", 3), ("ext", 4))

class HpnicfDot11AssocFailType(TextualConvention, Integer32):
    description = 'Enumeration of the reasons for station association failure. including: unknownfailure - unknown failure, toomanyassoc - too many association, invalidie - information element is invalid, unsupportedrate - rate is not supported, unsupportedpwrcap - power capability is not supported, unsupportedcap - capability is not supported'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknownfailure", 1), ("toomanyassoc", 2), ("invalidie", 3), ("unsupportedrate", 4), ("unsupportedpwrcap", 5), ("unsupportedcap", 6))

class HpnicfDot11AuthorFailType(TextualConvention, Integer32):
    description = 'Enumeration of the reasons for station authorization failure. including: unknownfailure - unknown failure, invalidie - information element is invalid, rsnieversionunsupported - rsn information element version is not supported, wpaieversionunsupported - wpa information element version is not supported, groupcipherinvalid - group cipher is invalid, pairwisecipherinvalid - pairwise cipher is invalid, akminvalid - akm is invalid'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknownfailure", 1), ("invalidie", 2), ("rsnieversionunsupported", 3), ("wpaieversionunsupported", 4), ("groupcipherinvalid", 5), ("pairwisecipherinvalid", 6), ("akminvalid", 7))

class HpnicfDot11QosAcType(TextualConvention, Integer32):
    description = '802.11e defines four types of access category, including: acbk - for background access category, acbe - for besteffort access category, acvi - for voice access category, acvo - for video access category '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4))

class HpnicfDot11RadioElementIndex(TextualConvention, Unsigned32):
    description = 'Represents index of radio. For split architecture, It comprises two parts. The lowest 8 bits mean radio ID. The highest 8 bits are reserved. The highest 8 bits stand for AP ID. The meaning is shown as follows: 31 23 15 7 0 + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + | reserved | AP ID | radio ID | + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + For FAT AP, the type represents ifIndex of radio. '
    status = 'current'

class HpnicfDot11WorkMode(TextualConvention, Integer32):
    description = 'Work mode of device. In normal mode, the device will provide WLAN service. In monitor mode, the device will monitor the environment. In hybrid mode, the device will provide WLAN service while monitoring the environment.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("monitor", 2), ("hybrid", 3))

class HpnicfDot11CirMode(TextualConvention, Integer32):
    description = "The mode of committed information rate. 'static' means station will use the configured CIR separately. For example, if the CIR is 1Mbps, every station can enjoy 1Mbps. 'dynamic' means all stations will share the configured CIR in common."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class HpnicfDot11SaIntfDevType(TextualConvention, Integer32):
    description = 'The type of interference device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("microwave", 1), ("microwaveInverter", 2), ("bluetooth", 3), ("fixedFreqOthers", 4), ("fixedFreqCordlessPhone", 5), ("fixedFreqVideo", 6), ("fixedFreqAudio", 7), ("freqHopperOthers", 8), ("freqHopperCordlessBase", 9), ("freqHopperCordlessNetwork", 10), ("freqHopperXbox", 11), ("genericInterferer", 12))

class HpnicfDot11TruthValueCM(TextualConvention, Integer32):
    description = 'Represents a boolean value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dot11false", 0), ("dot11true", 1))

hpnicfDot11Common = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12))
hpnicfDot11ElementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1))
hpnicfDot11APElementTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot11APElementTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementTable.setDescription('This table is used to represent fat AP and AP template on AC as one kind of AP element.')
hpnicfDot11APElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"))
if mibBuilder.loadTexts: hpnicfDot11APElementEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementEntry.setDescription('Each entry contains information for each AP element.')
hpnicfDot11APElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfDot11APElementIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementIndex.setDescription('This object represents the index of AP element.')
hpnicfDot11APElementTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementTemplateName.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementTemplateName.setDescription('This object represents the template name of AP element.')
hpnicfDot11APElementSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementSerialID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementSerialID.setDescription('This object represents the serial ID of AP element.')
hpnicfDot11APElementModelAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementModelAlias.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APElementModelAlias.setDescription('This object represents the alias of AP element model name.')
hpnicfDot11RadioElementTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot11RadioElementTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11RadioElementTable.setDescription('This table is used to represent the radio element of fat AP and AC.')
hpnicfDot11RadioElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"), (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11RadioElementRadioNum"))
if mibBuilder.loadTexts: hpnicfDot11RadioElementEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11RadioElementEntry.setDescription('Each entry contains information for each radio element.')
hpnicfDot11RadioElementRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioNum.setDescription('This object represents the number of the radio element.')
hpnicfDot11RadioElementRadioPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioPolicy.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioPolicy.setDescription('This object represents the radio policy of the radio element.')
hpnicfDot11RadioElementRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioIndex.setDescription('This object represents the index of the radio element. On AC, the higher 24 bits stand for the AP index, and the last 8 bits stand for the radio index. On fat AP, the index stands for the interface index of radio interface.')
mibBuilder.exportSymbols("HPN-ICF-DOT11-REF-MIB", hpnicfDot11ElementGroup=hpnicfDot11ElementGroup, PYSNMP_MODULE_ID=hpnicfDot11, HpnicfDot11RadioType=HpnicfDot11RadioType, HpnicfDot11NotifyReasonType=HpnicfDot11NotifyReasonType, hpnicfDot11Common=hpnicfDot11Common, HpnicfDot11TunnelSecSchemType=HpnicfDot11TunnelSecSchemType, hpnicfDot11RadioElementRadioPolicy=hpnicfDot11RadioElementRadioPolicy, HpnicfDot11SSIDStringType=HpnicfDot11SSIDStringType, hpnicfDot11=hpnicfDot11, hpnicfDot11APElementTemplateName=hpnicfDot11APElementTemplateName, hpnicfDot11RadioElementRadioNum=hpnicfDot11RadioElementRadioNum, HpnicfDot11TxPwrLevelScopeType=HpnicfDot11TxPwrLevelScopeType, hpnicfDot11APElementTable=hpnicfDot11APElementTable, HpnicfDot11SSIDEncryptModeType=HpnicfDot11SSIDEncryptModeType, HpnicfDot11MACModeType=HpnicfDot11MACModeType, hpnicfDot11RadioElementRadioIndex=hpnicfDot11RadioElementRadioIndex, HpnicfDot11WorkMode=HpnicfDot11WorkMode, hpnicfDot11APElementModelAlias=hpnicfDot11APElementModelAlias, HpnicfDot11AssocFailType=HpnicfDot11AssocFailType, hpnicfDot11RadioElementEntry=hpnicfDot11RadioElementEntry, HpnicfDot11PreambleType=HpnicfDot11PreambleType, HpnicfDot11ChannelScopeType=HpnicfDot11ChannelScopeType, hpnicfDot11RadioElementTable=hpnicfDot11RadioElementTable, HpnicfDot11AuthorFailType=HpnicfDot11AuthorFailType, HpnicfDot11RadioScopeType=HpnicfDot11RadioScopeType, HpnicfDot11ServicePolicyIDType=HpnicfDot11ServicePolicyIDType, HpnicfDot11RFModeType=HpnicfDot11RFModeType, HpnicfDot11RadioElementIndex=HpnicfDot11RadioElementIndex, HpnicfDot11SaIntfDevType=HpnicfDot11SaIntfDevType, HpnicfDot11ObjectIDType=HpnicfDot11ObjectIDType, hpnicfDot11APElementEntry=hpnicfDot11APElementEntry, HpnicfDot11TruthValueCM=HpnicfDot11TruthValueCM, HpnicfDot11CirMode=HpnicfDot11CirMode, hpnicfDot11APElementSerialID=hpnicfDot11APElementSerialID, HpnicfDot11SecIEStatusType=HpnicfDot11SecIEStatusType, HpnicfDot11QosAcType=HpnicfDot11QosAcType, HpnicfDot11RadioType2=HpnicfDot11RadioType2, hpnicfDot11APElementIndex=hpnicfDot11APElementIndex, HpnicfDot11AKMType=HpnicfDot11AKMType, HpnicfDot11AuthenType=HpnicfDot11AuthenType, HpnicfDot11CipherType=HpnicfDot11CipherType)
