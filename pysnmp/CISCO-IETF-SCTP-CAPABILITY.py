#
# PySNMP MIB module CISCO-IETF-SCTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-SCTP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Unsigned32, Integer32, Bits, ObjectIdentity, MibIdentifier, iso, NotificationType, Gauge32, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Integer32", "Bits", "ObjectIdentity", "MibIdentifier", "iso", "NotificationType", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSctpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 215))
ciscoSctpCapability.setRevisions(('2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoSctpCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoSctpCapability.setOrganization('Cisco Systems, Inc.')
ciscoSctpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 215, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-CAPABILITY", ciscoSctpCapability=ciscoSctpCapability, PYSNMP_MODULE_ID=ciscoSctpCapability, ciscoSctpCapabilityV12R024MB1=ciscoSctpCapabilityV12R024MB1)
