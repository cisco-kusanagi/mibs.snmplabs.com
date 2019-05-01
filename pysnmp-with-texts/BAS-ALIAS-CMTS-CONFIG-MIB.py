#
# PySNMP MIB module BAS-ALIAS-CMTS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-ALIAS-CMTS-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
BasChassisId, BasLogicalPortId, BasSlotId, basAliasCmtsCfg, BasInterfaceId = mibBuilder.importSymbols("BAS-MIB", "BasChassisId", "BasLogicalPortId", "BasSlotId", "basAliasCmtsCfg", "BasInterfaceId")
docsIfUpstreamChannelEntry, docsIfDownstreamChannelEntry, docsIfCmtsModulationEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfUpstreamChannelEntry", "docsIfDownstreamChannelEntry", "docsIfCmtsModulationEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, ModuleIdentity, Unsigned32, TimeTicks, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "Unsigned32", "TimeTicks", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "NotificationType", "Gauge32", "Counter32")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
basAliasCmtsCfgMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1))
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setLastUpdated('9810081200Z')
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setContactInfo(' Tech Support Broadband Access Systems 201 Forest Street Marlboro, MA 01752 U.S.A. 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basAliasCmtsCfgMib.setDescription('This MIB module defines the Alias CmtsCfg MIB objects for a Broadband Access System Cluster.')
basCmtsCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1))
basAlsCmtsMacToSidObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2))
class BasCmtsInt8(TextualConvention, Integer32):
    description = 'Range of INTEGER(-127..128).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-127, 128)

class BasCmtsUInt8(TextualConvention, Integer32):
    description = 'Range of INTEGER(0..255).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class BasCmtsByte(BasCmtsUInt8):
    description = 'Range of INTEGER(0..255).'
    status = 'current'
    displayHint = 'd'

class BasCmtsInt16(TextualConvention, Integer32):
    description = 'Range of INTEGER(-32768..32767).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class BasCmtsUInt16(TextualConvention, Integer32):
    description = 'Range of INTEGER(0..0x7fff).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BasCmtsInt32(TextualConvention, Integer32):
    description = 'Range of Integer32'
    status = 'current'
    displayHint = 'd'

class BasCmtsUInt32(TextualConvention, Integer32):
    description = 'Range of INTEGER(0..0x7fffffff).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BasCmtsRowAction(TextualConvention, Integer32):
    description = 'Defines Bas Cmts row action.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("basCmtsRowActionNone", 1), ("basCmtsRowActionApply", 2))

class BasCmtsHeadEndMapMode(TextualConvention, Integer32):
    description = 'HeadEndMgr map mode. 0 = Normal, free running maps. 99 = Scripted maps for test and debug.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(99, 99), )
class BasCmtsHeadEndMacAddr(TextualConvention, OctetString):
    description = 'HeadEndMgr MacAddress.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class BasCmtsHeadEndAuthString(TextualConvention, OctetString):
    description = 'HeadEndMgr Authorization String.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class BasCmtsUpChannelPreamblePattern(TextualConvention, OctetString):
    description = 'Bas Upstream Channel Preamble Pattern.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class BasCmtsModulationWsPattern(TextualConvention, OctetString):
    description = 'Bas upstream channel burst descriptor unique word pattern.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

basCmtsPLLTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2), )
if mibBuilder.loadTexts: basCmtsPLLTable.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLTable.setDescription('Provides ways to set the Phase Lock Loop on the CMTS.')
basCmtsPLLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1), ).setIndexNames((0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLChassis"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLSlot"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLIf"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLLPort"))
if mibBuilder.loadTexts: basCmtsPLLEntry.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLEntry.setDescription('')
basCmtsPLLChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basCmtsPLLChassis.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLChassis.setDescription('The BAS Chassis ID of this card.')
basCmtsPLLSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basCmtsPLLSlot.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLSlot.setDescription('The BAS Slot ID of this card.')
basCmtsPLLIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basCmtsPLLIf.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLIf.setDescription('The BAS interface ID of this card.')
basCmtsPLLLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basCmtsPLLLPort.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLLPort.setDescription('The BAS logical port ID of this card.')
basCmtsPLLState = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("pllSet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmtsPLLState.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLState.setDescription('This object triggers the CMTS PLL.')
basCmtsPLLValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 6), BasCmtsInt32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basCmtsPLLValue.setStatus('current')
if mibBuilder.loadTexts: basCmtsPLLValue.setDescription('This object specifies the current CMTS PLL value.')
basAlsCmtsMacToSidTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1), )
if mibBuilder.loadTexts: basAlsCmtsMacToSidTable.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidTable.setDescription('A list of BAS cmts mac to sid objects. ')
basAlsCmtsMacToSidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1), ).setIndexNames((0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidChassis"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidSlot"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidIf"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidLPort"), (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidMacAddr"))
if mibBuilder.loadTexts: basAlsCmtsMacToSidEntry.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidEntry.setDescription('An entry containing BAS CMTS MAC to SID settings.')
basAlsCmtsMacToSidMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidMacAddr.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidMacAddr.setDescription('The MAC address of the host or the cable modem')
basAlsCmtsMacToSidServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidServiceId.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidServiceId.setDescription('The SID of the host or the cable modem derived from the MAC')
basAlsCmtsMacToSidType = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("cableModem", 2), ("host", 3))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAlsCmtsMacToSidType.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidType.setDescription('Type of device attached to this SID')
basAlsCmtsMacToSidChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 4), BasChassisId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidChassis.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidChassis.setDescription('The BAS Chassis ID of this card.')
basAlsCmtsMacToSidSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 5), BasSlotId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidSlot.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidSlot.setDescription('The BAS Slot ID of this card.')
basAlsCmtsMacToSidIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 6), BasInterfaceId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidIf.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidIf.setDescription('The BAS interface ID of this card.')
basAlsCmtsMacToSidLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 7), BasLogicalPortId())
if mibBuilder.loadTexts: basAlsCmtsMacToSidLPort.setStatus('current')
if mibBuilder.loadTexts: basAlsCmtsMacToSidLPort.setDescription('The BAS logical port ID of this card.')
mibBuilder.exportSymbols("BAS-ALIAS-CMTS-CONFIG-MIB", BasCmtsUpChannelPreamblePattern=BasCmtsUpChannelPreamblePattern, BasCmtsByte=BasCmtsByte, BasCmtsUInt32=BasCmtsUInt32, basAlsCmtsMacToSidChassis=basAlsCmtsMacToSidChassis, BasCmtsHeadEndMapMode=BasCmtsHeadEndMapMode, BasCmtsInt32=BasCmtsInt32, basCmtsPLLIf=basCmtsPLLIf, BasCmtsModulationWsPattern=BasCmtsModulationWsPattern, basCmtsPLLTable=basCmtsPLLTable, BasCmtsUInt16=BasCmtsUInt16, basAlsCmtsMacToSidType=basAlsCmtsMacToSidType, basCmtsPLLState=basCmtsPLLState, basAlsCmtsMacToSidSlot=basAlsCmtsMacToSidSlot, basAliasCmtsCfgMib=basAliasCmtsCfgMib, basCmtsPLLValue=basCmtsPLLValue, basCmtsPLLChassis=basCmtsPLLChassis, basCmtsCfgObjects=basCmtsCfgObjects, basAlsCmtsMacToSidLPort=basAlsCmtsMacToSidLPort, BasCmtsInt16=BasCmtsInt16, basAlsCmtsMacToSidServiceId=basAlsCmtsMacToSidServiceId, basAlsCmtsMacToSidEntry=basAlsCmtsMacToSidEntry, BasCmtsRowAction=BasCmtsRowAction, basCmtsPLLLPort=basCmtsPLLLPort, BasCmtsInt8=BasCmtsInt8, basAlsCmtsMacToSidIf=basAlsCmtsMacToSidIf, basAlsCmtsMacToSidObjects=basAlsCmtsMacToSidObjects, basCmtsPLLEntry=basCmtsPLLEntry, basCmtsPLLSlot=basCmtsPLLSlot, basAlsCmtsMacToSidTable=basAlsCmtsMacToSidTable, PYSNMP_MODULE_ID=basAliasCmtsCfgMib, basAlsCmtsMacToSidMacAddr=basAlsCmtsMacToSidMacAddr, BasCmtsHeadEndAuthString=BasCmtsHeadEndAuthString, BasCmtsHeadEndMacAddr=BasCmtsHeadEndMacAddr, BasCmtsUInt8=BasCmtsUInt8)
