#
# PySNMP MIB module CISCO-IP-RAN-BACKHAUL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-RAN-BACKHAUL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, ObjectIdentity, Integer32, ModuleIdentity, Bits, IpAddress, Unsigned32, Counter64, NotificationType, iso, Counter32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "Bits", "IpAddress", "Unsigned32", "Counter64", "NotificationType", "iso", "Counter32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpRanBhCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 461))
ciscoIpRanBhCapability.setRevisions(('2010-07-14 00:00', '2005-09-15 00:00',))
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setLastUpdated('201007140000Z')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpRanBhCapabilityV12R0402MR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setProductRelease('Cisco IOS 12.4(2)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setStatus('current')
ciscoIpRanBhCapabilityV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setProductRelease('Cisco IOS 12.4(12)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-RAN-BACKHAUL-CAPABILITY", ciscoIpRanBhCapabilityV12R0412MR1=ciscoIpRanBhCapabilityV12R0412MR1, ciscoIpRanBhCapabilityV12R0402MR=ciscoIpRanBhCapabilityV12R0402MR, PYSNMP_MODULE_ID=ciscoIpRanBhCapability, ciscoIpRanBhCapability=ciscoIpRanBhCapability)
