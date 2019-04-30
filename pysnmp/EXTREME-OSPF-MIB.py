#
# PySNMP MIB module EXTREME-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
extremeVlanIfIndex, = mibBuilder.importSymbols("EXTREME-VLAN-MIB", "extremeVlanIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
extremeOspf = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 15))
if mibBuilder.loadTexts: extremeOspf.setLastUpdated('0006280000Z')
if mibBuilder.loadTexts: extremeOspf.setOrganization('Extreme Networks, Inc.')
extremeOspfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1), )
if mibBuilder.loadTexts: extremeOspfInterfaceTable.setStatus('current')
extremeOspfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1), ).setIndexNames((0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"))
if mibBuilder.loadTexts: extremeOspfInterfaceEntry.setStatus('current')
extremeOspfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeOspfAreaId.setStatus('current')
extremeOspfInterfacePassive = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeOspfInterfacePassive.setStatus('current')
extremeOspfInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeOspfInterfaceStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-OSPF-MIB", extremeOspfInterfacePassive=extremeOspfInterfacePassive, PYSNMP_MODULE_ID=extremeOspf, extremeOspf=extremeOspf, extremeOspfAreaId=extremeOspfAreaId, extremeOspfInterfaceEntry=extremeOspfInterfaceEntry, extremeOspfInterfaceStatus=extremeOspfInterfaceStatus, extremeOspfInterfaceTable=extremeOspfInterfaceTable)
