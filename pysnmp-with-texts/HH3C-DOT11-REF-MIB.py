#
# PySNMP MIB module HH3C-DOT11-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DOT11-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Gauge32, ObjectIdentity, TimeTicks, MibIdentifier, Counter32, Integer32, Unsigned32, iso, Bits, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "iso", "Bits", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cDot11 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 75))
hh3cDot11.setRevisions(('2010-01-07 20:00', '2009-05-07 20:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cDot11.setRevisionsDescriptions(('Modified for CMCC of GuangDong province.', 'Modified for CMCC of GuangDong province.', 'Modified for CMCC(China Mobile Communication Corporation) requirements.', 'Modified to add new TC.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cDot11.setLastUpdated('201001072000Z')
if mibBuilder.loadTexts: hh3cDot11.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cDot11.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cDot11.setDescription('This MIB defines the root node and TC for 802.11 features. By this way, the MIB series for 802.11 will be easily maintained. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. IEEE 802.11a This is a high speed physical layer extension to the 802.11 standard on the 5 GHz band. IEEE 802.11b High-rate wireless LAN standard for wireless data transfer at up to 11 Mbps. IEEE 802.11g Higher Speed Physical Layer (PHY) Extension to IEEE 802.11b, will boost wireless LAN speed to 54 Mbps by using OFDM (orthogonal frequency division multiplexing). The IEEE 802.11g specification is backward compatible with the widely deployed IEEE 802.11b standard. When configure radio with as bg mode, it means that radio will be compatible to 802.11b and 802.11g. When configure radio with as g mode, it means that radio will be only compatible to 802.11g. IEEE 802.11i As 802.11 has lot of deficiency in wireless security domain, especially for enterprise custom, IEEE defined a new standard 802.11i to extend security feature of 802.11 standard. AKM The authentication and key management method defined by 802.11i, and which includes 802.1x and pre-shared key.')
class Hh3cDot11ObjectIDType(TextualConvention, OctetString):
    description = 'Represents AP identifier value type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class Hh3cDot11RadioScopeType(TextualConvention, Integer32):
    description = 'Represents radio value scope.'
    status = 'current'

class Hh3cDot11RadioType(TextualConvention, Integer32):
    description = 'Represents AP 802.11 radio type of 802.11a/b/g/n as per the standard. The following values are supported: dot11a(1) - 802.11a dot11b(2) - 802.11b dot11g(4) - 802.11g dot11n(8) - 802.11n '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11n", 8), ("dot11gn", 16), ("dot11an", 32))

class Hh3cDot11MACModeType(TextualConvention, Integer32):
    description = 'CAPWAP defines three kinds MAC mode for fit AP. The management packet will be exchanged between AP and AC by CAPWAP control tunnel. For data packet, the following MAC mode are supported: split(1) - AP will tunnel 802.11 data message - to AC by CAPWAP, localtunnel(2) - AP will convert data to 802.3, then tunnel - it to AC by CAPWAP, localbridge(3) - AP will directly handle data packet without - sending to AC to process, fatAP - For fat AP, it will handle all 802.11 frames - by itself.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("split", 1), ("localtunnel", 2), ("localbridge", 3), ("fatAP", 4))

class Hh3cDot11ChannelScopeType(TextualConvention, Integer32):
    description = 'Represents the channel scope which consists of 802.11a/b/g.'
    status = 'current'

class Hh3cDot11NotifyReasonType(TextualConvention, OctetString):
    description = 'The explanation string is for the event notification of dot11.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Hh3cDot11SSIDStringType(TextualConvention, OctetString):
    description = 'SSID is a string to identify ESS for wireless network.'
    status = 'current'

class Hh3cDot11ServicePolicyIDType(TextualConvention, Integer32):
    description = 'Represents the type of service policy ID.'
    status = 'current'

class Hh3cDot11SSIDEncryptModeType(TextualConvention, Integer32):
    description = 'Represents encryption mode for the specific ESS: The following values are supported: cleartxt(1) - clear txt, cipher(2) - WPA and 802.11i wapi(3) - WAPI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("cipher", 2), ("wapi", 3))

class Hh3cDot11PreambleType(TextualConvention, Integer32):
    description = 'Represents the current radio preamble type. The following values are supported: long(1) - long preambles, short(2) - short preambles.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("long", 1), ("short", 2))

class Hh3cDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    description = 'Represents the Tx power level scope for 802.11.'
    status = 'current'

class Hh3cDot11RFModeType(TextualConvention, Integer32):
    description = 'Represents RF management mode. The following values are supported: manual(1) - Configure RF parameter by manual, auto(2) - Automaticall configure.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class Hh3cDot11TunnelSecSchemType(TextualConvention, Integer32):
    description = 'Represents which security scheme option is available for CAPWAP tunnel. The following values are supported: cleartxt(1) - No encryption protection, dtls(2) - Encrypted by DTLS, ipsec(3) - Encrypted by IPSEC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("dtls", 2), ("ipsec", 3))

class Hh3cDot11SecIEStatusType(TextualConvention, Integer32):
    description = 'To enable the WPA Information element in the beacon and probe response frames sent by AP. The following values are supported: none(1) - both wpa and rsn are disabled, rsn(2) - only enable rsn, wpa(3) - only enable wpa, all(4) - both wpa and rsn are enabled, wapi(5) - only enable wapi.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("rsn", 2), ("wpa", 3), ("all", 4), ("wapi", 5))

class Hh3cDot11CipherType(TextualConvention, Integer32):
    description = 'Represents the frame encryption cipher types for frames on IEEE 802.11 radio interfaces. The MIB defines TC by referring to the 802.11i protocol. The following values are supported: none(1) - clear text or no cipher method is configure, wep40(2) - 40-bit WEP key, tkip(4) - WPA Temporal Key encryption, aesccmp(16) - WPA AES CCMP encryption, wep104(32) - 104-bit WEP key, wpisms4(64) - WAPI encryption, wep128(128) - 128-bit WEP key.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 16, 32, 64, 128))
    namedValues = NamedValues(("none", 1), ("wep40", 2), ("tkip", 4), ("aesccmp", 16), ("wep104", 32), ("wpisms4", 64), ("wep128", 128))

class Hh3cDot11AuthenType(TextualConvention, Integer32):
    description = 'Represents the Authentication mode defined by 802.11. The following values are supported: none(1) - No authentication mode configured, opensystem(2) - In fact,no real authentication happened, sharedkey(3) - System will use challenge message to - authenticate the access user, all(4) - both open system and shared key.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("opensystem", 2), ("sharedkey", 3), ("all", 4))

class Hh3cDot11AKMType(TextualConvention, Integer32):
    description = 'Represents the key management mode defined by 802.11i. The following values are supported: none(1) - No key management mode configured, psk(2) - pre-shared key authentication, dot1x(3) - 802.1x authentication, wapi(4) - WAPI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("psk", 2), ("dot1x", 3), ("wapi", 4))

class Hh3cDot11AssocFailType(TextualConvention, Integer32):
    description = 'Enumeration of the reasons for station association failure. including: unknownfailure(1) - unknown failure, toomanyassoc(2) - too many association, invalidie(3) - information element is invalid, unsupportedrate(4) - rate is not supported, unsupportedpwrcap(5) - power capability is not supported unsupportedcap(6) - capability is not supported'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknownfailure", 1), ("toomanyassoc", 2), ("invalidie", 3), ("unsupportedrate", 4), ("unsupportedpwrcap", 5), ("unsupportedcap", 6))

class Hh3cDot11AuthorFailType(TextualConvention, Integer32):
    description = 'Enumeration of the reasons for station authorization failure. including: unknownfailure(1) - unknown failure, invalidie(2) - information element is invalid, rsnieversionunsupported(3) - rsn information element version is not supported, wpaieversionunsupported(4) - wpa information element version is not supported, groupcipherinvalid(5) - group cipher is invalid, pairwisecipherinvalid(6) - pairwise cipher is invalid, akminvalid(7) - akm is invalid'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknownfailure", 1), ("invalidie", 2), ("rsnieversionunsupported", 3), ("wpaieversionunsupported", 4), ("groupcipherinvalid", 5), ("pairwisecipherinvalid", 6), ("akminvalid", 7))

class Hh3cDot11QosAcType(TextualConvention, Integer32):
    description = '802.11e defines four types of access category, including: acbk(1) - for background access category, acbe(2) - for besteffort access category, acvi(3) - for voice access category, acvo(4) - for video access category '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4))

