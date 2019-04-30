#
# PySNMP MIB module HH3C-DOT11-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DOT11-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Gauge32, Integer32, Counter64, ObjectIdentity, MibIdentifier, NotificationType, IpAddress, Unsigned32, TimeTicks, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Gauge32", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cDot11 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 75))
hh3cDot11.setRevisions(('2010-01-07 20:00', '2009-05-07 20:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 19:00',))
if mibBuilder.loadTexts: hh3cDot11.setLastUpdated('201001072000Z')
if mibBuilder.loadTexts: hh3cDot11.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cDot11ObjectIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class Hh3cDot11RadioScopeType(TextualConvention, Integer32):
    status = 'current'

class Hh3cDot11RadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11n", 8), ("dot11gn", 16), ("dot11an", 32))

class Hh3cDot11MACModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("split", 1), ("localtunnel", 2), ("localbridge", 3), ("fatAP", 4))

class Hh3cDot11ChannelScopeType(TextualConvention, Integer32):
    status = 'current'

class Hh3cDot11NotifyReasonType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Hh3cDot11SSIDStringType(TextualConvention, OctetString):
    status = 'current'

class Hh3cDot11ServicePolicyIDType(TextualConvention, Integer32):
    status = 'current'

class Hh3cDot11SSIDEncryptModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("cipher", 2), ("wapi", 3))

class Hh3cDot11PreambleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("long", 1), ("short", 2))

class Hh3cDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    status = 'current'

class Hh3cDot11RFModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class Hh3cDot11TunnelSecSchemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("dtls", 2), ("ipsec", 3))

class Hh3cDot11SecIEStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("rsn", 2), ("wpa", 3), ("all", 4), ("wapi", 5))

class Hh3cDot11CipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 16, 32, 64, 128))
    namedValues = NamedValues(("none", 1), ("wep40", 2), ("tkip", 4), ("aesccmp", 16), ("wep104", 32), ("wpisms4", 64), ("wep128", 128))

class Hh3cDot11AuthenType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("opensystem", 2), ("sharedkey", 3), ("all", 4))

class Hh3cDot11AKMType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("psk", 2), ("dot1x", 3), ("wapi", 4))

class Hh3cDot11AssocFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknownfailure", 1), ("toomanyassoc", 2), ("invalidie", 3), ("unsupportedrate", 4), ("unsupportedpwrcap", 5), ("unsupportedcap", 6))

class Hh3cDot11AuthorFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknownfailure", 1), ("invalidie", 2), ("rsnieversionunsupported", 3), ("wpaieversionunsupported", 4), ("groupcipherinvalid", 5), ("pairwisecipherinvalid", 6), ("akminvalid", 7))

class Hh3cDot11QosAcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4))

class Hh3cDot11RadioElementIndex(TextualConvention, Unsigned32):
    status = 'current'

class Hh3cDot11WorkMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("monitor", 2), ("hybrid", 3))

class Hh3cDot11CirMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

hh3cDot11Common = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12))
hh3cDot11ElementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1))
hh3cDot11APElementTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1), )
if mibBuilder.loadTexts: hh3cDot11APElementTable.setStatus('current')
hh3cDot11APElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1), ).setIndexNames((0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"))
if mibBuilder.loadTexts: hh3cDot11APElementEntry.setStatus('current')
hh3cDot11APElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cDot11APElementIndex.setStatus('current')
hh3cDot11APElementTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementTemplateName.setStatus('current')
hh3cDot11APElementSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementSerialID.setStatus('current')
hh3cDot11APElementModelAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11APElementModelAlias.setStatus('current')
hh3cDot11RadioElementTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2), )
if mibBuilder.loadTexts: hh3cDot11RadioElementTable.setStatus('current')
hh3cDot11RadioElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1), ).setIndexNames((0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"), (0, "HH3C-DOT11-REF-MIB", "hh3cDot11RadioElementRadioNum"))
if mibBuilder.loadTexts: hh3cDot11RadioElementEntry.setStatus('current')
hh3cDot11RadioElementRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioNum.setStatus('current')
hh3cDot11RadioElementRadioPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioPolicy.setStatus('current')
hh3cDot11RadioElementRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDot11RadioElementRadioIndex.setStatus('current')
mibBuilder.exportSymbols("HH3C-DOT11-REF-MIB", Hh3cDot11RFModeType=Hh3cDot11RFModeType, hh3cDot11APElementEntry=hh3cDot11APElementEntry, Hh3cDot11RadioElementIndex=Hh3cDot11RadioElementIndex, Hh3cDot11AKMType=Hh3cDot11AKMType, Hh3cDot11CipherType=Hh3cDot11CipherType, hh3cDot11APElementModelAlias=hh3cDot11APElementModelAlias, hh3cDot11RadioElementRadioPolicy=hh3cDot11RadioElementRadioPolicy, Hh3cDot11QosAcType=Hh3cDot11QosAcType, Hh3cDot11ChannelScopeType=Hh3cDot11ChannelScopeType, hh3cDot11ElementGroup=hh3cDot11ElementGroup, Hh3cDot11MACModeType=Hh3cDot11MACModeType, Hh3cDot11NotifyReasonType=Hh3cDot11NotifyReasonType, hh3cDot11APElementTable=hh3cDot11APElementTable, Hh3cDot11RadioType=Hh3cDot11RadioType, hh3cDot11RadioElementTable=hh3cDot11RadioElementTable, Hh3cDot11ObjectIDType=Hh3cDot11ObjectIDType, hh3cDot11RadioElementRadioIndex=hh3cDot11RadioElementRadioIndex, Hh3cDot11WorkMode=Hh3cDot11WorkMode, Hh3cDot11ServicePolicyIDType=Hh3cDot11ServicePolicyIDType, Hh3cDot11AssocFailType=Hh3cDot11AssocFailType, Hh3cDot11SecIEStatusType=Hh3cDot11SecIEStatusType, hh3cDot11APElementIndex=hh3cDot11APElementIndex, hh3cDot11APElementSerialID=hh3cDot11APElementSerialID, Hh3cDot11TxPwrLevelScopeType=Hh3cDot11TxPwrLevelScopeType, Hh3cDot11PreambleType=Hh3cDot11PreambleType, Hh3cDot11SSIDStringType=Hh3cDot11SSIDStringType, PYSNMP_MODULE_ID=hh3cDot11, Hh3cDot11SSIDEncryptModeType=Hh3cDot11SSIDEncryptModeType, hh3cDot11APElementTemplateName=hh3cDot11APElementTemplateName, hh3cDot11RadioElementRadioNum=hh3cDot11RadioElementRadioNum, hh3cDot11=hh3cDot11, Hh3cDot11AuthenType=Hh3cDot11AuthenType, Hh3cDot11RadioScopeType=Hh3cDot11RadioScopeType, Hh3cDot11CirMode=Hh3cDot11CirMode, Hh3cDot11TunnelSecSchemType=Hh3cDot11TunnelSecSchemType, hh3cDot11RadioElementEntry=hh3cDot11RadioElementEntry, hh3cDot11Common=hh3cDot11Common, Hh3cDot11AuthorFailType=Hh3cDot11AuthorFailType)
