#
# PySNMP MIB module BAS-ALIAS-CMTS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-ALIAS-CMTS-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
BasSlotId, BasLogicalPortId, BasInterfaceId, basAliasCmtsCfg, BasChassisId = mibBuilder.importSymbols("BAS-MIB", "BasSlotId", "BasLogicalPortId", "BasInterfaceId", "basAliasCmtsCfg", "BasChassisId")
docsIfCmtsModulationEntry, docsIfUpstreamChannelEntry, docsIfDownstreamChannelEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsModulationEntry", "docsIfUpstreamChannelEntry", "docsIfDownstreamChannelEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, iso, Counter64, MibIdentifier, Unsigned32, NotificationType, IpAddress, Bits, ObjectIdentity, Integer32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "Unsigned32", "NotificationType", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "Gauge32", "TimeTicks")
TruthValue, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "TextualConvention")
basAliasCmtsCfgMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1))
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setLastUpdated('9810081200Z')
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setOrganization('Broadband Access Systems')
basCmtsCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1))
basAlsCmtsMacToSidObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2))
class BasCmtsInt8(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-127, 128)

class BasCmtsUInt8(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class BasCmtsByte(BasCmtsUInt8):
    status = 'current'
    displayHint = 'd'

class BasCmtsInt16(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class BasCmtsUInt16(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BasCmtsInt32(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class BasCmtsUInt32(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BasCmtsRowAction(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("basCmtsRowActionNone", 1), ("basCmtsRowActionApply", 2))

class BasCmtsHeadEndMapMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(99, 99), )
class BasCmtsHeadEndMacAddr(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class BasCmtsHeadEndAuthString(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class BasCmtsUpChannelPreamblePattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class BasCmtsModulationWsPattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

basCmtsPLLTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2), )
if mibBuilder.loadTexts: basCmtsPLLTable.setStatus('current')
basCmtsPLLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1), ).setIndexNames((0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLChassis"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLSlot"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLIf"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLLPort"))
if mibBuilder.loadTexts: basCmtsPLLEntry.setStatus('current')
basCmtsPLLChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basCmtsPLLChassis.setStatus('current')
basCmtsPLLSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basCmtsPLLSlot.setStatus('current')
basCmtsPLLIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basCmtsPLLIf.setStatus('current')
basCmtsPLLLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basCmtsPLLLPort.setStatus('current')
basCmtsPLLState = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("pllSet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmtsPLLState.setStatus('current')
basCmtsPLLValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 6), BasCmtsInt32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basCmtsPLLValue.setStatus('current')
basAlsCmtsMacToSidTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1), )
if mibBuilder.loadTexts: basAlsCmtsMacToSidTable.setStatus('current')
basAlsCmtsMacToSidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1), ).setIndexNames((0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidChassis"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidSlot"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidIf"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidLPort"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidMacAddr"))
if mibBuilder.loadTexts: basAlsCmtsMacToSidEntry.setStatus('current')
basAlsCmtsMacToSidMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidMacAddr.setStatus('current')
basAlsCmtsMacToSidServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidServiceId.setStatus('current')
basAlsCmtsMacToSidType = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("cableModem", 2), ("host", 3))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidType.setStatus('current')
basAlsCmtsMacToSidChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 4), BasChassisId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidChassis.setStatus('current')
basAlsCmtsMacToSidSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 5), BasSlotId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidSlot.setStatus('current')
basAlsCmtsMacToSidIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 6), BasInterfaceId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidIf.setStatus('current')
basAlsCmtsMacToSidLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 7), BasLogicalPortId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidLPort.setStatus('current')
mibBuilder.exportSymbols("BAS-ALIAS-CMTS-CONFIG-MIB", basCmtsPLLChassis=basCmtsPLLChassis, basAlsCmtsMacToSidServiceId=basAlsCmtsMacToSidServiceId, basAlsCmtsMacToSidEntry=basAlsCmtsMacToSidEntry, basCmtsPLLIf=basCmtsPLLIf, BasCmtsModulationWsPattern=BasCmtsModulationWsPattern, basAlsCmtsMacToSidTable=basAlsCmtsMacToSidTable, BasCmtsUpChannelPreamblePattern=BasCmtsUpChannelPreamblePattern, basAliasCmtsCfgMib=basAliasCmtsCfgMib, basAlsCmtsMacToSidMacAddr=basAlsCmtsMacToSidMacAddr, BasCmtsHeadEndMacAddr=BasCmtsHeadEndMacAddr, basAlsCmtsMacToSidIf=basAlsCmtsMacToSidIf, basCmtsCfgObjects=basCmtsCfgObjects, PYSNMP_MODULE_ID=basAliasCmtsCfgMib, basCmtsPLLLPort=basCmtsPLLLPort, BasCmtsByte=BasCmtsByte, basAlsCmtsMacToSidSlot=basAlsCmtsMacToSidSlot, BasCmtsInt32=BasCmtsInt32, BasCmtsUInt32=BasCmtsUInt32, basAlsCmtsMacToSidType=basAlsCmtsMacToSidType, basCmtsPLLTable=basCmtsPLLTable, basCmtsPLLValue=basCmtsPLLValue, BasCmtsUInt16=BasCmtsUInt16, BasCmtsInt8=BasCmtsInt8, basCmtsPLLEntry=basCmtsPLLEntry, BasCmtsHeadEndAuthString=BasCmtsHeadEndAuthString, basCmtsPLLState=basCmtsPLLState, basAlsCmtsMacToSidObjects=basAlsCmtsMacToSidObjects, basAlsCmtsMacToSidChassis=basAlsCmtsMacToSidChassis, BasCmtsUInt8=BasCmtsUInt8, BasCmtsInt16=BasCmtsInt16, BasCmtsRowAction=BasCmtsRowAction, basAlsCmtsMacToSidLPort=basAlsCmtsMacToSidLPort, basCmtsPLLSlot=basCmtsPLLSlot, BasCmtsHeadEndMapMode=BasCmtsHeadEndMapMode)
