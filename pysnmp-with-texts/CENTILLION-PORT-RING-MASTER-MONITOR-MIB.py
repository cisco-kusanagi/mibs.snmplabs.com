#
# PySNMP MIB module CENTILLION-PORT-RING-MASTER-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-PORT-RING-MASTER-MONITOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sysMonitor, MacAddress = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "sysMonitor", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Gauge32, TimeTicks, IpAddress, NotificationType, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
portRmLastChg = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmLastChg.setStatus('mandatory')
if mibBuilder.loadTexts: portRmLastChg.setDescription('The value of sysUpTime the last time an entry in the Port Ring master Table was added, deleted, or modified. If the Port Ring master Table has not changed since cold/warm start of the agent, then the value is zero.')
portRmTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3), )
if mibBuilder.loadTexts: portRmTable.setStatus('mandatory')
if mibBuilder.loadTexts: portRmTable.setDescription('Port Ring Master Monitor Table.')
portRmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1), ).setIndexNames((0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmSlotNum"), (0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmPortNum"))
if mibBuilder.loadTexts: portRmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portRmEntry.setDescription('A row in the Port NMM Table. Entries in the table can not be created or deleted via SNMP.')
portRmSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: portRmSlotNum.setDescription('The slot on which the topology message was received. NOTE: Non-modular devices that do not have multiplt slots should set this value to 1.')
portRmPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: portRmPortNum.setDescription('The port on which the RM_HELLO topology message was received.')
portRmIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: portRmIpAddr.setDescription('The IP address of the sender of the RM_HELLO topology message.')
portRmMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: portRmMacAddr.setDescription('The MAC address of the sender of the RM_HELLO topology message.')
mibBuilder.exportSymbols("CENTILLION-PORT-RING-MASTER-MONITOR-MIB", portRmSlotNum=portRmSlotNum, portRmEntry=portRmEntry, portRmIpAddr=portRmIpAddr, portRmLastChg=portRmLastChg, portRmMacAddr=portRmMacAddr, portRmPortNum=portRmPortNum, portRmTable=portRmTable)
