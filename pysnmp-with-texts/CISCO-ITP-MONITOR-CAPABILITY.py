#
# PySNMP MIB module CISCO-ITP-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-MONITOR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Counter64, NotificationType, IpAddress, TimeTicks, ObjectIdentity, Integer32, Unsigned32, Counter32, iso, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter64", "NotificationType", "IpAddress", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32", "iso", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 422))
ciscoItpMonCapability.setRevisions(('2004-11-23 00:00', '2004-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMonCapability.setRevisionsDescriptions(('Add the new ciscoItpmNotificationsGroupRev1 group to support ciscoItpMonitorState notification.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMonCapability.setLastUpdated('200411230000Z')
if mibBuilder.loadTexts: ciscoItpMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMonCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpMonCapability.setDescription('Agent capabilities for the CISCO-ITP-MONITOR-MIB.')
ciscoItpMonCapabilityV12R0221SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setProductRelease('Cisco IOS 12.2(21)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0221SW.setDescription('IOS 12.2(21)SW Cisco CISCO-ITP-MONITOR-MIB.my User Agent MIB capabilities.')
ciscoItpMonCapabilityV12R0251SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0251SW.setDescription('IOS 12.2(25)SW Cisco CISCO-ITP-MONITOR-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MONITOR-CAPABILITY", ciscoItpMonCapability=ciscoItpMonCapability, ciscoItpMonCapabilityV12R0251SW=ciscoItpMonCapabilityV12R0251SW, ciscoItpMonCapabilityV12R0221SW=ciscoItpMonCapabilityV12R0221SW, PYSNMP_MODULE_ID=ciscoItpMonCapability)
