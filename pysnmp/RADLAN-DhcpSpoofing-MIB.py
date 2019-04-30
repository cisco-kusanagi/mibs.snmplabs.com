#
# PySNMP MIB module RADLAN-DhcpSpoofing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DhcpSpoofing-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
dot1qVlanIndex, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Integer32, iso, Gauge32, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "iso", "Gauge32", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "MibIdentifier", "IpAddress", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlDhcpSpoofing = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 113))
rlDhcpSpoofing.setRevisions(('2006-05-15 00:00',))
if mibBuilder.loadTexts: rlDhcpSpoofing.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: rlDhcpSpoofing.setOrganization('Radlan Computer Communications Ltd.')
rlDhcpSpoofingServerPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 113, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingServerPorts.setStatus('current')
rlDhcpSpoofingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 89, 113, 2), )
if mibBuilder.loadTexts: rlDhcpSpoofingVlanTable.setStatus('current')
rlDhcpSpoofingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 113, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rlDhcpSpoofingVlanEntry.setStatus('current')
rlDhcpSpoofingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 113, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-DhcpSpoofing-MIB", PYSNMP_MODULE_ID=rlDhcpSpoofing, rlDhcpSpoofingVlanEntry=rlDhcpSpoofingVlanEntry, rlDhcpSpoofingVlanTable=rlDhcpSpoofingVlanTable, rlDhcpSpoofing=rlDhcpSpoofing, rlDhcpSpoofingServerPorts=rlDhcpSpoofingServerPorts, rlDhcpSpoofingEnabled=rlDhcpSpoofingEnabled)
