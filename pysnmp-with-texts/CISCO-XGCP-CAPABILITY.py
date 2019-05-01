#
# PySNMP MIB module CISCO-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-XGCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
CCallControlProfileIndexOrZero, = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "CCallControlProfileIndexOrZero")
CMgcGroupIndexOrZero, = mibBuilder.importSymbols("CISCO-MGC-MIB", "CMgcGroupIndexOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
CXgcpRetryMethod, = mibBuilder.importSymbols("CISCO-XGCP-MIB", "CXgcpRetryMethod")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, MibIdentifier, Integer32, Unsigned32, iso, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibIdentifier", "Integer32", "Unsigned32", "iso", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 408))
ciscoXgcpCapability.setRevisions(('2006-03-01 00:00', '2006-02-14 00:00', '2005-06-24 00:00', '2005-01-06 00:00', '2004-10-04 00:00', '2004-06-16 00:00', '2002-12-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoXgcpCapability.setRevisionsDescriptions(('Deprecated ciscoXgcpCapabilityV12R03AS5000 and added ciscoXgcpCapabilityV12R04AS5000.', 'Added ciscoXgcpCapabilityV5R300 for MGX8880 release 5.3.00. Deprecated ciscoXgcpCapabilityV12R03 and added ciscoXgcpCapabilityV12R03AS5000.', 'Added ciscoXgcpCapabilityV5R100 for MGX8850 release 5.1.00', 'Fixed syntax error in cXgcpMediaGwSupportedPackages of ciscoXgcpCapabilityV12R03.', 'Added ciscoXgcpCapabilityV5R015 for MGX8850 release 5.0.15', 'Added ciscoXgcpCapabilityV12R03 for Cisco IOS 12.3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoXgcpCapability.setLastUpdated('200603010000Z')
if mibBuilder.loadTexts: ciscoXgcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoXgcpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoXgcpCapability.setDescription('The agent capabilities for CISCO-XGCP-MIB.')
ciscoXgcpCapabilityV4R010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setProductRelease('MGX8850 Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV4R010.setDescription('XGCP MIB capabilities for VXSM in Release 4.0.10.')
ciscoXgcpCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R03.setDescription('Cisco XGCP MIB capabilities')
ciscoXgcpCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setProductRelease('MGX8850 release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R015.setDescription('XGCP MIB capabilities for VXSM in MGX8850 release 5.0.15.')
ciscoXgcpCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setProductRelease('MGX8880 release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R100.setDescription('XGCP MIB capabilities for VXSM in MGX8880 release 5.1.00.')
ciscoXgcpCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setProductRelease('MGX8880 release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R300.setDescription('XGCP MIB capabilities for VXSM in MGX8880 release 5.3.00.')
ciscoXgcpCapabilityV12R03AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R03AS5000.setDescription('Cisco XGCP MIB capabilities')
ciscoXgcpCapabilityV12R04AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R04AS5000.setDescription('Cisco XGCP MIB capabilities')
mibBuilder.exportSymbols("CISCO-XGCP-CAPABILITY", ciscoXgcpCapabilityV5R015=ciscoXgcpCapabilityV5R015, ciscoXgcpCapabilityV4R010=ciscoXgcpCapabilityV4R010, ciscoXgcpCapabilityV5R100=ciscoXgcpCapabilityV5R100, ciscoXgcpCapabilityV12R03=ciscoXgcpCapabilityV12R03, ciscoXgcpCapabilityV12R04AS5000=ciscoXgcpCapabilityV12R04AS5000, ciscoXgcpCapabilityV12R03AS5000=ciscoXgcpCapabilityV12R03AS5000, ciscoXgcpCapabilityV5R300=ciscoXgcpCapabilityV5R300, ciscoXgcpCapability=ciscoXgcpCapability, PYSNMP_MODULE_ID=ciscoXgcpCapability)
