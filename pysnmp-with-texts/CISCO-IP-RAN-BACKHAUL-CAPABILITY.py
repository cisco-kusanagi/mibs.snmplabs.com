#
# PySNMP MIB module CISCO-IP-RAN-BACKHAUL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-RAN-BACKHAUL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, iso, Counter32, Bits, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "iso", "Counter32", "Bits", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpRanBhCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 461))
ciscoIpRanBhCapability.setRevisions(('2010-07-14 00:00', '2005-09-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpRanBhCapability.setRevisionsDescriptions(('Changes to indicate conversion to cirbhShortHaulBulkTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setLastUpdated('201007140000Z')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ran-o@cisco.com')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setDescription('Agent capabilities for the CISCO-IP-RAN-BACKHAUL-MIB.')
ciscoIpRanBhCapabilityV12R0402MR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setProductRelease('Cisco IOS 12.4(2)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setStatus('current')
if mibBuilder.loadTexts: ciscoIpRanBhCapabilityV12R0402MR.setDescription('IOS 12.4(2)MR1 Cisco CISCO-IP-RAN-BACKHAUL-MIB User Agent MIB capabilities.')
ciscoIpRanBhCapabilityV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setProductRelease('Cisco IOS 12.4(12)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpRanBhCapabilityV12R0412MR1.setDescription('IOS 12.4(12)MR1 Cisco CISCO-IP-RAN-BACKHAUL-MIB User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-RAN-BACKHAUL-CAPABILITY", ciscoIpRanBhCapabilityV12R0402MR=ciscoIpRanBhCapabilityV12R0402MR, ciscoIpRanBhCapabilityV12R0412MR1=ciscoIpRanBhCapabilityV12R0412MR1, PYSNMP_MODULE_ID=ciscoIpRanBhCapability, ciscoIpRanBhCapability=ciscoIpRanBhCapability)
