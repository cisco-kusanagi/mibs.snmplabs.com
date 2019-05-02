#
# PySNMP MIB module CISCO-GPRS-ACC-PT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-ACC-PT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, Unsigned32, TimeTicks, NotificationType, MibIdentifier, iso, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Unsigned32", "TimeTicks", "NotificationType", "MibIdentifier", "iso", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cgprsAccPtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 298))
cgprsAccPtCapability.setRevisions(('2003-04-08 17:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsAccPtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsAccPtCapability.setLastUpdated('200304081750Z')
if mibBuilder.loadTexts: cgprsAccPtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsAccPtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsAccPtCapability.setDescription('Agent capabilities for CISCO-GPRS-ACC-PT-MIB.')
cgprsAccPtCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M4.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
cgprsAccPtCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M8.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-ACC-PT-CAPABILITY", cgprsAccPtCapability=cgprsAccPtCapability, cgprsAccPtCapabilityV12R2M4=cgprsAccPtCapabilityV12R2M4, cgprsAccPtCapabilityV12R2M8=cgprsAccPtCapabilityV12R2M8, PYSNMP_MODULE_ID=cgprsAccPtCapability)
