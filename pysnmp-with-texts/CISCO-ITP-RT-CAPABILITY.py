#
# PySNMP MIB module CISCO-ITP-RT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-RT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, Counter32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Gauge32, Unsigned32, MibIdentifier, TimeTicks, iso, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "iso", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpRtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 216))
ciscoItpRtCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpRtCapability.setRevisionsDescriptions(('Updated capabilities MIB as required for new groups. cItpRtNotificationsGroup, cItpRtScalarGroupRev1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpRtCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoItpRtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpRtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpRtCapability.setDescription('Agent capabilities for the CISCO-ITP-RT-MIB.')
ciscoItpRtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpRtCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-RT-MIB.my User Agent MIB capabilities.')
ciscoItpRtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoItpRtCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-ITP-RT-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-RT-CAPABILITY", ciscoItpRtCapabilityV12R024MB1=ciscoItpRtCapabilityV12R024MB1, ciscoItpRtCapabilityV12R0204MB3=ciscoItpRtCapabilityV12R0204MB3, PYSNMP_MODULE_ID=ciscoItpRtCapability, ciscoItpRtCapability=ciscoItpRtCapability)
