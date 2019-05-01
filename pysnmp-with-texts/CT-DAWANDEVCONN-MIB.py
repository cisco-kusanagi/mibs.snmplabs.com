#
# PySNMP MIB module CT-DAWANDEVCONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DAWANDEVCONN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, MibIdentifier, Integer32, iso, Counter64, IpAddress, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "iso", "Counter64", "IpAddress", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daWanDevConn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 23))
daWanDevConnTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1), )
if mibBuilder.loadTexts: daWanDevConnTable.setStatus('mandatory')
if mibBuilder.loadTexts: daWanDevConnTable.setDescription('A list of Demand Access remote WAN connections')
daWanDevConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1), ).setIndexNames((0, "CT-DAWANDEVCONN-MIB", "daWanDeviceIndex"), (0, "CT-DAWANDEVCONN-MIB", "daWanConnectionIndex"))
if mibBuilder.loadTexts: daWanDevConnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: daWanDevConnEntry.setDescription('An entry containing wan connection information and statistics.')
daWanDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanDeviceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: daWanDeviceIndex.setDescription('This is the index into this table. This index uniquely identifies the connection associated with the device.')
daWanConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionIndex.setDescription('This is the index into this table. This index uniquely identifies the connection associated with the device.')
mibBuilder.exportSymbols("CT-DAWANDEVCONN-MIB", daWanDeviceIndex=daWanDeviceIndex, daWanConnectionIndex=daWanConnectionIndex, daWanDevConnEntry=daWanDevConnEntry, daWanDevConn=daWanDevConn, daWanDevConnTable=daWanDevConnTable, ctSSA=ctSSA)
