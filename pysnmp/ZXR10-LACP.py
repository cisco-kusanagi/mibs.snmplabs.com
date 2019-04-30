#
# PySNMP MIB module ZXR10-LACP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-LACP
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, Gauge32, Bits, NotificationType, Counter64, MibIdentifier, Counter32, TimeTicks, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "Gauge32", "Bits", "NotificationType", "Counter64", "MibIdentifier", "Counter32", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
zxr10, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10")
lacpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 125))
if mibBuilder.loadTexts: lacpMIB.setLastUpdated('200609010000Z')
if mibBuilder.loadTexts: lacpMIB.setOrganization('ZTE Corporation')
lacpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1))
class UINT32(Unsigned32):
    pass

class Char(OctetString):
    pass

class LACPMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bondModeOn", 0), ("bondMode8023AD", 1))

class LACPLoadBalanceType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 50, 51))
    namedValues = NamedValues(("dst-ip", 1), ("dst-mac", 2), ("src-dst-ip", 3), ("src-dst-mac", 4), ("src-ip", 5), ("src-mac", 6), ("src-port", 7), ("dst-port", 8), ("src-dst-port", 9), ("dst-ip-dst-port", 10), ("src-ip-src-port", 11), ("src-dst-ip-src-dst-port", 12), ("pub-label", 13), ("pri-label", 14), ("pub-pri-label", 15), ("per-packet", 16), ("perDestination", 50), ("perPacket", 51))

class LACPPortType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("passive", 1), ("on", 2), ("active", 3))

class LACPPortTimeoutType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("long-time", 0), ("short-time", 1))

lacpAggregatingPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1))
lacpAggregatedPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2))
lacpAggregatingTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1), )
if mibBuilder.loadTexts: lacpAggregatingTable.setStatus('current')
lacpAggregatingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lacpAggregatingEntry.setStatus('current')
lacpAggSgIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 1), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSgIfName.setStatus('current')
lacpAggMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggMacAddress.setStatus('current')
lacpAggActorSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 3), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggActorSystemPriority.setStatus('current')
lacpAggMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 4), LACPMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggMode.setStatus('current')
lacpAggLoadBalanceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 5), LACPLoadBalanceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggLoadBalanceMode.setStatus('current')
lacpAggJumboframe = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggJumboframe.setStatus('current')
lacpAggSubIfIndexName1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 7), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName1.setStatus('current')
lacpAggSubIfIndexName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 8), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName2.setStatus('current')
lacpAggSubIfIndexName3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 9), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName3.setStatus('current')
lacpAggSubIfIndexName4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 10), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName4.setStatus('current')
lacpAggSubIfIndexName5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 11), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName5.setStatus('current')
lacpAggSubIfIndexName6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 12), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName6.setStatus('current')
lacpAggSubIfIndexName7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 13), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName7.setStatus('current')
lacpAggSubIfIndexName8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 14), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName8.setStatus('current')
lacpAggregatedTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1), )
if mibBuilder.loadTexts: lacpAggregatedTable.setStatus('current')
lacpAggregatedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lacpAggregatedEntry.setStatus('current')
lacpAggSgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 1), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggSgId.setStatus('current')
lacpAggregatedIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 2), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggregatedIfName.setStatus('current')
lacpAggPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 3), LACPPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggPortMode.setStatus('current')
lacpAggPortTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 4), LACPPortTimeoutType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggPortTimeOut.setStatus('current')
lacpAggLacpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 5), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggLacpPriority.setStatus('current')
lacpAggPortActorOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortActorOperKey.setStatus('current')
lacpAggPortActorOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 7), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortActorOperState.setStatus('current')
lacpAggPortPartnerOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 8), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortPartnerOperKey.setStatus('current')
lacpAggPortPartnerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 9), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortPartnerOperState.setStatus('current')
mibBuilder.exportSymbols("ZXR10-LACP", lacpAggregatingPara=lacpAggregatingPara, lacpAggregatingEntry=lacpAggregatingEntry, lacpAggPortActorOperState=lacpAggPortActorOperState, PYSNMP_MODULE_ID=lacpMIB, lacpAggSgIfName=lacpAggSgIfName, lacpAggLoadBalanceMode=lacpAggLoadBalanceMode, lacpAggSubIfIndexName2=lacpAggSubIfIndexName2, lacpAggPortPartnerOperState=lacpAggPortPartnerOperState, lacpAggSubIfIndexName3=lacpAggSubIfIndexName3, LACPPortTimeoutType=LACPPortTimeoutType, lacpAggMacAddress=lacpAggMacAddress, UINT32=UINT32, lacpAggSubIfIndexName1=lacpAggSubIfIndexName1, lacpAggSubIfIndexName5=lacpAggSubIfIndexName5, lacpAggSgId=lacpAggSgId, lacpMIB=lacpMIB, lacpAggActorSystemPriority=lacpAggActorSystemPriority, lacpAggMode=lacpAggMode, LACPLoadBalanceType=LACPLoadBalanceType, lacpAggLacpPriority=lacpAggLacpPriority, lacpAggPortActorOperKey=lacpAggPortActorOperKey, lacpAggregatingTable=lacpAggregatingTable, lacpAggregatedTable=lacpAggregatedTable, LACPMode=LACPMode, lacpAggPortPartnerOperKey=lacpAggPortPartnerOperKey, lacpAggSubIfIndexName8=lacpAggSubIfIndexName8, Char=Char, lacpMibObjects=lacpMibObjects, lacpAggSubIfIndexName7=lacpAggSubIfIndexName7, lacpAggSubIfIndexName4=lacpAggSubIfIndexName4, lacpAggregatedPara=lacpAggregatedPara, lacpAggPortTimeOut=lacpAggPortTimeOut, lacpAggJumboframe=lacpAggJumboframe, lacpAggSubIfIndexName6=lacpAggSubIfIndexName6, lacpAggPortMode=lacpAggPortMode, lacpAggregatedEntry=lacpAggregatedEntry, lacpAggregatedIfName=lacpAggregatedIfName, LACPPortType=LACPPortType)
