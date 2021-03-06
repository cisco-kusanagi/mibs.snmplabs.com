#
# PySNMP MIB module ELTEX-MES-eltInterfaces (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-eltInterfaces
# Produced by pysmi-0.3.4 at Wed May  1 13:02:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
eltMesSwInterfaces, = mibBuilder.importSymbols("ELTEX-MES", "eltMesSwInterfaces")
ifIndex, InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Unsigned32, Counter64, ModuleIdentity, TimeTicks, iso, Gauge32, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter64", "ModuleIdentity", "TimeTicks", "iso", "Gauge32", "MibIdentifier", "Bits", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eltSwIfTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1), )
if mibBuilder.loadTexts: eltSwIfTable.setStatus('current')
if mibBuilder.loadTexts: eltSwIfTable.setDescription('Switch media specific information and configuration of the device interfaces.')
eltSwIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1), ).setIndexNames((0, "ELTEX-MES-eltInterfaces", "eltSwIfIndex"))
if mibBuilder.loadTexts: eltSwIfEntry.setStatus('current')
if mibBuilder.loadTexts: eltSwIfEntry.setDescription('Defines the contents of each line in the eltSwIfTable table.')
eltSwIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfIndex.setStatus('current')
if mibBuilder.loadTexts: eltSwIfIndex.setDescription('Index to the eltSwIfTable. The interface defined by a particular value of this index is the same interface as identified by the same value of ifIndex (MIB II).')
eltSwIfSfpOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("fiber", 0), ("directAttach", 1), ("copperSfp", 2), ("unknown", 3))).clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSwIfSfpOperationMode.setStatus('current')
if mibBuilder.loadTexts: eltSwIfSfpOperationMode.setDescription(' This variable indicates plugged in SFP transceiver operation mode.')
eltSwIfUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2), )
if mibBuilder.loadTexts: eltSwIfUtilizationTable.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationTable.setDescription('Switch ports utilization configuration and information.')
eltSwIfUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1), ).setIndexNames((0, "ELTEX-MES-eltInterfaces", "eltSwIfUtilizationIfIndex"))
if mibBuilder.loadTexts: eltSwIfUtilizationEntry.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationEntry.setDescription('Defines the contents of each line in the eltSwIfUtilizationTable table.')
eltSwIfUtilizationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationIfIndex.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationIfIndex.setDescription("A unique value for each interface. Its value ranges between 1 and the value of ifNumber. The value for each interface must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
eltSwIfUtilizationAverageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSwIfUtilizationAverageTime.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationAverageTime.setDescription('An average load time in seconds for which interface utilization is calculated.')
eltSwIfUtilizationCurrentInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentInPkts.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentInPkts.setDescription('The total number of all (UC, MC and BC) packets received on the interface during last 5 seconds.')
eltSwIfUtilizationCurrentInRate = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentInRate.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentInRate.setDescription('The inbound rate in kbit/sec on the interface during last 5 seconds.')
eltSwIfUtilizationCurrentOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentOutPkts.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentOutPkts.setDescription('The total number of all (UC, MC and BC) packets sent out of the interface during last 5 seconds.')
eltSwIfUtilizationCurrentOutRate = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentOutRate.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationCurrentOutRate.setDescription('The outbound rate in kbit/sec on the interface during last 5 seconds.')
eltSwIfUtilizationAverageInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationAverageInPkts.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationAverageInPkts.setDescription('The total number of all (UC, MC and BC) packets received on the interface during configured load average time for this interface.')
eltSwIfUtilizationAverageInRate = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationAverageInRate.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationAverageInRate.setDescription('The inbound rate in kbit/sec on the interface during configured load average time for this interface.')
eltSwIfUtilizationAverageOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationAverageOutPkts.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationAverageOutPkts.setDescription('The total number of all (UC, MC and BC) packets sent out of the interface during configured load average time for this interface.')
eltSwIfUtilizationAverageOutRate = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltSwIfUtilizationAverageOutRate.setStatus('current')
if mibBuilder.loadTexts: eltSwIfUtilizationAverageOutRate.setDescription('The outbound rate in kbit/sec on the interface during configured load average time for this interface.')
mibBuilder.exportSymbols("ELTEX-MES-eltInterfaces", eltSwIfUtilizationAverageOutPkts=eltSwIfUtilizationAverageOutPkts, eltSwIfIndex=eltSwIfIndex, eltSwIfUtilizationTable=eltSwIfUtilizationTable, eltSwIfUtilizationCurrentOutRate=eltSwIfUtilizationCurrentOutRate, eltSwIfUtilizationAverageInRate=eltSwIfUtilizationAverageInRate, eltSwIfUtilizationAverageInPkts=eltSwIfUtilizationAverageInPkts, eltSwIfEntry=eltSwIfEntry, eltSwIfUtilizationAverageOutRate=eltSwIfUtilizationAverageOutRate, eltSwIfUtilizationAverageTime=eltSwIfUtilizationAverageTime, eltSwIfUtilizationIfIndex=eltSwIfUtilizationIfIndex, eltSwIfSfpOperationMode=eltSwIfSfpOperationMode, eltSwIfTable=eltSwIfTable, eltSwIfUtilizationCurrentInPkts=eltSwIfUtilizationCurrentInPkts, eltSwIfUtilizationEntry=eltSwIfUtilizationEntry, eltSwIfUtilizationCurrentInRate=eltSwIfUtilizationCurrentInRate, eltSwIfUtilizationCurrentOutPkts=eltSwIfUtilizationCurrentOutPkts)
