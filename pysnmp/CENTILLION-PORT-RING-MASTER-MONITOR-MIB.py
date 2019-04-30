#
# PySNMP MIB module CENTILLION-PORT-RING-MASTER-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-PORT-RING-MASTER-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
MacAddress, sysMonitor = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "MacAddress", "sysMonitor")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, TimeTicks, ObjectIdentity, Integer32, Bits, Counter32, MibIdentifier, iso, Counter64, NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "ObjectIdentity", "Integer32", "Bits", "Counter32", "MibIdentifier", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
portRmLastChg = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmLastChg.setStatus('mandatory')
portRmTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3), )
if mibBuilder.loadTexts: portRmTable.setStatus('mandatory')
portRmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1), ).setIndexNames((0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmSlotNum"), (0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmPortNum"))
if mibBuilder.loadTexts: portRmEntry.setStatus('mandatory')
portRmSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmSlotNum.setStatus('mandatory')
portRmPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmPortNum.setStatus('mandatory')
portRmIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmIpAddr.setStatus('mandatory')
portRmMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRmMacAddr.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-PORT-RING-MASTER-MONITOR-MIB", portRmSlotNum=portRmSlotNum, portRmLastChg=portRmLastChg, portRmMacAddr=portRmMacAddr, portRmTable=portRmTable, portRmIpAddr=portRmIpAddr, portRmEntry=portRmEntry, portRmPortNum=portRmPortNum)
