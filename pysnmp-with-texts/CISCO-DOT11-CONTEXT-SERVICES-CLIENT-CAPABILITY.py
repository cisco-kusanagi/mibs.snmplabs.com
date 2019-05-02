#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, MibIdentifier, TimeTicks, Gauge32, iso, Integer32, Counter32, NotificationType, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "Gauge32", "iso", "Integer32", "Counter32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDot11CscCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 336))
ciscoDot11CscCapability.setRevisions(('2004-07-24 00:00', '2003-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11CscCapability.setRevisionsDescriptions(('Added ciscoDot11CscCapabilityV2 for IOS 12.3(2).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDot11CscCapability.setLastUpdated('200407240000Z')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setDescription('Agent capabilities for CISCO-CONTEXT-SERVICES- CLIENT-MIB')
ciscoDot11CscCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV1.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT MIB capabilities')
ciscoDot11CscCapabilityV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setProductRelease('Cisco IOS 12.3(2) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV2.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT MIB capabilities for IOS 12.3(2).')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY", ciscoDot11CscCapability=ciscoDot11CscCapability, PYSNMP_MODULE_ID=ciscoDot11CscCapability, ciscoDot11CscCapabilityV1=ciscoDot11CscCapabilityV1, ciscoDot11CscCapabilityV2=ciscoDot11CscCapabilityV2)
