#
# PySNMP MIB module CISCO-GGSN-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GGSN-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, Gauge32, Counter64, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Integer32, ObjectIdentity, IpAddress, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter64", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Integer32", "ObjectIdentity", "IpAddress", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGgsnQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 295))
ciscoGgsnQosCapability.setRevisions(('2003-04-08 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGgsnQosCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setLastUpdated('200304081600Z')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setDescription('Agent capabilities for CISCO-GGSN-QOS-MIB.')
ciscoGgsnQosCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX, 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setStatus('current')
if mibBuilder.loadTexts: ciscoGgsnQosCapabilityV12R2M4.setDescription('Cisco GGSN QOS MIB capabilities.')
ciscoGgsnQosCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setStatus('current')
if mibBuilder.loadTexts: ciscoGgsnQosCapabilityV12R2M8.setDescription('Cisco GGSN QOS MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GGSN-QOS-CAPABILITY", ciscoGgsnQosCapability=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M4=ciscoGgsnQosCapabilityV12R2M4, ciscoGgsnQosCapabilityV12R2M8=ciscoGgsnQosCapabilityV12R2M8, PYSNMP_MODULE_ID=ciscoGgsnQosCapability)
