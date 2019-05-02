#
# PySNMP MIB module CISCO-WAN-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-TOPOLOGY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, IpAddress, Integer32, NotificationType, Bits, Unsigned32, ObjectIdentity, TimeTicks, iso, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "NotificationType", "Bits", "Unsigned32", "ObjectIdentity", "TimeTicks", "iso", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 254))
ciscoWanTopologyCapability.setRevisions(('2003-01-15 00:00', '2002-10-31 00:00', '2001-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanTopologyCapability.setRevisionsDescriptions(('- Added ciscoWanTopologyV4R0000 capability for release 4.0.00.', '- Replace the objects cwtLanIP and cwtAtmIP in ciscoWanTopologyCapabilityV3R00 with objects cwtPrimIPIfType, cwtPrimIPIfName, cwtPrimIPAddrType, cwtPrimIP, cwtSecIPIfType, cwtSecIPIfName, cwtSecIPAddrType, cwtSecIP. - Added ciscoWanTopologyV3R0020 capability for release 3.0.20.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setLastUpdated('200301150000Z')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setDescription('The Agent Capabilities for CISCO-WAN-TOPOLOGY-MIB. This MIB is used in the MGX8850 product family, which contains the MGX8850 and MGX8950 switches.')
ciscoWanTopologyCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setProductRelease('MGX8850 and BPX-SES Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV3R00.setDescription('Persistent Topology MIB Capabilities.')
ciscoWanTopologyCapabilityV3R0020 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setProductRelease('MGX8850 and BPX-SES Release 3.0.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV3R0020.setDescription('Persistent Topology MIB Capabilities.')
ciscoWanTopologyCapabilityV4R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setProductRelease('MGX8850 and BPX-SES Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV4R0000.setDescription('Persistent Topology MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-TOPOLOGY-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanTopologyCapability, ciscoWanTopologyCapabilityV3R0020=ciscoWanTopologyCapabilityV3R0020, ciscoWanTopologyCapabilityV3R00=ciscoWanTopologyCapabilityV3R00, ciscoWanTopologyCapabilityV4R0000=ciscoWanTopologyCapabilityV4R0000, ciscoWanTopologyCapability=ciscoWanTopologyCapability)
