#
# PySNMP MIB module ZXR10-LACP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-LACP
# Produced by pysmi-0.3.4 at Wed May  1 15:48:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, iso, Integer32, Gauge32, Unsigned32, IpAddress, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "iso", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
zxr10, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10")
lacpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 125))
if mibBuilder.loadTexts: lacpMIB.setLastUpdated('200609010000Z')
if mibBuilder.loadTexts: lacpMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: lacpMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 ZiJinghua Rd. YuHuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: lacpMIB.setDescription('ZXROS V4.6.03B LACP MIB')
lacpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1))
class UINT32(Unsigned32):
    pass

class Char(OctetString):
    pass

class LACPMode(TextualConvention, Integer32):
    description = 'LACP Mode'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bondModeOn", 0), ("bondMode8023AD", 1))

class LACPLoadBalanceType(TextualConvention, Integer32):
    description = 'LACP Load Balance Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 50, 51))
    namedValues = NamedValues(("dst-ip", 1), ("dst-mac", 2), ("src-dst-ip", 3), ("src-dst-mac", 4), ("src-ip", 5), ("src-mac", 6), ("src-port", 7), ("dst-port", 8), ("src-dst-port", 9), ("dst-ip-dst-port", 10), ("src-ip-src-port", 11), ("src-dst-ip-src-dst-port", 12), ("pub-label", 13), ("pri-label", 14), ("pub-pri-label", 15), ("per-packet", 16), ("perDestination", 50), ("perPacket", 51))

class LACPPortType(TextualConvention, Integer32):
    description = 'LACP Port Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("passive", 1), ("on", 2), ("active", 3))

class LACPPortTimeoutType(TextualConvention, Integer32):
    description = 'LACP Port Timeout Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("long-time", 0), ("short-time", 1))

lacpAggregatingPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1))
lacpAggregatedPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2))
lacpAggregatingTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1), )
if mibBuilder.loadTexts: lacpAggregatingTable.setStatus('current')
if mibBuilder.loadTexts: lacpAggregatingTable.setDescription('Configure Aggregating Port parameters.')
lacpAggregatingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lacpAggregatingEntry.setStatus('current')
if mibBuilder.loadTexts: lacpAggregatingEntry.setDescription('Each row index by ifIndex And contain imformation of Aggregating Port.')
lacpAggSgIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 1), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSgIfName.setStatus('current')
if mibBuilder.loadTexts: lacpAggSgIfName.setDescription('Smartgroup interface name.')
lacpAggMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggMacAddress.setStatus('current')
if mibBuilder.loadTexts: lacpAggMacAddress.setDescription('Mac address.')
lacpAggActorSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 3), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggActorSystemPriority.setStatus('current')
if mibBuilder.loadTexts: lacpAggActorSystemPriority.setDescription('LACP System priority.')
lacpAggMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 4), LACPMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggMode.setStatus('current')
if mibBuilder.loadTexts: lacpAggMode.setDescription('Aggregation Type.')
lacpAggLoadBalanceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 5), LACPLoadBalanceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggLoadBalanceMode.setStatus('current')
if mibBuilder.loadTexts: lacpAggLoadBalanceMode.setDescription('Aggregation Load Balance Type.')
lacpAggJumboframe = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggJumboframe.setStatus('current')
if mibBuilder.loadTexts: lacpAggJumboframe.setDescription('Jumboframe Type.')
lacpAggSubIfIndexName1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 7), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName1.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName1.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 8), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName2.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName2.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 9), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName3.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName3.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 10), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName4.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName4.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 11), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName5.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName5.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 12), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName6.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName6.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 13), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName7.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName7.setDescription('Aggregated Port Name.')
lacpAggSubIfIndexName8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 14), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggSubIfIndexName8.setStatus('current')
if mibBuilder.loadTexts: lacpAggSubIfIndexName8.setDescription('Aggregated Port Name.')
lacpAggregatedTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1), )
if mibBuilder.loadTexts: lacpAggregatedTable.setStatus('current')
if mibBuilder.loadTexts: lacpAggregatedTable.setDescription('Configure Aggregated Port parameters.')
lacpAggregatedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lacpAggregatedEntry.setStatus('current')
if mibBuilder.loadTexts: lacpAggregatedEntry.setDescription('Each row index by aggregating and aggregated ifIndex And contain imformation of Aggregated Port.')
lacpAggSgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 1), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggSgId.setStatus('current')
if mibBuilder.loadTexts: lacpAggSgId.setDescription('Add to smartgroup interface.')
lacpAggregatedIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 2), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggregatedIfName.setStatus('current')
if mibBuilder.loadTexts: lacpAggregatedIfName.setDescription('Aggregated interface name.')
lacpAggPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 3), LACPPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggPortMode.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortMode.setDescription('LACP Port Type.')
lacpAggPortTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 4), LACPPortTimeoutType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggPortTimeOut.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortTimeOut.setDescription('LACP Port Timeout.')
lacpAggLacpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 5), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lacpAggLacpPriority.setStatus('current')
if mibBuilder.loadTexts: lacpAggLacpPriority.setDescription('Lacp Priority.')
lacpAggPortActorOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortActorOperKey.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortActorOperKey.setDescription('Lacp Port Operation Key.')
lacpAggPortActorOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 7), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortActorOperState.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortActorOperState.setDescription('Lacp Port Operation Status.')
lacpAggPortPartnerOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 8), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortPartnerOperKey.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortPartnerOperKey.setDescription('Lacp Partner Operation Key.')
lacpAggPortPartnerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 9), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lacpAggPortPartnerOperState.setStatus('current')
if mibBuilder.loadTexts: lacpAggPortPartnerOperState.setDescription('Lacp Partner Operation Status.')
mibBuilder.exportSymbols("ZXR10-LACP", LACPLoadBalanceType=LACPLoadBalanceType, lacpAggregatingTable=lacpAggregatingTable, lacpAggPortActorOperKey=lacpAggPortActorOperKey, lacpAggPortActorOperState=lacpAggPortActorOperState, lacpAggSubIfIndexName5=lacpAggSubIfIndexName5, lacpAggPortPartnerOperState=lacpAggPortPartnerOperState, lacpAggregatedTable=lacpAggregatedTable, lacpAggSubIfIndexName3=lacpAggSubIfIndexName3, lacpAggSgIfName=lacpAggSgIfName, Char=Char, lacpAggSubIfIndexName2=lacpAggSubIfIndexName2, lacpAggSubIfIndexName4=lacpAggSubIfIndexName4, LACPMode=LACPMode, lacpAggActorSystemPriority=lacpAggActorSystemPriority, lacpMIB=lacpMIB, lacpAggSubIfIndexName8=lacpAggSubIfIndexName8, lacpAggMode=lacpAggMode, lacpAggPortTimeOut=lacpAggPortTimeOut, lacpAggSubIfIndexName7=lacpAggSubIfIndexName7, lacpAggSgId=lacpAggSgId, lacpAggregatedIfName=lacpAggregatedIfName, lacpMibObjects=lacpMibObjects, UINT32=UINT32, LACPPortType=LACPPortType, lacpAggregatingEntry=lacpAggregatingEntry, lacpAggPortMode=lacpAggPortMode, PYSNMP_MODULE_ID=lacpMIB, lacpAggregatedPara=lacpAggregatedPara, lacpAggSubIfIndexName1=lacpAggSubIfIndexName1, lacpAggLacpPriority=lacpAggLacpPriority, LACPPortTimeoutType=LACPPortTimeoutType, lacpAggMacAddress=lacpAggMacAddress, lacpAggregatedEntry=lacpAggregatedEntry, lacpAggLoadBalanceMode=lacpAggLoadBalanceMode, lacpAggSubIfIndexName6=lacpAggSubIfIndexName6, lacpAggregatingPara=lacpAggregatingPara, lacpAggJumboframe=lacpAggJumboframe, lacpAggPortPartnerOperKey=lacpAggPortPartnerOperKey)
