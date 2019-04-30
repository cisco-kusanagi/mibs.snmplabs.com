#
# PySNMP MIB module ZYXEL-PORT-ISOLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-PORT-ISOLATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, IpAddress, Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "IpAddress", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPortIsolation = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64))
if mibBuilder.loadTexts: zyxelPortIsolation.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPortIsolation.setOrganization('Enterprise Solution ZyXEL')
zyxelPortIsolationSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1))
zyxelPortIsolationPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1), )
if mibBuilder.loadTexts: zyxelPortIsolationPortTable.setStatus('current')
zyxelPortIsolationPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortIsolationPortEntry.setStatus('current')
zyPortIsolationPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortIsolationPortState.setStatus('current')
zyPortIsolationSmartIsolationState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortIsolationSmartIsolationState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-ISOLATION-MIB", zyxelPortIsolation=zyxelPortIsolation, zyxelPortIsolationPortTable=zyxelPortIsolationPortTable, zyPortIsolationPortState=zyPortIsolationPortState, zyxelPortIsolationPortEntry=zyxelPortIsolationPortEntry, PYSNMP_MODULE_ID=zyxelPortIsolation, zyPortIsolationSmartIsolationState=zyPortIsolationSmartIsolationState, zyxelPortIsolationSetup=zyxelPortIsolationSetup)