class Hh3cDot11RadioElementIndex(TextualConvention, Unsigned32):
    description = 'Represents index of radio. For split architecture, It comprises two parts. The lowest 8 bits mean radio ID. The highest 8 bits are reserved. The highest 8 bits stand for AP ID. The meaning is shown as follows: 31 23 15 7 0 + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + | reserved | AP ID | radio ID | + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + For FAT AP, the type represents ifIndex of radio. '
    status = 'current'

class Hh3cDot11WorkMode(TextualConvention, Integer32):
    description = 'Work mode of device. In normal mode, the device will provide WLAN service. In monitor mode, the device will monitor the environment. In hybrid mode, the device will provide WLAN service while monitoring the environment.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("monitor", 2), ("hybrid", 3))

class Hh3cDot11CirMode(TextualConvention, Integer32):
    description = "The mode of committed information rate. 'static' means station will use the configured CIR seperately. For example, if the CIR is 1Mbps, every station can enjoy 1Mbps. 'dynamic' means all stations will share the configured CIR in common."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

hh3cDot11Common = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12))
hh3cDot11ElementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1))
hh3cDot11APElementTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1), )
if mibBuilder.loadTexts: hh3cDot11APElementTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementTable.setDescription('This table is used to represent fat AP and AP template on AC as one kind of AP element.')
hh3cDot11APElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1), ).setIndexNames((0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"))
if mibBuilder.loadTexts: hh3cDot11APElementEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementEntry.setDescription('Each entry contains information for each AP element.')
hh3cDot11APElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cDot11APElementIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementIndex.setDescription('This object represents the index of AP element.')
hh3cDot11APElementTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementTemplateName.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementTemplateName.setDescription('This object represents the template name of AP element.')
hh3cDot11APElementSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementSerialID.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementSerialID.setDescription('This object represents the serial ID of AP element.')
hh3cDot11APElementModelAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementModelAlias.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11APElementModelAlias.setDescription('This object represents the alias of AP element model name.')
hh3cDot11RadioElementTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2), )
if mibBuilder.loadTexts: hh3cDot11RadioElementTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11RadioElementTable.setDescription('This table is used to represent the radio element of fat AP and AC.')
hh3cDot11RadioElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1), ).setIndexNames((0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"), (0, "HH3C-DOT11-REF-MIB", "hh3cDot11RadioElementRadioNum"))
if mibBuilder.loadTexts: hh3cDot11RadioElementEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11RadioElementEntry.setDescription('Each entry contains information for each radio element.')
hh3cDot11RadioElementRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioNum.setDescription('This object represents the number of the radio element.')
hh3cDot11RadioElementRadioPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioPolicy.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioPolicy.setDescription('This object represents the radio policy of the radio element.')
hh3cDot11RadioElementRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioIndex.setDescription('This object represents the index of the radio element. On AC, the higher 24 bits stand for the AP index, and the last 8 bits stand for the radio index. On fat AP, the index stands for the interface index of radio interface.')
mibBuilder.exportSymbols("HH3C-DOT11-REF-MIB", Hh3cDot11RadioElementIndex=Hh3cDot11RadioElementIndex, hh3cDot11APElementSerialID=hh3cDot11APElementSerialID, hh3cDot11APElementTable=hh3cDot11APElementTable, hh3cDot11APElementEntry=hh3cDot11APElementEntry, Hh3cDot11WorkMode=Hh3cDot11WorkMode, hh3cDot11=hh3cDot11, hh3cDot11APElementTemplateName=hh3cDot11APElementTemplateName, Hh3cDot11SecIEStatusType=Hh3cDot11SecIEStatusType, PYSNMP_MODULE_ID=hh3cDot11, Hh3cDot11SSIDEncryptModeType=Hh3cDot11SSIDEncryptModeType, Hh3cDot11RFModeType=Hh3cDot11RFModeType, Hh3cDot11AKMType=Hh3cDot11AKMType, Hh3cDot11SSIDStringType=Hh3cDot11SSIDStringType, hh3cDot11RadioElementTable=hh3cDot11RadioElementTable, Hh3cDot11RadioScopeType=Hh3cDot11RadioScopeType, hh3cDot11RadioElementRadioIndex=hh3cDot11RadioElementRadioIndex, Hh3cDot11QosAcType=Hh3cDot11QosAcType, Hh3cDot11AuthenType=Hh3cDot11AuthenType, Hh3cDot11CirMode=Hh3cDot11CirMode, hh3cDot11RadioElementRadioPolicy=hh3cDot11RadioElementRadioPolicy, Hh3cDot11ServicePolicyIDType=Hh3cDot11ServicePolicyIDType, Hh3cDot11ObjectIDType=Hh3cDot11ObjectIDType, hh3cDot11APElementIndex=hh3cDot11APElementIndex, Hh3cDot11ChannelScopeType=Hh3cDot11ChannelScopeType, hh3cDot11RadioElementEntry=hh3cDot11RadioElementEntry, Hh3cDot11AssocFailType=Hh3cDot11AssocFailType, hh3cDot11ElementGroup=hh3cDot11ElementGroup, hh3cDot11APElementModelAlias=hh3cDot11APElementModelAlias, Hh3cDot11PreambleType=Hh3cDot11PreambleType, Hh3cDot11MACModeType=Hh3cDot11MACModeType, Hh3cDot11NotifyReasonType=Hh3cDot11NotifyReasonType, Hh3cDot11TunnelSecSchemType=Hh3cDot11TunnelSecSchemType, hh3cDot11RadioElementRadioNum=hh3cDot11RadioElementRadioNum, Hh3cDot11TxPwrLevelScopeType=Hh3cDot11TxPwrLevelScopeType, Hh3cDot11RadioType=Hh3cDot11RadioType, hh3cDot11Common=hh3cDot11Common, Hh3cDot11CipherType=Hh3cDot11CipherType, Hh3cDot11AuthorFailType=Hh3cDot11AuthorFailType)
