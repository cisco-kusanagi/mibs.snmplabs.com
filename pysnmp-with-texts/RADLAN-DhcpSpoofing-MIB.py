#
# PySNMP MIB module RADLAN-DhcpSpoofing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DhcpSpoofing-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:46:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
dot1qVlanIndex, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, TimeTicks, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Integer32, Counter64, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "Bits", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlDhcpSpoofing = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 113))
rlDhcpSpoofing.setRevisions(('2006-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDhcpSpoofing.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDhcpSpoofing.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: rlDhcpSpoofing.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlDhcpSpoofing.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlDhcpSpoofing.setDescription('The private MIB module definition for DhcpSpoofing.')
rlDhcpSpoofingServerPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 113, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingServerPorts.setStatus('current')
if mibBuilder.loadTexts: rlDhcpSpoofingServerPorts.setDescription('Each bit that is set in this portList represent a port that A dhcp server reside.')
rlDhcpSpoofingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 89, 113, 2), )
if mibBuilder.loadTexts: rlDhcpSpoofingVlanTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpSpoofingVlanTable.setDescription('A table that contains all existing vlans.')
rlDhcpSpoofingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 113, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rlDhcpSpoofingVlanEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpSpoofingVlanEntry.setDescription('A vlan.')
rlDhcpSpoofingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 113, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingEnabled.setStatus('current')
if mibBuilder.loadTexts: rlDhcpSpoofingEnabled.setDescription('DHCP spoofing enabled or not.')
mibBuilder.exportSymbols("RADLAN-DhcpSpoofing-MIB", rlDhcpSpoofing=rlDhcpSpoofing, PYSNMP_MODULE_ID=rlDhcpSpoofing, rlDhcpSpoofingEnabled=rlDhcpSpoofingEnabled, rlDhcpSpoofingVlanEntry=rlDhcpSpoofingVlanEntry, rlDhcpSpoofingServerPorts=rlDhcpSpoofingServerPorts, rlDhcpSpoofingVlanTable=rlDhcpSpoofingVlanTable)
