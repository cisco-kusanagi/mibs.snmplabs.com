#
# PySNMP MIB module CISCO-ITP-GSCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSCCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, MibIdentifier, ModuleIdentity, Counter32, IpAddress, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibIdentifier", "ModuleIdentity", "Counter32", "IpAddress", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 539))
ciscoGsccpCapability.setRevisions(('2007-05-17 00:00', '2005-01-14 00:00', '2004-10-07 00:00', '2003-12-08 00:00', '2003-10-28 00:00', '2003-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGsccpCapability.setRevisionsDescriptions(('Added ciscoGsccpCapabilityV12R0218IXA and ciscoGsccpCapabilityV12R0411SW capability statements. Corrected all capability statements to indicate that cgsccpGttConPcRowStatus was implemented as read-only rather than cgsccpGttConPcTable.', 'Added ciscoGsccpCapabilityV12R025000SW1 capability statement. Added ciscoGsccpNotificationsGroupSup1, ciscoGsccpGttErrorsGroup and ciscoGsccpGttPrefGroupSup1 object goups.', 'Added ciscoGsccpCapabilityV12R023000SW1 capability statement. Replaced ciscoGsccpGttAppGroupRev2 object group with ciscoGsccpGttAppGroupRev3.', 'Support for cross instance global title translation. Added ciscoGsccpCapabilityV12R022004SW capability statement. Replaced ciscoGsccpGttAppGroup object group with ciscoGsccpGttAppGroupRev2. Replaced ciscoGsccpGttGtaGroup with ciscoGsccpGttGtaGroupRev2.', 'Changes to allow GTT prefix conversion to be specified per instance. Added ciscoGsccpCapabilityV12R0204MB13 capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGsccpCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoGsccpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGsccpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGsccpCapability.setDescription('Agent capabilities for the CISCO-ITP-GSCCP-MIB.')
ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setProductRelease('Cisco IOS 12.2(4)MB13')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0204MB13.setDescription('IOS 12.2(4)MB13 Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R022004SW.setDescription('IOS 12.2(20.4)SW Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R023000SW1.setDescription('IOS 12.2(23)SW1 Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R025000SW1.setDescription('IOS 12.2(25)SW1 Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
ciscoGsccpCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setProductRelease('Cisco IOS IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0411SW.setDescription('Cisco IOS IOS 12.4(11)SW Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GSCCP-CAPABILITY", ciscoGsccpCapabilityV12R022004SW=ciscoGsccpCapabilityV12R022004SW, ciscoGsccpCapabilityV12R0218IXA=ciscoGsccpCapabilityV12R0218IXA, ciscoGsccpCapabilityV12R0204MB10=ciscoGsccpCapabilityV12R0204MB10, PYSNMP_MODULE_ID=ciscoGsccpCapability, ciscoGsccpCapabilityV12R023000SW1=ciscoGsccpCapabilityV12R023000SW1, ciscoGsccpCapabilityV12R0411SW=ciscoGsccpCapabilityV12R0411SW, ciscoGsccpCapabilityV12R0204MB13=ciscoGsccpCapabilityV12R0204MB13, ciscoGsccpCapabilityV12R025000SW1=ciscoGsccpCapabilityV12R025000SW1, ciscoGsccpCapability=ciscoGsccpCapability)
