#
# PySNMP MIB module HPNSAEISA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSAEISA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Bits, iso, Gauge32, ModuleIdentity, Counter32, ObjectIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "iso", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "IpAddress", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaEISA = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9))
hpnsaEISAMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1))
hpnsaEISAAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2))
hpnsaEISACfgUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3))
hpnsaEISASlotInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4))
hpnsaEISAMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMibRevMajor.setDescription('The major revision level of the MIB.')
hpnsaEISAMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMibRevMinor.setDescription('The minor revision level of the MIB.')
hpnsaEISAAgentTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1), )
if mibBuilder.loadTexts: hpnsaEISAAgentTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentTable.setDescription('A table of SNMP agents that satisfy requests for this MIB.')
hpnsaEISAAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAAgentIndex"))
if mibBuilder.loadTexts: hpnsaEISAAgentEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentEntry.setDescription('A description of the agent/agents that access EISA information.')
hpnsaEISAAgentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentIndex.setDescription('A unique index for this agent.')
hpnsaEISAAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentName.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentName.setDescription('Name of the agent/agents satisfying SNMP requests for this MIB.')
hpnsaEISAAgentVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentVersion.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentVersion.setDescription('Version number of the agent/agents satisfying SNMP requests for this MIB.')
hpnsaEISAAgentDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentDate.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAAgentDate.setDescription('The date on which this agent was created. field octets contents range _________________________________________________ 1 1 years since 1900 0..255 2 2 month 1..12 3 3 day 1..31 4 4 hour 0..23 5 5 minute 0..59 6 6 second 0..59')
hpnsaEISACfgUtilRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMajor.setDescription('The major revision level of the EISA Config Utility.')
hpnsaEISACfgUtilRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMinor.setDescription('The minor revision level of the EISA Config Utility.')
hpnsaEISABoardTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1), )
if mibBuilder.loadTexts: hpnsaEISABoardTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISABoardTable.setDescription('Plug in EISA board information table.')
hpnsaEISABoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISASlotIndex"))
if mibBuilder.loadTexts: hpnsaEISABoardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISABoardEntry.setDescription('Information for each of the EISA boards in the system.')
hpnsaEISASlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISASlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISASlotIndex.setDescription('Number of this slot.')
hpnsaEISASlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("expansion", 0), ("embedded", 1), ("virtual", 2), ("reserved", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISASlotType.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISASlotType.setDescription('Type of slot this board is installed in.')
hpnsaEISACfgRevMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISACfgRevMajor.setDescription('Major CFG file revision level; 0 if no CFG file.')
hpnsaEISACfgRevMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISACfgRevMinor.setDescription('Minor CFG file revision level; 0 if no CFG file.')
hpnsaEISABoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISABoardID.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISABoardID.setDescription("Seven-character EISA board ID. First three characters are manufacturer's ID, followed by three characters product ID, followed by one character CFG file revision level.")
hpnsaEISABoardDupCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISABoardDupCfg.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISABoardDupCfg.setDescription('Specifies the duplicate CFG filenumber. 0 - No duplicate filenames, 1 - 15 number of the duplicate file.')
hpnsaEISANumFunctions = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISANumFunctions.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISANumFunctions.setDescription('Specifies the number of functions this board implements.')
hpnsaEISAFunctTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2), )
if mibBuilder.loadTexts: hpnsaEISAFunctTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctTable.setDescription('A table of EISA function information entries.')
hpnsaEISAFunctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAFunctSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAFunctIndex"))
if mibBuilder.loadTexts: hpnsaEISAFunctEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctEntry.setDescription('Information describing an EISA function.')
hpnsaEISAFunctSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctSlotIndex.setDescription('The EISA slot number that registered this function.')
hpnsaEISAFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctIndex.setDescription('The index of the function this entry describes.')
hpnsaEISAFunctStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctStatus.setDescription('Specifies whether this function is enabled or disabled.')
hpnsaEISAFunctType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctType.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAFunctType.setDescription('The type of the function. The type may be followed by one or more subtype description fields. Some currently defined types are: Type Meaning ============== ================================================== COM Communication device CPU Microprocessor KEY Keyboard MFC Multifunction board MSD Mass storage device NET Network board PAR ISA compatible parallel port PTR Pointing device SYS System board VID Video board This list describes some of the more common types found. It is not an exhaustive list.')
hpnsaEISAMemTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3), )
if mibBuilder.loadTexts: hpnsaEISAMemTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemTable.setDescription('A list of EISA function memory configuration entries.')
hpnsaEISAMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAMemSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAMemFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAMemAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISAMemEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemEntry.setDescription('A description of an EISA function memory configuration.')
hpnsaEISAMemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemSlotIndex.setDescription('The EISA slot number of the board that registered the memory configuration this entry describes.')
hpnsaEISAMemFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemFunctIndex.setDescription('The function in which this memory configuration was registered.')
hpnsaEISAMemAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemAllocIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemAllocIndex.setDescription('The index for this memory allocation entry in the EISA function block.')
hpnsaEISAMemStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemStartAddr.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemStartAddr.setDescription('The starting address of the memory configuration, in KB.')
hpnsaEISAMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemSize.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemSize.setDescription('The size of the memory configuration, in KB.')
hpnsaEISAMemShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nonshareable", 0), ("shareable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemShare.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemShare.setDescription('This value indicates if the memory is shareable.')
hpnsaEISAMemType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("systemBaseOrExtended", 1), ("expanded", 2), ("virtual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemType.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemType.setDescription('The type of memory.')
hpnsaEISAMemCache = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notCached", 1), ("writeThroughCached", 2), ("writeBackCached", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemCache.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemCache.setDescription('This value indicates if and how the memory is cached.')
hpnsaEISAMemAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemAccess.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAMemAccess.setDescription('The type of access permitted for this memory.')
hpnsaEISAIntTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4), )
if mibBuilder.loadTexts: hpnsaEISAIntTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntTable.setDescription('A list of EISA function interrupt configuration entries.')
hpnsaEISAIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAIntSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAIntFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAIntAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISAIntEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntEntry.setDescription('A description of an EISA function interrupt configuration.')
hpnsaEISAIntSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntSlotIndex.setDescription('The EISA slot number of the board that registered the interrupt configuration this entry describes.')
hpnsaEISAIntFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntFunctIndex.setDescription('The function in which this interrupt configuration was registered.')
hpnsaEISAIntAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntAllocIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntAllocIndex.setDescription('The index for this interrupt allocation entry in the EISA function block.')
hpnsaEISAIntNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntNum.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntNum.setDescription('The interrupt number described in this entry.')
hpnsaEISAIntShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntShare.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntShare.setDescription('This value indicates if the interrupt is shareable.')
hpnsaEISAIntTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("edgeTriggered", 0), ("levelTriggered", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntTrigger.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAIntTrigger.setDescription('This value indicates whether the interrupt is edge or level triggered.')
hpnsaEISADmaTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5), )
if mibBuilder.loadTexts: hpnsaEISADmaTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaTable.setDescription('A list of EISA function DMA configuration entries.')
hpnsaEISADmaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISADmaSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISADmaFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISADmaAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISADmaEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaEntry.setDescription('A description of an EISA function DMA configuration.')
hpnsaEISADmaSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaSlotIndex.setDescription('The EISA slot number of the board that registered the DMA configuration this entry describes.')
hpnsaEISADmaFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaFunctIndex.setDescription('The function in which this DMA configuration was registered.')
hpnsaEISADmaAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaAllocIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaAllocIndex.setDescription('The index for this DMA channel allocation entry in the EISA function block.')
hpnsaEISADmaChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaChannelNum.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaChannelNum.setDescription('The DMA channel number described in this entry.')
hpnsaEISADmaShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaShare.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaShare.setDescription('This value indicates whether the DMA channel is shared.')
hpnsaEISADmaTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("defaultISACompat", 0), ("typeA", 1), ("typeB", 2), ("burstC", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaTiming.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaTiming.setDescription('DMA timing type.')
hpnsaEISADmaXferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("eightBit", 0), ("sixteenBit", 1), ("thirtyTwoBit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaXferSize.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISADmaXferSize.setDescription('DMA transfer size.')
hpnsaEISAPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6), )
if mibBuilder.loadTexts: hpnsaEISAPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortTable.setDescription('Table containing port information.')
hpnsaEISAPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAPortSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortEntryIndex"))
if mibBuilder.loadTexts: hpnsaEISAPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortEntry.setDescription('Address of port for the card.')
hpnsaEISAPortSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortSlotIndex.setDescription('Number of the slot for this port entry.')
hpnsaEISAPortFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortFunctIndex.setDescription('Number of the function for this port entry.')
hpnsaEISAPortEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortEntryIndex.setDescription('Index of the entry in the entry table.')
hpnsaEISAPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortAddress.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortAddress.setDescription('Port address.')
hpnsaEISAPortSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortSize.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortSize.setDescription('0-based number of ports (i.e., 0 means 1 port).')
hpnsaEISAPortShared = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortShared.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortShared.setDescription('Indicates whether port is shared.')
hpnsaEISAPortInitTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7), )
if mibBuilder.loadTexts: hpnsaEISAPortInitTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitTable.setDescription('Table containing port init values.')
hpnsaEISAPortInitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAPortInitSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitEntryIndex"))
if mibBuilder.loadTexts: hpnsaEISAPortInitEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitEntry.setDescription('Table entry of port init values.')
hpnsaEISAPortInitSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitSlotIndex.setDescription('Slot number for this port init entry.')
hpnsaEISAPortInitFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitFunctIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitFunctIndex.setDescription('Function index for this port init entry.')
hpnsaEISAPortInitEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitEntryIndex.setDescription('Index of this port init entry.')
hpnsaEISAPortInitData = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitData.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaEISAPortInitData.setDescription('Port initialization data. Byte 0 Initialization Type Byte 1 LSB of port I/O address Byte 2 MSB of port I/O address Byte 3 - 10 port value/mask')
mibBuilder.exportSymbols("HPNSAEISA-MIB", hpnsaEISADmaTable=hpnsaEISADmaTable, hpnsaEISAFunctType=hpnsaEISAFunctType, hpnsaEISACfgRevMinor=hpnsaEISACfgRevMinor, hpnsaEISAMibRev=hpnsaEISAMibRev, hpnsaEISADmaAllocIndex=hpnsaEISADmaAllocIndex, hpnsaEISAPortInitFunctIndex=hpnsaEISAPortInitFunctIndex, hpnsaEISAMemCache=hpnsaEISAMemCache, hpnsaEISASlotInfo=hpnsaEISASlotInfo, hpnsaEISAAgentTable=hpnsaEISAAgentTable, hpnsaEISAAgentName=hpnsaEISAAgentName, hpnsaEISACfgUtil=hpnsaEISACfgUtil, hpnsaEISABoardDupCfg=hpnsaEISABoardDupCfg, hpnsaEISAPortSlotIndex=hpnsaEISAPortSlotIndex, hpnsaEISABoardEntry=hpnsaEISABoardEntry, hpnsaEISADmaSlotIndex=hpnsaEISADmaSlotIndex, hpnsaEISAFunctTable=hpnsaEISAFunctTable, hpnsaEISAMemEntry=hpnsaEISAMemEntry, hpnsaEISADmaXferSize=hpnsaEISADmaXferSize, hpnsaEISABoardID=hpnsaEISABoardID, hpnsaEISAMemSize=hpnsaEISAMemSize, hpnsaEISAPortSize=hpnsaEISAPortSize, hpnsaEISAPortInitData=hpnsaEISAPortInitData, hpnsaEISADmaFunctIndex=hpnsaEISADmaFunctIndex, hpnsaEISAFunctSlotIndex=hpnsaEISAFunctSlotIndex, hpnsaEISA=hpnsaEISA, hpnsaEISAAgent=hpnsaEISAAgent, hpnsaEISAAgentEntry=hpnsaEISAAgentEntry, hpnsaEISAMemAccess=hpnsaEISAMemAccess, hpnsaEISAMemTable=hpnsaEISAMemTable, hpnsaEISAMemStartAddr=hpnsaEISAMemStartAddr, hpnsaEISAMemFunctIndex=hpnsaEISAMemFunctIndex, hpnsaEISAFunctIndex=hpnsaEISAFunctIndex, hpnsaEISAPortInitTable=hpnsaEISAPortInitTable, hpnsaEISADmaChannelNum=hpnsaEISADmaChannelNum, hpnsaEISAPortTable=hpnsaEISAPortTable, hpnsaEISAPortInitEntryIndex=hpnsaEISAPortInitEntryIndex, hpnsaEISAPortShared=hpnsaEISAPortShared, hp=hp, hpnsaEISADmaShare=hpnsaEISADmaShare, hpnsaEISADmaTiming=hpnsaEISADmaTiming, hpnsaEISASlotType=hpnsaEISASlotType, hpnsaEISAFunctStatus=hpnsaEISAFunctStatus, hpnsaEISAMemSlotIndex=hpnsaEISAMemSlotIndex, hpnsaEISAIntAllocIndex=hpnsaEISAIntAllocIndex, nm=nm, hpnsaEISANumFunctions=hpnsaEISANumFunctions, hpnsaEISAIntTable=hpnsaEISAIntTable, hpnsaEISAIntSlotIndex=hpnsaEISAIntSlotIndex, hpnsaEISAMemType=hpnsaEISAMemType, hpnsaEISAPortAddress=hpnsaEISAPortAddress, hpnsaEISAFunctEntry=hpnsaEISAFunctEntry, hpnsaEISAPortInitEntry=hpnsaEISAPortInitEntry, hpnsaEISAPortInitSlotIndex=hpnsaEISAPortInitSlotIndex, hpnsaEISASlotIndex=hpnsaEISASlotIndex, hpnsaEISACfgUtilRevMinor=hpnsaEISACfgUtilRevMinor, hpnsaEISAIntEntry=hpnsaEISAIntEntry, hpnsaEISACfgUtilRevMajor=hpnsaEISACfgUtilRevMajor, hpnsaEISAAgentDate=hpnsaEISAAgentDate, hpnsaEISAIntTrigger=hpnsaEISAIntTrigger, hpnsaEISAMibRevMinor=hpnsaEISAMibRevMinor, hpnsaEISAMibRevMajor=hpnsaEISAMibRevMajor, hpnsaEISAPortEntry=hpnsaEISAPortEntry, hpnsaEISABoardTable=hpnsaEISABoardTable, hpnsaEISAIntShare=hpnsaEISAIntShare, hpnsaEISAPortFunctIndex=hpnsaEISAPortFunctIndex, hpnsa=hpnsa, hpnsaEISAAgentVersion=hpnsaEISAAgentVersion, hpnsaEISAMemAllocIndex=hpnsaEISAMemAllocIndex, hpnsaEISAIntNum=hpnsaEISAIntNum, hpnsaEISADmaEntry=hpnsaEISADmaEntry, hpnsaEISAPortEntryIndex=hpnsaEISAPortEntryIndex, hpnsaEISAIntFunctIndex=hpnsaEISAIntFunctIndex, hpnsaEISAAgentIndex=hpnsaEISAAgentIndex, hpnsaEISACfgRevMajor=hpnsaEISACfgRevMajor, hpnsaEISAMemShare=hpnsaEISAMemShare)
