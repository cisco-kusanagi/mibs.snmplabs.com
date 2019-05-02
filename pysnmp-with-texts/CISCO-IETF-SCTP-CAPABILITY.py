#
# PySNMP MIB module CISCO-IETF-SCTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-SCTP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Integer32, NotificationType, Counter32, ObjectIdentity, Unsigned32, IpAddress, TimeTicks, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Integer32", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSctpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 215))
ciscoSctpCapability.setRevisions(('2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSctpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSctpCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoSctpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSctpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sctp@cisco.com')
if mibBuilder.loadTexts: ciscoSctpCapability.setDescription('Agent capabilities for the CISCO-IETF-SCTP-MIB.')
ciscoSctpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 215, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-IETF-SCTP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-CAPABILITY", ciscoSctpCapabilityV12R024MB1=ciscoSctpCapabilityV12R024MB1, PYSNMP_MODULE_ID=ciscoSctpCapability, ciscoSctpCapability=ciscoSctpCapability)
