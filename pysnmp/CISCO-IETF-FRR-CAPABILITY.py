#
# PySNMP MIB module CISCO-IETF-FRR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-FRR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, MibIdentifier, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, iso, Integer32, Bits, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "iso", "Integer32", "Bits", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfFrrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 310))
ciscoIetfFrrCapability.setRevisions(('2003-05-23 12:00',))
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setLastUpdated('200305231200Z')
if mibBuilder.loadTexts: ciscoIetfFrrCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfFrrCapabilityV12R0026S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 310, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfFrrCapabilityV12R0026S = ciscoIetfFrrCapabilityV12R0026S.setProductRelease('Cisco IOS 12.0(26)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfFrrCapabilityV12R0026S = ciscoIetfFrrCapabilityV12R0026S.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-FRR-CAPABILITY", ciscoIetfFrrCapability=ciscoIetfFrrCapability, ciscoIetfFrrCapabilityV12R0026S=ciscoIetfFrrCapabilityV12R0026S, PYSNMP_MODULE_ID=ciscoIetfFrrCapability)
