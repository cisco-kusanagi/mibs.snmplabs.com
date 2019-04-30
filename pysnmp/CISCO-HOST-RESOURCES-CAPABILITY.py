#
# PySNMP MIB module CISCO-HOST-RESOURCES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HOST-RESOURCES-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, ModuleIdentity, Unsigned32, Counter64, MibIdentifier, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits, Integer32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Unsigned32", "Counter64", "MibIdentifier", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits", "Integer32", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHostResourcesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 547))
ciscoHostResourcesCapability.setRevisions(('2007-10-04 00:00', '2007-09-17 00:00',))
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setLastUpdated('200710040000Z')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setOrganization('Cisco Systems, Inc.')
ciscoHostResourcesCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setStatus('current')
ciscoHostResourcesCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-HOST-RESOURCES-CAPABILITY", ciscoHostResourcesCapability=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityCTSV120=ciscoHostResourcesCapabilityCTSV120, PYSNMP_MODULE_ID=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityV12R04=ciscoHostResourcesCapabilityV12R04)
