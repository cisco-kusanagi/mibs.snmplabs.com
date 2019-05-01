#
# PySNMP MIB module CISCO-CONTENT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONTENT-SERVICES-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, Counter64, ObjectIdentity, Unsigned32, Gauge32, iso, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "iso", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoContentServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 581))
ciscoContentServicesCapability.setRevisions(('2010-12-23 00:00', '2010-02-11 00:00', '2009-08-21 00:00', '2009-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContentServicesCapability.setRevisionsDescriptions(('Added following object groups: ciscoContentServicesLoadStatRadiusGroupSup1 ciscoContentServicesLoadStatUserDBGroupSup1 ciscoContentServicesLoadStatSessionGroupSup1 ciscoContentServicesLoadStatBMAGroupSup1 ciscoContentServicesLoadStatQuotaMgrGroupSup1 ciscoContentServicesLoadStatGxEventGroupSup1', 'Added following object group: ciscoContentServicesBillingPlanStatsGroup', 'Added following object groups: ciscoContentServiceProtocolStatsGroup ciscoContentServicesLoadStatGxEventGroup', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContentServicesCapability.setLastUpdated('201012230000Z')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-csg@cisco.com')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setDescription('Agent capabilities for CISCO-CONTENT-SERVICES-MIB')
ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setProductRelease('Cisco IOS 12.4MF')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityAdcV01R00.setDescription('Cisco Content Services MIB for AdControl capabilities')
ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setProductRelease('Cisco IOS 12.4(22)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R03.setDescription('Cisco Content Services MIB for CSG2 R3 capabilities')
ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setProductRelease('Cisco IOS 12.4(22)MDA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R0305.setDescription('Added ciscoContentServicesCapabilityCSG2R0305 agent capabilities for Content Service Gateway version 3.5. This verion contains the statistics for Layer 7 protocols including Nbar protocol. Also added load statistical information related to Gx Events.')
ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setProductRelease('Cisco IOS 12.4(24)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R04.setDescription('Added ciscoContentServicesCapabilityCSG2R04 agent capabilities for Content Service Gateway 2 release 4. In addition to existing features, the release also provides the statistics of associated subscribers per billing plan.')
ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setProductRelease('Cisco IOS R6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R06.setDescription('Added ciscoContentServicesCapabilityCSG2R06 agent capabilities for Content Service Gateway 2 release 6. In addition to existing features, the release also provides 64 bit version of allowed and denial rate for load statistics.')
mibBuilder.exportSymbols("CISCO-CONTENT-SERVICES-CAPABILITY", ciscoContentServicesCapabilityCSG2R03=ciscoContentServicesCapabilityCSG2R03, ciscoContentServicesCapabilityCSG2R04=ciscoContentServicesCapabilityCSG2R04, PYSNMP_MODULE_ID=ciscoContentServicesCapability, ciscoContentServicesCapabilityAdcV01R00=ciscoContentServicesCapabilityAdcV01R00, ciscoContentServicesCapability=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R0305=ciscoContentServicesCapabilityCSG2R0305, ciscoContentServicesCapabilityCSG2R06=ciscoContentServicesCapabilityCSG2R06)
