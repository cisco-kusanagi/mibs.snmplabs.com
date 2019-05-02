#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-SCTP-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ObjectIdentity, TimeTicks, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Counter32, Unsigned32, IpAddress, Integer32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "TimeTicks", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Counter32", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSctpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 220))
ciscoSctpExtCapability.setRevisions(('2002-01-21 00:00', '2001-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSctpExtCapability.setRevisionsDescriptions(('Updated capabilities to support additional objects and a new notification.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSctpExtCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sctp@cisco.com')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setDescription('Agent capabilities for the CISCO-IETF-SCTP-EXT-MIB.')
ciscoSctpExtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpExtCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-IETF-SCTP-EXT-MIB.my User Agent MIB capabilities.')
ciscoSctpExtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpExtCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-IETF-SCTP-EXT-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-CAPABILITY", ciscoSctpExtCapability=ciscoSctpExtCapability, PYSNMP_MODULE_ID=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R024MB1=ciscoSctpExtCapabilityV12R024MB1, ciscoSctpExtCapabilityV12R0204MB3=ciscoSctpExtCapabilityV12R0204MB3)
