#
# PySNMP MIB module CISCO-IKE-FLOW-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IKE-FLOW-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, Bits, ModuleIdentity, ObjectIdentity, Counter32, Integer32, NotificationType, MibIdentifier, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 490))
ciscoIkeFlowExtCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setDescription('Agent capabilities for CISCO-IKE-FLOW-EXT-MIB')
cIkeFlowExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 490, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIkeFlowExtCapSanOSV30R1MDS9000.setDescription('Cisco Internet Key Exchange(IKE) MIB extension to CISCO-IKE-FLOW-MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-EXT-CAPABILITY", ciscoIkeFlowExtCapability=ciscoIkeFlowExtCapability, cIkeFlowExtCapSanOSV30R1MDS9000=cIkeFlowExtCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIkeFlowExtCapability)
