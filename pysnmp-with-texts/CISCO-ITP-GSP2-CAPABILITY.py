#
# PySNMP MIB module CISCO-ITP-GSP2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSP2-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, Unsigned32, TimeTicks, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Integer32, iso, Counter32, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "TimeTicks", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Counter32", "Counter64", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsp2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 307))
ciscoGsp2Capability.setRevisions(('2004-08-25 00:00', '2003-11-24 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGsp2Capability.setRevisionsDescriptions(('Added support for objects to indicate whether device support non-stop operations feature. Added ciscoGsp2CapabilityV12R023000SW1 agent capability statement.', 'Added ciscoGsp2Mtp3ErrorsGroup. Added ciscoGsp2CapabilityV12R022004SW agent capability statement. This capability contains groups from ciscoGsp2CapabilityV12R0204MB4 agent capability statement as well as ciscoGsp2Mtp3ErrorsGroup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGsp2Capability.setLastUpdated('200408250000Z')
if mibBuilder.loadTexts: ciscoGsp2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGsp2Capability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGsp2Capability.setDescription('Agent capabilities for the CISCO-ITP-GSP2-MIB.')
ciscoGsp2CapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GSP2-MIB.my User Agent MIB capabilities.')
ciscoGsp2CapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R022004SW.setDescription('IOS 12.2(20.4)SW Cisco CISCO-ITP-GSP2-MIB.my User Agent MIB capabilities.')
ciscoGsp2CapabilityV12R022300SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R022300SW1.setDescription('IOS 12.2(23)SW1 Cisco CISCO-ITP-GSP2-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GSP2-CAPABILITY", ciscoGsp2CapabilityV12R0204MB4=ciscoGsp2CapabilityV12R0204MB4, ciscoGsp2CapabilityV12R022004SW=ciscoGsp2CapabilityV12R022004SW, PYSNMP_MODULE_ID=ciscoGsp2Capability, ciscoGsp2CapabilityV12R022300SW1=ciscoGsp2CapabilityV12R022300SW1, ciscoGsp2Capability=ciscoGsp2Capability)
