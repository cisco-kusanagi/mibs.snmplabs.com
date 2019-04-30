#
# PySNMP MIB module CISCO-WAN-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-TOPOLOGY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, iso, Integer32, NotificationType, Unsigned32, Bits, Counter64, ModuleIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "NotificationType", "Unsigned32", "Bits", "Counter64", "ModuleIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 254))
ciscoWanTopologyCapability.setRevisions(('2003-01-15 00:00', '2002-10-31 00:00', '2001-10-10 00:00',))
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setLastUpdated('200301150000Z')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanTopologyCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setProductRelease('MGX8850 and BPX-SES Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setStatus('current')
ciscoWanTopologyCapabilityV3R0020 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setProductRelease('MGX8850 and BPX-SES Release 3.0.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setStatus('current')
ciscoWanTopologyCapabilityV4R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setProductRelease('MGX8850 and BPX-SES Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-TOPOLOGY-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanTopologyCapability, ciscoWanTopologyCapabilityV3R0020=ciscoWanTopologyCapabilityV3R0020, ciscoWanTopologyCapabilityV4R0000=ciscoWanTopologyCapabilityV4R0000, ciscoWanTopologyCapability=ciscoWanTopologyCapability, ciscoWanTopologyCapabilityV3R00=ciscoWanTopologyCapabilityV3R00)
