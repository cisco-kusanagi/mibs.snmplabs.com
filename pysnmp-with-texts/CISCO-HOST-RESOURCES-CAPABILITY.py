#
# PySNMP MIB module CISCO-HOST-RESOURCES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HOST-RESOURCES-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, NotificationType, Counter32, TimeTicks, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Gauge32, Counter64, Unsigned32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter32", "TimeTicks", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Gauge32", "Counter64", "Unsigned32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHostResourcesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 547))
ciscoHostResourcesCapability.setRevisions(('2007-10-04 00:00', '2007-09-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHostResourcesCapability.setRevisionsDescriptions(('Added Agent Capability for CTS 1000/3000 platform', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setLastUpdated('200710040000Z')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setDescription('Agent capabilities for HOST-RESOURCES-MIB')
ciscoHostResourcesCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoHostResourcesCapabilityV12R04.setDescription('HOST RESOURCES MIB capabilities')
ciscoHostResourcesCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setStatus('current')
if mibBuilder.loadTexts: ciscoHostResourcesCapabilityCTSV120.setDescription('HOST RESOURCES MIB capabilities')
mibBuilder.exportSymbols("CISCO-HOST-RESOURCES-CAPABILITY", PYSNMP_MODULE_ID=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityV12R04=ciscoHostResourcesCapabilityV12R04, ciscoHostResourcesCapability=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityCTSV120=ciscoHostResourcesCapabilityCTSV120)
