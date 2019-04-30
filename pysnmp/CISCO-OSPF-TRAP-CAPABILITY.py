#
# PySNMP MIB module CISCO-OSPF-TRAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OSPF-TRAP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, Unsigned32, iso, Counter32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "Unsigned32", "iso", "Counter32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOspfTrapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 288))
ciscoOspfTrapCapability.setRevisions(('2002-11-24 00:00',))
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setLastUpdated('200211240000Z')
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setOrganization('Cisco Systems, Inc.')
ciscoOspfTrapCapabilityV12R026S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 288, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapCapabilityV12R026S = ciscoOspfTrapCapabilityV12R026S.setProductRelease('Cisco IOS 12.0(26)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapCapabilityV12R026S = ciscoOspfTrapCapabilityV12R026S.setStatus('current')
mibBuilder.exportSymbols("CISCO-OSPF-TRAP-CAPABILITY", PYSNMP_MODULE_ID=ciscoOspfTrapCapability, ciscoOspfTrapCapabilityV12R026S=ciscoOspfTrapCapabilityV12R026S, ciscoOspfTrapCapability=ciscoOspfTrapCapability)
