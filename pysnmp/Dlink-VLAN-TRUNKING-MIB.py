#
# PySNMP MIB module Dlink-VLAN-TRUNKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-VLAN-TRUNKING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, ObjectIdentity, iso, Bits, IpAddress, MibIdentifier, Unsigned32, Gauge32, NotificationType, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ObjectIdentity", "iso", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "Gauge32", "NotificationType", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlVlanTrunking = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136))
rlVlanTrunking.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlVlanTrunking.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlVlanTrunking.setOrganization('Dlink, Inc.')
rlVlanTrunkingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingEnabled.setStatus('current')
rlVlanTrunkingUplinkPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingUplinkPorts.setStatus('current')
mibBuilder.exportSymbols("Dlink-VLAN-TRUNKING-MIB", PYSNMP_MODULE_ID=rlVlanTrunking, rlVlanTrunkingEnabled=rlVlanTrunkingEnabled, rlVlanTrunkingUplinkPorts=rlVlanTrunkingUplinkPorts, rlVlanTrunking=rlVlanTrunking)
