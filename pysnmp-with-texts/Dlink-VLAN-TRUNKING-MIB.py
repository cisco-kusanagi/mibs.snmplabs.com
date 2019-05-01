#
# PySNMP MIB module Dlink-VLAN-TRUNKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-VLAN-TRUNKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:58:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, IpAddress, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Gauge32, TimeTicks, MibIdentifier, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Gauge32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Integer32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlVlanTrunking = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136))
rlVlanTrunking.setRevisions(('2007-11-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlVlanTrunking.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlVlanTrunking.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlVlanTrunking.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: rlVlanTrunking.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlVlanTrunking.setDescription('Dlink Vlan Trunking MIBs')
rlVlanTrunkingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingEnabled.setStatus('current')
if mibBuilder.loadTexts: rlVlanTrunkingEnabled.setDescription("VLAN Trunking feature's status")
rlVlanTrunkingUplinkPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingUplinkPorts.setStatus('current')
if mibBuilder.loadTexts: rlVlanTrunkingUplinkPorts.setDescription('VLAN Trunking Uplink PortList ')
mibBuilder.exportSymbols("Dlink-VLAN-TRUNKING-MIB", rlVlanTrunking=rlVlanTrunking, PYSNMP_MODULE_ID=rlVlanTrunking, rlVlanTrunkingUplinkPorts=rlVlanTrunkingUplinkPorts, rlVlanTrunkingEnabled=rlVlanTrunkingEnabled)
