#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-SCTP-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, IpAddress, Bits, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, NotificationType, MibIdentifier, Counter32, TimeTicks, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Bits", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSctpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 220))
ciscoSctpExtCapability.setRevisions(('2002-01-21 00:00', '2001-11-30 00:00',))
if mibBuilder.loadTexts: ciscoSctpExtCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSctpExtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setStatus('current')
ciscoSctpExtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-CAPABILITY", ciscoSctpExtCapability=ciscoSctpExtCapability, PYSNMP_MODULE_ID=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R024MB1=ciscoSctpExtCapabilityV12R024MB1, ciscoSctpExtCapabilityV12R0204MB3=ciscoSctpExtCapabilityV12R0204MB3)
